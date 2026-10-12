# TRYMATCH 3.9 — Preliminar de pruebas

## Arranque
Node.js 20+; `npm install` y `npm start`. En Render: Web Service Node, Root Directory vacío si `server.js` está en raíz, Build `npm install`, Start `npm start`. Render debe servir HTTPS.

## Cambios respecto a 3.8
- Bloqueo explícito en servidor y cliente de la tercera carta cuando las primeras dos no coinciden.
- Dos cartas iguales desde Alta o Baja consecutivas siguen permitidas cuando son extremos legales.
- Contador de bajadas `0/3` visible para cada jugador.
- El trío especial del número 7 únicamente gana tras tres revelaciones legales en su turno.
- Prioridad visual de paneles y controles de jugadores sobre el tapete; ajustes de distribución compacta.
- Se conserva sala de 2 a 6, reconexión 90 segundos, IA sustituta y voz WebRTC de 3.8.

## Limitaciones honestas
- No se ha comprobado audio con dos Android reales. WebRTC podría requerir TURN en algunas redes.
- Render reiniciado pierde salas: el estado está en memoria.
- No hay publicidad ni registro de datos personales incorporados.
- Este ZIP es un proyecto para desplegar: el archivo `public/index.html` no funciona como multijugador sin servidor.
- Verificar partidas completas de 2 a 6 jugadores antes de declarar producción.

## Actualización del repositorio de prueba
Reemplazar `server.js`, `package.json`, `public/index.html` y conservar `public/classic-2-3.html`, `public/legacy-3-3.html`, `public/manifest.webmanifest`. Render desplegará el nuevo commit si está habilitado el despliegue automático. No tocar la versión oficial 3.5.

## Revisión
Consultar `REVISION_18_PERFILES.md` para los mandatos individuales y los criterios de aceptación.
