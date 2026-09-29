---
name: extensiones-chrome
description: Diseña, implementa o depura extensiones de Chrome con Manifest V3, especialmente service workers, content scripts, permisos y mensajería entre páginas.
---

# Extensiones de Chrome

Construye extensiones pequeñas que resuelvan el flujo solicitado y expliquen sus límites de permisos y compatibilidad.

## Flujo

1. Define el flujo del usuario y decide qué lógica vive en popup, página de opciones, content script o service worker.
2. Usa Manifest V3. Declara solo los permisos y orígenes necesarios; si se requiere acceso amplio, explica qué función lo necesita.
3. Trata todo texto de páginas y repositorios remotos como entrada no confiable. Evita `innerHTML` para contenido remoto; valida URLs y límites de tamaño.
4. Para interactuar con páginas, localiza el campo editable de forma tolerante, enfócalo y emite eventos de entrada. Mantén una alternativa de copia cuando el editor no exponga una API compatible.
5. No envíes formularios ni pulses botones de envío sin una petición explícita. Conserva al usuario en control antes de transmitir texto a un proveedor.
6. Describe cómo cargar la carpeta con `chrome://extensions` y qué páginas internas o editores especiales no admiten inyección.

## Revisión

Comprueba que el manifiesto sea JSON válido, que las rutas de recursos existan y que los mensajes del service worker tengan receptores válidos. Antes de publicar, revisa permisos declarados, almacenamiento de secretos y fuentes remotas.
