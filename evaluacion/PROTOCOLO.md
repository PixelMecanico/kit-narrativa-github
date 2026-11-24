# Protocolo de evaluación comparativa (`Sin skills` vs. `Kit v1.0.0`)

Este protocolo describe cómo comparar de forma justa y reproducible el desempeño de un modelo **sin skills** frente al mismo modelo usando **Kit de Narrativa `v1.0.0`** sobre las premisas originales de [`../premisas/`](../premisas/).

---

## 1. Control de variables entre corridas

Para aislar el efecto real del kit y evitar contaminación experimental:

1. **Aislamiento obligatorio contra invocación implícita:** las skills incluyen `allow_implicit_invocation: true`. Antes de ejecutar la corrida **Sin skills**, retira o desactiva temporalmente las 7 skills del entorno (o usa una carpeta/perfil sin ellas). No basta con omitir su mención en el prompt.
2. **Prompts simétricos (solo cambia el kit):**
   - Corrida **Sin skills:** usar [`plantilla-base-sin-skills.md`](plantilla-base-sin-skills.md).
   - Corrida **Con kit:** usar [`../plantilla-modo-lector.md`](../plantilla-modo-lector.md).
   Ambas fijan el mismo contrato operativo (delegación total, variedad `español neutro`, regla sin spoilers, Etapa I → Etapa II, entrega en Markdown limpio y subagentes autorizados).
3. **Premisas 100 % originales (matriz A/B balanceada 3 × 2):** se evalúan las mismas 3 premisas contrastadas en ambas condiciones (`Sin skills` vs. `Con Kit v1.0.0`, 6 corridas por modelo), sin entregar nunca [`00_GUIA_DEL_EVALUADOR.md`](../premisas/00_GUIA_DEL_EVALUADOR.md) al modelo autor:
   - [`26 - Renacido como dragón`](../premisas/26%20-%20Renacido%20como%20dragón/26_Renacido_como_dragon.md) — fantasía isekai clásica, ventanas de estado, protagonista no humano y vínculo bajo presión social.
   - [`02 - Horror de duelo`](../premisas/02%20-%20Horror%20de%20duelo/02_Horror_de_duelo.md) — terror psicológico íntimo, cero acción, subtexto, duelo real y contención sin conductismo vacío.
   - [`21 - Whodunit cerrado`](../premisas/21%20-%20Whodunit%20cerrado/21_Whodunit_cerrado.md) — misterio deductivo clásico en escenario cerrado, 8 sospechosos, continuidad temporal (`retro`) y pistas justas.
4. **Esfuerzo controlado:** mantener fijo el nivel de esfuerzo (`high` predeterminado) en todas las corridas comparadas de un mismo modelo.

---

## 2. Evaluación cuantitativa (`habitos.py`)

Al terminar cada novela (tanto la línea base como la corrida con kit), ejecutar el analizador de forma uniforme sobre el manuscrito completo:

```bash
python skills/narrativa-prosa/scripts/habitos.py ruta/al/manuscrito/ --variedad neutro
```

Registrar como mínimo: total de palabras y capítulos, porcentaje de diálogo directo, diálogo reportado (`/10k`), comodines vagos (`/10k`), mediana y rango `p10–p90` de oración, proporción de párrafos breves (`≤20` palabras), puntuación narrativa (`; : ¿ ¡`), cierres repetidos, marcas ajenas a la variedad declarada y alertas totales.

---

## 3. Panel de jueces ciegos independientes (doble ciego)

1. **Anonimización:** copiar los manuscritos con nombres neutros (`manuscrito_A.md`, `manuscrito_B.md`) sin metadatos ni menciones al kit.
2. **Sesiones limpias:** cada juez recibe **solo** el manuscrito y el texto de [`prompt-juez-ciego.md`](prompt-juez-ciego.md).
3. **Composición del panel:**
   - **Núcleo obligatorio (2 jueces externos de familias distintas):** aportan evaluación independiente sin compartir el idiolecto del modelo autor (con peso igual `50 % / 50 %` cuando actúan solos).
   - **Juez opcional del mismo modelo autor (con menor peso):** solo debe incluirse para medir «autoceguera» cuando el entorno garantice aislamiento total de sesión (API limpia sin memoria de cuenta). Si la aplicación cliente puede retener contexto previo entre conversaciones, se excluye para evitar contaminación experimental (criterio aplicado en `v1.0.0`).
4. **Verificación literal:** antes de consolidar conclusiones o modificar el kit a partir de una reseña, comprobar en el manuscrito que cada cita y error señalado por un juez existe realmente en el texto.

---

## 4. Resultados publicados (`v1.0.0`)

- [`RESULTADOS_V1.0.md`](RESULTADOS_V1.0.md) — informe comparativo completo de las 12 corridas (`281.777` palabras), auditoría literal de las 24 reseñas y línea de base diagnóstica para `v1.1.0`.
- [`registro_corridas.csv`](registro_corridas.csv) — métricas de `habitos.py` y notas desglosadas por corrida (`M01`–`M12`).
- [`comparativa_ab_resumen.csv`](comparativa_ab_resumen.csv) — deltas apareados `Sin skills` vs. `Kit v1.0.0`.
- [`datos_habitos/`](datos_habitos/) — salidas íntegras reproducibles de `habitos.py` para cada manuscrito.
- [`../corridas/`](../corridas/) — los 12 manuscritos completos junto con sus reseñas `juez1.md` y `juez2.md`.
