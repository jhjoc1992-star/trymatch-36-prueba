# TRYMATCH 4.0 — prueba de distribución y memoria

Actualización de la 3.9: botones SWAP/Cancelar y micrófono próximos a la mano; capas de controles por delante de la mesa; paneles de rivales distribuidos según 2–6 jugadores; carta revelada junto al rival correspondiente y en el centro.

La lógica del servidor conserva un máximo de tres revelaciones por turno y prohíbe la tercera si las primeras dos no coinciden. Permite repetir Alta/Baja si hay otra carta en ese extremo.

## Publicación

En el repositorio de PRUEBA ya conectado a Render, reemplaza `server.js`, `package.json` y `public/index.html`. No borres `public/classic-2-3.html`, `public/legacy-3-3.html` ni `public/manifest.webmanifest`. Render debería desplegar automáticamente o puedes usar Manual Deploy → Deploy latest commit.

## Límites

No se ha validado con seis dispositivos reales ni se garantiza el audio WebRTC en redes que requieren TURN. El diseño móvil necesita comprobarse en los teléfonos de los participantes. Las partidas permanecen en memoria del servidor.
