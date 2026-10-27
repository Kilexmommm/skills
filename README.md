# Kilexmommm Skills

Colección de skills portables en formato Agent Skills. Cada skill vive en `dominio/nombre-del-skill/SKILL.md` y puede sincronizarse desde SkillBridge.

El contenido se prepara para su publicación: instrucciones reutilizables, ejemplos sintéticos y ninguna información privada de clientes. Las reglas de creación, privacidad y sincronización están en [AGENTS.md](AGENTS.md).

## Dominios

- `diseno/`: revisión UX de interfaces y flujos.
- `ingenieria/`: revisión de cambios de código.
- `extensiones/`: construcción y depuración de extensiones Chrome MV3.
- `playlists/`: curaduría de playlists.

## Prueba inicial

1. Sincroniza este repositorio en SkillBridge. Si el repositorio es privado, configura el acceso de lectura en la aplicación; nunca guardes credenciales en los skills ni en Git.
2. Abre una página de chat web y selecciona texto.
3. Elige uno de los cuatro skills importados. Confirma que el prompt correcto queda insertado y envíalo manualmente.

Los skills contienen instrucciones de dominio y no ejecutan código ni publican cambios.

## Crear o mejorar un skill

Primero aclaramos la tarea y el resultado esperado; después analizamos el alcance, escribimos el skill, revisamos privacidad y portabilidad, lo validamos y sincronizamos el commit con GitHub.

Antes de enviar cambios:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
python -m unittest discover -s tests
```

GitHub Actions repite estas comprobaciones en cada push y pull request. El validador comprueba estructura, metadatos y patrones frecuentes de información privada en archivos de texto versionados. No certifica anonimato: los nombres de clientes, el contexto identificable, los archivos binarios y el historial requieren revisión adicional antes de hacer público el repositorio.

La estructura sigue la [guía de skills de OpenAI](https://learn.chatgpt.com/docs/build-skills). La verificación funcional de cada skill debe hacerse con un caso de uso realista y datos sintéticos.
