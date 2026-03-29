# ADR-003: Artefactos Inmutables y Promoción

**Contexto:** Cada release debe producir un artefacto versionado que se promueva entre entornos (promote, don't rebuild).
**Decisión:** Empaquetaremos la API (Python/Flask) usando Docker. El `Dockerfile` se construirá una sola vez, generando una imagen que se etiquetará y usará tanto en Stage como en Producción.
**Consecuencias:**
- Positivo: Garantiza que lo que se prueba en Stage es exactamente el mismo binario que va a Producción.
- Negativo: Mayor consumo de espacio de almacenamiento en el registry por cada versión construida.