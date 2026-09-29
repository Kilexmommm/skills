---
name: ingenieria-code-review
description: Analiza código o un diff para encontrar fallos funcionales, riesgos de seguridad y regresiones concretas; úsala en revisiones de cambios de software.
---

# Revisión de ingeniería de software

Revisa el cambio respecto a su comportamiento esperado. Prioriza defectos demostrables sobre estilo o preferencias personales.

## Flujo

1. Lee el diff y el contexto mínimo de los archivos afectados. Averigua qué comportamiento intenta implementar.
2. Sigue los datos y el control a través de las rutas modificadas; comprueba entradas límite, errores, permisos, concurrencia y compatibilidad con usos existentes cuando sean relevantes.
3. Reporta solo hallazgos accionables. Para cada uno incluye severidad, archivo y ubicación, escenario de activación y consecuencia.
4. Distingue los defectos confirmados de preguntas o riesgos que requieren más contexto. Si no encuentras defectos, dilo con claridad y menciona qué áreas no pudiste verificar.

## Prioridad

- **P1:** pérdida de datos, exposición de información o fallo amplio que bloquea el uso.
- **P2:** fallo importante en un flujo central, con una forma realista de activarlo.
- **P3:** defecto acotado que degrada una función secundaria.

No marques como fallo una posibilidad puramente hipotética. No edites el código durante una revisión, salvo que el usuario pida además corregir los hallazgos.
