#!/usr/bin/env python3
"""Informe de hábitos, designaciones, variedad y referencias al pasado de un manuscrito narrativo.

Muestra lo que ningún capítulo deja ver por sí solo: construcciones que se vuelven molde a lo
largo del volumen, negaciones y abstenciones que se acumulan, la manera en que la narración nombra
a cada personaje, comienzos de oración y cierres de sección que se repiten, marcas de una variedad
de la lengua distinta de la declarada y las frases que vuelven sobre algo anterior, que es donde
más se rompe la continuidad.

Cada familia se muestra por capítulo desde el primero, para distinguir la deriva de un rasgo
estable. Las cifras localizan casos para leerlos; no son cuotas ni errores.

Uso:
  python habitos.py RUTA [RUTA ...] [opciones]

  RUTA puede ser un archivo con todo el manuscrito (se divide por los encabezados de capítulo) o
  varios archivos o carpetas (cada archivo es un capítulo, en orden alfabético).

Informes (--informe, separados por comas; por defecto, todo):
  habitos        construcciones por capítulo y su deriva; frases, imágenes, comienzos de párrafo
                 e inventarios repetidos entre capítulos
  negaciones     oraciones narrativas que empiezan con negación, «sin + infinitivo», «no… ni» y
                 abstenciones de habla o intervención
  designaciones  cómo nombra la narración a cada personaje: nombres, partes de un nombre
                 compuesto, epítetos y alias declarados
  comienzos      con qué palabras empiezan las oraciones narrativas
  cierres        última oración de cada sección, una al lado de la otra
  ritmo          largo de oración narrativa, diálogo directo/reportado, comodines vagos y puntuación (; : ¿ ¡)
  variedad       marcas de variedades de la lengua y perfecto compuesto en el diálogo
  retro          frases que vuelven sobre algo anterior, incluidas las del narrador
  todo           todos los anteriores

Opciones:
  --capitulos 5,7-9           Limita los listados de ejemplos a esos capítulos (contados desde 1).
                              Las tablas por capítulo muestran siempre el volumen entero.
  --variedad VAR              neutro, peninsular, americano o rioplatense: señala las familias
                              de marcas ajenas a la variedad declarada.
  --alias "X=forma1|forma2"   Agrupa las designaciones de un personaje (repetible), p. ej.
                              --alias "Konrad=el capitán|el viejo". Los nombres que coinciden
                              con palabras comunes (un título, una clase, un verbo) no se
                              detectan solos: decláralos aquí.
  --patron "etiqueta=regex"   Agrega una construcción al informe de hábitos (repetible).
  --marcador "etiqueta=regex" Agrega una familia de marcas al informe de variedad (repetible).
  --encabezado REGEX          Encabezado de capítulo (por defecto, líneas Markdown que empiezan
                              con «Capítulo» o «Chapter», o «Capítulo N» sin almohadillas).
  --max N                     Máximo de filas por listado (por defecto: 12).
"""

import argparse
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

PALABRA = re.compile(r"[^\W\d_]+")
ORACION = re.compile(r"[^.!?…]+[.!?…]*")
SEPARADORES = {"***", "* * *", "---", "⁂", "* * * *"}

VACIAS = set("""
a al algo algún alguna algunas alguno algunos ante antes aquel aquella aquello así aun aún bajo bien cada
casi como con contra cual cuales cuando cuanto de del desde donde dos e el él ella ellas ellos en entre era
eran es esa esas ese eso esos esta está estaba estaban estar este esto estos fue fueron ha había habían hacia
hasta hay la las le les lo los más me mi mientras mis muy nada ni no nos o otra otras otro otros para pero
poco por porque que qué quien se sea ser si sí sin sino sobre su sus también tan tanto te tenía tiene todo
todos tu un una uno unos unas y ya yo usted ustedes uno una vez veces
""".split())

AUXILIARES = set("""
hubiera hubieran hubiese hubiesen haber habido sido estado fuera fueran fuese tuviera tuvieran estuviera
estuvieran pudiera pudieran quisiera dado hecho hacer hizo iba iban podía podían quería tenían algo alguien
""".split())

CONSTRUCCIONES = [
    ("como si", r"\bcomo si\b"),
    ("como se + verbo", r"\bcomo se [^\W\d_]+"),
    ("como quien / como alguien que", r"\bcomo (?:quien|alguien que)\b"),
    ("lectura de rostros", r"\b(?:cara|mirada|voz|expresión|gesto|ojeras) de (?:alguien|quien)\b"
                           r"|\b(?:vio|leyó|supo|notó) (?:en|por) (?:su|la) (?:cara|mirada|voz|expresión)\b"),
    ("no era X sino / No era X. Era Y", r"\bno era\b[^.;!?]{1,70}(?:\bsino\b|[.;] Era\b)"),
    ("verbos de saber", r"\b(?:supo que|se dio cuenta de que|comprendió que|entendió que|lo supo)\b"),
    ("pensó en", r"\bpensó en\b"),
    ("pausa (quedarse, un rato, silencio)", r"\b(?:se qued(?:ó|aron)|permaneci(?:ó|eron)|un rato|un momento largo|en silencio|no dijo nada|no contestó)\b"),
    ("lentitud (despacio, lentamente)", r"\b(?:despacio|lentamente|sin prisa|con calma)\b"),
]

MESES = "enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre"
HORAS = "una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce"

RETRO = [
    ("intervalo", r"\bhace (?:un|una|unos|unas|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|quince|veinte|treinta|cuarenta|cincuenta|cien|varios|varias|\d+) [a-záéíóúñ]+"
                  r"|\b(?:un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|quince|veinte|\d+) (?:días|día|semanas|semana|meses|mes|años|año|horas|noches) (?:antes|después|atrás|más tarde)\b"
                  r"|\bdesde hac(?:e|ía)\b|\ben (?:días|semanas|meses|años)\b"
                  r"|\b(?:ayer|anteayer|anoche|la semana pasada|el mes pasado|el año pasado)\b"),
    ("referencia del narrador", r"\b(?:el|la) (?:día|noche|tarde|mañana|semana) (?:anterior|siguiente|previa|previo)\b"
                                r"|\bla víspera\b|\b(?:aquella|esa) (?:mañana|tarde|noche|semana|vez)\b"
                                r"|\b(?:aquel|ese) (?:día|mes|año|invierno|verano|otoño)\b"
                                r"|\bal día siguiente\b|\ba la (?:mañana|tarde|noche) siguiente\b"
                                r"|\b(?:días|semanas|meses|años) atrás\b|\bla última vez\b"),
    ("fecha u hora", rf"\ba (?:primeros|principios|mediados|finales|fines) de (?:{MESES})\b|\b\d{{1,2}} de (?:{MESES})\b"
                     rf"|\b(?:en|desde|hasta) (?:{MESES})\b"
                     rf"|\ba las (?:\d{{1,2}}(?::\d\d)?|(?:{HORAS})(?=\s*(?:[.,;:!?)]|$|y\b|menos\b|de la\b|en punto\b|horas\b)))"
                     rf"|(?-i:\bA) las (?:{HORAS})\b"
                     rf"|\b(?:{HORAS}) menos (?:cinco|diez|cuarto|veinte|veinticinco)\b"),
    ("primera vez / hábito", r"\bpor primera vez(?: en)?\b|\bcomo (?:todos|cada) (?:los|las)? ?(?:días|lunes|martes|miércoles|jueves|viernes|sábados|domingos|semanas|noches|mañanas)\b|\bnunca (?:había|lo había)\b"),
    ("día de la semana", r"\b(?:el|la|ese|este|aquel) (?:lunes|martes|miércoles|jueves|viernes|sábado|domingo)\b"),
    ("cantidad", r"\b\d[\d.,]*\s*(?:dólares|euros|pesos|libras|yenes|wones|metros|kilómetros|km|kilos|kg|cm|grados|minutos|horas)\b"
                 r"|\b(?:con|del|el) dinero (?:de|del)\b"
                 r"|\b(?:cien|doscientos|trescientos|cuatrocientos|quinientos|seiscientos|setecientos|ochocientos|novecientos|mil|[a-z]+ mil)(?: [a-záéíóú]+){0,3} (?:dólares|euros|pesos|libras|yenes|wones)\b"),
    ("cita de un texto", r"\b(?:la nota|la carta|el mensaje|el informe|el registro|el contrato|el documento|la declaración|el correo|la postal|la tarjeta|el formulario|la factura|el recibo)\b[^.;]{0,40}\b(?:dice|decía|dijo|ponía|pone|no dice|no decía|tenía escrito|había escrito)\b"),
    ("atribución de palabras", r"\b(?:la palabra|las palabras|la frase|lo que había dicho|como había dicho|como dijo|había dicho que|le había dicho)\b"),
]

# Negaciones y abstenciones (sobre oraciones narrativas).
NEG_INICIO = re.compile(r"^(?:No|Ni|Nunca|Nadie|Nada|Tampoco|Jamás)\b")
NO_NI = re.compile(r"\bno\b[^.;!?]{1,120}\bni\b", re.IGNORECASE)
SIN_PALABRA = re.compile(r"\bsin (?:siquiera |apenas )?([^\W\d_]+)", re.IGNORECASE)
ABSTENCION = re.compile(
    r"\b(?:no|sin|ni)\s+(?:(?:se|le|lo|la|les|los|las|me|te|nos)\s+)*"
    r"(?:pregunt|añad|intent|insist|aprovech|coment|dij|dec[ií]r|hiz|hac|interrump|toc|mencion|reproch|explic|corrig|discut|protest|ofrec|pid|ped|agradec)\w*"
    r"|\bagradeci[óo]\w* que\b|\blo que \w+ agradeci[óo]\b", re.IGNORECASE)
NO_INFINITIVOS = {"lugar", "azucar", "par", "mujer", "taller", "collar", "altar", "hogar", "dolar", "mar", "bar",
                  "militar", "familiar", "particular", "popular", "similar", "regular", "pilar", "telar", "placer",
                  "poder", "deber", "pesar", "amanecer", "atardecer", "anochecer", "parecer", "saber", "haber"}
# «sin poder», «sin saber», «sin deber» son infinitivos frecuentes: se cuentan aparte para no excluirlos.
INFINITIVOS_AMBIGUOS = {"poder", "deber", "pesar", "saber", "haber", "parecer"}
CLITICOS = sorted(["selas", "selos", "sela", "selo", "sele", "seles", "melo", "mela", "telo", "tela", "noslo",
                   "nosla", "les", "las", "los", "le", "la", "lo", "se", "me", "te", "nos", "os"], key=len, reverse=True)

# Designaciones.
EPITETOS = ["joven", "muchacho", "muchacha", "chico", "chica", "hombre", "mujer", "anciano", "anciana", "viejo",
            "vieja", "niño", "niña", "desconocido", "desconocida", "recién llegado", "recién llegada", "extranjero",
            "extranjera", "forastero", "forastera", "arquero", "arquera", "espadachín", "guerrero", "guerrera",
            "soldado", "capitán", "capitana", "caballero", "dama", "señor", "señora", "encargado", "encargada",
            "conductor", "conductora", "visitante", "invitado", "invitada", "pelirrojo", "pelirroja", "rubio",
            "rubia", "moreno", "morena", "maestro", "maestra", "anfitrión", "anfitriona"]
DETERMINANTES = r"(?:[Ee]l|[Ll]a|[Dd]el|[Aa]l|[Aa]quel|[Aa]quella|[Ee]se|[Ee]sa|[Ee]ste|[Ee]sta)"
EPITETO_RX = re.compile(rf"\b{DETERMINANTES} ({'|'.join(EPITETOS)})\b(?:\s+([^\W\d_]+))?")

# Variedad de la lengua: marcas firmes por defecto. Una marca no es un error: se compara con la
# variedad declarada. Se amplían con --marcador.
VARIEDAD = [
    ("vosotros", r"\bvosotr[oa]s\b|\bos\b|\b(?:vais|veis|dais|sois)\b|\b(?!(?:dieci|veinti|treintai)séis\b)[a-záéíóúñ]+(?:áis|éis)\b"),
    ("voseo", r"\b(?:vos|sos|tenés|sabés|querés|podés|hacés|pensás|mirá|vení|decime|fijate|andá|contame|escuchame)\b"),
    ("léxico peninsular", r"\baparcamientos?\b|\baparc(?:ar|ó|aba|aban|ado|ados|ada|adas|aron)\b|\bpatinetes?\b"
                          r"|\bordenador(?:es)?\b|\bzumos?\b|\bapetec[a-záéíóúñ]*\b|\bmecheros?\b|\bchaval[a-záéíóúñ]*\b"
                          r"|\bfurgonetas?\b|\bbombillas?\b|\bpatatas?\b|\bguay\b|\b(?:su|mi|tu) móvil\b"
                          r"|(?-i:(?:—|¡)Vale(?=[.,!]|$))"
                          r"|\b(?:coger|cogió|cogía|cogían|coge|cogen|cogieron|cogido|cogida|cogiendo|cógelo|cógela)\b"),
    ("léxico americano", r"\bestacionamientos?\b|\bcelular(?:es)?\b|\bcomputadoras?\b|\banteojos\b|\bjugos?\b"
                         r"|\bap[uú]r(?:ate|ese|ense|arse)\b|\bse apur[a-záéíóúñ]+\b|\bplatic[a-záéíóúñ]+\b|\bahorita\b"
                         r"|\bchamarras?\b|\bcamperas?\b|\bremeras?\b|\bpolleras?\b|\bpiletas?\b|\bboletos?\b"
                         r"|\brecién [a-záéíóúñ]+(?:ó|aron|ieron|aste|iste)\b"),
]
PRESETS = {
    "neutro": {"ajenas": {"vosotros", "voseo", "léxico peninsular"}, "perfecto": True},
    "peninsular": {"ajenas": {"voseo", "léxico americano"}, "perfecto": False},
    "americano": {"ajenas": {"vosotros", "léxico peninsular"}, "perfecto": True},
    "rioplatense": {"ajenas": {"vosotros", "léxico peninsular"}, "perfecto": True},
}
PERFECTO = re.compile(r"\b(?:he|has|ha|hemos|habéis|han)\s+[a-záéíóúñ]*(?:ado|ido|ído|to|cho|so)\b", re.IGNORECASE)

DEFAULT_ENCABEZADO = r"^(?:#{1,3}\s*)?(?:Cap[ií]tulo|Chapter)\b.*$"

NOMBRES = set()
STATS = {}


# ---------------------------------------------------------------- lectura

def leer_capitulos(rutas, encabezado):
    """Devuelve una lista de capítulos: (titulo, [(origen, linea, texto), ...])."""
    archivos = []
    for r in rutas:
        p = Path(r)
        if p.is_dir():
            archivos += sorted(x for x in p.rglob("*") if x.suffix.lower() in (".md", ".txt"))
        elif p.is_file():
            archivos.append(p)
        else:
            sys.exit(f"No existe: {r}")
    if not archivos:
        sys.exit("No hay archivos .md o .txt en las rutas indicadas.")
    patron = re.compile(encabezado, re.IGNORECASE)
    caps = []
    for f in archivos:
        lineas = f.read_text(encoding="utf-8").splitlines()
        cortes = [i for i, l in enumerate(lineas) if patron.match(l.strip())]
        if len(archivos) == 1 and cortes:
            for k, ini in enumerate(cortes):
                fin = cortes[k + 1] if k + 1 < len(cortes) else len(lineas)
                fin = min(fin, siguiente_parte(lineas, ini, fin))
                caps.append((lineas[ini].strip("# ").strip(), [(f.name, i + 1, lineas[i]) for i in range(ini + 1, fin)]))
        else:
            titulo = next((l.strip("# ").strip() for l in lineas if patron.match(l.strip())), f.stem)
            caps.append((titulo, [(f.name, i + 1, l) for i, l in enumerate(lineas)]))
    return caps


def siguiente_parte(lineas, ini, fin):
    """Corta antes de un encabezado de nivel 1 (p. ej., «# Segunda parte») dentro del capítulo."""
    for i in range(ini + 1, fin):
        if re.match(r"^#\s", lineas[i]):
            return i
    return fin


def es_texto(l):
    s = l.strip()
    return bool(s) and not s.startswith("#") and not s.startswith("<!--") and s not in SEPARADORES


def es_dialogo(l):
    return l.strip().startswith(("—", "–"))


def partir_dialogo(s):
    """Separa una línea de diálogo en (habla, acotaciones)."""
    partes = re.split(r"[—–]", s.strip())[1:]
    habla = [p for i, p in enumerate(partes) if i % 2 == 0]
    acot = [p for i, p in enumerate(partes) if i % 2 == 1]
    return habla, acot


def oraciones_narrativas(lineas):
    """(origen, num, oración) de la narración: párrafos narrativos y oraciones completas de las acotaciones.
    Se descarta el verbo de habla inicial de una acotación («dijo él»)."""
    out = []
    for origen, num, l in lineas:
        if not es_texto(l):
            continue
        if es_dialogo(l):
            _, acot = partir_dialogo(l)
            for seg in acot:
                fr = [o.strip() for o in ORACION.findall(seg) if o.strip(" .,;")]
                if fr and fr[0][:1].islower():
                    fr = fr[1:]
                out += [(origen, num, o) for o in fr if PALABRA.search(o)]
        else:
            out += [(origen, num, o.strip()) for o in ORACION.findall(l.strip()) if PALABRA.search(o)]
    return out


def narracion_por_parrafo(lineas):
    """(origen, num, texto narrativo) por párrafo, incluidas las acotaciones del diálogo."""
    out = []
    for origen, num, l in lineas:
        if not es_texto(l):
            continue
        if es_dialogo(l):
            _, acot = partir_dialogo(l)
            t = " ".join(acot).strip()
            if t:
                out.append((origen, num, t))
        else:
            out.append((origen, num, l.strip()))
    return out


def habla_total(lineas):
    out = []
    for origen, num, l in lineas:
        if es_texto(l) and es_dialogo(l):
            habla, _ = partir_dialogo(l)
            out.append((origen, num, " ".join(habla)))
    return out


def secciones(lineas):
    secs, cur = [], []
    for origen, num, l in lineas:
        s = l.strip()
        if s in SEPARADORES or (s.startswith("#") and cur):
            if cur:
                secs.append(cur)
            cur = []
            continue
        if es_texto(l):
            cur.append((origen, num, s))
    if cur:
        secs.append(cur)
    return secs


def detectar_nombres(caps):
    """Palabras que, fuera del comienzo de oración, casi siempre aparecen con mayúscula: nombres propios.
    La proporción se calcula solo sobre las apariciones interiores, porque un nombre que abre muchas
    oraciones (el del focalizador, típicamente) no debe quedar fuera."""
    mayus, interior, total = defaultdict(int), defaultdict(int), defaultdict(int)
    for _, lineas in caps:
        for _, _, l in lineas:
            if not es_texto(l):
                continue
            for frase in ORACION.findall(re.sub(r"[—–«»“”\"]", ". ", l)):
                ws = PALABRA.findall(frase)
                for k, w in enumerate(ws):
                    total[w.lower()] += 1
                    if k > 0:
                        interior[w.lower()] += 1
                        if w[0].isupper():
                            mayus[w.lower()] += 1
    NOMBRES.update(w for w, n in total.items()
                   if n >= 3 and interior[w] >= 1 and mayus[w] >= 0.8 * interior[w] and w not in VACIAS)


def tokens(texto):
    return [w.lower() for w in PALABRA.findall(texto)]


def contenido(ws):
    return [w for w in ws if w not in VACIAS and len(w) > 2]


def contenido_imagen(ws):
    return [w for w in contenido(ws) if w not in AUXILIARES and w not in NOMBRES]


def quitar_tilde(w):
    return w.translate(str.maketrans("áéíóú", "aeiou"))


def es_infinitivo(w):
    w = w.lower()
    for _ in range(2):
        for c in CLITICOS:
            if w.endswith(c) and len(w) - len(c) >= 3 and quitar_tilde(w[:-len(c)]).endswith(("ar", "er", "ir")):
                w = w[:-len(c)]
                break
    w = quitar_tilde(w)
    if w in INFINITIVOS_AMBIGUOS:
        return True
    return len(w) > 3 and w.endswith(("ar", "er", "ir")) and w not in NO_INFINITIVOS


def elegido(ci, elegidos):
    return not elegidos or ci in elegidos


def pct(a, b):
    return f"{100 * a / b:.1f} %" if b else "·"


def por10k(a, n):
    return f"{a * 10000 / n:.1f}" if a else "·"


def palabras(lineas):
    return max(1, sum(len(PALABRA.findall(l)) for _, _, l in lineas if es_texto(l)))


# ---------------------------------------------------------------- hábitos

def densidades(caps, construcciones):
    filas = []
    for titulo, lineas in caps:
        texto = "\n".join(l for _, _, l in lineas if es_texto(l))
        n = max(1, len(texto.split()))
        filas.append((titulo, n, [len(re.findall(rx, texto, re.IGNORECASE)) for _, rx in construcciones]))
    return filas


def informe_habitos(caps, construcciones, maximo, elegidos):
    filas = densidades(caps, construcciones)
    total = sum(n for _, n, _ in filas)
    print(f"# Hábitos del volumen\n\n{len(caps)} capítulos, {total:,} palabras.".replace(",", "."))
    print("\nLas densidades son apariciones cada 10.000 palabras. Sirven para encontrar familias de casos y leerlas; no son cuotas ni errores.\n")

    print("## Construcciones por capítulo\n")
    claves = [f"C{i + 1}" for i in range(len(construcciones))]
    for c, (etq, _) in zip(claves, construcciones):
        print(f"- **{c}**: {etq}")
    print("\n| Cap. | Palabras | " + " | ".join(claves) + " |")
    print("|---|---:|" + "---:|" * len(claves))
    for idx, (titulo, n, cuentas) in enumerate(filas, 1):
        celdas = [f"{c * 10000 / n:.1f}" if c else "·" for c in cuentas]
        print(f"| {idx} | {n} | " + " | ".join(celdas) + " |")

    print("\n## Deriva\n")
    print("Construcciones cuya densidad en un capítulo duplica la mediana de los capítulos anteriores (mínimo 3 apariciones, desde el capítulo 2; con menos de tres capítulos previos la comparación es orientativa). Una construcción que crece en todos los focalizadores suele ser un hábito del narrador, no de una voz.\n")
    hubo = False
    tercio = max(1, len(filas) // 3)
    for j, (etq, _) in enumerate(construcciones):
        dens = [c[j] * 10000 / n for _, n, c in filas]
        marcados = []
        for i in range(1, len(filas)):
            med = statistics.median(dens[:i])
            if filas[i][2][j] >= 3 and dens[i] >= 2 * max(med, 1.0):
                marcados.append(f"{i + 1} ({dens[i]:.1f} frente a {med:.1f}{', orientativa' if i < 3 else ''})")
        ini = statistics.mean(dens[:tercio])
        fin = statistics.mean(dens[-tercio:])
        if marcados or (len(filas) >= 3 and fin >= 2 * max(ini, 1.0) and sum(c[j] for _, _, c in filas[-tercio:]) >= 5):
            hubo = True
            print(f"- **{etq}**: primer tercio {ini:.1f}, último tercio {fin:.1f}." + (f" Capítulos por encima: {', '.join(marcados)}." if marcados else ""))
    if not hubo:
        print("Sin deriva marcada.")

    STATS.update(frases=[], imagenes=[], comienzos=0, inventarios=0)
    frases_repetidas(caps, maximo, elegidos)
    imagenes_repetidas(caps, maximo, elegidos)
    comienzos_repetidos(caps, maximo, elegidos)
    inventarios(caps, maximo, elegidos)
    if not elegidos:
        resumen(filas, construcciones, total)


def resumen(filas, construcciones, total):
    print("\n## Resumen para comparar entre manuscritos\n")
    print("Cifras del volumen entero, comparables entre obras distintas aunque los casos no lo sean.\n")
    tercio = max(1, len(filas) // 3)
    print("| Medida | Valor |")
    print("|---|---:|")
    for j, (etq, _) in enumerate(construcciones):
        tot = sum(c[j] for _, _, c in filas)
        dens = [c[j] * 10000 / n for _, n, c in filas]
        print(f"| {etq}: cada 10.000 palabras (primer tercio → último) | {tot * 10000 / total:.1f} ({statistics.mean(dens[:tercio]):.1f} → {statistics.mean(dens[-tercio:]):.1f}) |")
    fr3 = sum(1 for k in STATS["frases"] if k >= 3)
    print(f"| Frases repetidas en 3 o más capítulos, cada 10.000 palabras | {fr3 * 10000 / total:.1f} |")
    im2 = len(STATS["imagenes"])
    im3 = sum(1 for k in STATS["imagenes"] if k >= 3)
    print(f"| Imágenes repetidas en 2 o más capítulos, cada 10.000 palabras (en 3 o más) | {im2 * 10000 / total:.1f} ({im3 * 10000 / total:.1f}) |")
    print(f"| Comienzos de párrafo repetidos entre capítulos, cada 10.000 palabras | {STATS['comienzos'] * 10000 / total:.1f} |")
    print(f"| Párrafos con inventario anafórico, cada 10.000 palabras | {STATS['inventarios'] * 10000 / total:.1f} |")


def ngramas_por_capitulo(caps, n_min=5, n_max=10):
    """Mapa n-grama -> lista de (cap, origen, línea)."""
    vistos = defaultdict(list)
    for ci, (_, lineas) in enumerate(caps):
        for origen, num, l in lineas:
            if not es_texto(l):
                continue
            for frase in ORACION.findall(l):
                ws = tokens(frase)
                for n in range(n_min, n_max + 1):
                    for k in range(len(ws) - n + 1):
                        g = tuple(ws[k:k + n])
                        if len(contenido(g)) >= 3:
                            vistos[g].append((ci, origen, num))
    return vistos


def frases_repetidas(caps, maximo, elegidos):
    print("\n## Frases repetidas entre capítulos\n")
    print("Secuencias de cinco o más palabras (con al menos tres palabras con contenido) que aparecen en capítulos distintos. Los motivos deliberados también aparecen aquí; lo que conviene revisar es la frase hecha que se aplica a cosas sin relación.\n")
    vistos = ngramas_por_capitulo(caps)
    rep = {g: occ for g, occ in vistos.items() if len({c for c, _, _ in occ}) >= 2}
    largos = sorted(rep, key=len, reverse=True)
    elegidas = []
    for g in largos:
        s = " ".join(g)
        if any(s in " ".join(h) and len(rep[h]) >= len(rep[g]) for h in elegidas):
            continue
        elegidas.append(g)
    elegidas = [g for g in elegidas if not elegidos or any(c in elegidos for c, _, _ in rep[g])]
    elegidas.sort(key=lambda g: (-len({c for c, _, _ in rep[g]}), -len(g)))
    STATS["frases"] = [len({c for c, _, _ in rep[g]}) for g in elegidas]
    if not elegidas:
        print("Ninguna.")
        return
    for g in elegidas[:maximo]:
        lugares = ", ".join(f"cap. {c + 1} ({o}:{n})" for c, o, n in sorted(set(rep[g]))[:8])
        print(f"- «{' '.join(g)}» — {lugares}")


def imagenes_repetidas(caps, maximo, elegidos):
    print("\n## Imágenes repetidas\n")
    print("Comparaciones introducidas por «como» que comparten un par de palabras con contenido en capítulos distintos.\n")
    simil = re.compile(r"\bcomo (?:si|se|un|una|el|la|los|las|quien|alguien|cuando|uno|lo|a)\b[^.;:!?—]{3,90}", re.IGNORECASE)
    pares = defaultdict(list)
    textos = {}
    for ci, (_, lineas) in enumerate(caps):
        for origen, num, l in lineas:
            if not es_texto(l):
                continue
            for m in simil.finditer(l):
                ws = contenido_imagen(tokens(m.group(0))[1:])
                vistos = set()
                for i, a in enumerate(ws):
                    for b in ws[i + 1:i + 3]:
                        if a == b or (a, b) in vistos:
                            continue
                        vistos.add((a, b))
                        pares[(a, b)].append((ci, origen, num))
                        textos[(a, b, ci, num)] = m.group(0).strip()
    rep = [(p, occ) for p, occ in pares.items() if len({c for c, _, _ in occ}) >= 2]
    rep = [(p, o) for p, o in rep if not elegidos or any(c in elegidos for c, _, _ in o)]
    rep.sort(key=lambda x: (-len({c for c, _, _ in x[1]}), -len(x[1])))
    if not rep:
        print("Ninguna.")
        return
    mostrados, unicos = [], []
    for par, occ in rep:
        lugares = {(c, n) for c, _, n in occ}
        if any(lugares <= m for m in mostrados):
            continue
        mostrados.append(lugares)
        unicos.append((par, occ))
    STATS["imagenes"] = [len({c for c, _, _ in occ}) for _, occ in unicos]
    for (a, b), occ in unicos[:maximo]:
        ejemplos = []
        for c, o, n in sorted(set(occ))[:4]:
            ejemplos.append(f"cap. {c + 1} ({o}:{n}) «{textos[(a, b, c, n)][:70]}»")
        print(f"- **{a} … {b}** ({len(occ)}): " + "; ".join(ejemplos))


def comienzos_repetidos(caps, maximo, elegidos):
    print("\n## Comienzos de párrafo repetidos\n")
    print("Primeras cinco palabras de párrafos narrativos que se repiten en capítulos distintos. Señalan escenas armadas con la misma plantilla.\n")
    vistos = defaultdict(list)
    for ci, (_, lineas) in enumerate(caps):
        for origen, num, l in lineas:
            s = l.strip()
            if not es_texto(l) or s.startswith(("—", "–", "-", "*", ">", "|")):
                continue
            ws = tokens(s)[:5]
            if len(ws) == 5 and len(contenido(ws)) >= 2:
                vistos[tuple(ws)].append((ci, origen, num))
    rep = [(g, o) for g, o in vistos.items() if len({c for c, _, _ in o}) >= 2]
    rep = [(g, o) for g, o in rep if not elegidos or any(c in elegidos for c, _, _ in o)]
    rep.sort(key=lambda x: -len(x[1]))
    STATS["comienzos"] = len(rep)
    if not rep:
        print("Ninguno.")
        return
    for g, occ in rep[:maximo]:
        print(f"- «{' '.join(g)}…» — " + ", ".join(f"cap. {c + 1} ({o}:{n})" for c, o, n in occ[:8]))


def inventarios(caps, maximo, elegidos):
    print("\n## Inventarios anafóricos\n")
    print("Párrafos con tres o más oraciones seguidas que empiezan igual («Pensó en…», «No…», «Era…»). Pueden sostener una insistencia de la voz o recapitular motivos ya establecidos; conviene leerlos juntos.\n")
    por_inicio = defaultdict(list)
    for ci, (_, lineas) in enumerate(caps):
        if elegidos and ci not in elegidos:
            continue
        for origen, num, l in lineas:
            if not es_texto(l) or es_dialogo(l):
                continue
            inicios = []
            for o in ORACION.findall(l):
                ws = tokens(o)
                if ws:
                    inicios.append(" ".join(ws[:2]) if ws[0] in ("pensó", "era", "fue", "había", "sabía", "tenía") or ws[0] in NOMBRES else ws[0])
            mejor, racha, prev = None, 1, None
            for ini in inicios:
                racha = racha + 1 if ini == prev else 1
                if racha >= 3 and (mejor is None or racha > mejor[1]):
                    mejor = (ini, racha)
                prev = ini
            if mejor:
                por_inicio[mejor[0]].append((ci, origen, num, mejor[1]))
    por_inicio = {k: v for k, v in por_inicio.items() if len(v) >= 2 and len(k) > 1}
    STATS["inventarios"] = sum(len(v) for v in por_inicio.values())
    if not por_inicio:
        print("Ninguno que se repita en dos o más párrafos.")
        return
    for ini, occ in sorted(por_inicio.items(), key=lambda x: -len(x[1]))[:maximo]:
        caps_ = sorted({c + 1 for c, _, _, _ in occ})
        lugares = ", ".join(f"{o}:{n}" for _, o, n, _ in occ[:10])
        print(f"- «{ini.capitalize()}…»: {len(occ)} párrafos en {len(caps_)} capítulos — {lugares}" + (" …" if len(occ) > 10 else ""))


# ---------------------------------------------------------------- negaciones

def informe_negaciones(caps, maximo, elegidos):
    print("\n# Negaciones y abstenciones\n")
    print("Oraciones de la narración (fuera del habla). Una negación registra una expectativa activa o acredita un rasgo o un vínculo por lo que un personaje no hace; el recuento sirve para encontrar las segundas y leerlas. «Abstenciones» son negaciones de habla o intervención («no preguntó», «sin aprovechar», «agradeció que no…»).\n")
    print("| Cap. | Oraciones | Empiezan con negación | «sin + infinitivo» (cada 10.000 palabras) | «no… ni» | Abstenciones |")
    print("|---|---:|---:|---:|---:|---:|")
    detalle = []
    for ci, (_, lineas) in enumerate(caps):
        ors = oraciones_narrativas(lineas)
        n_pal = palabras(lineas)
        neg = [(o, n, t) for o, n, t in ors if NEG_INICIO.match(t)]
        sin = [(o, n, t) for o, n, t in ors if any(es_infinitivo(m.group(1)) for m in SIN_PALABRA.finditer(t))]
        noni = [(o, n, t) for o, n, t in ors if NO_NI.search(t)]
        abst = [(o, n, t) for o, n, t in ors if ABSTENCION.search(t)]
        print(f"| {ci + 1} | {len(ors)} | {len(neg)} ({pct(len(neg), len(ors))}) | {len(sin)} ({por10k(len(sin), n_pal)}) | {len(noni)} | {len(abst)} |")
        detalle.append((ci, neg, abst))
    print("\n## Ejemplos para leer\n")
    for ci, neg, abst in detalle:
        if not elegido(ci, elegidos):
            continue
        print(f"### Cap. {ci + 1}\n")
        if abst:
            print("Abstenciones:")
            for o, n, t in abst[:maximo]:
                print(f"- {o}:{n} {t[:200]}")
        vistos = {(o, n, t) for o, n, t in abst}
        resto = [x for x in neg if x not in vistos]
        if resto:
            print("\nOtras oraciones que empiezan con negación:")
            for o, n, t in resto[:maximo]:
                print(f"- {o}:{n} {t[:200]}")
        print()


# ---------------------------------------------------------------- designaciones

def informe_designaciones(caps, alias, maximo):
    print("\n# Designaciones\n")
    print("Cómo nombra la narración (fuera del habla, con las acotaciones) a cada personaje, por capítulo. Un cambio de designación es un acontecimiento de la voz; una alternancia sin patrón perceptible es un hábito. Los epítetos se cuentan por forma: decide al leerlos a quién se refieren.\n")
    parrafos = [narracion_por_parrafo(lineas) for _, lineas in caps]
    ncap = len(caps)
    cab = " | ".join(f"Cap. {i + 1}" for i in range(ncap))
    sep = "---:|" * ncap

    # Nombres propios más frecuentes.
    cuenta = [Counter() for _ in caps]
    for ci, ps in enumerate(parrafos):
        for _, _, t in ps:
            for w in PALABRA.findall(t):
                if w.lower() in NOMBRES and w[0].isupper():
                    cuenta[ci][w] += 1
    tot = Counter()
    for c in cuenta:
        tot.update(c)
    if tot:
        print("## Nombres en la narración\n")
        print(f"| Nombre | {cab} |\n|---|{sep}")
        for w, _ in tot.most_common(maximo):
            print(f"| {w} | " + " | ".join(str(cuenta[ci][w]) if cuenta[ci][w] else "·" for ci in range(ncap)) + " |")

    # Nombres compuestos (en cualquier parte del texto): partes usadas por separado en la narración.
    pares = Counter()
    for _, lineas in caps:
        for _, _, l in lineas:
            if es_texto(l):
                ms = list(PALABRA.finditer(l))
                for i in range(len(ms) - 1):
                    if l[ms[i].end():ms[i + 1].start()] != " ":
                        continue
                    a, b = ms[i].group(0), ms[i + 1].group(0)
                    if len(a) >= 2 and len(b) >= 2 and a[0].isupper() and a[1:].islower() and b[0].isupper() and b[1:].islower():
                        if a.lower() in NOMBRES and b.lower() in NOMBRES:
                            pares[(a, b)] += 1
    if pares:
        print("\n## Partes de un nombre compuesto\n")
        print("Uso por separado de cada parte de un nombre completo (p. ej., nombre de pila y apellido). Los cambios entre párrafos contiguos muestran si la alternancia sigue un patrón.\n")
        print(f"| Nombre completo | Forma | {cab} |\n|---|---|{sep}")
        cambios_txt = []
        for (a, b) in sorted(pares, key=lambda p: -pares[p]):
            completo = re.compile(rf"\b{a} {b}\b")
            solo_a = re.compile(rf"\b{a}\b(?! {b}\b)")
            solo_b = re.compile(rf"(?<!\b{a} )\b{b}\b")
            filas = {"completo": [], a: [], b: []}
            cambios = []
            for ps in parrafos:
                fc, fa, fb, sec = 0, 0, 0, []
                for _, _, t in ps:
                    c, x, y = len(completo.findall(t)), len(solo_a.findall(t)), len(solo_b.findall(t))
                    fc, fa, fb = fc + c, fa + x, fb + y
                    if x and not y:
                        sec.append("a")
                    elif y and not x:
                        sec.append("b")
                filas["completo"].append(fc)
                filas[a].append(fa)
                filas[b].append(fb)
                cambios.append(sum(1 for i in range(1, len(sec)) if sec[i] != sec[i - 1]))
            if sum(filas[a]) + sum(filas[b]) < 3:
                continue
            print(f"| {a} {b} | «{a} {b}» | " + " | ".join(str(v) if v else "·" for v in filas["completo"]) + " |")
            print(f"|  | «{a}» | " + " | ".join(str(v) if v else "·" for v in filas[a]) + " |")
            print(f"|  | «{b}» | " + " | ".join(str(v) if v else "·" for v in filas[b]) + " |")
            if any(cambios):
                cambios_txt.append(f"- {a} ↔ {b}: " + ", ".join(f"cap. {i + 1}: {v}" for i, v in enumerate(cambios) if v))
        if cambios_txt:
            print("\nCambios entre menciones sucesivas en párrafos distintos:")
            print("\n".join(cambios_txt))

    # Epítetos.
    ep = [Counter() for _ in caps]
    for ci, ps in enumerate(parrafos):
        for _, _, t in ps:
            for m in EPITETO_RX.finditer(t):
                sig = m.group(2)
                if sig and sig[0].isupper():
                    continue
                ep[ci][m.group(1).lower()] += 1
    tot_ep = Counter()
    for c in ep:
        tot_ep.update(c)
    filas_ep = [(f, n) for f, n in tot_ep.most_common() if n >= 2]
    if filas_ep:
        print("\n## Epítetos\n")
        print("Determinante + sustantivo que designa a una persona («el joven», «la mujer», «aquel desconocido»), sin contar los títulos seguidos de nombre («la señora Albers»).\n")
        print(f"| Forma | {cab} |\n|---|{sep}")
        for f, _ in filas_ep[:maximo]:
            print(f"| {f} | " + " | ".join(str(ep[ci][f]) if ep[ci][f] else "·" for ci in range(ncap)) + " |")

    # Alias declarados.
    if alias:
        print("\n## Alias declarados\n")
        print(f"| Personaje | Forma | {cab} |\n|---|---|{sep}")
        for nombre, formas in alias:
            todas = [nombre] + formas
            for k, f in enumerate(todas):
                if k == 0:
                    rx = re.compile(rf"\b{re.escape(f)}\b")
                else:
                    cuerpo = re.escape(f[1:]) if len(f) > 1 else ""
                    rx = re.compile(rf"\b[{f[0].upper()}{f[0].lower()}]{cuerpo}\b")
                vals = [sum(len(rx.findall(t)) for _, _, t in ps) for ps in parrafos]
                print(f"| {nombre if k == 0 else ''} | «{f}» | " + " | ".join(str(v) if v else "·" for v in vals) + " |")


# ---------------------------------------------------------------- comienzos

def informe_comienzos(caps, maximo):
    print("\n# Comienzos de oración\n")
    print("Primeras palabras de las oraciones narrativas, por capítulo. Muchas oraciones seguidas que empiezan con el mismo nombre o la misma estructura producen una cadencia de inventario; decide al leerlas si pertenece a la voz.\n")
    print("| Cap. | Oraciones | Primeras palabras más frecuentes | Nombres al comienzo | Pares más frecuentes |")
    print("|---|---:|---|---|---|")
    for ci, (_, lineas) in enumerate(caps):
        ors = oraciones_narrativas(lineas)
        n = len(ors)
        primeras, pares_, nombres = Counter(), Counter(), Counter()
        for _, _, t in ors:
            ws = PALABRA.findall(t)
            if not ws:
                continue
            primeras[ws[0]] += 1
            if len(ws) > 1:
                pares_[f"{ws[0]} {ws[1]}"] += 1
            if ws[0].lower() in NOMBRES:
                nombres[ws[0]] += 1
        p = " · ".join(f"{w} {100 * k / n:.0f} %" for w, k in primeras.most_common(5)) if n else "·"
        nm = " · ".join(f"{w} {100 * k / n:.0f} %" for w, k in nombres.most_common(3)) if nombres else "·"
        pr = " · ".join(f"{w} ({k})" for w, k in pares_.most_common(4)) if pares_ else "·"
        print(f"| {ci + 1} | {n} | {p} | {nm} | {pr} |")


# ---------------------------------------------------------------- cierres

PRET_IRREG = {
    "puso", "pusieron", "hizo", "hicieron", "fue", "fueron", "tuvo", "tuvieron",
    "dijo", "dijeron", "vio", "vieron", "dio", "dieron", "trajo", "trajeron",
    "vino", "vinieron", "pudo", "pudieron", "supo", "supieron", "quiso", "quisieron",
    "anduvo", "anduvieron", "estuvo", "estuvieron", "condujo", "condujeron",
    "produjo", "produjeron", "redujo", "redujeron", "sostuvo", "sostuvieron",
    "mantuvo", "mantuvieron", "detuvo", "detuvieron", "retuvo", "retuvieron",
    "obtuvo", "obtuvieron", "contuvo", "contuvieron", "deshizo", "deshicieron",
    "compuso", "compusieron", "dispuso", "dispusieron", "expuso", "expusieron",
    "propuso", "propusieron", "supuso", "supusieron", "repuso", "repusieron",
}


def etiqueta_cierre(parrafo):
    """Tipo de cierre según el último párrafo y su última oración."""
    if es_dialogo(parrafo):
        habla, _ = partir_dialogo(parrafo)
        return "réplica breve" if len(PALABRA.findall(" ".join(habla))) <= 8 else "diálogo"
    ultima = [o for o in ORACION.findall(parrafo) if PALABRA.search(o)]
    ultima = ultima[-1] if ultima else parrafo
    pret = [
        w for w in PALABRA.findall(ultima)
        if w.lower() in PRET_IRREG or (re.search(r"(?:ó|aron|ieron)$", w.lower()) and len(w) > 3)
    ]
    if len(pret) >= 3:
        return "serie de gestos"
    if pret:
        return "gesto"
    return "narración"


def informe_cierres(caps, elegidos):
    print("\n# Cierres de sección\n")
    print("Último párrafo de cada sección (separadas por *** o encabezados), con su última oración. Varios cierres del mismo tipo seguidos —una réplica breve, un gesto contenido de objeto— vuelven previsibles los finales.\n")
    print("| Cap. | Secciones | Tipos de cierre |")
    print("|---|---:|---|")
    listados = []
    tot_tipos = Counter()
    tot_secs = 0
    for ci, (titulo, lineas) in enumerate(caps):
        secs = secciones(lineas)
        tipos = []
        filas = []
        for k, sec in enumerate(secs, 1):
            origen, num, par = sec[-1]
            et = etiqueta_cierre(par)
            tipos.append(et)
            tot_tipos[et] += 1
            tot_secs += 1
            ultima = [o.strip() for o in ORACION.findall(par) if o.strip()]
            filas.append(f"{k}. [{et}] {origen}:{num} {(ultima[-1] if ultima else par)[:180]}")
        resumen_ = ", ".join(f"{t} {n}" for t, n in Counter(tipos).most_common())
        print(f"| {ci + 1} | {len(secs)} | {resumen_} |")
        listados.append((ci, titulo, filas))
    if tot_secs >= 4:
        gestos = tot_tipos["gesto"] + tot_tipos["serie de gestos"]
        if gestos / tot_secs >= 0.70:
            print(f"\nObservación: {gestos}/{tot_secs} secciones ({100 * gestos / tot_secs:.0f} %) cierran en gesto físico; conviene comprobar si se volvió plantilla.")
        else:
            dom, n_dom = tot_tipos.most_common(1)[0]
            if n_dom / tot_secs >= 0.70:
                print(f"\nObservación: {n_dom}/{tot_secs} secciones ({100 * n_dom / tot_secs:.0f} %) cierran como «{dom}»; conviene comprobar si se volvió plantilla.")
    for ci, titulo, filas in listados:
        if elegido(ci, elegidos):
            print(f"\n### Cap. {ci + 1}. {titulo}\n")
            print("\n".join(filas))


# ---------------------------------------------------------------- ritmo

REPORTADO = re.compile(
    r"\b(?:dijo|pidió|preguntó|contestó|respondió|avisó|explicó|aseguró|confirmó|indicó|advirtió|comentó|añadió|contó)"
    r"\s+(?:a\s+[^\W\d_]+\s+)?(?:que|si|cuándo|dónde|qué|cuánto|cómo|quién)\b",
    re.IGNORECASE,
)
COMODINES = re.compile(
    r"\b(?:algo|eso|esto|aquello|cosa|cosas|lado|sitio|parte|punto|lugar|extremo|tramo)\b",
    re.IGNORECASE,
)
DOS_PUNTOS_NARR = re.compile(r"(?<!\d):(?!\d)")


def percentil(vals, p):
    if not vals:
        return 0.0
    xs = sorted(vals)
    k = (len(xs) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


def informe_ritmo(caps):
    print("\n# Ritmo y puntuación narrativa\n")
    print("Largo de las oraciones narrativas (fuera del habla), proporción de diálogo directo, diálogo reportado en indirecto («dijo/pidió/preguntó que/si…», c/10.000 pal.), comodines vagos («algo/eso/lado/sitio/parte/extremo…», c/10.000 pal.) y puntuación narrativa (`;`, `:`, `¿`, `¡`). Sirve para ver si la prosa modula el pulso o se vuelve plana u oblicua.\n")
    print("| Cap. | % diálogo | Reportado /10k | Comodines /10k | Med. oración | p10–p90 | `;` | `:` | `¿` | `¡` | Párrafos ≤20 pal. |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    meds, tot_punt = [], Counter()
    all_lens = []
    tot_rep, tot_com, tot_pal = 0, 0, 0
    for ci, (_, lineas) in enumerate(caps):
        ors = oraciones_narrativas(lineas)
        lens = [len(PALABRA.findall(t)) for _, _, t in ors if PALABRA.search(t)]
        all_lens.extend(lens)
        n_habla = sum(len(PALABRA.findall(t)) for _, _, t in habla_total(lineas))
        n_narr = sum(len(PALABRA.findall(t)) for _, _, t in narracion_por_parrafo(lineas))
        tot_w = n_habla + n_narr
        tot_pal += tot_w
        p_dial = f"{100 * n_habla / tot_w:.1f} %" if tot_w else "·"
        med = statistics.median(lens) if lens else 0.0
        meds.append(med)
        p10, p90 = percentil(lens, 0.1), percentil(lens, 0.9)
        narr_txt = "\n".join(t for _, _, t in narracion_por_parrafo(lineas))
        full_txt = "\n".join(l for _, _, l in lineas if es_texto(l))
        rep = len(REPORTADO.findall(narr_txt))
        com = len(COMODINES.findall(full_txt))
        tot_rep += rep
        tot_com += com
        sc = narr_txt.count(";")
        col = len(DOS_PUNTOS_NARR.findall(narr_txt))
        qm = narr_txt.count("¿")
        ex = narr_txt.count("¡")
        tot_punt.update({";": sc, ":": col, "¿": qm, "¡": ex})
        p_narr = [l.strip() for _, _, l in lineas if es_texto(l) and not es_dialogo(l)]
        cortos = sum(1 for p in p_narr if len(PALABRA.findall(p)) <= 20)
        print(f"| {ci + 1} | {p_dial} | {por10k(rep, tot_w)} | {por10k(com, tot_w)} | {med:.1f} | {p10:.0f}–{p90:.0f} | {sc or '·'} | {col or '·'} | {qm or '·'} | {ex or '·'} | {cortos}/{len(p_narr)} |")
    if len(caps) >= 2 and all_lens:
        rep_vol = tot_rep * 10000 / tot_pal if tot_pal else 0.0
        com_vol = tot_com * 10000 / tot_pal if tot_pal else 0.0
        print(f"\nVolumen: mediana {statistics.median(all_lens):.1f} palabras/oración (p10–p90: {percentil(all_lens, 0.1):.0f}–{percentil(all_lens, 0.9):.0f}); rango de medianas por capítulo: {min(meds):.1f}–{max(meds):.1f}; diálogo reportado: {rep_vol:.1f} c/10.000 pal.; comodines vagos: {com_vol:.1f} c/10.000 pal.")
        ceros = [s for s in (";", ":", "¿", "¡") if tot_punt[s] == 0]
        if len(ceros) >= 3 and len(caps) >= 3:
            print(f"Observación: la narración no usa {' '.join(ceros)} en todo el volumen; conviene comprobar si corresponde a la voz o a sobrecontención.")
        if rep_vol >= 28.0 and tot_rep >= 15:
            print(f"Observación: densidad alta de diálogo reportado ({rep_vol:.1f} c/10.000 pal.); conviene revisar si escenas vivas, despedidas o conflictos ganan pasando a diálogo directo.")
        if com_vol >= 115.0 and tot_com >= 40:
            print(f"Observación: densidad alta de comodines vagos ({com_vol:.1f} c/10.000 pal.); conviene revisar si la prosa o el diálogo recurren a «eso/algo/lado/sitio/parte» donde un referente concreto daría mayor claridad.")


# ---------------------------------------------------------------- variedad

def informe_variedad(caps, marcadores, variedad, maximo, elegidos):
    print("\n# Variedad de la lengua\n")
    preset = PRESETS.get(variedad) if variedad else None
    if preset:
        print(f"Variedad declarada: {variedad}. Las familias marcadas con ⚠ son ajenas a ella.\n")
    else:
        print("Sin variedad declarada (--variedad): se muestran todas las familias sin juzgarlas.\n")
    print("Marcas firmes por defecto, ampliables con --marcador. Una marca no es un error: se compara con la variedad que fija el proyecto. Las palabras compartidas por varias variedades no figuran.\n")
    familias = VARIEDAD + marcadores
    cab = " | ".join(f"Cap. {i + 1}" for i in range(len(caps)))
    print(f"| Familia | {cab} |\n|---|" + "---:|" * len(caps))
    ejemplos = defaultdict(list)
    for etq, rx in familias:
        r = re.compile(rx, re.IGNORECASE)
        vals = []
        for ci, (_, lineas) in enumerate(caps):
            k = 0
            for origen, num, l in lineas:
                if not es_texto(l):
                    continue
                for m in r.finditer(l):
                    k += 1
                    if elegido(ci, elegidos) and len(ejemplos[etq]) < maximo:
                        ejemplos[etq].append(f"cap. {ci + 1} ({origen}:{num}) «{m.group(0).strip()}»")
            vals.append(k)
        marca = " ⚠" if preset and etq in preset["ajenas"] and sum(vals) else ""
        print(f"| {etq}{marca} | " + " | ".join(str(v) if v else "·" for v in vals) + " |")
    # Perfecto compuesto en el habla.
    fila_h, fila_n, ej_perf = [], [], []
    for ci, (_, lineas) in enumerate(caps):
        habla = habla_total(lineas)
        n_h = max(1, sum(len(PALABRA.findall(t)) for _, _, t in habla))
        k_h = 0
        for origen, num, t in habla:
            for m in PERFECTO.finditer(t):
                k_h += 1
                if elegido(ci, elegidos) and len(ej_perf) < maximo:
                    ej_perf.append(f"cap. {ci + 1} ({origen}:{num}) «{m.group(0)}»")
        k_n = sum(len(PERFECTO.findall(t)) for _, _, t in narracion_por_parrafo(lineas))
        fila_h.append(f"{k_h} ({k_h * 1000 / n_h:.1f}‰)" if k_h else "·")
        fila_n.append(str(k_n) if k_n else "·")
    marca = " (revisar)" if preset and preset["perfecto"] and any(f != "·" for f in fila_h) else ""
    print(f"| perfecto compuesto en el habla{marca} | " + " | ".join(fila_h) + " |")
    print(f"| perfecto compuesto en la narración | " + " | ".join(fila_n) + " |")
    if preset and preset["perfecto"]:
        print("\nEn esta variedad lo terminado suele ir en pretérito simple aunque sea reciente («Llamó», «Esta mañana me pasé…»); el compuesto queda para lo que sigue abierto o la experiencia («nunca he ido»). Revisa los casos del habla uno por uno.")
    if ejemplos or ej_perf:
        print("\n## Ejemplos\n")
        for etq, xs in ejemplos.items():
            print(f"- **{etq}**: " + "; ".join(xs))
        if ej_perf:
            print("- **perfecto compuesto en el habla**: " + "; ".join(ej_perf))


# ---------------------------------------------------------------- referencias al pasado

def informe_retro(caps, maximo, elegidos):
    print("\n# Referencias al pasado\n")
    print("Frases que vuelven sobre algo anterior, en el diálogo y en la narración. Cada una se comprueba contra la fuente (el pasaje, el documento o el calendario del volumen) antes de darla por buena.\n")
    total = 0
    for ci, (titulo, lineas) in enumerate(caps):
        if not elegido(ci, elegidos):
            continue
        hallazgos = []
        for origen, num, l in lineas:
            if not es_texto(l):
                continue
            for frase in ORACION.findall(l):
                cats = [etq for etq, rx in RETRO if re.search(rx, frase, re.IGNORECASE)]
                if cats:
                    hallazgos.append((origen, num, cats, frase.strip()))
        if not hallazgos:
            continue
        total += len(hallazgos)
        print(f"## {ci + 1}. {titulo} ({len(hallazgos)})\n")
        for origen, num, cats, frase in hallazgos[: maximo * 4]:
            print(f"- {origen}:{num} [{', '.join(cats)}] {frase[:220]}")
        if len(hallazgos) > maximo * 4:
            print(f"- … {len(hallazgos) - maximo * 4} más (usa --capitulos para acotar)")
        print()
    if not total:
        print("Ninguna.")


# ---------------------------------------------------------------- principal

def parse_capitulos(spec, n):
    if not spec:
        return set()
    elegidos = set()
    for parte in spec.split(","):
        parte = parte.strip()
        if "-" in parte:
            a, b = parte.split("-", 1)
            elegidos.update(range(int(a) - 1, int(b)))
        elif parte:
            elegidos.add(int(parte) - 1)
    return {c for c in elegidos if 0 <= c < n}


def parse_pares(valores, nombre):
    out = []
    for p in valores:
        if "=" not in p:
            sys.exit(f"{nombre} sin «etiqueta=regex»: {p}")
        etq, rx = p.split("=", 1)
        try:
            re.compile(rx)
        except re.error as e:
            sys.exit(f"Expresión no válida en «{etq}»: {e}")
        out.append((etq.strip(), rx))
    return out


INFORMES = ["habitos", "negaciones", "designaciones", "comienzos", "cierres", "ritmo", "variedad", "retro"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rutas", nargs="+")
    ap.add_argument("--informe", default="todo")
    ap.add_argument("--capitulos", default="")
    ap.add_argument("--variedad", choices=sorted(PRESETS), default=None)
    ap.add_argument("--alias", action="append", default=[])
    ap.add_argument("--patron", action="append", default=[])
    ap.add_argument("--marcador", action="append", default=[])
    ap.add_argument("--encabezado", default=DEFAULT_ENCABEZADO)
    ap.add_argument("--max", type=int, default=12)
    a = ap.parse_args()

    pedidos = [x.strip() for x in a.informe.split(",") if x.strip()]
    if "todo" in pedidos:
        pedidos = INFORMES
    desconocidos = [x for x in pedidos if x not in INFORMES]
    if desconocidos:
        sys.exit(f"Informe desconocido: {', '.join(desconocidos)}. Opciones: {', '.join(INFORMES)}, todo.")

    construcciones = list(CONSTRUCCIONES) + parse_pares(a.patron, "Patrón")
    marcadores = parse_pares(a.marcador, "Marcador")
    alias = []
    for p in a.alias:
        if "=" not in p:
            sys.exit(f"Alias sin «Nombre=forma1|forma2»: {p}")
        nombre, formas = p.split("=", 1)
        alias.append((nombre.strip(), [f.strip() for f in formas.split("|") if f.strip()]))

    caps = leer_capitulos(a.rutas, a.encabezado)
    detectar_nombres(caps)
    elegidos = parse_capitulos(a.capitulos, len(caps))
    if "habitos" in pedidos:
        informe_habitos(caps, construcciones, a.max, elegidos)
    if "negaciones" in pedidos:
        informe_negaciones(caps, a.max, elegidos)
    if "designaciones" in pedidos:
        informe_designaciones(caps, alias, a.max)
    if "comienzos" in pedidos:
        informe_comienzos(caps, a.max)
    if "cierres" in pedidos:
        informe_cierres(caps, elegidos)
    if "ritmo" in pedidos:
        informe_ritmo(caps)
    if "variedad" in pedidos:
        informe_variedad(caps, marcadores, a.variedad, a.max, elegidos)
    if "retro" in pedidos:
        informe_retro(caps, a.max, elegidos)


if __name__ == "__main__":
    main()
