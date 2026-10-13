# TRYMATCH — REVISIÓN 07

Paquete de prueba web para Android Chrome, iPhone Safari y escritorio. Incluye servidor Node.js, WebSocket, interfaz y documentación. **No es un APK/IPA y no está desplegado automáticamente**.

## Publicación
1. Hacer copia de seguridad del proyecto estable y utilizar el repositorio de pruebas.
2. Subir `server.js`, `package.json` y `public/index.html` al repositorio de GitHub conectado a Render.
3. Render: `npm install` y `npm start`, Node.js >= 20. HTTPS para micrófono.
4. Abrir la URL existente del servicio. `/health` informa la revisión del servidor.

## Mecánica
Reglas de TRIO (36 cartas, extremos Alta/Baja, máximo 3 revelaciones) con SWAP una vez por turno antes de revelar: elegir carta propia y destino Mesa/rival; carta destino aleatoria. Modo Simple: 3 tríos; Picante: 7 o 2 tríos conectados. Modo de 2 jugadores es una variante digital propia. Ver `docs/REGLAMENTO_REV07.md`.

## Cambios principales
- Corrección del bloqueo de pulsación causado por superposición transparente del dock sobre cartas centrales.
- Selección SWAP contra jugador y Mesa verificada en navegador automatizado.
- Mensajes de error explícitos en jugadas rechazadas.
- Modo Simple/Picante alineado con el reglamento consultado.
- Asientos visualmente ligeros sin cajas rectangulares oscuras; avatares con apariencia 3D (CSS, no modelos 3D reales).
- Conserva cronómetro, espacio publicitario superior, IA y opciones mixtas, volumen, efectos y voz beta.

## Pruebas
`node --test tests/test-engine.mjs` (10 pruebas de lógica, sin dependencia `ws`), `python tests/ui_interactions.py` y `python tests/visual_check.py` (requieren Playwright y Chromium). Ver `docs/AUDITORIA_Y_PRUEBAS.md` para resultados y límites.

**Importante:** no se ha completado una partida multijugador real ni se ha validado la voz entre Android y iPhone. Las partidas viven en memoria y se pierden si el servidor reinicia. `npm install` no pudo finalizar en el entorno de preparación; Render instalará dependencias al desplegar si la red está disponible.
