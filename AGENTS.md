# Creación y mantenimiento de skills públicos

Este repositorio contiene skills destinados a compartirse públicamente. Aplica estas reglas al crear o actualizar su contenido.

## Conversar y analizar antes de crear

- Parte de la tarea real del usuario. Pregunta lo que falte para entender entradas, resultado esperado, límites y un ejemplo de uso; evita repetir preguntas ya respondidas.
- Analiza si conviene crear un skill o mejorar uno existente. Resume su propósito y alcance antes de escribirlo; avanza cuando el contexto sea suficiente.
- Conserva la estructura `dominio/nombre-del-skill/SKILL.md`. Usa nombres en minúsculas con guiones, una descripción precisa y recursos adicionales solo cuando aporten utilidad.
- Si está disponible, utiliza la guía `skill-creator` de OpenAI. Mantén el formato Agent Skills y declara dependencias reales, sin asumir herramientas instaladas en otra máquina.

## Privacidad y portabilidad

- Escribe instrucciones agnósticas respecto del cliente: sin nombres de clientes, marcas privadas, proyectos internos, contactos, identificadores de cuentas ni información contractual.
- Usa ejemplos sintéticos como «Organización de ejemplo», `persona@example.com` y `https://example.com`. Generaliza también el contexto que pueda identificar a un cliente indirectamente.
- No copies credenciales, tokens, archivos de entorno, conversaciones, capturas, datos reales de usuarios ni documentos de clientes. Sustituye rutas personales por rutas relativas o variables configurables.
- Los nombres de herramientas públicas pueden aparecer cuando son necesarios para la función del skill. Separa esas dependencias de cualquier configuración propia de un cliente.
- Revisa todos los archivos que acompañen al skill, incluidos scripts, referencias, imágenes y sus metadatos. Un detector automático no reconoce todos los datos privados ni todos los nombres de clientes.

## Verificar y sincronizar

- Ejecuta `python scripts/validate_skills.py` con las dependencias de `requirements-dev.txt`. Si está disponible, ejecuta también `quick_validate.py` de `skill-creator` sobre cada skill modificado.
- Comprueba enlaces y rutas locales, coherencia de los metadatos y al menos un caso de uso representativo. Ejecuta los scripts nuevos o modificados con datos sintéticos y dentro del alcance autorizado.
- Revisa el diff y los archivos que entrarán al commit. Antes de hacer público el repositorio, revisa también su historial: borrar un secreto del último archivo no lo elimina de commits anteriores.
- Para sincronizar cambios solicitados con GitHub, comprueba primero la rama remota, crea un commit acotado y envíalo sin forzar el historial. Resuelve cualquier cambio concurrente antes de continuar.
- Verifica que el commit remoto coincida con el preparado y consulta el resultado de las comprobaciones. Distingue «validado localmente», «sincronizado» y «verificado en GitHub» según la evidencia disponible.
- No cambies la visibilidad del repositorio ni instales o modifiques skills locales como parte de esta sincronización, salvo petición del usuario.
