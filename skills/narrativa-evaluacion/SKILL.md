---
name: narrativa-evaluacion
description: "Evaluar y editar ficción con diagnósticos localizados, y decidir qué hacer con lo que encuentran los controles, el usuario o una reseña: planes, capítulos, manuscritos completos, personajes, ritmo y experiencia lectora. Úsala ante pedidos de crítica, edición o revisión."
metadata:
  version: "1.0.0"
---

# Evaluación narrativa

## Elegir el modo

- **Informada (por defecto):** lees el material con el contexto del proyecto que haga falta. Es la que haces tú, también en la autorrevisión de un capítulo.
- **Independiente:** otra ejecución sin tu contexto: auditoría, revisión o lectura ciega. Solo existe con agentes; `narrativa-agentes` define qué examina y qué recibe cada control, y contiene sus consignas. Si el usuario pide expresamente uno de estos controles, ese pedido autoriza agentes para ese control.
- **Sobre una evaluación ajena:** cuando el usuario trae una reseña, decides sobre ella con «Decidir sobre los hallazgos».

No presentes una lectura informada como ciega o independiente. Si el pedido es ambiguo, haz una evaluación informada del material disponible y declara su alcance; no interrumpas para ofrecer un menú de revisiones. Una crítica aislada no implica ejecutar el flujo completo de capítulo.

Dentro de un proyecto, el flujo y la precedencia los define `narrativa`.

## Apoyar cada diagnóstico en la obra

Lee el texto y precisa versión y alcance antes de diagnosticar; no diagnostiques capítulos que no leíste a partir de un resumen. Consulta voz, plan o canon solo cuando ayuden a valorar una dificultad concreta. Distingue lo que ocurrió en la página, su interpretación y el efecto buscado: la intención no prueba el resultado, y el plan no demuestra que una escena ya desarrolló una emoción o una relación.

Examina a la escala adecuada: una frase puede funcionar sola y agotarse por repetición; una escena tranquila puede sostener un arco sin producir un giro. No confundas corrección, fluidez o cumplimiento de fichas con calidad literaria.

Conserva la particularidad de la voz, el humor, la aspereza y la interioridad. No maximices transparencia, compresión o eficacia argumental a costa de la experiencia, ni exijas que todos los personajes formulen la interpretación más completa de lo que viven.

## Lentes

### Lentes de capítulo
Úsalas en la autorrevisión del flujo de capítulo y en la edición de desarrollo.

- **Escena por escena:** entrada, deseo inmediato, fricción, giro, salida y cambio de estado; su aporte al capítulo y sus transiciones. Cuenta también los cambios de percepción, cercanía, comprensión o estado emocional, y la experiencia que necesita tiempo. Una escena de convivencia, contemplación o descanso no necesita giro argumental; una que no altera ni desarrolla nada sobra, aunque figure en el plan.
- **Personajes y diálogo:** voz propia; objetivos compatibles con lo que cada uno sabe; reacciones coherentes; conversaciones con fines distintos de informar al lector. Corrige los diálogos demasiado limpios, utilitarios, **crípticos por alusión** o uniformemente ecuánimes bajo presión sin añadir torpeza artificial, así como el **abuso de diálogo reportado** («dijo que…», «pidió que…») en despedidas, conflictos o escenas de vínculo que piden presencia viva; preserva silencios, equívocos, asimetrías, temperamento distinto, humor e interioridad de cada personaje.
- **Focalización e información:** qué puede saber el focalizador, qué interpreta, qué supone y qué no debería afirmar el narrador; omnisciencia accidental, conocimiento prematuro y certificaciones, incluida la que se hace por abstención («no preguntó», «agradeció que no…»). Vigila también los defectos inversos: **sub-realización conductista** (una decisión irreversible reducida a secuencia neutra de gestos y objetos sin presión interior), **prosa oblicua por comodines** («eso», «algo», «el sitio», «el otro lado», «la parte») que obliga a releer, y **elementos importados sin ancla** para un lector que no trae canon externo. Mantén la focalización establecida, incluido un narrador omnisciente cuando es una elección de la obra. El criterio está en `narrativa-informacion`; no aclares un subtexto deliberado para demostrar que el autor conoce la respuesta, ni pases una explicación redundante al diálogo. Al reducir reiteraciones, conserva los indicios que sostienen el subtexto.
- **Verosimilitud y reglas operativas:** si los hechos visibles tienen las consecuencias que el lector esperaría —testigos, autoridades, reacciones— o una razón en la página para no tenerlas, y si **un lector sin notas puede explicar en dos frases cómo funciona el mecanismo central y qué pierde alguien si falla**. Si el vocabulario técnico se acumula sin anclarse o las reglas quedan a la inferencia, la tensión cae. Tu conocimiento del plan no cuenta como página.
- **Tensión y ritmo:** alternancia de acción, conversación, introspección, transición y descanso; valles demasiado largos (como dos capítulos seguidos de reuniones o trámites sin cambio visible), escenas redundantes, intensidad acumulada sin respiración, **huida inmediata hacia la logística** tras una muerte o ruptura que corta el eco emocional, procedimientos o **peligros físicos que se repiten** con la misma coreografía, ensayos previos que gastan el clímax y pasajes de acción donde la **doble carga** (espacio con muchas piezas + causalidad técnica nueva simultáneos) obliga a reconstruir antes de sentir el riesgo. Comprueba si el pulso de la prosa varía entre escenas tranquilas y escenas de máxima presión. Juzga la duración por su efecto, sin proporciones fijas.
- **Extensión:** dónde sobra texto y dónde falta desarrollo; momentos emocionales con poco espacio, reiteraciones, tramos que exceden su función, secuencias narradas paso a paso sin que el detalle lo justifique y escenas narradas enteras con la misma minucia (criterio en `narrativa-prosa`, «Granularidad»). No persigas la brevedad uniforme ni un número de palabras por costumbre; respeta la extensión acordada si existe. Decídelo antes del pulido: lo que se expande debe pasar por él, y lo que se corta no necesita pulirse. Antes de cortar, haz el inventario de siembras («Antes de cortar»).

### Lentes de plan
- **Estructura:** capítulos redundantes, causalidad débil, personajes pasivos, progresión demasiado rápida o lenta, conflictos resueltos con facilidad, setups olvidados, repeticiones, coincidencias convenientes y escenas sin función. Comprueba decisiones y consecuencias antes de recomendar más escenas o más adversidad. Considera la función emocional, relacional y de experiencia; no exijas conflicto o giro a cada escena ni hagas depender el diagnóstico de que las fichas estén completas. Un plan puede demostrar preparación, no que la prosa futura producirá la experiencia.
- **Progresión global:** qué hereda el tramo, qué transforma, qué deja abierto y qué prepara; si la forma de sus capítulos repite la de los anteriores. Pregunta qué pierde la novela si se elimina: acontecimientos, experiencia, vínculos, comprensión o promesas. Si pierde poco, señala con evidencia el problema de función, ubicación o duración.
- **Continuidad:** la hace `narrativa-memoria`, que juzga coherencia factual, temporal, de mundo y de acceso, no calidad dramática.

### Lentes de volumen
Para manuscritos completos o tramos de varios capítulos: al cerrar una parte, al terminar un volumen o cuando el usuario pide revisar un manuscrito completo. Algunos problemas solo existen a esa escala: cada escena es razonable, pero el conjunto repite, confirma o deriva.

**Orden.**
1. Continuidad (`narrativa-memoria`): referencias al pasado contra sus fuentes y contra el calendario, documentos y datos que se reutilizan. Son correcciones pequeñas y verificables; conviene sacarlas primero.
2. Lentes de volumen (abajo): deciden qué información sobra o falta entre capítulos.
3. Hábitos de prosa (`narrativa-prosa`), sobre el texto que quedó después del paso 2, para no pulir lo que se va a cortar.
4. Revisión local de los capítulos afectados con las lentes de capítulo.

**Lentes.**
- *Recorrido de un cambio central:* elige los dos o tres cambios principales (de un personaje, de una relación, del mundo) y lista cada aparición con capítulo y canal (gesto, pensamiento, diálogo, documento, cierre). Distingue las que aportan algo nuevo —otra relación, otro acceso, otro costo, otra experiencia— de las que solo reaseguran. Conserva la primera aparición desarrollada, las que cambian algo y las recurrencias que son motivo. Reformular con otras palabras no convierte una confirmación en aporte.
- *Convergencia de voces:* ¿cuántos personajes formulan, con lucidez parecida, el sentido del arco? Usa el registro de formulaciones de `narrativa-memoria` o búscalas en los diálogos con contenido reflexivo; marca las que llegan con la misma claridad desde intereses distintos, sobre todo las que validan al protagonista. Conserva las que discuten, se equivocan en parte o tienen un costo para quien habla, y las máximas propias de un personaje. No arregles la convergencia volviendo torpes a los personajes.
- *Inventarios y recapitulaciones:* párrafos que enumeran imágenes o hechos de capítulos anteriores para que el lector reconozca un patrón que ya reconoce. Conserva el reconocimiento presente que hace avanzar la escena; reduce la enumeración de antecedentes.
- *Lo que el lector ya sabe y el personaje descubre:* la escena se centra en lo que saberlo le hace al personaje; reduce la repetición de cifras y criterios que el lector ya tiene. No alargues el suspenso sobre algo que el título o los indicios ya volvieron previsible.
- *Forma de los capítulos:* secuencia de tipos de escena, aperturas y cierres de capítulos consecutivos, y variedad de los peligros físicos u obstáculos. Una plantilla repetida sin intención hace que el lector anticipe. Revisa también la **deriva hacia la contención uniforme**: focalizadores y escenas de distinta intensidad con el mismo pulso declarativo plano, abuso de diálogo reportado que enfría clímax y despedidas, puntuación narrativa vaciada de inflexiones (`;`, `:`, `¿`, `¡`) o secciones cerradas en serie con un mismo gesto silencioso de objeto.
- *Siembra relacional, oposición y reparto:* comprueba si las muertes, renuncias, traiciones, duelos y **escaladas de oponentes** tienen antes al menos una escena vivida del vínculo o la responsabilidad que está en juego, si los primeros capítulos dosifican las entradas de secundarios sin saturar la memoria del lector y si lo que espera a un personaje fuera de escena tiene peso concreto legible (sin apilar nombres importados sin contexto). Un secundario que solo aparece para salir de escena, o un oponente que solo entra para bloquear y escalar, sostiene la trama pero no el peso humano.
- *Compromisos y fechas:* expectativas abiertas, hallazgos aceptados con condición y fechas previstas cuyo horizonte ya pasó.
- *Balance del desenlace:* ¿el clímax tiene espacio propio o quedó apretado junto al epílogo? ¿Las promesas centrales sembradas durante la obra se pagan en escena o se despachan fuera de escena? ¿El cierre completa el balance una vez o varias, y en extensión proporcionada sin estirarlo con trámites menores? Conserva las consecuencias que todavía cambian algo y los costos que quedan abiertos. No exijas que cada costo termine sin aprendizaje, ni que todo quede absuelto.

**Informar.** Separa lo que solo el autor puede decidir (dirección, estructura, el estatuto de un elemento fantástico, qué cambio central se prioriza) de los patrones que el kit puede corregir. Lo primero va adelante, con alternativas; lo segundo se agrupa por familia con dos o tres ejemplos localizados, su frecuencia por capítulo y las apariciones que conviene conservar.

### Edición de desarrollo
Revisa causalidad, ritmo, distribución de la atención, desarrollo de los vínculos, acceso a la información y recurrencias entre escenas. Atiende a la identidad mental y a las diferencias de procesamiento entre personajes, no solo a sus modales. No infieras lentitud del número de palabras ni dramatismo de la cantidad de conflictos.

Comprueba si los cambios tienen desarrollo suficiente en el texto, sin exigir una explicación que los certifique. Distingue una elipsis comprensible de un salto que obliga a inventar una transición esencial. No recomiendes más exposición como primera reparación.

Detecta los patrones cuya repetición produce un efecto involuntario: todos los personajes diagnostican lo que viven, los cierres son sentenciosos, los conflictos se resuelven siempre igual, cada costo se amortiza, la discreción de un personaje se acredita una y otra vez por lo que no hace. No prohíbas recursos aislados ni impongas variedad por cuota.

## Formular hallazgos

Para cada hallazgo importante, indica pasaje o secuencia, efecto en la lectura, evidencia, grado de certeza, intervención proporcionada y lo que podría perderse al aplicarla. Separa observación textual, inferencia y preferencia. Prioriza lo que amenaza la comprensión, la voz o la experiencia pedida; no infles la lista con preferencias menores ni inventes fallos para llenar el informe.

Nombra las fortalezas concretas que una corrección podría dañar, en especial humor, aspereza, intimidad, cadencia, ambivalencia e interioridad. No repartas elogios por equilibrio. Una observación como «demasiado diálogo» debe mostrar qué se repite, qué se pierde o qué se vuelve difícil de seguir. Si dos realizaciones funcionan, prefiere la del pasaje salvo una ventaja clara.

- **Patrones con línea de base.** Al señalar un patrón —un epíteto, una negación, un comienzo, un cierre—, da su frecuencia por capítulo desde su primera aparición (el script de `narrativa-prosa` la produce). Así se distingue la deriva de un rasgo estable o de un pico local, y no se señala en un capítulo lo que era más frecuente en otro anterior sin decirlo.
- **Hallazgos con condición.** Si un hallazgo queda aceptado con una condición —«funciona si se retoma», «se responderá después»—, regístralo como compromiso en `narrativa-memoria`, con su horizonte, para que alguien lo compruebe cuando llegue.

### Antes de cortar
Antes de recomendar cortar, comprimir o fundir un tramo, haz el inventario de lo que siembra: información que otra escena usa, la mecánica que después se aprovecha, un setup, un gesto que vuelve, una relación que se apoya en él. Para cada elemento, indica dónde se cosecha. Un corte que elimina una siembra necesita reubicarla; si no puede reubicarse, el corte cambia. Una escena que repite la mecánica de otra se comprime en lo sabido, no en lo que prepara.

## Decidir sobre los hallazgos

Un hallazgo puede venir de tu autorrevisión, de un control independiente, del usuario o de una reseña externa. Los controles diagnostican; quien produce decide, y registra cada decisión: corregido, rechazado con su razón, aceptado con condición (pasa a `narrativa-memoria`) o pendiente de una decisión reservada.

1. **Comprensión y experiencia son ejes distintos.** Que un lector haya entendido lo que se buscaba no dice qué le pasó al leer: dónde bajó su atención, qué le pareció inverosímil, qué esperaba y no llegó, dónde desconfió. Contrasta la comprensión con las intenciones y la experiencia con la experiencia buscada, por separado. Una experiencia distinta de la buscada es un hallazgo aunque la comprensión coincida.
2. **Una duda se responde con la página.** Si un lector pregunta por qué nadie reacciona, cómo sabe alguien algo o por qué una regla del mundo no se aplica, busca el pasaje que lo responde. Si la respuesta solo está en el plan, la memoria o la verdad privada, el lector no la tiene. Hay tres salidas: una señal mínima en la página —un detalle, una reacción o una frase dentro de la escena, no una defensa del narrador—; mantener la duda abierta a propósito, registrando dónde y cuándo se responderá; o cambiar el hecho. «El plan lo explica» no es una salida. Distingue la duda que la obra busca (un misterio, una ambigüedad de personaje) de la duda de verosimilitud: la primera puede conservarse; la segunda, sin señal en la página, se lee como descuido.
3. **La función de cada parte no refuta una caída de atención.** El ritmo pertenece a la secuencia: un tramo puede perder al lector aunque cada intercambio cumpla una función distinta. Trata una caída localizada con ritmo —comprimir lo sabido, fundir lo que repite un mismo molde, interrumpir con una acción, mover información al punto donde se usa, variar la forma— y conserva lo que cada parte aporta de verdad.
4. **La coincidencia sube la certeza.** Si dos lecturas independientes entre sí —dos controles, o un control y el usuario o una reseña— señalan el mismo tramo por razones compatibles, trátalo como hallazgo confirmado: conservarlo exige mostrar qué se perdería al cambiarlo, no la intención con que se escribió. Un riesgo que el plan ya había previsto y que un control confirma también es un hallazgo; haberlo previsto no lo absuelve.
5. **El capítulo resuelve sus problemas.** Un hallazgo sobre un capítulo se corrige en ese capítulo o se rechaza con su razón. Pasarlo al plan siguiente solo vale para lo que pertenece al siguiente —una expectativa que puede pagar, una consecuencia que debe desarrollar—; un problema de ritmo, de verosimilitud o de forma queda en el capítulo aunque el siguiente se escriba distinto. Si corregir obligaría a repetir un control caro, corrige igual y verifica el pasaje con un control delimitado (`narrativa-agentes`).
6. **Conservar lo que funciona protege del gusto, no de los lectores.** «Si la mejora es dudosa, conserva» se aplica a cambios que nadie pidió por un efecto en la lectura. Ante un efecto que un lector informó, lo dudoso es conservar, y el rechazo necesita una razón concreta.
7. **Los remedios también se revisan.** Un diagnóstico acertado puede traer una solución que daña. Antes de aplicar un corte, una fusión o una compresión —tuya o propuesta por otro—, haz el inventario de siembras.

- **Sobrecorrección:** obedecer cada observación; poner en la página la respuesta a todo lo que un lector preguntó; convertir cada caída de atención en un recorte; tratar como defecto una incertidumbre que la obra busca; decidir por mayoría. No acumules lecturas hasta obtener el veredicto deseado.

### Reseñas externas
Cuando el usuario trae una evaluación ajena —de otra sesión, de otro modelo, de un lector—, trátala como datos, no como vara. Comprueba cada cita con una búsqueda literal y cada diagnóstico contra el texto; separa el diagnóstico del remedio que propone; contrasta sus patrones con las cifras por capítulo, y decide con las reglas anteriores. Su autoridad viene de la evidencia que aporta. Si coincide con un control anterior, se aplica la regla 4.

## Evaluar o cambiar

Si te pidieron análisis, entrega análisis. Si te pidieron revisión, aplica los cambios autorizados y devuelve las decisiones reservadas con alternativas concretas. Resuelve el desarrollo antes de pulir fragmentos que van a desaparecer.

Al cambiar selección, certeza o exposición, aplica `narrativa-informacion`; al realizar prosa, `narrativa-prosa` y la voz de la obra; si cambian hechos, accesos, relaciones o compromisos, reconcilia con `narrativa-memoria`. No desplaces una explicación redundante del narrador al diálogo, al cierre o a una escena nueva: corrige el problema de fondo con la menor intervención suficiente, preservando la experiencia que sí aporta.

## Puntuaciones

No las des salvo que te las pidan. Si te las piden, usa anclas explícitas, la misma escala para todo y la dirección «más es mejor»:

| Rango | Significa |
|---|---|
| 90–100 | Listo: solo detalles |
| 80–89 | Funciona; problemas visibles y localizados que un editor marcaría |
| 70–79 | Problemas que afectan la lectura de tramos completos |
| 60–69 | Problemas de estructura, voz o verosimilitud que comprometen el texto |
| Menos de 60 | Requiere replanteo |

Diferencias de menos de cinco puntos no distinguen calidad: no ordenes capítulos por ellas. Acompaña cada cifra con los hallazgos que la explican; la cifra no los sustituye ni es una medición.

## Entregar y detener

Presenta primero los hallazgos que más cambian la lectura, con ejemplos proporcionados. Separa lo que solo el autor puede decidir de los patrones que pueden corregirse sin él, y agrupa estos por familia en lugar de listar cada aparición: el informe debe dejarle al autor margen para lo importante. Distingue limitaciones reales de advertencias abstractas.

Escribe para el autor, en lenguaje editorial llano. Los términos de trabajo del kit (certificación, propiedad cognitiva, rendimiento, homologación) se traducen a lo que describen: «la escena explica dos veces lo mismo», «el personaje no puede saber esto», «el detalle promete algo que no llega». Antes de entregar, comprueba cada cita con una búsqueda literal en la versión revisada, y calibra la certeza de cada incidencia de continuidad con las clases de `narrativa-memoria` antes de llamarla contradicción. No prometas que una lectura representa a todo el público ni que una revisión parcial certifica la obra completa.

Detente cuando no queden problemas concretos relevantes o las mejoras adicionales sean dudosas; un efecto de lectura que un lector informó cuenta como problema concreto. No reescribas pasajes logrados para expresar tu gusto.
