# TRYMATCH 3.8 — versión de pruebas

Cambios: doble selección consecutiva de Alta/Baja para trío (sin seleccionar dos veces la misma carta), revelación central con origen, controles simétricos, jugadores por encima de la mesa, reconexión con token local y espera de 90 s, sustitución por IA tras la espera, voz PTT WebRTC con señalización entre 2–6 personas.

## Publicación
En el mismo repositorio de pruebas sustituye `server.js`, `package.json` y `public/index.html`. Render despliega el último commit si Auto Deploy está activo. No necesitas otro servicio.

## Límites
El estado de las salas está en memoria: un reinicio del servidor (incluidos reinicios del plan gratuito de Render) elimina las salas. La voz usa STUN público; en redes móviles con NAT restrictiva puede necesitar TURN para funcionar. La prueba real entre Android todavía es necesaria. La IA utiliza una estrategia básica, no el motor estratégico completo de la versión individual.

## Privacidad
El token de sesión se almacena en localStorage del navegador; no lo compartas. Audio entre navegadores por WebRTC, sin grabación en servidor.
