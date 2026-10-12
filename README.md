# TRYMATCH 3.6 — Preliminar jugable

Proyecto basado en la **interfaz 2.3** y el **servidor de partidas 3.5**.

## Contenido
- `public/index.html`: menú y tablero online con el estilo verde, borde y cartas de 2.3, SWAP/Cancelar a la izquierda, botón HABLAR a la derecha.
- `public/classic-2-3.html`: versión 2.3 original, intacta, para jugar contra IA.
- `server.js`: servidor de salas 3.5, sin cambios en protocolo.
- `public/legacy-3-3.html`: demo 3.3 conservada.

## Cómo probar sin tocar tu despliegue actual
1. Crea **otro repositorio** GitHub, por ejemplo `trymatch-36-prueba`.
2. Sube los archivos de esta carpeta conservando `public/`.
3. Crea **otro Web Service** en Render con `npm install` y `npm start`, seleccionando Free si existe. No conectes este proyecto al servicio que ya funciona.
4. Abre el enlace HTTPS nuevo en dos teléfonos, crea sala y entra con QR.
5. Ambos pulsan **Activar audio** y conceden permiso. Mantener HABLAR para transmitir.

## Limitaciones
- Beta de dos jugadores; el servidor todavía no soporta reconexión tras cerrar la pestaña.
- Voz P2P con STUN público: en algunas redes móviles necesita TURN; no se garantiza audio hasta probarlo.
- El botón de SWAP de la partida online intercambia dos cartas de tu propia mano, como en la beta 3.5. La regla original 2.3 de SWAP contra rival requiere adaptar el protocolo del servidor antes de publicar.
- La mesa online conserva la estética 2.3 pero aún no implementa seis asientos humanos, selección de dificultad para IA en red, fotos compartidas ni todos los modos de juego. El modo IA original sigue intacto en `classic-2-3.html`.
- El código QR usa un servicio público de generación de imágenes; para producción debe sustituirse por QR local.
- No hay anuncios reales ni monetización todavía.

## Verificación
`npm install && npm start`, visitar `http://localhost:3000/health`.
