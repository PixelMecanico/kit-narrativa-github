# Kit de Narrativa (`v1.0.0`)

Un conjunto modular de **7 skills editoriales**, un **analizador estilométrico en Python (`habitos.py`)** y un **banco de 26 premisas originales de evaluación** diseñados para escribir, editar y evaluar ficción larga en español con modelos de lenguaje (LLMs), evitando los vicios habituales de la prosa generada por IA.

> **Primera publicación pública (`v1.0.0`):** consolida múltiples iteraciones internas de diseño, calibración editorial y correcciones sobre textos largos antes de abrir el repositorio.
>
> *English summary:* A modular suite of 7 narrative-craft agent skills (`SKILL.md`), a zero-dependency Spanish prose analyzer (`habitos.py`), and 26 original long-form benchmark premises built for Spanish long-form fiction with LLMs.

---

## ¿Qué problema resuelve?

Escribir un relato corto con un LLM es relativamente sencillo; sostener una novela de decenas de miles de palabras sin que la voz se aplane y la continuidad se rompa es otro problema. En textos largos, los modelos tienden a repetir patrones muy concretos:

- **Certificación:** explicar en otra capa lo que la escena ya mostró (*«comprendió que nada volvería a ser igual»*), como si el narrador buscara aprobar ante un evaluador imaginario.
- **Desplazamiento y abstenciones narradas:** cuando se les prohíbe explicar emociones, pasan a certificarlas por lo que el personaje *no* hace (*«no preguntó»*, *«agradeció que no insistiera»*).
- **Sub-realización conductista:** por miedo a sobreexplicar, vacían decisiones clave de presión interior y las reducen a coreografías frías de manos, tazas y puertas.
- **Deriva a escala de volumen:** construcciones que funcionan bien aisladas (*«como si»*, *«no era X, sino Y»*, cierres en gesto físico, comodines vagos como *«algo/eso/el otro lado»*) pero se vuelven plantilla al cabo de diez capítulos.
- **Contaminación de contexto al autoevaluarse:** un modelo que conoce el esquema cree que un subtexto o una regla del mundo se entienden en la página solo porque los leyó en el plan.

Este kit ataca esos fallos separando responsabilidades, añadiendo **contrapesos explícitos contra la sobrecorrección** en cada regla y combinando criterio editorial cualitativo con medición objetiva en Python.

---

## Arquitectura del kit (7 skills modulares)

El principio rector es separar tres decisiones: **qué pasa** (planificación), **qué se sabe en cada momento** (información) y **cómo se dice** (prosa).

| Skill | Qué gobierna | Cuándo se carga |
|---|---|---|
| [`narrativa`](skills/narrativa/SKILL.md) | Centro del kit: flujo de trabajo, archivos del proyecto (`proyecto.md`, `voz.md`, `plan.md`, `memoria.md`, `estado.md`), precedencia y niveles de delegación | Al iniciar, escribir o retomar un proyecto |
| [`narrativa-planificacion`](skills/narrativa-planificacion/SKILL.md) | Arcos, capítulos, economía de reparto, mapas operativos (3–4 piezas), escaleras escénicas y proporción del clímax | Al planificar o preparar una escena sin ficha |
| [`narrativa-informacion`](skills/narrativa-informacion/SKILL.md) | Propiedad cognitiva, focalización, subtexto, certificación, sub-realización conductista y claridad de reglas operativas | Al preparar, redactar o revisar escenas |
| [`narrativa-prosa`](skills/narrativa-prosa/SKILL.md) | Cadencia, granularidad, diálogo directo vs. reportado, designaciones, variedad del español y hábitos a escala de volumen (`habitos.py`) | Al redactar y pulir prosa |
| [`narrativa-memoria`](skills/narrativa-memoria/SKILL.md) | Canon vigente, calendario, continuidad, conocimiento por personaje, motivos y compromisos abiertos | Al consultar canon, revisar continuidad o cerrar capítulo |
| [`narrativa-evaluacion`](skills/narrativa-evaluacion/SKILL.md) | Lentes de plan, capítulo y volumen; criterios para decidir qué corregir, conservar o rechazar de una reseña | Al diagnosticar, editar o contrastar críticas |
| [`narrativa-agentes`](skills/narrativa-agentes/SKILL.md) | Controles independientes con aislamiento de contexto: **Auditor** (con plan), **Revisor** (sin plan) y **Lector ciego** (solo texto) | Solo cuando se autoriza delegar controles en subagentes |

### Carga progresiva y compatibilidad

- **No se cargan todas a la vez:** aunque el kit completo suma ~184 KB entre los 7 `SKILL.md`, `narrativa` indica cargar cada especialista únicamente en el paso que le corresponde.
- **Funcionan también por separado:** puedes usar `narrativa-prosa` para pulir un capítulo existente o `narrativa-evaluacion` para diagnosticar un borrador sin adoptar el flujo completo.
- **Autocontenidas:** cada `SKILL.md` incluye todo lo obligatorio de su procedimiento por si el entorno no permite ejecutar scripts o abrir referencias auxiliares.
- **Estándar abierto:** siguen el formato `SKILL.md`, compatible con agentes como Codex, Claude Code, Antigravity y otros clientes que soporten skills locales.

---

## Analizador de hábitos en español (`habitos.py`)

Incluido en [`skills/narrativa-prosa/scripts/habitos.py`](skills/narrativa-prosa/scripts/habitos.py), es un script de **Python 3 sin dependencias externas** que analiza un manuscrito completo (`.md` o `.txt`) para detectar lo que ningún capítulo aislado deja ver. **Sirve tanto para textos escritos con IA como para escritores y editores humanos.**

Qué mide:
- **Hábitos y deriva (`habitos`):** construcciones por capítulo cada 10.000 palabras (`como si`, lectura de rostros, `no era X sino Y`, verbos de saber, pausas/lentitudes), frases e imágenes repetidas entre capítulos e inventarios anafóricos.
- **Negaciones y abstenciones (`negaciones`):** oraciones iniciadas con negación, `sin + infinitivo`, `no… ni` y abstenciones de habla/intervención.
- **Designaciones (`designaciones`):** cómo nombra el narrador a cada personaje recurrente (nombre, apellido, epítetos) y si el patrón deriva sin motivo.
- **Comienzos y cierres (`comienzos`, `cierres`):** repetición de aperturas de oración y listado lado a lado de los cierres de cada sección (con alerta si un mismo tipo de cierre supera el 70 %).
- **Ritmo y puntuación (`ritmo`):** mediana y percentiles `p10–p90` del largo de oración, porcentaje de diálogo directo, diálogo reportado (`/10k`), comodines vagos (`/10k`), párrafos breves y uso de `; : ¿ ¡`.
- **Variedad del español (`variedad`):** detección de marcas ajenas a la variedad elegida (`neutro`, `peninsular`, `americano`, `rioplatense`) y uso del pretérito perfecto compuesto en diálogo.
- **Referencias al pasado (`retro`):** intervalos, días, horas, cantidades y citas de documentos para facilitar la auditoría de continuidad.

### Uso rápido

```bash
python skills/narrativa-prosa/scripts/habitos.py ruta/al/manuscrito/ --variedad neutro
```

Opciones útiles:

```bash
# Ejecutar solo el informe de ritmo y variedad sobre un archivo único
python skills/narrativa-prosa/scripts/habitos.py novela.md --informe ritmo,variedad --variedad rioplatense

# Agrupar designaciones de un personaje con alias o epítetos
python skills/narrativa-prosa/scripts/habitos.py manuscrito/ --alias "Konrad=el capitán|el viejo"

# Ver todas las opciones disponibles
python skills/narrativa-prosa/scripts/habitos.py --help
```

### Ejemplo del formato de salida (`--informe ritmo`)

```markdown
| Cap. | % diálogo | Reportado /10k | Comodines /10k | Med. oración | p10–p90 | `;` | `:` | `¿` | `¡` | Párrafos ≤20 pal. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 17.5 % | 3.9 | 122.0 | 13.0 | 5–24 | · | · | · | · | 11/45 |
| 4 | 28.0 % | 16.6 | 74.7 | 10.0 | 5–20 | · | · | 1 | · | 10/38 |
| 9 | 24.4 % | 3.6 | 43.6 | 13.0 | 5–27 | · | 1 | · | · | 6/36 |
| 11 | 14.1 % | · | 96.3 | 11.0 | 4–23 | · | · | 2 | 1 | 3/30 |

Volumen: mediana 13.0 palabras/oración (p10–p90: 5–24); diálogo reportado: 3.8 c/10.000 pal.; comodines vagos: 94.4 c/10.000 pal.
```

---

## Cómo empezar a usarlo

### 1. Instalar las skills en tu agente
Copia las 7 carpetas dentro de [`skills/`](skills/) al directorio de skills de tu herramienta de preferencia (la carpeta de skills del proyecto o tu carpeta global de skills).

### 2. Elegir cómo trabajar
- **Modo coautor (por defecto):** pide al agente trabajar con `narrativa` sobre tu idea o manuscrito. El kit distingue qué decides tú y qué queda delegado.
- **Modo lector autónomo (sin spoilers):** usa [`plantilla-modo-lector.md`](plantilla-modo-lector.md) como instrucción inicial junto con una premisa. El modelo diseña la obra en privado (Etapa I) y luego entrega los capítulos limpios en Markdown sin revelar giros ni planificación en el chat (Etapa II).

### 3. Probar o evaluar modelos con el banco de premisas
En [`premisas/`](premisas/) encontrarás **26 premisas 100 % originales** en español (numeradas `01`–`26`) que cubren fantasía, ciencia ficción, terror, comedia, romance, tragedia moral, misterio, *noir*, epistolar, narrador poco fiable y reparto coral:
- [`00_INDICE.md`](premisas/00_INDICE.md) — listado completo.
- [`00_CATALOGO_DE_PREMISAS.md`](premisas/00_CATALOGO_DE_PREMISAS.md) — sinopsis por género.
- [`00_GUIA_DEL_EVALUADOR.md`](premisas/00_GUIA_DEL_EVALUADOR.md) — qué sesgo o fallo típico de LLM pone a prueba cada premisa *(pensada para el evaluador humano, no para entregar al modelo autor)*.

---

## Evaluación pública (`v1.0.0`)

El repositorio incluye un primer benchmark público y documentado ([`evaluacion/RESULTADOS_V1.0.md`](evaluacion/RESULTADOS_V1.0.md)), ejecutado sobre **12 novelas completas** (**151 capítulos, 281.777 palabras** en total) generadas íntegramente a partir de premisas originales de [`premisas/`](premisas/) bajo [`evaluacion/PROTOCOLO.md`](evaluacion/PROTOCOLO.md):

- **Diseño comparativo A/B (matriz balanceada `2 × 3 × 2`):** línea base **sin skills** ([`plantilla-base-sin-skills.md`](evaluacion/plantilla-base-sin-skills.md), con las skills retiradas del entorno para impedir invocación implícita) frente a **Kit de Narrativa `v1.0.0`** ([`plantilla-modo-lector.md`](plantilla-modo-lector.md)) sobre 3 premisas contrastadas (`26 - Renacido como dragón`, `02 - Horror de duelo` y `21 - Whodunit cerrado`) en dos escalas de modelo (`6.2 Sol` y `Astra 6.2`, esfuerzo `high`).
- **Panel doble ciego y verificación literal:** 2 jueces externos independientes de familias distintas (`Juez 1` = **Gemini Neon**; `Juez 2` = **Opus 5.5**) evaluando únicamente el manuscrito limpio con [`prompt-juez-ciego.md`](evaluacion/prompt-juez-ciego.md) (excluyendo autoevaluación del modelo autor para evitar contaminación por contexto de cuenta), con **100 % de exactitud comprobada** sobre las **638 citas textuales** de las 24 reseñas.

| Modelo | Condición | Media Global | `Juez 1` | `Juez 2` | Prosa y voz | Comodines `/10k` | Reportado `/10k` | Alertas `habitos.py` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **`6.2 Sol`** | Sin skills | 7,02 | 7,37 | 6,67 | 7,40 | 122,9 | 23,5 | 12 |
| **`6.2 Sol`** | **Con Kit `v1.0.0`** | **7,43 (`+0,42`)** | **7,73 (`+0,37`)** | **7,13 (`+0,47`)** | **7,78 (`+0,38`)** | **100,1 (`-18,6 %`)** | **20,5** | **7 (`-41,7 %`)** |
| **`Astra 6.2`** | Sin skills | 7,70 | 8,20 | 7,20 | 8,25 | 98,9 | 6,7 | 3 |
| **`Astra 6.2`** | **Con Kit `v1.0.0`** | **7,92 (`+0,22`)** | **8,27 (`+0,07`)** | **7,57 (`+0,37`)** | **8,57 (`+0,32`)** | 103,3 | 7,2 | 5 |

En esta muestra pequeña, `Kit v1.0.0` supera a la línea base en **las 6 comparaciones apareadas (`6/6`)** tanto en la media del panel como en `Juez 2` (`0` derrotas en `Juez 1`). Las mejoras son modestas (en torno a `+0,3` puntos sobre 10) y proceden de una sola corrida por combinación, así que deben leerse como una señal consistente, no como una prueba concluyente. Todos los datos crudos están disponibles en [`evaluacion/registro_corridas.csv`](evaluacion/registro_corridas.csv), [`evaluacion/comparativa_ab_resumen.csv`](evaluacion/comparativa_ab_resumen.csv), [`evaluacion/datos_habitos/`](evaluacion/datos_habitos/) y [`corridas/`](corridas/).

---

## Estructura del repositorio

```text
.
├── README.md
├── LICENSE                        # Apache 2.0
├── NOTICE
├── plantilla-modo-lector.md       # Prompt de delegación con el kit (lectura sin spoilers)
├── skills/                        # Kit v1.0.0 (7 skills modulares en formato SKILL.md)
│   ├── narrativa/
│   ├── narrativa-planificacion/
│   ├── narrativa-informacion/
│   ├── narrativa-prosa/           # Incluye scripts/habitos.py
│   ├── narrativa-memoria/
│   ├── narrativa-evaluacion/
│   └── narrativa-agentes/         # Incluye references/pruebas.md
├── premisas/                      # Banco de 26 premisas originales (01–26) + guía del evaluador
├── corridas/                      # 12 manuscritos completos (Sol/Astra × Base/Kit) + 24 reseñas
└── evaluacion/                    # Protocolo, RESULTADOS_V1.0.md, tablas CSV y datos_habitos/
```

---

## Licencia

Este repositorio se distribuye bajo la **[Licencia Apache 2.0](LICENSE)** (ver también [`NOTICE`](NOTICE)).

- Puedes usar, modificar y redistribuir el kit, `habitos.py` y las premisas, incluso con fines comerciales, siempre que conserves el aviso de copyright y la licencia, e indiques los cambios que hagas.
- **Tus historias son tuyas:** las novelas, relatos o borradores que escribas *utilizando* estas skills o analices con `habitos.py` te pertenecen íntegramente y no quedan sujetos a esta licencia.
