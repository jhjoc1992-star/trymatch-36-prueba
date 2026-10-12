# TRYMATCH 3.9 — Mandatos individuales de revisión

Los siguientes son **18 perspectivas simuladas de IA**, no evaluaciones realizadas por profesionales humanos. Cada rol debe leer los archivos reales, señalar la evidencia, distinguir pruebas ejecutadas de pendientes y proponer cambios sin alterar la identidad visual 2.3.

1. **Diseñador de reglas:** verifica el reglamento original; tercera carta SOLO cuando las dos primeras coinciden; trío 7 gana únicamente si se completa en el turno legal; tres bajadas para ganar; evalúa casos extremos.
2. **Programador de juego:** audita `reveal`, `advance`, `reset`, `action`; evita índices reutilizados, dobles pulsaciones y carreras entre temporizadores; añade pruebas reproducibles.
3. **UX móvil:** verifica que todo jugador pueda distinguir su turno, carta revelada y propietario; máximo dos gestos para acciones esenciales; controles táctiles cómodos.
4. **Diseñador UI:** preserva mesa verde ovalada, borde marrón, fondo azul, cartas con número central único y colores; alinea SWAP y micrófono cerca de la mano; no superponer paneles.
5. **QA:** ejecuta matriz de 2–6 jugadores, coincidencias/no coincidencias, dos Alta seguidas, siete especial, reconexión, IA y regresión. Bloquea entrega por fallos P0.
6. **Artista del juego:** revisa contraste, iconos y coherencia; elimina ruido ornamental, conserva estética clásica y cartas distinguibles.
7. **Ingeniero de IA:** la IA sustituta respeta exactamente el turno, las cartas visibles y las reglas; nunca actúa durante la pausa de reconexión.
8. **Especialista en animaciones:** carta revelada visible en centro y referencia clara a origen; transiciones no impiden tocar otros controles.
9. **Ingeniero de voz:** valida micrófono y recepción WebRTC en Android HTTPS; push-to-talk real, permisos, STUN/TURN, audio desbloqueado y privacidad; no declarar probado sin dos dispositivos.
10. **Rendimiento Android:** mide tamaños 740×360, 915×412, 1280×720, latencia y FPS; optimiza DOM y red.
11. **Accesibilidad:** controles legibles, foco y etiquetas, tamaños táctiles, no depender solo del color, mensajes claros de turno.
12. **Seguridad:** servidor autoritativo, tokens de reconexión privados, salas con límite de seis, no filtrar manos ajenas ni permitir acciones fuera de turno.
13. **Backend multijugador:** valida WebSocket, reconexión 90 s, pausas, reemplazo IA, sincronía de estado, reinicios Render y reglas del servidor.
14. **Producto comercial:** evalúa publicidad no intrusiva, sin recopilar datos personales adicionales ni pedir registro; nunca mostrar publicidad durante la revelación o un turno.
15. **Analítica y observabilidad:** registra fallos técnicos sin datos personales, latencias y eventos de errores; explica qué métricas faltan.
16. **Legal y privacidad:** analiza diferencias con el juego de inspiración, marcas, contenido, consentimiento del micrófono y requisitos legales antes de publicar.
17. **Marketing/ASO:** valora nombre, claridad del menú y primer minuto de juego; inspiración en estándares de mesas de póker sin copiar recursos de PokerStars.
18. **Director de producto:** reúne hallazgos, ordena P0/P1/P2/P3, exige pruebas verificables y entrega veredicto APROBADO PARA PRUEBAS / CON LIMITACIONES / RECHAZADO.

## Puertas de aceptación
- No se puede revelar una tercera carta si las primeras dos difieren.
- Se permite repetir Alta/Baja si existe una nueva carta extrema legal.
- El trío de 7 solo gana al completarse legalmente durante el turno.
- El contador de bajadas es visible para todos; tres tríos normales completan la victoria.
- Los botones de todos los rivales permanecen accesibles con seis participantes en Android horizontal.
- Nunca anunciar voz, reconexión o persistencia como verificadas sin pruebas reales correspondientes.
