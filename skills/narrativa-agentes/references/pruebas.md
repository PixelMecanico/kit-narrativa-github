# Comprobar el funcionamiento delegado

Usa estos casos al validar o ajustar el protocolo. No son pruebas ya ejecutadas. No lances un piloto sobre una obra real sin que el usuario autorice su alcance. Valida una regla en un texto distinto del que la originó: ese caso ya se conoce, y encontrarlo de nuevo no demuestra nada.

## Coordinación

| Caso | Conducta esperada |
|---|---|
| El productor encuentra una solución local mejor | La adopta dentro de su autonomía, sin consultar cada paso. |
| Un cambio afecta un capítulo que otro agente está escribiendo | Se comunica la dependencia antes de integrar resultados. |
| Dos agentes producen novedades incompatibles | Se reconcilian antes de escribir en la memoria compartida. |
| La coordinación solo recibió una sinopsis | No declara lectura ni aprobación de la prosa completa. |
| El usuario cambia una restricción durante la ejecución | Las tareas afectadas se reorientan y sus resultados se invalidan o reconcilian. |
| No hay subdelegación | La conversación principal despacha las solicitudes sin fingir agentes subordinados. |
| Falta un control por límites de ejecución | Se entrega un estado parcial o pendiente, sin cierre ficticio. |
| Una preferencia de estilo no resuelve un problema identificable | Se conserva la formulación que funciona. |

## Controles

| Caso | Conducta esperada |
|---|---|
| El lector recibió el plan | La lectura no se llama ciega: se repite con contexto limpio o se declara informada. |
| El revisor recibió el plan, `proyecto.md` o los rótulos del registro de formulaciones | No vale como revisión sin plan: se repite con un agente limpio o se declara informada. |
| El auditor recibió la cubierta del productor | No es independiente: se repite sin ella o se declara informada. |
| El productor redacta el encargo de su propio control | La coordinación lo rehace con la consigna sin cambios. |
| El usuario pide «una revisión independiente» sin decir de qué | Se elige el control por lo que quiere comprobar y se dice en una línea. |
| Un control puede leer los archivos del proyecto | Recibe su material aparte, la prohibición de abrir otros y declara qué archivos abrió. |
| Un auditor encuentra una contradicción grave y el responsable discrepa | La objeción original y la respuesta llegan en la entrega; el informe completo queda accesible. |
| El revisor encuentra que un personaje actúa con información que no tiene | Lo anota en una línea para el auditor, sin desarrollarlo. |
| El revisor llama tic a un rasgo descrito en la voz o a un motivo registrado | Se conserva; llamar tic a un rasgo exige mostrar distribución y deriva, no solo frecuencia. |
| Un rasgo de la voz crece de capítulo en capítulo sin que la obra lo pida | El revisor lo señala como deriva, con cifras por capítulo y las apariciones que conviene conservar. |
| Una frase formula lo que los indicios anteriores ya daban a entender | El revisor la señala como subtexto aplanado; la corrección la retira sin trasladarla al diálogo ni al cierre. |
| Una corrección de reiteraciones borraría los indicios de un subtexto | El revisor los marca para conservar y la corrección los respeta. |
| La extracción no registra un cambio que el plan asigna al capítulo | Se busca el pasaje; si existe, es un dato de visibilidad para el autor, no una orden de explicitar. |
| La extracción registra, aunque sea como subtexto, algo que el plan reserva | Se trata como candidato de información prematura. |
| El auditor cita para una función del plan un pasaje que el revisor no registró | Se trata como una función que quizá solo se lee conociendo el plan. |

## Decisiones sobre los hallazgos

| Caso | Conducta esperada |
|---|---|
| La lectura ciega entiende lo que se buscaba y señala una caída de atención en un tramo | El contraste registra los dos ejes por separado; la caída se trata con ritmo, aunque cada parte del tramo tenga función. |
| Un lector pregunta por qué nadie reacciona a un hecho público y la respuesta está en el plan | Señal mínima en la página, duda abierta a propósito con su horizonte registrado o cambio del hecho; no «el plan lo explica». |
| La lectura ciega y una reseña del usuario señalan el mismo tramo | Hallazgo confirmado: conservarlo exige mostrar qué se perdería, no la intención. |
| Un riesgo previsto en la revisión del plan aparece confirmado en la lectura | Es hallazgo del capítulo; haberlo previsto no lo absuelve. |
| Un problema de ritmo del capítulo se anota «para el plan siguiente» | Se corrige en el capítulo o se rechaza con razón; el plan siguiente solo hereda lo que pertenece a su tramo. |
| Tras la lectura ciega se corrige un pasaje | Control delimitado nuevo sobre el pasaje con una pregunta neutra; cobertura registrada (lectura de rN, control de rN+1). |
| Una reseña propone cortar una escena que siembra información usada después | Se hace el inventario de siembras; el corte reubica lo sembrado o cambia. |
| Un hallazgo se acepta «si se retoma más adelante» | Queda en memoria como compromiso con horizonte y se comprueba al llegar. |
| El usuario trae una reseña con puntuaciones | Se comprueban sus citas y diagnósticos contra el texto; sus remedios se revisan; sus cifras no se toman como mediciones. |

## Pilotos

En un piloto autorizado, incluye un capítulo y una revisión posterior que altere un hecho con dependencias. Observa qué texto intermedio llega realmente a la conversación principal, qué decisiones se omitieron, qué defectos aparecieron después de la entrega, la calidad de la prosa y la facilidad para retomar. Si hay métricas, registra contexto principal, consumo total, concurrencia y latencia.

Para evaluar los tres controles, prepara una copia de un capítulo con elementos que solo conoce quien evalúa. Para comprobar que se encuentran: una certificación, una abstención que acredita un rasgo, una decisión clave reducida a gestos físicos neutros (sub-realización), un subtexto aplanado, la reiteración de un sentido ya mostrado, un molde que crece entre capítulos (incluido un cierre contenido de objeto en serie), abuso de diálogo reportado en una escena que pide habla directa, una acción con opacidad espacial, una designación que alterna sin patrón, una marca de otra variedad de la lengua, un conocimiento prematuro, una fecha prevista que pasa sin decisión, un hecho público sin consecuencia ni razón en la página, una ruptura causal y una secuencia narrada paso a paso sin aporte. Para comprobar que se respetan: un rasgo de voz deliberado, un motivo registrado, un subtexto logrado y una minucia que caracteriza. Ningún control debe saber qué se sembró, ni por la consigna ni por el nombre del archivo: esa información lo vuelve delimitado. Registra qué control encuentra cada elemento, si lo atribuye al rol correcto, qué elementos deliberados se propuso corregir y si la extracción registra el subtexto logrado. Repite con al menos dos capítulos antes de ajustar el protocolo: un solo caso no distingue un fallo del protocolo de una lectura aislada.

Para evaluar las decisiones, observa además qué hace quien integra con lo que los controles encontraron: si separa comprensión y experiencia, si resuelve las dudas con pasajes, si corrige en el capítulo lo que pertenece al capítulo y si registra las razones de lo que rechaza.

Juzga el éxito por control creativo, lectura suficiente y memoria reconciliada, además de la carga de contexto. Distingue siempre el protocolo descrito, las acciones ejecutadas y los controles pendientes.
