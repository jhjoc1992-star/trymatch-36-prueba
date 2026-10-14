# TRYMATCH — Revisión 7.3 (beta de corrección)

Actualización de la Revisión 7.2 centrada en **desbloquear SWAP/Cancelar**, corregir la presentación de las cartas y despejar la mesa de seis jugadores.

## Instalación en GitHub + Render

1. Conserva una copia de la revisión anterior.
2. Sube a la raíz del repositorio `server.js` y `package.json`.
3. Sustituye `public/index.html` y sube **todos** los archivos de `public/assets/` conservando sus nombres.
4. En Render despliega el último commit y comprueba `/health` (debe indicar `revision: 07.3`).
5. En Chrome recarga forzosamente la página para evitar caché.

## Pruebas

- `node --check server.js`
- `npm test` (la suite original inicia un servidor de prueba y puede dejar el proceso abierto tras informar los resultados)
- `python tests/ui_interactions.py` (requiere Playwright y Chromium)
- `python tests/visual_rev73.py` (capturas de 915×412 y 390×844)

Consulta `docs/CAMBIOS_REV73.md` para detalles y limitaciones.
