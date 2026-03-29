# ADR-002: Configuración por Entornos

**Contexto:** El sistema SCM requiere configuraciones separadas para dev, stage y prod, manteniendo los secretos seguros.
**Decisión:** Utilizaremos variables de entorno (`.env`) inyectadas vía Docker Compose para definir los contratos por entorno. Los secretos (como contraseñas de BD) no se versionarán en Git.
**Consecuencias:**
- Positivo: Cumple con la regla SCM de separar configuración del código fuente.
- Negativo: Requiere que cada desarrollador configure su propio archivo local de secretos.