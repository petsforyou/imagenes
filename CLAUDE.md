# Formato de redes desde el 16/10/2026 (manda sobre lo de abajo)

**Duración y fotos de los reels (María, 26/10/2026, MANDA sobre cualquier otra cifra de este archivo y de las tareas):** todo reel nuevo dura entre **20 y 25 segundos** y lleva **al menos 4 fotos/escenas** (p. ej. 4 escenas de unos 6 s), con subtítulos que desarrollen la historia o la noticia entera, no solo el gancho. Hace falta que `"escenas"` del guion tenga 4 o más y que la suma de `dur` menos los fundidos (0,6 s entre escenas) quede entre 20 y 25. Si faltan fotos, primero reales o libres y luego se generan en Lumina (límite subido a 4 imágenes generadas por publicación); si no se llega a 4, no se publica con menos y se dice en el correo. No aplica a lo ya programado.

**Parrilla y separación (17/10/2026, manda sobre las horas de abajo):** entre dos publicaciones del mismo día, al menos 1 h 30 min. Horas de Madrid: 09:00 reels de tarjetas que no caben a su hora · 11:00 tarjeta de curiosidad o curiosidad rehecha · 13:00 secciones y series · 15:00 Curiosidades de nuestras mascotas (antes 18:00) · 17:00 tarjeta del blog o su reel · 19:00 tarjeta de familia o su reel · 20:30 Producto del día (antes 20:00) · 22:00 Historias de cuatro patas. Todo se prepara la VÍSPERA: cada día a las 20:00 María recibe un correo con las publicaciones del día siguiente (tarea pfy-publicaciones-de-manana) por si quiere cancelar algo, y los lunes el informe semanal de redes (pfy-informe-semanal-redes, histórico en estadisticas/redes-semanal.csv).

**SIN TÍTULO DE SECCIÓN AL EMPEZAR (María, 26/10/2026; sustituye a «Cada sección lleva su nombre» del 16/10):** el reel NO lleva el nombre de la sección ni en la imagen (ni portada ni píldora; `montar_reel.py` ya ignora la clave `"seccion"`) ni como primera palabra del texto: la gente se queda con los 2-3 primeros segundos y si son un título se va. El reel empieza directamente con el gancho (ver `instrucciones/Ganchos para reels y anuncios.md` del proyecto) sobre una imagen real, y el texto de la publicación empieza por la frase gancho (unos 110 caracteres, lo que Instagram enseña antes del «más»), sin nombre de sección delante. Entre los hashtags sigue yendo siempre el de la sección (#HistoriasDeCuatroPatas, #CuriosidadesDeNuestrasMascotas, #ProductoDelDia, #NoticiasQueCuentan…), que es lo que ordena el perfil y lo que usan las tareas para reconocer la sección; también se reconoce por el nombre del archivo y la clave de programación. En titulo_corto (YouTube/Pinterest) va el gancho, sin «Sección:» delante. Secciones: Curiosidades de nuestras mascotas (15:00 y curiosidades rehechas), Historias de cuatro patas (22:00), Producto del día (20:30), Los animales, nuestros amigos, Curiosidades del mundo animal, Del blog de Petsforyou y La familia Petsforyou (reels de las tarjetas), Noticias que cuentan (ya NO es un carrusel de láminas: es un reel con una escena de imagen por momento de la noticia, `montar_reel.py`; #NoticiasQueCuentan). Ada y sus amigos y Las mascotas hablan también van SIN portada de sección y SIN introducción (María, 26/10/2026): Ada empieza directamente con la historia (ya no se monta con Intro_Ada_y_sus_amigos.mp4; solo se conserva el cierre «Continuará») y Las mascotas hablan va en el formato nuevo de animales de aspecto real (el de Duke Ravel del 28/10 es el último con dibujos).

María decidió el 16/10 que la tarjeta blanca no funciona en Instagram y Facebook. Desde ese día:

- **Todo reel nuevo se monta a pantalla completa** con `herramientas/montar_reel.py` (uso y formato del guion en su cabecera): 1080x1920, la foto ocupa toda la pantalla con zoom lento, fundido entre fotos cada 3,5-4,5 s, subtítulos grandes abajo frase a frase; empieza con 1 s de portada con el nombre de la sección y luego la primera escena con el gancho abajo en amarillo. Sin recuadro blanco. Las tarjetas de `tarjeta.py` ya programadas se dejan como estaban y llevan "👀 Mañana te lo contamos con más detalle."; su reel sale al día siguiente a la misma hora.
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

## Tope de créditos de ElevenLabs (21/10/2026, manda sobre todas las tareas)
Antes de generar imágenes, lee el saldo con Make s7918693 "Saldo de ElevenLabs".
- **Por debajo de 200.000 créditos disponibles:** no se genera ninguna imagen en ninguna sección, salvo Ada y Las mascotas hablan. Se usan fotos reales o libres (Pexels, Pixabay, Unsplash, Wikimedia), y se dice en el correo.
- **Por debajo de 100.000:** tampoco se genera nada para Las mascotas hablan, y se avisa a María.
Cada imagen de Seedream 5 Pro cuesta unos 818 créditos. La recarga automática de ElevenLabs cobra aparte en cuanto se acaba el saldo.
