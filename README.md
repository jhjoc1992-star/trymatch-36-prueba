# TRYMATCH 3.7 — Mesa corregida y salas de 2 a 6

## Instalación en GitHub y Render

Actualiza el repositorio **de prueba** `trymatch-36-prueba` (NO el repositorio de la 3.5). Reemplaza en GitHub los siguientes archivos manteniendo sus rutas:

- `server.js` (raíz)
- `package.json` (raíz)
- `public/index.html`

Los demás archivos del proyecto anterior permanecen intactos. Si no existe la carpeta public, créala y sube index.html dentro. En Render abre el servicio de pruebas, sección Events / Deploys, y espera el auto-deploy. Si no se activa, usa Manual Deploy > Deploy latest commit. **No crees otro Web Service.**

## Reglas de reparto

36 cartas: 3 copias de cada número 1-12. Dos jugadores: 12 por persona, 12 centro; tres: 9 y 9 centro; cuatro: 7 y 8 centro; cinco: 6 y 6 centro; seis: 5 y 6 centro.

## Limitaciones explícitas

- Salas de 2 a 6 jugadores reales con turnos, Alta/Baja y cartas centrales sincronizadas. La partida se inicia por el anfitrión cuando hay 2 o más participantes.
- No permite entrar una vez iniciada la partida; si alguien se desconecta durante la partida no hay reconexión de su asiento en esta beta.
- Voz PTT WebRTC disponible SOLO para salas de 2 jugadores; **voz grupal para 3-6 pendiente**, el botón se deshabilita para evitar falsa funcionalidad. WebRTC puede necesitar TURN incluso con dos personas.
- SWAP online es intercambio de dos cartas propias, regla provisional heredada de 3.5, todavía no la regla clásica completa.
- Pruebas visuales automatizadas realizadas con navegador simulado en tamaños 915x412, 740x360, 1280x720; falta validación con teléfonos Android reales y despliegue en Render.

## Notas

Abrir en Chrome Android en horizontal. Para audio, tocar 🔊 del HUD para habilitar y mantener HABLAR. El juego individual original se conserva en `public/classic-2-3.html`.
