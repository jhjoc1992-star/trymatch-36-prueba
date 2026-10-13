# TRYMATCH — REVISIÓN 7.2 (beta de integración)

Aplicación web multijugador basada en la revisión 07. Contiene servidor Node.js + WebSocket, interfaz responsive y pruebas del motor. **No es una aplicación nativa APK o IPA.**

## Instalación

1. Haz copia de seguridad de la revisión estable y utiliza solo el repositorio de pruebas.
2. Copia `server.js`, `package.json` y toda la carpeta `public/` (incluido `public/assets/`).
3. En Render utiliza Node >= 20, `npm install` y `npm start`.
4. Abre el servicio HTTPS desde Android Chrome o iPhone Safari. No se ha verificado aún en teléfonos reales.

## Cambios

- Nuevo diseño azul y dorado basado en la imagen aportada, retratos de avatar prerenderizados, cinco paletas de mesa y botones SWAP junto a cada rival.
- SWAP una vez por turno, selección visible de carta saliente y resaltado de carta entrante.
- Solo modo clásico, 3 tríos para ganar y trío 7 especial.
- Solucionado defecto que daba trío falso cuando la tercera carta difería.
- Bienvenida de 7 segundos al entrar en la mesa.

## Verificación

`npm test` ejecuta diez pruebas del motor. `node --check server.js` comprueba sintaxis. Ver `docs/ESTADO_REV72.md` para las limitaciones. Las capturas de `docs/VISTA_REV72_*.png` son simulaciones de interfaz en Chromium, no capturas de teléfonos.
