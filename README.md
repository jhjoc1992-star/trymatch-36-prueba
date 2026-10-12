# TRYMATCH — Revisión 08

Aplicación web multijugador para navegadores móviles Android (Chrome) y iPhone (Safari). No requiere instalación de APK/IPA.

## Instalación

1. Sustituir `server.js`, `package.json` y `public/index.html` en el repositorio de pruebas conectado a Render.
2. Render: comando de instalación `npm install`, inicio `npm start`. Necesita Node >=20 y conexión HTTPS para el micrófono.
3. Abrir el enlace HTTPS de Render en Chrome Android o Safari iPhone. Para voz, permitir acceso al micrófono y mantener pulsado HABLAR. La conectividad entre redes celulares puede requerir servidor TURN, no incluido.

## Cambios principales

- SWAP: elegir carta propia y destino mesa o rival; selección aleatoria por el servidor. Resaltado de la carta recibida.
- Revelaciones sin espera entre primera, segunda y tercera si la jugada sigue siendo legal. Al fallar o cerrar un trío se mantiene el intervalo elegido de 6/8/10 s, predeterminado 8 s.
- Cartas reveladas en color sólido, etiqueta de origen, panel de jugador destacado.
- Bienvenida breve, sonidos sintetizados Web Audio y celebraciones visuales de trío y victoria. Volumen inicial 75%, configurable.
- Avatares adicionales, paneles compactos, cronómetro y espacio publicitario en la misma barra.
- Mesa de 2 a 6 participantes, con amigos y/o IA.

## Limitaciones y verificación

La sintaxis de servidor y cliente fue verificada con `node --check`. No se pudo instalar `ws` ni abrir una sesión gráfica de navegador en el entorno de creación; no se han ejecutado partidas completas ni pruebas en dispositivos Android/iPhone reales. La voz WebRTC puede necesitar TURN, y el modo pantalla completa depende del navegador (Safari iOS tiene restricciones). Las partidas están en memoria: un reinicio de Render las elimina. Los 18 perfiles son criterios de revisión simulados, no personas contratadas.

Consultar `docs/REGLAMENTO.md`, `docs/CAMBIOS_REV_08.md` y `docs/TERMINOS_Y_PRIVACIDAD.md`.
