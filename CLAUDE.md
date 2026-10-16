# Formato de redes desde el 16/10/2026 (manda sobre lo de abajo)

**Cada sección lleva su nombre** (decisión de María, 16/10): en el guion de montar_reel.py pon `"seccion"` (sale como etiqueta de color arriba en la primera escena) y empieza el texto de la publicación con el nombre en mayúsculas. Secciones: Curiosidades de mascotas (18:00 y curiosidades rehechas), Historias de cuatro patas (22:00), Producto del día (20:00), Los animales, nuestros amigos (lunes y jueves 13:00), Curiosidades del mundo animal (sábado y domingo 13:00), Del blog de Petsforyou y La familia Petsforyou (reels de las tarjetas). Ada y sus amigos y Las mascotas hablan ya tienen su propia intro.

María decidió el 16/10 que la tarjeta blanca no funciona en Instagram y Facebook. Desde ese día:

- **Todo reel nuevo se monta a pantalla completa** con `herramientas/montar_reel.py` (uso y formato del guion en su cabecera): 1080x1920, la foto ocupa toda la pantalla con zoom lento, fundido entre fotos cada 3,5-4,5 s, subtítulos grandes abajo frase a frase y un gancho arriba desde el segundo 0. Sin recuadro blanco. Las tarjetas de `tarjeta.py` ya programadas se dejan como estaban y llevan "👀 Mañana te lo contamos con más detalle."; su reel sale al día siguiente a la misma hora.
- **Contenido con información de verdad**: curiosidades y noticias con 6-8 datos concretos y comprobables (25-30 s), ordenados de más sorprendente a más útil, y una pregunta final. Nada de relleno.
- **Historias**: rescates, héroes, abandonos con final feliz, superación. Una imagen por cada frase de la historia (lo que se cuenta en ese momento), nunca la misma foto repetida. Fotos reales primero: de cuentas oficiales (Guardia Civil, Policía, bomberos, 112, ayuntamientos) o de los dueños/protagonistas, mencionándolos y etiquetándolos. Fotos de agencias (EFE, Europa Press…) o periódicos no: busca la misma historia en otra fuente. Si no hay foto real de una escena, se genera (ElevenLabs, bytedance-seedream-5-pro; sale en 16:9, usa "x" para el recorte) y se marca "Imágenes ilustrativas creadas con IA".
- **Música acorde a la historia** (en `audio/`): héroes → `musica-heroe-epica.mp3`; abandono → `musica-abandono-triste.mp3`; superación → `musica-superacion-inspiradora.mp3`; historias tiernas → `musica-historias-emocionante.mp3`; curiosidades → `musica-curiosidades-pegadiza.mp3`.
- **Publicar**: subir el mp4 a `videos/` de este repositorio y programarlo con "🎬 Programar vídeo en redes (Upload-Post)" (Instagram, Facebook, TikTok, YouTube y Pinterest).
- **Historias de cuatro patas: todos los días a las 22:00** (hora de Madrid; hasta el 16/10 a las 20:30, se movió para separarla del Producto del día de las 20:00).
- **Producto del día: todos los días a las 20:00** desde el 17/10/2026 (sustituye a "máximo 2 productos por semana"): producto dentro de un consejo útil, imágenes bonitas de mascotas usando el producto generadas a partir de su foto real (etiqueta "Imágenes creadas con IA a partir del producto real") y precio y stock comprobados en Shopify el mismo día.

# Normas de publicación

- **Todo lo que se publique en redes va también a YouTube** (Shorts).
  - Vídeos: el flujo de Make "🎬 Programar vídeo en redes (Upload-Post)" ya incluye YouTube.
  - Carruseles y fotos: además del carrusel, montar un vídeo vertical "foto con música"
    (1080x1920, 15-20 s, guardado en `videos/<nombre>.mp4`) y programarlo con el flujo de Make
    "▶️ Vídeo solo en YouTube (Upload-Post)" (escenario 7741886: video, titulo, texto, fecha, clave).
- (Hasta el 16/10) Las fotos con música funcionaban mejor que los reels.

# Calendario de redes (desde el 12/10/26)

- Calendario vigente en `calendario/` (y en Drive, carpeta "Calendario editorial", documento "(VIGENTE)").
- 13 publicaciones por semana (hora de Madrid): curiosidad en vídeo cada día a las 18:00; "Historias de cuatro patas" todos los días a las 20:30 (antes martes y sábado 13:00); producto dentro de un consejo miércoles 13:00; avance de Ada jueves 13:00; capítulo de Ada viernes 13:00; guía en carrusel con producto domingo 13:00.
- (Hasta el 16/10) Máximo 2 publicaciones de producto por semana. Desde el 17/10, uno al día a las 20:00, siempre dentro de un consejo útil.
- No se publican: Cosas de casa, Quién es quién, Las mascotas hablan, Antes y después, frase de la semana, Frases de vida.
- María no aparece en cámara y no se colabora con protectoras.
- (Solo para lo ya programado) Tarjetas 1080x1350 con el estilo de la casa: `herramientas/tarjeta.py`. Lo nuevo va con `herramientas/montar_reel.py`. Músicas reutilizables: `audio/musica-noticias.mp3` y `audio/musica-curiosidades.mp3`.
- El envío es gratis siempre (no poner "desde 25 €").
