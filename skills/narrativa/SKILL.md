---
name: narrativa
description: "Flujo de trabajo para novelas, seriales y fanfics: planificar, escribir capítulos, revisar y retomar un proyecto. Úsala en todo trabajo de ficción larga; indica qué otras skills del kit cargar."
metadata:
  version: "1.0.0"
---

# Narrativa: centro del kit

Este kit sirve para escribir ficción larga con el usuario. Esta skill define el flujo de trabajo, los archivos del proyecto, la precedencia y la autoridad. Cada oficio lo define su especialista; esta skill no lo repite.

## El kit

| Skill | Es dueña de | Léela cuando |
|---|---|---|
| `narrativa-planificacion` | Arcos, capítulos, escaleras escénicas, fichas de escena | Planificas, o vas a redactar sin ficha |
| `narrativa-informacion` | Qué información entra en una escena, de quién es y con qué precisión; certificación y subtexto | Preparas, redactas o revisas una escena |
| `narrativa-prosa` | Realización verbal, cadencia, granularidad, designaciones, variedad de la lengua y hábitos a escala de volumen | Redactas o pules |
| `narrativa-memoria` | Canon, calendario, continuidad, compromisos y registros para volver sobre el pasado | Consultas canon, vuelves sobre algo anterior, revisas continuidad o cierras un capítulo |
| `narrativa-evaluacion` | Diagnóstico y decisión sobre los hallazgos: lentes de plan, de capítulo y de volumen | Criticas, editas, haces la autorrevisión o decides qué hacer con lo que encontró una lectura |
| `narrativa-agentes` | Delegación y controles independientes: auditor, revisor y lector ciego | Solo con autorización de agentes (ver «Agentes») |

Lee cada skill cuando llegue su paso, no todas al principio. Cada especialista funciona sola para tareas locales —pulir un párrafo, consultar un dato— sin esta skill.

**Lo obligatorio está en cada SKILL.md.** Hay entornos que cargan una skill sin dar acceso a sus archivos auxiliares. Por eso cada SKILL.md contiene todo lo que su procedimiento exige; las referencias solo amplían, y el script de `narrativa-prosa` automatiza mediciones que esa skill describe para hacerlas a mano. Si una parte del kit no está accesible, sigue con lo que está, anótalo en `estado.md` y no la declares consultada ni ejecutada.

## Principios del kit

- **Tres decisiones separadas:** qué pasa (planificación), qué se sabe en cada momento (información) y cómo se dice (prosa). Mejorar la forma no autoriza a inventar conocimientos; ordenar la trama no autoriza a exponerla.
- **El canon es reserva, no lista de exposición.** Que algo sea verdadero no lo obliga a aparecer. Lo que solo está en el plan, tampoco llega al lector.
- **Coherencia completa, representación selectiva.** La coherencia física y causal de una escena no tiene huecos; su representación se elige. La página muestra lo que aporta algo o evita un error de lectura, y la experiencia de lectura va antes que el registro exhaustivo de lo que ocurre (`narrativa-prosa`, «Granularidad»).
- **Ni sobreexplicación ni conductismo vacío.** Contener la certificación no significa vaciar la interioridad ni reducir las decisiones decisivas a secuencias neutras de objetos y gestos (`narrativa-informacion`, «Sub-realización»). Cada regla del kit tiene contrapeso en ambos sentidos.
- **La convivencia, la espera, la contemplación y la interioridad son funciones válidas.** No se fabrica conflicto, giro, castigo o revelación para justificar una escena.
- **Intervención proporcionada:** la menor que resuelva un problema concreto. Si la mejora es dudosa, se conserva lo que funciona.
- **Lo que un lector informa sobre su lectura se responde con la página.** Una experiencia de lectura —una caída de atención, una duda, una desconfianza— no se refuta con la intención ni con la función de cada parte (`narrativa-evaluacion`, «Decidir sobre los hallazgos»).

## Roles y autoridad

El usuario es el director creativo; tú escribes y editas, salvo que el usuario elija otra división del trabajo. No le pidas datos que puedes recuperar de los archivos. Resuelve las elecciones creativas reversibles dentro de la delegación y deja abiertas las incógnitas que no impiden avanzar.

Separa la procedencia de cada decisión: instrucción del usuario, documento identificado o elección tuya dentro de la delegación. No atribuyas al usuario lo que decidiste tú.

| Nivel | Ejemplos | Tratamiento |
|---|---|---|
| Realización local | Diálogo, formulación, microestructura, transiciones, detalles compatibles | Resuélvelo sin consultar. |
| Cambio material delegado | Hecho duradero nuevo, reorganización entre capítulos, solución nueva | Hazlo si la delegación lo cubre; regístralo e infórmalo al entregar. |
| Decisión reservada | Alterar un hecho protegido, una relación fijada, un secreto o el alcance | Presenta una propuesta concreta y espera la decisión del usuario. |

Una solución que excede la delegación se queda como propuesta: no la introduzcas en la versión vigente ni la propagues como hecho. Mientras tanto, avanza en las partes independientes.

Distingue cuatro autorizaciones: aprobar el método, autorizar a planificar, autorizar a redactar y aprobar un resultado. Reconoce la que ya existe sin pedirla de nuevo y no pidas confirmación entre pasos ya autorizados. Una idea en discusión es una propuesta hasta que el encargo permita adoptarla.

## Precedencia

Ante fuentes en tensión, sigue este orden:

1. La instrucción vigente del usuario. Una instrucción nueva revisa las anteriores en su alcance. Si parece contradecir el canon sin querer, señala el conflicto antes de seguir. Si llega a mitad del trabajo, identifica qué partes afecta y rehazlas antes de entregar.
2. El canon establecido y las decisiones firmes (`proyecto.md`, `memoria.md`).
3. El plan autorizado (`plan.md`).
4. La voz de la obra (`voz.md` o la skill de voz de esa obra).
5. Los criterios de este kit.

No apliques el orden a ciegas: un resumen antiguo no prevalece sobre el manuscrito que resume, y una propuesta reciente no es canon. Cuando el resumen no alcance para decidir, consulta el pasaje. Cada especialista tiene además su desempate local.

## Archivos del proyecto

| Archivo | Contenido | Lo escribe |
|---|---|---|
| `proyecto.md` | Premisa, experiencia buscada, límites, delegación, decisiones reservadas, convenciones (incluida la variedad de la lengua), obra fuente | Esta skill |
| `voz.md` | Focalización, persona, tiempo, distancia, registro, cadencia, designaciones, identidad mental, muestras | Esta skill, con los esquemas de `narrativa-prosa` |
| `plan.md` | Horizonte del arco, próximo trabajo, decisiones firmes, alternativas abiertas, estado de ratificación | `narrativa-planificacion` |
| `memoria.md` | Canon, calendario, documentos y datos que se reutilizan, conocimiento y acceso, compromisos, incidencias | `narrativa-memoria` |
| `estado.md` | Punto de reanudación | Esta skill |

El manuscrito va aparte (`manuscrito/capitulo_XX.md` u otra organización ya establecida), sin fichas ni notas dentro de la prosa. Conserva los nombres y la estructura de un proyecto existente si cumplen su función. Crea los archivos cuando el proyecto empieza de verdad, no ante una pregunta teórica. Si existe una skill de voz para una obra concreta, `voz.md` remite a ella y no copia sus reglas.

Cada archivo tiene un solo escritor en cada momento. Guarda con el mecanismo persistente disponible y no afirmes que algo quedó guardado si la escritura falló.

### Plantillas mínimas

```markdown
# proyecto.md
## Premisa
## Experiencia buscada
## Límites
## Delegación
(qué puede decidir el escritor; qué debe informar al entregar)
## Decisiones reservadas al usuario
## Convenciones
- Variedad de la lengua: nombre y rasgos verificables (tratamiento plural, pasado reciente, tuteo o voseo, léxico de los objetos que vuelven; ver narrativa-prosa)
- Nombres de personajes, lugares e instituciones
- Extensión de capítulos y organización de los puntos de vista
## Obra fuente
(solo en fanfic: versión y continuidad; divergencias decididas; términos que la fuente fija con un sentido; personajes de la fuente que aparecen y dónde están verificadas sus capacidades)
```

```markdown
# voz.md
## Narración
(focalización, persona, tiempo verbal, distancia, registro)
## Cadencia
(párrafo narrativo, frase, línea aislada, densidad: ver narrativa-prosa)
## Identidad mental
(cómo percibe, asocia, recuerda, interpreta y habla la narración)
## Designaciones
(cómo nombra la narración a cada personaje recurrente; cuándo cambia y por qué)
## Diferencias por focalizador o tramo
## Recursos propios y motivos
(qué construcciones, imágenes o gestos pertenecen a qué voz y vuelven a propósito; lo que no figura aquí y se repite es un hábito a vigilar)
## Diálogo
(idiolecto de cada personaje)
## Muestras
(pasajes reales de la obra)
```

```markdown
# plan.md
## Horizonte del arco
## Próximo trabajo
(con estado: pendiente, ratificado por el usuario o adoptado por delegación)
## Decisiones firmes
## Alternativas abiertas
```

```markdown
# memoria.md
(estructura en narrativa-memoria)
## Canon vigente
## Calendario, documentos y datos que se reutilizan
## Candidatos
## Conocimiento y acceso
## Relaciones
## Compromisos
(incluye formulaciones del sentido, retornos de motivos y hallazgos aceptados con condición)
## Incidencias
```

```markdown
# estado.md
- Proyecto y línea:
- Manuscrito (versiones adoptadas):
- Memoria (reconciliada hasta):
- Plan (estado de ratificación):
- Controles hechos y pendientes:
- Hallazgos abiertos y decisión pendiente:
- Conflictos y dependencias:
- Próximas fechas de la historia (previstas en el calendario para el siguiente tramo):
- Partes del kit que no estuvieron accesibles:
- Siguiente operación:
```

### Iniciar un proyecto

Recupera lo que el usuario ya decidió. Distingue premisa, condiciones firmes, preferencias, propuestas y decisiones delegadas. Avanza con lo autorizado y resuelve las elecciones creativas reversibles dentro de la delegación, registradas como decisiones tuyas. Pregunta solo por una decisión importante que esté reservada o cuya ausencia impida avanzar con fidelidad, y hazlo después de presentar trabajo útil y alternativas concretas. No exijas entrevista, público objetivo, obras comparables, título definitivo ni desenlace para poder escribir.

Registra la procedencia de cada decisión (instrucción del usuario, documento identificado, elección del escritor dentro de su delegación) y su estado (vigente, propuesta, pendiente, deliberadamente abierta, no aplicable, sustituida). Una idea tentativa sigue siendo propuesta si el contexto no autoriza adoptarla. Una instrucción de cambio revisa la decisión anterior en su alcance: identifica los efectos retroactivos sin ampliar por tu cuenta lo que se cambió.

Los archivos pueden empezar breves; no rellenes fichas exhaustivas del mundo para demostrar preparación ni crees carpetas vacías. Si una sección crece hasta dificultar su consulta, pásala a un archivo propio y anótalo en `estado.md`.

- **Voz.** Describe cómo la narración percibe, asocia, recuerda, interpreta y habla; distingue la identidad mental de los tics de vocabulario. Declara la cadencia con los ejes de `narrativa-prosa` y las designaciones de los personajes recurrentes. Si no están declaradas, infiérelas del manuscrito vigente y regístralas como decisión tuya. Si hace falta, elige una voz provisional dentro de la delegación e identifícala como tuya. Usa como muestras pasajes reales de la obra cuando existan; no inventes muestras supuestamente aceptadas.
- **Variedad de la lengua.** La fija el usuario. Si solo hay un nombre («español neutro»), registra en `proyecto.md` los rasgos verificables que se siguen de él (`narrativa-prosa`, «Variedad de la lengua»), como decisión tuya, para que el cierre de cada capítulo pueda comprobarlos.
- **Fanfic.** Registra la versión y la continuidad de la obra fuente, las divergencias decididas y los términos que la fuente fija con un sentido que la divergencia cambia (un ordinal, un título, el nombre de un acontecimiento). Verifica las capacidades de los personajes de la fuente que aparezcan, igual que las de los personajes nuevos, aunque no sean el foco.

### Resolver fuentes en conflicto

Respeta las instrucciones explícitas vigentes, incluidas las que revisan decisiones anteriores. Examina el alcance y la procedencia de las demás fuentes:

- Corrige un registro derivado que copió mal el texto.
- Mantén como verdad privada una decisión autoral no revelada, sin trasladarla al conocimiento de los personajes ni del lector.
- Registra la incompatibilidad entre el manuscrito en uso y una decisión firme; resuélvela dentro del margen autorizado o plantea la decisión reservada.
- Conserva como pendientes los cambios aún no aplicados; no afirmes que el manuscrito ya los contiene.
- Consulta el material concreto si el resumen no basta para decidir.

### Trasladar un proyecto existente

Mapea primero sus documentos y versiones. Empieza por el arco activo y por las dependencias del próximo trabajo. Identifica los registros sin procedencia verificable y contrástalos cuando importen. No reescribas la obra ni reconstruyas toda su documentación solo para ajustarla a esta estructura. Si falta acceso a un documento, recupéralo por una vía autorizada o declara la dependencia; no lo reconstruyas de memoria.

## Flujos por tarea

### Conversar o explorar una premisa
Conversa y aporta ideas concretas. No escribas capítulos ni crees archivos de proyecto. Pregunta solo por decisiones que impidan avanzar con fidelidad, y después de ofrecer trabajo útil; el inicio no es un interrogatorio.

### Planificar
Sigue `narrativa-planificacion` y entrega el plan para su decisión. Pasa a la prosa solo con una autorización que cubra ese alcance: aprobación expresa del plan o delegación vigente.

### Escribir un capítulo
Es el flujo completo; aplícalo a cada capítulo de un proyecto.

1. **Preparar.** Atiende primero los pendientes de `estado.md` que afecten al capítulo. Identifica el plan vigente, la voz, el canon pertinente y la prosa cercana; relee pasajes cuando importen ritmo, gesto o subtexto, porque un resumen puede convertir una vacilación en una decisión. Ten a mano el calendario, los documentos reproducidos y los datos que se reutilizan (`narrativa-memoria`): cada vez que el capítulo vuelva sobre algo anterior, compruébalo ahí antes de escribirlo. Mira en el calendario las fechas previstas que caen dentro del capítulo —un viaje, un plazo, una cita— y comprueba que el plan decida qué hace el capítulo con cada una. Si el capítulo toca el sentido del arco, mira el registro de formulaciones. Si el plan no trae ficha de escena, prepárala con `narrativa-planificacion`. Selecciona la información con `narrativa-informacion`.
2. **Borrador completo.** Escribe todo el capítulo con `narrativa-prosa` y la voz de la obra, priorizando causalidad, claridad, progresión y transiciones; la prosa puede quedar áspera. No sustituyas el capítulo por un esquema o un resumen.
3. **Revisión de desarrollo.** Aplica las lentes de capítulo de `narrativa-evaluacion`, incluida la decisión de expandir o comprimir y la de los procedimientos que se repiten. Corrige aquí la estructura, antes de pulir.
4. **Pulido.** Trabaja frase por frase con `narrativa-prosa` y haz la auditoría silenciosa de `narrativa-informacion`. Compara el capítulo con los anteriores con el informe de hábitos de `narrativa-prosa` —o con su medición manual, si el script no está accesible— y corrige los moldes que señale para este capítulo.
5. **Continuidad.** Contrasta el capítulo con el canon, los capítulos previos y el plan mediante `narrativa-memoria`, empezando por sus referencias al pasado y siguiendo por las reglas del mundo y las fechas previstas. Es una revisión informada y se hace siempre.
6. **Cierre.** Corrige gramática, puntuación, consistencia de nombres, tipografía y pequeños defectos de estilo; comprueba la variedad de la lengua contra `proyecto.md` y las designaciones contra `voz.md`; relee el capítulo completo. Entrega la prosa limpia. Extrae los candidatos para la memoria y reconcílialos según la delegación; actualiza el calendario (con lo narrado y lo previsto), los documentos, los datos que se reutilizan, las formulaciones del sentido, los retornos de motivos y los hallazgos aceptados con condición; actualiza el plan si hubo descubrimientos y deja `estado.md` al día. Al cerrar una parte del volumen, haz además la revisión de volumen.

Con archivos disponibles, escribe el borrador en un archivo y haz los pasos 3 a 6 como ediciones reales; guarda una versión recuperable antes de cambios amplios. Sin archivos, aplica las lentes antes de entregar. Si un cambio posterior altera estructura, voz, información o hechos, repite los pasos afectados.

### Escribir varios capítulos
Aplica el flujo completo a cada uno y lleva un registro de avance por capítulo; no lo sustituyas por una lectura general del lote ni pulas el primero mientras los demás quedan como borradores sin revisar. Redacta los consecutivos sobre bases estabilizadas: escribe varios en paralelo solo si sus entradas, salidas y dependencias están fijadas, porque una desviación importante en un capítulo invalida lo que los siguientes suponían de él. Propaga los cambios relevantes antes de cerrar los posteriores y revisa entre ellos transiciones, información, relaciones, setups y payoffs. Actualiza la memoria y ejecuta el informe de hábitos después de cada capítulo, no al final del lote: los moldes y los deslices se acumulan y cuestan más cuanto más tarde se ven. Entrega solo las versiones finales y un resumen único del lote. Si el lote es demasiado extenso para revisarlo en una sola operación, divídelo y registra qué cubre cada revisión; no llames integral a una revisión por muestreo. Al terminar el lote o la parte, haz la revisión de volumen.

### Escribir una escena suelta o un fragmento
Versión breve del flujo: prepara la información, redacta, pule con la auditoría silenciosa y comprueba la continuidad si hay canon. Una escena exploratoria no fija canon por sí sola; después, registra lo que efectivamente quedó.

### Pulir o corregir un fragmento
Usa `narrativa-prosa`; añade `narrativa-informacion` si el pulido toca qué se sabe, quién lo sabe o cómo se interpreta. No hace falta un diagnóstico de desarrollo previo. Consulta `narrativa-memoria` solo si cambian hechos, accesos o relaciones. Una corrección formal no autoriza a inventar contenido: revisa solo lo afectado y no digas que revisaste todo el capítulo.

### Revisar el desarrollo de un texto
Diagnostica con `narrativa-evaluacion` y decide el alcance; cambia la selección de información con `narrativa-informacion`; realiza con `narrativa-prosa`; reconcilia con `narrativa-memoria` si cambiaron hechos, accesos o relaciones. Para el control de un capítulo ya escrito, usa el manuscrito como borrador del paso 2 y aplica los pasos siguientes sin reescribirlo entero.

### Evaluar
Sigue `narrativa-evaluacion`. Una evaluación tuya es informada; no la presentes como ciega. Si el usuario trae una evaluación ajena, `narrativa-evaluacion` dice cómo decidir sobre ella.

### Revisar un volumen o un tramo largo
Al cerrar una parte, al terminar un volumen o cuando el usuario pide revisar un manuscrito completo. Sigue la revisión de volumen de `narrativa-evaluacion`: primero la continuidad, después las lentes de volumen, después los hábitos de prosa y al final la revisión local de lo afectado. Estos problemas no se ven capítulo por capítulo; por eso tienen su propio paso.

### Mantener la memoria o revisar continuidad
Sigue `narrativa-memoria`.

### Retomar
Lee `estado.md`, contrasta versiones y pendientes y recupera las fuentes indicadas antes de depender de ellas. No reconstruyas el estado mezclando resúmenes de versiones distintas.

## Controles

Toda revisión tiene una forma informada, que haces tú con lo que sabes del proyecto; llámala así cuando la menciones. La forma independiente, otra ejecución sin tu contexto, solo existe con agentes, y tiene tres roles: el auditor examina qué pasa y qué se sabe; el revisor, cómo se dice; el lector ciego, la experiencia de lectura. Si el usuario no pidió independencia, no la registres como pendiente ni la anuncies.

Lo que encuentre una lectura —un control tuyo o independiente, el usuario o una reseña externa— se decide con las reglas de `narrativa-evaluacion` («Decidir sobre los hallazgos»). En síntesis: la comprensión y la experiencia se contrastan por separado; una duda se responde con un pasaje, no con el plan; la función de cada parte no refuta una caída de atención; y un problema del capítulo se resuelve en el capítulo, no en el plan siguiente.

## Agentes

No crees agentes ni delegues en ellos salvo que el usuario lo autorice de forma expresa, para el encargo actual o para un alcance que él defina. La autorización para escribir, planificar o revisar no incluye agentes. Si el usuario pide expresamente un control independiente —auditoría, revisión o lectura ciega—, eso autoriza agentes solo para ese control. Con autorización, lee `narrativa-agentes` y limita los agentes a lo autorizado.

## Entregar y detener

Entrega el producto pedido —prosa, plan, diagnóstico— sin fichas, auditorías ni administración dentro de la narración. Fuera de la prosa, informa en pocas líneas las decisiones materiales, las desviaciones del plan, los conflictos y lo pendiente. No muestres informes de cada paso salvo que te los pidan.

El kit existe para que el usuario dedique su atención a lo importante. Lo que puedes corregir dentro de la delegación —deslices de continuidad, moldes de prosa, explicaciones repetidas, marcas de otra variedad— corrígelo sin preguntar y menciónalo agrupado, en una línea. Lleva al usuario lo que solo él puede decidir.

Detén las revisiones cuando no queden problemas concretos relevantes y los cambios adicionales sean de mejora dudosa. Un efecto de lectura que un lector informó es un problema concreto, aunque cada parte del pasaje tenga función. Si un control necesario no pudo hacerse, dilo; no rebajes el estándar en silencio ni declares terminado lo que no lo está. Bloquea solo lo que depende de una incompatibilidad real.

Entrega, aceptación, revisión, reconciliación y aprobación del usuario no son sinónimos. Mantén separados estos ejes, en `estado.md` y en lo que informes:

| Eje | Estados |
|---|---|
| Texto | Preparación, borrador, revisado, adoptado para continuar |
| Controles | Hechos, parciales o pendientes, con versión y alcance |
| Hallazgos | Corregidos, rechazados con razón, aceptados con condición (en memoria) o pendientes de decisión |
| Memoria | Con novedades pendientes, o reconciliada con una versión identificada |
| Conflictos | Ninguno detectado, incidencia no bloqueante o dependencia bloqueada |
| Aprobación del usuario | No solicitada, pendiente o expresa |

## El punto de reanudación

`estado.md` es un punto de reanudación, no una bitácora: el historial de versiones y controles vive en sus informes, y aquí queda lo necesario para seguir. Mantén:

- proyecto, línea y archivos con sus versiones;
- versión adoptada de cada capítulo y alcance de lo leído;
- controles hechos y pendientes, y los hallazgos que esperan decisión;
- cambios sin reconciliar, conflictos y dependencias afectadas;
- decisiones reservadas y propuestas, separadas de lo vigente;
- las fechas de la historia previstas para el siguiente tramo, tomadas del calendario;
- las partes del kit que no estuvieron accesibles;
- siguiente operación autorizada y fuentes que necesita.

Actualízalo en los hitos cuya reconstrucción sería costosa. Ante una interrupción, registra qué archivos quedaron actualizados y cuáles no.
