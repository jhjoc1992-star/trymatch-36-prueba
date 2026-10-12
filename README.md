# TRYMATCH — Revisión 10

Reinicio estructurado del proyecto: mesa estilo póker con gráficos propios, reglas clásicas TRIO + SWAP, IA mixta y salas multijugador 2–6.

## Instalación
`npm install` y `npm start` (Node.js 20+). Visitar `http://localhost:3000`.

## Actualizar GitHub / Render
En el repositorio de pruebas `trymatch-36-prueba`, sustituir `server.js`, `package.json` y `public/index.html`. Render ejecuta `npm install` y `npm start`. No sustituir el repositorio original de respaldo.

## Documentación
- `docs/REGLAMENTO.md`: mecánica, SWAP, variantes y aceptación.
- `docs/TERMINOS_Y_PRIVACIDAD.md`: borrador de términos y privacidad.
- `docs/AUDITORIA_18_PERFILES.md`: decisiones de los 18 roles.

## Limitaciones
No hay servidor TURN, base de datos persistente, autenticación de cuentas ni clasificación online. La voz no está validada en teléfonos reales. Esta es una revisión funcional de desarrollo, no un producto comercial certificado.
