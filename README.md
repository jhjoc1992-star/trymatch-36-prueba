# TRYMATCH 4.1 — Mesa mixta (preliminar)

Actualización de 4.0. Mantiene el estilo aprobado. Paneles compactos de rivales en una fila que se adapta a 1–5 rivales; botones Alta/Baja por encima del tapete. Dock SWAP / Cancelar / mano / HABLAR unido.

## Nueva opción
En el menú marca «Completar asientos vacíos con IA», selecciona jugadores totales 2–6 y dificultad principiante, normal o experta. Entra en la sala, invita a amigos si quieres y pulsa iniciar: el servidor completa los asientos libres con IA. También puedes jugar una sola persona contra IA.

La IA básica no usa información oculta para elegir: solo memoriza cartas reveladas anteriormente con probabilidad según dificultad. La memoria se reinicia después de un trío, porque cambian índices de cartas.

## Actualización
Reemplaza server.js, package.json y public/index.html en el repositorio de pruebas de GitHub. Render despliega la actualización automáticamente o Manual Deploy → Deploy latest commit. No crear un nuevo servidor.

## Limitaciones
No se ha probado con seis teléfonos reales; la voz WebRTC sigue dependiendo de conectividad entre redes y puede necesitar TURN. Las partidas se almacenan en memoria. La interfaz se debe comprobar en los Android reales. El botón de voz permanece visible también contra IA, pero la IA no habla ni escucha. El modo de un humano + IA requiere el servidor 4.1; no funciona solo abriendo el HTML.

Referencia de reglas: https://es.boardgamearena.com/gamepanel?game=trio. El modo clásico de TRIO y las adaptaciones propias de TRYMATCH no deben confundirse.
