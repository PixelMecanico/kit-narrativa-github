---
name: narrativa-memoria
description: "Canon y continuidad de una obra: hechos, creencias, calendario y documentos con procedencia; reconciliar versiones y detectar contradicciones. Úsala al cerrar capítulos o volver sobre el pasado."
metadata:
  version: "1.0.0"
---

# Memoria narrativa

## Fuentes y alcance

Identifica proyecto, línea o variante, versión del manuscrito, registros existentes y operación pedida. Distingue consulta, propuesta de actualización y mantenimiento ya delegado. Lee las fuentes concretas que necesitas, no solo fragmentos de búsqueda: la falta de resultados no prueba que un dato nunca se estableció.

Conserva las instrucciones vigentes y su alcance. Las ideas en discusión son propuestas hasta que el encargo permita adoptarlas. No atribuyas al usuario decisiones tuyas. Un registro sin procedencia comprobada no tiene más autoridad que el texto que dice resumir.

En fanfic, identifica la continuidad y la versión de la obra fuente, y separa su canon, las divergencias decididas y las consecuencias ya introducidas. Verifica los datos de la fuente que no estén establecidos: un recuerdo incierto no es una restricción, y el canon original no se impone sobre una divergencia decidida. No traslades hechos entre obras ni entre variantes por compartir nombres o personajes. Registra además:

- los **términos que la fuente fija con un sentido** (un ordinal, un título, el nombre de un acontecimiento) y que la divergencia usa con otro: el lector de la fuente leerá el sentido original, así que la página desambigua o el término cambia;
- las **capacidades verificadas de los personajes de la fuente** que aparecen, también de los que no son el foco: lo que pueden hacer en una escena es canon operativo, y su ausencia sin motivo se nota.

Dentro de un proyecto, el flujo y la precedencia los define `narrativa`.

## Modos

| Operación | Qué hacer | Sección |
|---|---|---|
| Consultar canon | Determinar qué está vigente y con qué autoridad | «Registros» |
| Revisar continuidad | Distinguir incompatibilidades de variaciones plausibles | «Revisión de continuidad» |
| Extraer novedades | Proponer altas, cambios y retiradas con evidencia | «Extraer y reconciliar» |
| Reconciliar o cambiar retrospectivamente | Contrastar los registros con la versión final y sus dependencias | «Extraer y reconciliar» |
| Seguir compromisos y conocimiento | Pistas, secretos, relaciones, expectativas, formulaciones del sentido, retornos de motivos y hallazgos con condición | «Compromisos y conocimiento» |
| Llevar calendario, documentos y datos que se reutilizan | Registros que se consultan antes de volver sobre algo anterior o de llegar a una fecha prevista | «Registros» |

Reutiliza los formatos e IDs existentes cuando preservan las distinciones necesarias; no exijas una migración completa para continuar el arco activo.

## Separaciones esenciales

- Distingue verdad del mundo, afirmación de un hablante, creencia de un personaje, interpretación tuya y plan aún no realizado.
- Separa lo que sabe el escritor, lo que puede conocer cada personaje y lo que el texto permitió conocer al lector.
- Conserva certeza, temporalidad y alcance. Una acusación no demuestra el acto acusado ni que su destinatario la crea. Una emoción o una relación momentánea no se vuelve rasgo permanente.
- Registra lo explícito y las implicaciones necesarias bien sustentadas; mantén como inferencia lo que admite alternativas relevantes. No subas la certeza para completar un campo.
- El canon es reserva, no lista de exposición. Registra compromisos sin exigir que cada detalle, costo o fracaso produzca un payoff, y no añadas explicaciones a la prosa para demostrar que los registros están al día.

## Registros

### Qué registrar
Registra los hechos que condicionan decisiones futuras, capacidades, cronología, relaciones, secretos o revelaciones, y los detalles con probabilidad razonable de volver a usarse. Lo demás queda localizable en el texto y se promueve si adquiere relevancia; exhaustividad no es utilidad. Mantén secciones distintas para canon, candidatos, conocimiento y acceso, incidencias y compromisos. Pueden compartir `memoria.md`; sepáralas en archivos cuando su tamaño o su consulta lo justifiquen.

Registra también las **consecuencias que el mundo espera** de un hecho público, no solo el hecho: si hubo policía, testigos o alguien filmando, la investigación, el rumor o el video son expectativas abiertas con horizonte, aunque el texto todavía no las trate.

### Calendario, documentos y datos que se reutilizan
Son baratos de mantener y evitan la mayoría de los errores de continuidad de un volumen largo. Actualízalos al cerrar cada capítulo y consúltalos antes de escribir una frase que vuelva sobre algo anterior.

- **Calendario:** una fila por fecha, con lo narrado y lo **previsto**: plazos, viajes, citas, días que un personaje marcó o prometió. Basta con los días que el texto nombra, los que sostienen un intervalo y los que el texto anticipa. Con él se comprueban «hace dos días», «el martes» o «por primera vez en dos semanas», y se ve qué fechas previstas caen en el próximo tramo.
- **Documentos reproducidos:** cada nota, carta, contrato, registro o mensaje cuyo texto aparece en la obra, con su ubicación y los datos que contiene (cifras, fechas, nombres). Lo que un personaje diga después sobre ese texto se compara con él.
- **Datos que se reutilizan:** cantidades (dinero disponible, precios, medidas), atributos de objetos que vuelven (material, color, tamaño), hábitos establecidos y frases que otro personaje podría citar, con quién las dijo.

```markdown
## Calendario
| Fecha | Día | Narrado | Previsto o pendiente | Fuente |
|---|---|---|---|---|
| 09-10 | viernes | Zarpa el correo de Oporto; Tomás se queda con el sextante de su tío | | cap. 3 |
| 12-10 | lunes | | Audiencia ante el Consejo del Puerto (cita fijada en cap. 3) | cap. 3 |
| 14-10 | miércoles | | Regreso de Sara a Valparaíso (anunciado en cap. 2; sin cancelar) | cap. 2 |

## Documentos reproducidos
- Carta de patente (cap. 5): 38 barriles de pólvora; flete de 4.100 reales; firmada por H. Valdés.

## Datos que se reutilizan
- Dinero de Sara: 300 pesos cosidos en el forro de la capa (cap. 4).
- Sextante del tío: latón oscuro, espejo trizado en una esquina (cap. 1).
- «El mar perdona un mal timón, nunca una mala guardia»: lo decía el tío; lo recuerda Tomás (cap. 4).
```

Cuando una fecha prevista llega en la narración, el capítulo decide qué hace con ella —narrarla, dejarla pasar con un silencio que el lector perciba, cancelarla o moverla— y el calendario registra la decisión. Una fecha prevista que pasa sin decisión es un hueco de continuidad, aunque ninguna frase sea falsa.

### Dimensiones de un registro

| Dimensión | Tratamiento |
|---|---|
| Contenido | Formula exactamente lo establecido, con su alcance |
| Naturaleza | Hecho del mundo, acto de habla, creencia, recuerdo, inferencia o cuestión abierta |
| Procedencia | Decisión o archivo, escena y versión que lo sustentan |
| Estado de trabajo | Candidato, vigente, sustituido o descartado |
| Tiempo | Rasgo estable, estado temporal o acontecimiento |
| Acceso | Quién sabe, cree, sospecha o recibió una afirmación, y desde cuándo; revelación al lector aparte |
| Incidencias | Dudas o conflictos relacionados, sin convertirlos automáticamente en falsedad |

Usa IDs estables para las entidades y afirmaciones que deban enlazarse. Conserva los existentes; en registros nuevos, usa prefijos sencillos como `CHAR-`, `CAN-`, `DEC-`, `INC-` y `HIL-`. Comprueba que sean únicos, no reutilices un ID descartado y no dependas del título de un capítulo para preservar la identidad. Usa texto, tablas o un formato como este, y omite los campos irrelevantes sin perder las distinciones necesarias:

```yaml
id: CAN-0042
contenido: Nora acusa a Jonas de destruir la carta ante Elias.
naturaleza: acto_de_habla
fuente: capitulo_04 / escena_02 / r03
estado: vigente
alcance: La veracidad de la acusación sigue abierta.
acceso:
  Elias: Recibió la acusación; su convicción no está establecida.
  lector: Conoce la acusación desde esta escena.
```

Si no hay marcadores estables, ancla el pasaje con la escena y una cita breve, y actualiza los localizadores después de cada revisión.

### Contenido y verdad
Si Nora afirma que Jonas destruyó una carta, registra el acto de habla cuando sea relevante. Eso no establece la destrucción, la sinceridad de Nora ni que su interlocutor le crea. Si la dirección fijó que miente, guarda esa verdad como privada hasta que el texto la revele; si no se decidió, la cuestión sigue abierta.

Trata recuerdos y pensamientos según el contrato narrativo. Un sentimiento experimentado puede quedar establecido aunque la explicación causal que el personaje le da no sea verdadera. Una focalización enfática no elimina sus límites de conocimiento. Una narración fiable puede establecer hechos: no relativices todo el manuscrito por precaución abstracta. No exijas fórmulas literales para reconocer algo que la escena establece sin ambigüedad.

No inventes la fuente de un registro heredado: marca su procedencia como pendiente y verifícala antes de usarlo como restricción decisiva. Registra qué se revisó realmente; una extracción parcial no representa todo el libro. Mantén separados la fuente vigente, el texto retirado, la idea no aplicada y la variante.

## Referencias al pasado

La mayoría de las roturas de continuidad ocurren cuando el texto vuelve sobre algo anterior y lo reconstruye de memoria: qué decía una nota, quién usó una palabra, cuánto dinero había, cuántos días pasaron, qué día fue, cuándo ocurrió algo por última vez, de qué material era un objeto. Cada pasaje parece correcto por sí solo; el error aparece al compararlo con su fuente.

- **Al escribir:** antes de que una frase afirme algo sobre el pasado de la obra, comprueba la fuente: el pasaje, el documento reproducido o el registro. Si no puedes comprobarlo, formula sin la precisión que no tienes.
- **Al revisar:** localiza las referencias al pasado del capítulo y contrasta cada una. El script de `narrativa-prosa` las lista (`--informe retro --capitulos N`); sin él, búscalas leyendo: intervalos («hace», «antes», «desde»), referencias del narrador («el día anterior», «la víspera», «aquella mañana», «a primeros de…»), horas, «por primera vez», días de la semana, cantidades, citas de documentos y atribuciones de palabras.
- **Lo que un personaje afirma sobre un texto reproducido** —nota, carta, contrato, registro— se compara al pie de la letra con lo que el texto muestra. Si la afirmación es falsa y nadie lo nota, la escena da por buena una premisa rota.

## Revisión de continuidad

Hazla al cerrar cada capítulo y cuando un cambio pueda afectar hechos, accesos o relaciones. Es una revisión informada; su versión independiente solo existe con agentes (`narrativa-agentes`).

Delimita las versiones y el material que de verdad revisaste. Recupera las fuentes concretas cuando una conclusión depende de una formulación, una posición o un matiz que el resumen no conserva. Examina, según el caso:

- **Factual:** edades, fechas y días de la semana, intervalos, distancias, ubicaciones, trayectos, cantidades y dinero disponible, objetos con su material y procedencia (también dentro de una misma escena), hábitos establecidos, secuencia y capacidades.
- **Calendario:** las fechas previstas que el capítulo alcanza o atraviesa, y qué decidió hacer con cada una.
- **Atribución:** quién dijo qué y con qué palabras, sobre todo cuando otro personaje lo cita después.
- **Cognitiva:** quién pudo acceder a una información, cuándo y con qué certeza; información prematura.
- **Semántica:** relaciones, motivaciones, competencias, voz y efectos de acontecimientos anteriores.
- **Mundo:** las reglas del mundo y su aplicación —ocultamiento, testigos, autoridades, quién puede ver o saber qué en el orden social— y las consecuencias que un hecho público debería tener. Si el texto no las desarrolla, comprueba que la página dé una razón mínima o que la expectativa siga registrada como abierta; que el plan tenga la solución no basta. En fanfic, las capacidades de los personajes de la fuente presentes y los términos de la fuente usados con otro sentido.
- **De consecuencias:** condiciones que una revisión cambia o deja sin sustento, incluida la arquitectura futura del plan.

Clasifica cada hallazgo como contradicción apoyada, tensión interpretativa, información insuficiente o variación plausible. Un paso que la página omite y el lector reconstruye sin esfuerzo no es información insuficiente: la continuidad exige que nada se contradiga, no que todo se narre. No llames contradicción a una desviación del plan, una mentira, un recuerdo defectuoso o una ambivalencia que la escena sostiene. Si la incompatibilidad está en lo que un personaje recuerda o percibe (por ejemplo, en estilo indirecto libre), pregúntate si puede ser un error suyo con sentido; si el texto no lo señala, preséntala como consulta con dos salidas: corregirla o hacer perceptible el error. Un personaje competente puede fallar, una relación puede retroceder y alguien puede actuar distinto bajo otra presión. No inventes excusas para salvar una incoherencia, ni exijas que la narración se explique para defenderse. Esta revisión juzga coherencia, no calidad dramática.

Para cada incidencia, indica la fuente de ambos lados, su naturaleza, su alcance y la operación afectada; propone una reparación dentro de lo delegado, o alternativas con sus costos. Distingue un arreglo documental de un cambio narrativo. Bloquea solo lo que depende de resolver una incompatibilidad real; una incertidumbre que permite continuar sin comprometer decisiones firmes queda abierta. «Ninguna detectada» no garantiza nada sobre el material no revisado.

## Compromisos y conocimiento

### Clases de compromiso

| Clase | Criterio |
|---|---|
| Compromiso deliberado | Decisión autoral identificada; puede no haberse presentado aún al lector |
| Pregunta o expectativa textual | Efecto apoyado en pasajes y en su prominencia, sin suponer que todos los lectores la comparten |
| Expectativa posible | Interpretación razonable pero discutible; conserva ese grado de certeza |
| Observación débil | Conjetura tuya que todavía no restringe el plan |

Da seguimiento a pistas, secretos, tensiones, trayectorias relacionales, fechas previstas y consecuencias esperadas de hechos públicos. Enlaza fuentes, personajes, grado de exposición, horizonte si existe y estado: abierto, transformado, resuelto, retirado o deliberadamente sin cierre.

No trates todo detalle específico como promesa ni exijas recompensa, explicación o retorno a cada objeto, fracaso o costo. Si una expectativa involuntaria domina la lectura, propone ajustar su prominencia o desarrollar sus consecuencias; no impongas automáticamente un payoff. La intención de un setup vive en `plan.md`; la promesa que el manuscrito efectivamente creó vive aquí.

### Hallazgos aceptados con condición
Un hallazgo de revisión aceptado con condición —«funciona si se retoma», «se responderá en el capítulo siguiente», «aceptable en un primer capítulo»— es un compromiso: regístralo con su fuente, la condición y el horizonte, y compruébalo cuando el horizonte llega. Si llega sin cumplirse, el hallazgo vuelve a estar abierto.

### Conocimiento frente a expectativa
Registra que el lector conoce una acusación sin dar por cierta la acusación. Distingue la promesa que hace un personaje de la garantía del autor de que se cumplirá. Conserva las diferencias entre saber, creer, sospechar y haber oído. Sigue las relaciones por evidencia y por momentos: no conviertas «confía en parte» o «está resentida» en propiedades permanentes. Una actualización puede ser asimétrica y no dicha.

### Formulaciones del sentido y retornos de motivos
En un volumen largo, lo que más se repite sin que ninguna escena lo note es la explicación del sentido: varios personajes, en capítulos distintos, dicen con palabras casi iguales lo que el arco significa, y cada vuelta de un motivo trae otra vez su interpretación. Llevar la cuenta hace visible ese patrón mientras se escribe.

- **Formulaciones del sentido:** cada vez que alguien —personaje, narrador, documento— dice en voz alta qué significa el cambio central de un personaje o del arco, anótalo: quién, dónde y en una línea qué afirma.
- **Retornos de motivos:** para cada motivo deliberado (un objeto, una imagen, un gesto que vuelve), anota dónde vuelve y si vuelve solo o con una explicación de su sentido.

```markdown
## Formulaciones del sentido
- Cambio de Tomás (de obedecer a mandar): capitana Vera, cap. 9 («nunca dio una orden suya»); Sara, cap. 12.

## Retornos de motivos
- Sextante trizado: cap. 3 (solo); cap. 5 (solo); cap. 8 (con la explicación de Sara de lo que significa).
```

Antes de escribir una formulación nueva del mismo sentido, consulta la lista. Una nueva formulación se justifica si discute, matiza, cambia de propietario con un motivo propio o tiene un costo; si solo confirma lo ya dicho, sobra. Un motivo puede volver muchas veces; lo que se agota es la explicación de lo que significa.

### Evitar la contaminación por el registro
El registro es un recordatorio para decisiones futuras. No traslades sus diagnósticos al narrador, al diálogo ni a los cierres para demostrar continuidad. La elección de qué se expone la decide `narrativa-informacion`; los cambios de dirección, el usuario.

## Extraer y reconciliar

### Extraer candidatos
Identifica la versión leída y su alcance. Compárala con el canon y, cuando corresponda, con la versión anterior. Propón altas, modificaciones, retiradas y cambios de acceso o de vigencia temporal, con evidencia suficiente para comprobar cada novedad relevante. Distingue una contradicción con una decisión firme, una diferencia con un plan provisional y una simple novedad. No corrijas la prosa durante la extracción ni pases los candidatos a la memoria estable automáticamente.

### Reconciliar la versión que quedó en uso
1. Confirma cuál es la versión elegida para continuar y qué modificaciones se autorizaron.
2. Revisa sus candidatos y los registros que dependían de los pasajes alterados.
3. Comprueba cada alta o cambio contra las fuentes vigentes y el alcance de la delegación.
4. Decide el destino de la información retirada con la tabla siguiente.
5. Actualiza el conocimiento de los personajes, la exposición al lector, el calendario, las incidencias y los compromisos afectados.
6. Consolida lo compatible, conserva visible el conflicto pendiente cuando corresponda y asocia la memoria a la versión final.

| Situación de la información que desapareció del texto | Tratamiento |
|---|---|
| Un acontecimiento salió de la línea principal y su única fuente era la versión descartada | Retira o sustituye su registro activo; revisa las dependencias |
| Se retiró una explicación, pero el hecho sigue fijado por una decisión vigente o por otras fuentes | Mantén la verdad y ajusta qué se reveló, cuándo y a quién |
| Un registro perdió su única evidencia y no está claro si el cambio pretendía revocarlo | Señala la pérdida de sustento; resuélvelo dentro de la delegación o consulta solo si es una decisión reservada |
| El hecho fue sustituido por otro | Conserva la relación de sustitución y actualiza las referencias |
| El pasaje ahora pertenece a una variante | Mantén su información en esa variante, fuera del canon principal |

Ni borrar una frase borra el hecho, ni todo hecho sigue vigente cuando se eliminó el acontecimiento que lo establecía.

Consolida las novedades compatibles cuando la escritura y su mantenimiento estén delegados, sin pedir autorización para cada registro. Separa «vigente para continuar» de «aprobado expresamente por el usuario». No consolides como línea principal una prueba exploratoria presentada como alternativa. Las novedades del manuscrito adoptado se identifican como hechos narrados o decisiones del escritor, sin inventar aprobación del usuario. Un plan o una previsión no se vuelven canon; mantén las variantes y las versiones descartadas fuera de la línea principal.

### Efectos transitivos
Parte de los registros modificados y revisa solo sus dependencias pertinentes: acontecimientos posteriores, conocimientos, relaciones, limitaciones o compromisos. Amplía el alcance cuando aparezca una dependencia concreta. No reaudites todo el libro por rutina ni detengas tramas independientes por un conflicto local. Propaga los cambios materiales antes de cerrar las tareas que dependen de ellos. En un cambio retroactivo, guarda una versión recuperable, describe su alcance y respeta las decisiones reservadas; no maquilles el conflicto reescribiendo los registros para que parezca que la nueva versión siempre estuvo decidida.

Ante una incompatibilidad, identifica fuentes, alcance y consecuencias. Corrige los errores documentales comprobables dentro del encargo. No reescribas decisiones firmes para ocultar un conflicto ni detengas trabajo independiente por una incertidumbre local. Lleva al usuario los cambios de dirección que exceden el mantenimiento autorizado.

## Versiones y guardado

Usa la identificación existente o una versión legible y única, como `capitulo_04@r03`, ligada al archivo real; no inventes identificadores de proveedores. Guarda una versión recuperable antes de cambios amplios. Revisa sobre una base identificada que no cambie mientras la revisas, con un solo escritor por registro compartido.

Actualiza los registros con el mecanismo persistente disponible, preservando la identidad y el historial del proyecto. Asocia la memoria a una versión concreta y deja visibles las operaciones incompletas. Antes de una modificación amplia, marca que hay una actualización en curso; marca la reconciliación como terminada solo cuando las escrituras necesarias se completaron y las fuentes coinciden. Mantén en `estado.md` el par de versiones manuscrito y memoria, las actualizaciones pendientes y las próximas fechas previstas. No prometas atomicidad que las herramientas no ofrecen; ante una interrupción, registra qué archivos quedaron actualizados y cuáles no.

Al retomar, contrasta versiones y pendientes antes de usar registros afectados, y evita duplicados comparando IDs, contenido y fuentes. No declares cobertura de todo el manuscrito si revisaste un fragmento.

## Entregar

En el mantenimiento ordinario, actualiza los registros y comunica solo los conflictos y las decisiones materiales; no vuelques la memoria entera al terminar cada capítulo. Si te pidieron un informe, muestra evidencia, destinos y límites de forma legible. No corrijas la prosa salvo autorización específica.
