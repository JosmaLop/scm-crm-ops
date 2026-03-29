# ADR-001: Estrategia de Branching y Releases

**Contexto:** Necesitamos un flujo de trabajo para que el equipo (3-5 personas) trabaje de forma segura sin romper la rama principal.
**Decisión:** Adoptamos un modelo de Feature Branches (GitHub Flow). La rama `main` estará protegida. Todo cambio requiere un Pull Request (PR) y revisión antes del merge.
**Consecuencias:**
- Positivo: Evita despliegues de código roto en `main`.
- Negativo: Agrega fricción al obligar a hacer PRs para cambios mínimos.