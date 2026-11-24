# Resultados de la evaluación comparativa A/B (`Sin skills` vs. `Kit v1.0.0`)

Informe consolidado del benchmark público y documentado del **Kit de Narrativa `v1.0.0`** sobre **12 novelas completas** (**151 capítulos**, **281.777 palabras** en total) generadas de forma autónoma sobre premisas 100 % originales en español.

- **Protocolo aplicado:** [`PROTOCOLO.md`](PROTOCOLO.md)
- **Tabla maestra por corrida (`M01`–`M12`):** [`registro_corridas.csv`](registro_corridas.csv)
- **Resumen apareado de deltas A/B:** [`comparativa_ab_resumen.csv`](comparativa_ab_resumen.csv)
- **Informes completos de `habitos.py`:** [`datos_habitos/`](datos_habitos/)
- **Manuscritos y reseñas ciegas originales:** [`../corridas/`](../corridas/)

---

## 1. Diseño ejecutado y control metodológico

1. **Matriz factorial balanceada `2 × 3 × 2` (12 corridas):**
   - **2 modelos autores** de distinta escala, ambos con nivel de esfuerzo fijado en `high`: **`6.2 Sol`** (modelo pequeño) y **`Astra 6.2`** (modelo grande).
   - **3 premisas originales contrastadas** de [`../premisas/`](../premisas/), entregadas sin [`00_GUIA_DEL_EVALUADOR.md`](../premisas/00_GUIA_DEL_EVALUADOR.md):
     - [`02 - Horror de duelo`](../premisas/02%20-%20Horror%20de%20duelo/02_Horror_de_duelo.md) — terror psicológico íntimo sin monstruo visible, subtexto emocional y duelo real.
     - [`21 - Whodunit cerrado`](../premisas/21%20-%20Whodunit%20cerrado/21_Whodunit_cerrado.md) — misterio deductivo clásico en isla incomunicada, 8 sospechosos, continuidad horaria y juego limpio (*fair play*).
     - [`26 - Renacido como dragón`](../premisas/26%20-%20Renacido%20como%20dragón/26_Renacido_como_dragon.md) — fantasía *isekai* con ventanas de estado, cuerpo no humano, barrera lingüística y fricción social.
   - **2 condiciones simétricas:**
     - **`sin_skills` (línea base):** [`plantilla-base-sin-skills.md`](plantilla-base-sin-skills.md), con las 7 skills retiradas/desactivadas del entorno para impedir cualquier invocación implícita.
     - **`con_kit_v1.0.0`:** [`../plantilla-modo-lector.md`](../plantilla-modo-lector.md), con el flujo completo de las 7 skills de `v1.0.0`.
2. **Evaluación doble ciego con 2 jueces externos independientes:**
   - Cada manuscrito fue evaluado en sesión limpia bajo [`prompt-juez-ciego.md`](prompt-juez-ciego.md) por **dos modelos externos de familias distintas** (`Juez 1` = **Gemini Neon**; `Juez 2` = **Opus 5.5**), sin acceso a la premisa, al plan ni a la condición experimental.
   - *Nota metodológica sobre el panel:* se descartó incluir una tercera evaluación realizada por el propio modelo autor (`6.2 Sol` / `Astra 6.2`) porque el comportamiento de memoria y contexto de sesión en la aplicación cliente no permitía garantizar aislamiento estricto frente a las corridas de escritura. En consecuencia, todas las medias reportadas corresponden al promedio directo (`50 % / 50 %`) de los dos jueces externos independientes.

---

## 2. Resultado principal A/B (Panel de jueces ciegos)

En esta muestra, `Kit v1.0.0` supera a la línea base `Sin skills` en **las 6 comparaciones apareadas (`6/6`)** tanto en la **media del panel** como en el juez más severo (**`Juez 2`**), y obtiene **4 victorias y 2 empates (`0 derrotas`)** en **`Juez 1`**.

> **Alcance y límites.** Se trata de una sola corrida por combinación de modelo, premisa y condición (6 pares en total), evaluada por dos jueces que también son modelos de lenguaje. Las diferencias son modestas (`+0,32` de media sobre 10). El resultado es una señal consistente a favor del kit, no una prueba estadística; repetir las corridas o ampliar premisas y jueces permitiría confirmarlo o matizarlo.

### 2.1. Resumen agregado por modelo y condición

| Modelo | Condición | Media Global | `Juez 1` Global | `Juez 2` Global | Prosa y voz | Personajes y diál. | Estructura y ritmo | Coherencia y reglas | Experiencia / cierre |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`6.2 Sol`** | `sin_skills` | 7,02 | 7,37 | 6,67 | 7,40 | 7,18 | 6,38 | 6,55 | 7,43 |
| **`6.2 Sol`** | **`con_kit_v1.0.0`** | **7,43** | **7,73** | **7,13** | **7,78** | **7,62** | **6,95** | **6,98** | **7,72** |
| *Delta `6.2 Sol`* | *Kit vs. Base* | ***+0,42*** | ***+0,37*** | ***+0,47*** | ***+0,38*** | ***+0,43*** | ***+0,57*** | ***+0,43*** | ***+0,28*** |
| **`Astra 6.2`** | `sin_skills` | 7,70 | 8,20 | 7,20 | 8,25 | 8,18 | 7,12 | 6,88 | 8,07 |
| **`Astra 6.2`** | **`con_kit_v1.0.0`** | **7,92** | **8,27** | **7,57** | **8,57** | **8,42** | **7,13** | **7,10** | **8,22** |
| *Delta `Astra 6.2`* | *Kit vs. Base* | ***+0,22*** | ***+0,07*** | ***+0,37*** | ***+0,32*** | ***+0,23*** | ***+0,02*** | ***+0,22*** | ***+0,15*** |
| **Global (12 corridas)** | `sin_skills` → `Kit` | **7,36 → 7,68 (`+0,32`)** | **7,78 → 8,00 (`+0,22`)** | **6,93 → 7,35 (`+0,42`)** | **7,83 → 8,18 (`+0,35`)** | **7,68 → 8,02 (`+0,33`)** | **6,75 → 7,04 (`+0,29`)** | **6,72 → 7,04 (`+0,33`)** | **7,75 → 7,97 (`+0,22`)** |

### 2.2. Comparación apareada en las 12 corridas (`M01`–`M12`)

| ID | Modelo | Premisa | Condición | Título del manuscrito | `J1` Global *(Prosa)* | `J2` Global *(Prosa)* | Media Global | Delta Par |
|---|---|---|---|---|---:|---:|---:|---:|
| `M01` | `6.2 Sol` | `26 - Dragón` | `sin_skills` | *(Cap. 1: La cáscara)* | 7,2 *(7,6)* | 6,3 *(6,8)* | 6,75 | — |
| `M02` | `6.2 Sol` | `26 - Dragón` | `con_kit_v1.0.0` | *La casa de la orilla* | **7,7 *(8,4)*** | **7,0 *(7,4)*** | **7,35** | **`+0,60`** |
| `M03` | `6.2 Sol` | `02 - Duelo` | `sin_skills` | *Desde el lavadero* | 7,5 *(7,8)* | 6,9 *(6,4)* | 7,20 | — |
| `M04` | `6.2 Sol` | `02 - Duelo` | `con_kit_v1.0.0` | *(Cap. 1: El largo de los paños)* | **7,9 *(8,4)*** | **7,4 *(7,0)*** | **7,65** | **`+0,45`** |
| `M05` | `6.2 Sol` | `21 - Whodunit` | `sin_skills` | *La raya de pleamar* | 7,4 *(8,2)* | 6,8 *(7,6)* | 7,10 | — |
| `M06` | `6.2 Sol` | `21 - Whodunit` | `con_kit_v1.0.0` | *Mientras la isla callaba* | **7,6 *(8,4)*** | **7,0** *(7,1)* | **7,30** | **`+0,20`** |
| `M07` | `Astra 6.2` | `26 - Dragón` | `sin_skills` | *Lo que cabe bajo un ala* | 8,2 *(8,8)* | 7,3 *(8,3)* | 7,75 | — |
| `M08` | `Astra 6.2` | `26 - Dragón` | `con_kit_v1.0.0` | *(Cap. 1: El lado frío)* | 8,2 *(8,8)* | **7,6 *(8,7)*** | **7,90** | **`+0,15`** |
| `M09` | `Astra 6.2` | `02 - Duelo` | `sin_skills` | *Hasta donde se oye* | 8,3 *(8,8)* | 7,7 *(7,4)* | 8,00 | — |
| `M10` | `Astra 6.2` | `02 - Duelo` | `con_kit_v1.0.0` | *Una noche tranquila* | **8,5 *(9,0)*** | **7,8 *(7,9)*** | **8,15** | **`+0,15`** |
| `M11` | `Astra 6.2` | `21 - Whodunit` | `sin_skills` | *Al pie de la fotografía* | 8,1 *(8,8)* | 6,6 *(7,4)* | 7,35 | — |
| `M12` | `Astra 6.2` | `21 - Whodunit` | `con_kit_v1.0.0` | *La parte de abajo* | 8,1 *(8,9)* | **7,3 *(8,1)*** | **7,70** | **`+0,35`** |

**Lecturas clave del cuadro:**
- **La mejora es mayor con el juez más severo:** `Juez 2` (media `7,14`, más sensible a opacidad sintáctica, agujeros lógicos y muletillas) registra un salto neto de **`+0,42` puntos globales** con el kit (`+0,47` en `6.2 Sol` y `+0,37` en `Astra 6.2`), y en `Astra 6.2` sube **Prosa y voz en `+0,53`** (`7,70 → 8,23`, ganando en las tres premisas). Con solo 6 pares, es una tendencia observada en esta muestra, no una regla general.
- **Reducción de la brecha de escala:** `6.2 Sol` con `Kit v1.0.0` (`7,43` global; `7,13` en `Juez 2`) recorta más de la mitad de la distancia que lo separaba de `Astra 6.2` sin skills (`7,70` global; `7,20` en `Juez 2`), superando incluso a `Astra` base en el *whodunit* según `Juez 2` (`7,0` en `M06` vs. `6,6` en `M11`).
- **Único retroceso parcial de subdimensión:** en `M06` (`Sol` + `21 - Whodunit`), aunque sube la nota global en ambos jueces (`7,10 → 7,30`), `Juez 2` baja `Prosa y voz` de `7,6` a `7,1` por exceso de microcoreografía de objetos y elipsis espaciales en los primeros capítulos.

---

## 3. Métricas estilométricas uniformes (`habitos.py --variedad neutro`)

| ID | Modelo / Condición | Premisa | Caps. | Palabras | % Diál. | Report. `/10k` | Comod. `/10k` | `habría`+part. `/10k` | `podía` `/10k` | Med. oración *(p10–p90)* | Párraf. `≤20` pal. | Punt. `;:¿¡` | Cierre gesto | `Var⚠` | Alertas |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|---:|
| `M01` | `Sol` base | P26 | 24 | 26.155 | 3,4 % | 23,0 | 154,2 | 11,5 | 45,9 | 13,0 *(5–24)* | 7,5 % | `11/33/0/0` | 83,3 % | 1 | 4 |
| `M02` | `Sol` **Kit v1.0** | P26 | 16 | 35.589 | **8,5 %** | **16,3** | **114,1** | **10,7** | **36,8** | 13,0 *(6–23)* | 7,4 % | `0/3/2/0` | **63,6 %** | **0** | **1** |
| `M03` | `Sol` base | P02 | 12 | 18.830 | 7,8 % | 14,9 | 126,4 | 25,0 | 52,6 | 13,0 *(5–24)* | 9,4 % | `0/0/6/0` | 75,0 % | 0 | 5 |
| `M04` | `Sol` **Kit v1.0** | P02 | 9 | 19.554 | **11,1 %** | 15,3 | **101,3** | 28,1 | **51,1** | 15,0 *(6–27)* | 4,7 % | `0/0/8/0` | **44,4 %** | 0 | **2** |
| `M05` | `Sol` base | P21 | 16 | 18.933 | 21,6 % | 32,7 | 88,2 | 3,2 | 21,1 | 11,0 *(5–21)* | 25,3 % | `0/2/0/0` | 50,0 % | 0 | 3 |
| `M06` | `Sol` **Kit v1.0** | P21 | 11 | 28.293 | 17,8 % | **30,0** | **84,8** | 8,5 | 29,7 | 13,0 *(6–22)* | 10,0 % | `0/0/3/0` | 71,4 % | 0 | 4 |
| `M07` | `Astra` base | P26 | 15 | 27.600 | 6,2 % | 6,9 | 101,8 | 17,0 | 18,5 | 12,0 *(4–25)* | 20,4 % | `12/7/2/0` | 60,7 % | 1 | 2 |
| `M08` | `Astra` **Kit v1.0** | P26 | 11 | 35.021 | **11,1 %** | **6,0** | 115,1 | **14,8** | 21,7 | 13,0 *(5–27)* | 15,2 % | **`26/12/3/2`** | **57,1 %** | 3 | 2 |
| `M09` | `Astra` base | P02 | 9 | 17.026 | 13,9 % | 2,3 | 86,3 | 18,8 | 17,0 | 14,0 *(4–31)* | 11,4 % | `4/3/6/1` | 55,6 % | 7 | 0 |
| `M10` | `Astra` **Kit v1.0** | P02 | 8 | 20.601 | **15,6 %** | 4,9 | 102,9 | 25,2 | 33,0 | 14,0 *(6–30)* | 11,1 % | **`4/6/11/0`** | 87,5 % | 9 | 1 |
| `M11` | `Astra` base | P21 | 8 | 16.463 | 24,7 % | 10,9 | 108,7 | 9,7 | 12,8 | 13,0 *(5–26)* | 23,9 % | `14/5/1/0` | 50,0 % | 2 | 1 |
| `M12` | `Astra` **Kit v1.0** | P21 | 8 | 17.712 | 18,4 % | **10,7** | **92,0** | 13,6 | **10,2** | 14,0 *(5–28)* | 17,6 % | **`5/9/9/0`** | 50,0 % | 2 | 2 |

*(Nota: `habría+part. /10k` y `podía /10k` se calcularon complementariamente sobre el texto completo a raíz de los hallazgos reiterados de los jueces ciegos; las demás columnas provienen directamente de `habitos.py`).*

### Patrones cuantitativos observados

1. **Mayor desarrollo escénico por capítulo (menos fragmentación):** en ambos modelos, el kit reduce la subdivisión en capítulos cortos y aumenta el desarrollo por escena (`6.2 Sol` pasa de `17,3` capítulos y `21.306` palabras de media a `12,0` capítulos y `27.812` palabras, **`+30,5 %`** de extensión; `Astra 6.2` pasa de `10,7` capítulos y `20.363` palabras a `9,0` capítulos y `24.445` palabras, **`+20,0 %`**).
2. **Limpieza clara de hábitos en `6.2 Sol`:** comodines vagos cae un **`-18,6 %`** (`122,9 → 100,1 /10k`), diálogo reportado baja de `23,5` a `20,5 /10k` (en P26 cae un `-29 %`, duplicando además el diálogo directo `3,4 % → 8,5 %`), los cierres en gesto bajan de `69,4 %` a `59,8 %` y las alertas totales de `habitos.py` se reducen un **`-41,7 %`** (`12 → 7`).
3. **Relieve expresivo en `Astra 6.2`, pero con tres señales de vigilancia:** `Astra` con el kit mantiene el diálogo reportado en niveles muy bajos (`7,2 /10k`, un tercio de `Sol`) y más que duplica la puntuación expresiva en narración (`35 → 87` signos `; : ¿ ¡`), pero muestra:
   - persistencia de peninsularismos en variedad `neutro` (`Var⚠` pasa de `10` a `14` casos totales, concentrados en `coger/cogió` y `apetece` en `M10`);
   - repunte puntual de cierres en gesto físico en `M10` (`87,5 %`, `7/8` capítulos);
   - aumento de estructuras conjeturales (`habría + participio` en `25,2 /10k` y `podía` en `33,0 /10k` en `M10`), paralelo al observado en `Sol` para la misma premisa de duelo (`28,1` y `51,1 /10k`).

---

## 4. Auditoría de verificación literal de las reseñas

Siguiendo la regla 3.4 de [`PROTOCOLO.md`](PROTOCOLO.md), se auditaron programáticamente las **24 reseñas** contra sus respectivos manuscritos:

- **Exactitud de citas literales (`100 %`):** sobre **638 citas textuales** extraídas de las 24 reseñas (`200` en `Juez 1` y `438` en `Juez 2`, excluyendo 9 cadenas entrecomilladas que correspondían a etiquetas estructurales o propuestas de corrección gramatical del propio reseñador), **el 100 % existe en el manuscrito evaluado** (`631` idénticas carácter por carácter y `7` con corte limpio de elipsis o barra de diálogo). La exigencia de verificación literal incorporada en [`prompt-juez-ciego.md`](prompt-juez-ciego.md) eliminó por completo las citas fabricadas.
- **Exactitud de recuentos y observaciones fácticas:** los conteos léxicos reportados por `Juez 2` coinciden con el texto real (`podía/podían`: `100` en `M04`, `73` en `M06`, `22` en inicio de frase y `119` totales en `M02`; `ganas de`: `23` en `M04`; `se le ocurrió`: `11` en `M04`; `sitio/sitios`: `27` en `M06`; `a la altura`: `19` y `de canto`: `17` en `M02`; `coger` conjugado: `6` en `M10`; `paño/paños`: `18`, `taza/tazas`: `17` y `plato/platos`: `13` en `M05`).
- **Matices interpretativos contrastados contra el texto:**
  - En `M10` (*Una noche tranquila*), `Juez 1` señaló como posible contradicción perceptiva que Ada piense que la voz desde el pasillo no puede verla y aun así la voz comente su pelo recién cortado o sus ojos apretados; `Juez 2` lo leyó en cambio como consecuencia coherente de la regla epistémica (la voz sabe todo lo que *Ada* sabe de sí misma, aunque solo hable fuera de su campo visual). Aun así, la observación de `Juez 1` identifica una fricción real de lectura: Ada no registra extrañeza ante esa asimetría en el Capítulo 5.
  - En `M06` (*Mientras la isla callaba*), `Juez 1` objetó que Orel mencione un «negativo» y muestre una copia en papel horas después; en el texto (`L991`), el negativo aludido era de diecisiete años atrás (*«uno de aquella noche»*), pero la crítica central sigue siendo válida porque nunca se aclara cómo obtuvo una copia positiva en papel de la foto tomada la víspera en una isla incomunicada.
  - En `M12` (*La parte de abajo*), la colisión espacial señalada por `Juez 2` en la despensa al final de la primera toma se confirma línea por línea (`L521` sitúa allí a Irdo escuchando el final y `L759` sitúa allí a Sesca tomando agua en ese mismo intervalo).

---

## 5. Desempeño cualitativo por premisa

### `02 - Horror de duelo` (`M03→M04` en `Sol`, `M09→M10` en `Astra`)
- **Qué resolvió el kit:** es la premisa donde el kit alcanza el techo literario más alto del experimento (`8,5` en `Juez 1` con `9,0` en Prosa, `7,8` en `Juez 2` para `M10`; y salto de `+1,15` en `Coherencia y reglas` para `Sol`, de `6,90` a `8,05`). Las corridas con kit eliminan los coqueteos inconclusos con terror físico que dañaban a ambas líneas base (la marca húmeda bajo la taza en `M03`; los pasos e imitación corporal detrás de la puerta en `M09`) y sostienen una regla epistémica limpia: la voz no asusta, complace.
- **Dónde queda margen:** ambos modelos rellenan el segundo cuarto del libro con anécdotas de clientes de costura de estructura muy similar, abusan del condicional conjetural (`podía`, `habría + participio`) y resuelven la desaparición final de la voz de forma algo abrupta entre el penúltimo capítulo y el epílogo.

### `21 - Whodunit cerrado` (`M05→M06` en `Sol`, `M11→M12` en `Astra`)
- **Qué resolvió el kit:** mejora la nota global en ambos modelos (`+0,20` en `Sol`, `+0,35` en `Astra`, con `+0,70` en `Juez 2` sobre `Astra`: `6,6 → 7,3` y salto de Prosa `7,4 → 8,1`). Las pistas materiales (el reflejo invertido del lazo de Sesca en `M12`, la ranura y la pasarela en `M06`) respetan el juego limpio y los cierres éticos sobre la autoría y los nombres borrados figuran entre los pasajes mejor valorados de todo el corpus.
- **Dónde queda margen:** es el género más castigado en `Estructura` y `Coherencia` (`6,2–7,5`). Se repiten cuatro problemas específicos: (1) planta arquitectónica difícil de visualizar cuando la deducción depende de líneas de visión o tabiques; (2) ventanas temporales de 1 a 3 minutos demasiado estrechas e inaudibles en casas donde antes se oía todo; (3) tramo central armado como «carrusel de confesiones» por turnos sobre faltas documentales menores; y (4) confesiones finales de los asesinos demasiado dóciles o sin resistencia dramática.

### `26 - Renacido como dragón` (`M01→M02` en `Sol`, `M07→M08` en `Astra`)
- **Qué resolvió el kit:** produce el mayor salto individual de toda la matriz en `6.2 Sol` (**`+0,60` global**, de `6,75` a `7,35`, con `+0,70` en `Prosa`, `+0,60` en `Personajes` y `+0,60` en `Estructura`), corrigiendo la fragmentación extrema de `M01` (24 capítulos con 3,4 % de diálogo y un clímax donde ni el lector entendía qué intentaba hacer el dragón). En `Astra` (`M08`), eleva `Prosa y voz` a `8,75` de media (`8,8` / `8,7`) y afina la construcción social del miedo a través de oficios y consecuencias económicas reales.
- **Dónde queda margen:** en las **4 corridas** (con y sin kit), los dos jueces señalan de manera unánime la misma fractura de diseño: por pudor literario ante el tropo comercial, los modelos sabotean o dejan a medio usar las **ventanas de estado (*LitRPG*)** y el **pasado humano (*isekai*)** pedidos por la premisa (además de omitir cualquier intento creíble de un adulto alfabetizado por trazar signos simples o justificar por qué falla al intentarlo).

---

## 6. Línea de base diagnóstica para `v1.1.0` (frentes verificados)

Sin prescribir todavía cambios sobre las skills, la evidencia convergente de las 12 corridas y los informes de `habitos.py` delimita con precisión los cuellos de botella reales del kit `v1.0.0`:

1. **Claridad referencial y sintáctica frente a la sobre-elipsis:** en momentos de alta carga emocional o transición de escena, evitar la sobreexplicación deriva ocasionalmente en frases sobre-subordinadas, sujetos tácitos ambiguos tras cambio de foco (`él/ella`, `su madre`) o aperturas en acertijo que exigen releer para saber quién hace qué sobre qué.
2. **Control efectivo de variedad lingüística y dobletes léxicos:** la declaración de `español neutro` sigue dejando pasar peninsularismos en `Astra` (`coger`, `apetece`, leísmo, perfecto compuesto en diálogo reciente), mezclas sin territorio en `Sol` (`encimera/calcetín` junto a `departamento/medianera` sin voseo) y alternancia involuntaria de sinónimos regionales para el mismo objeto doméstico dentro de una misma obra (`refrigerador`/`nevera`, `acera`/`vereda`, `anteojos`/`gafas`/`lentes`).
3. **Orientación espacial temprana en escenarios de geometría crítica:** el *blocking* breve de crisis no basta cuando toda una novela depende de la planta de un edificio, líneas ópticas o una obra hidráulica (P21 y P26); las piezas arquitectónicas necesitan fijarse con anclas estables antes de que empiece la deducción o el peligro.
4. **Saturación deliberativa (`podía` / `habría + participio`) y no detección actual en `habitos.py`:** en novelas introspectivas, la deliberación en condicional e imperfecto modal se acumula hasta frenar las decisiones en hipótesis de lo no hecho, sin que el analizador actual la visibilice como familia medible.
5. **Diferenciación del ingenio y la temperatura emocional en el reparto:** cuando la voz narrativa es seca, irónica y contenida, los secundarios episódicos tienden a hablar con el mismo filo elíptico del protagonista, y las reacciones ante muertes o confesiones graves pecan a veces de exceso de civilidad administrativa.
6. **Integración honesta de premisas de género y dosificación del tramo medio:** cuando una premisa fija elementos de género explícitos (como ventanas de estado o reencarnación en P26), desactivarlos por pudor estético rompe la coherencia tanto como abusar de ellos; y en el segundo acto, tanto las viñetas costumbristas repetidas (P02/P26) como las rondas simétricas de secretos secundarios (P21) diluyen la urgencia principal.
