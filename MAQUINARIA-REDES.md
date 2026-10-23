# La maquinaria de publicación en redes de PetsForYou

Informe de situación a 23 de octubre de 2026. Describe qué secciones se publican, a qué hora, cómo tienen que ir publicadas, quién las prepara, cuándo se preparan y de qué materiales se sirven.

---

## 1. Qué documento manda

Hay tres sitios donde viven las reglas, y se contradicen entre sí. El orden de autoridad es:

1. **`CLAUDE.md` en la raíz de `petsforyou/imagenes`** (16 y 17/10/2026). Es la norma vigente. Su primera línea dice expresamente que manda sobre lo de abajo.
2. **`calendario/2026-10-12_a_2026-11-08.md`** (del 11/10). Útil para los temas concretos de cada día, pero su parrilla y sus reglas de producto están **superadas**.
3. Los prompts de cada tarea programada, que pueden llevar decisiones con fecha propia (por ejemplo la suspensión de Holywin).

**Contradicciones vivas que hay que resolver** (ninguna la puede decidir una tarea, las decide María):

- Curiosidad en vídeo: el calendario dice 18:00; el `CLAUDE.md` la movió a las **15:00**. Manda las 15:00.
- Historias de cuatro patas: el calendario dice martes y sábado a las 13:00; el `CLAUDE.md` dice **todos los días**, y dentro del propio `CLAUDE.md` aparece a las 22:00 en la parrilla del 17/10 y a las 20:30 en la sección de calendario. Manda **22:00**, por ser la parrilla del 17/10.
- Producto del día: el calendario dice máximo 2 por semana; el `CLAUDE.md` lo sustituyó el 17/10 por **uno al día**, y aparece a las 20:30 en la parrilla y a las 20:00 más abajo. Manda **20:30**.
- Holywin: el prompt de "Producto de la semana" dice que **desde el 26/10 no se publica nada de Holywin ni Halloween**, pero el calendario llama a la semana 3 "(Holywin)", hay seis vídeos de Holywin programados del 26 al 31, y el especial de Halloween de Ada está previsto para el viernes 30.

Mientras el calendario del repo no se actualice, cualquier informe que lo use como referencia dará falsos positivos. Pasó el 23/10 con el informe de los viernes.

---

## 2. La parrilla del día (vigente, `CLAUDE.md` 17/10)

Horas de Madrid. **Entre dos publicaciones del mismo día, mínimo 1 hora y 30 minutos.**

| Hora | Qué va |
|---|---|
| 09:00 | Reels de tarjetas que no caben a su hora |
| 11:00 | Tarjeta de curiosidad, o curiosidad rehecha |
| 13:00 | Secciones y series |
| 15:00 | Curiosidades de nuestras mascotas |
| 17:00 | Tarjeta del blog, o su reel |
| 19:00 | Tarjeta de familia, o su reel |
| 20:30 | Producto del día |
| 22:00 | Historias de cuatro patas |

Son ocho huecos fijos. Con las noticias de X (hasta 2 al día) y los reels de repesca, salen unas 10 publicaciones diarias.

El hueco de las 13:00 lo reparten las secciones por día: Los animales, nuestros amigos (lunes y jueves), Curiosidades del mundo animal (sábado y domingo), Ada y sus amigos (viernes el capítulo, jueves el avance), Producto útil dentro de un consejo (miércoles) y Guía en carrusel (domingo).

---

## 3. Las secciones, una a una

Cada sección lleva su nombre (decisión de María del 16/10): el reel empieza con 1 segundo de portada con el nombre de la sección, el texto de la publicación abre con el nombre en mayúsculas más emoji más la frase gancho (unos 110 caracteres, lo que Instagram enseña antes del "más"), y entre los hashtags va siempre el de la sección.

**Curiosidades de nuestras mascotas** — 15:00. El formato que mejor funciona: unas 1.100 visualizaciones en YouTube y la gente ve el 77-82 % del vídeo. De 6 a 8 datos concretos y comprobables, de más sorprendente a más útil, 25-30 segundos, y una pregunta final. Materiales: los vídeos ya montados `videos/curiosidad-NN.mp4` (hay del 51 al 90), más las versiones rehechas `curiosidad-<tema>-reel.mp4`. Hashtag `#CuriosidadesDeNuestrasMascotas`.

**Historias de cuatro patas** — 22:00. Rescates, héroes, abandonos con final feliz, superación. Noticia real y positiva, mejor de España, buscada la misma semana y siempre con la fuente citada. Segundo formato que mejor funciona (600-750 visualizaciones; esta semana la de Clark y el niño de 6 años hizo 2.224). Una imagen por cada frase de la historia, nunca la misma foto repetida. Fotos reales primero, de cuentas oficiales (Guardia Civil, Policía, bomberos, 112, ayuntamientos) o de los dueños, mencionándolos y etiquetándolos; nunca de agencias ni de periódicos. Si no hay foto real de una escena, se genera con ElevenLabs (`bytedance-seedream-5-pro`) y se marca "Imágenes ilustrativas creadas con IA". Hashtag `#HistoriasDeCuatroPatas`.

**Producto del día** — 20:30, uno al día desde el 17/10. Producto dentro de un consejo útil, nunca anuncio a secas. Imágenes bonitas de mascotas usando el producto, generadas a partir de su foto real, con la etiqueta "Imágenes creadas con IA a partir del producto real". Precio y stock comprobados en Shopify el mismo día. Envío gratis siempre, sin pedido mínimo: se escribe "Envío gratis" y nunca "desde 25 €". Hashtag `#ProductoDelDia`.

**Los animales, nuestros amigos** — lunes y jueves a las 13:00. Fauna salvaje rescatada o liberada.

**Curiosidades del mundo animal** — sábado y domingo a las 13:00. Conservación, datos de especies.

**Noticias que cuentan** — martes a las 11:00. Carrusel de 5 láminas hecho con `herramientas/carrusel_noticias.py`: portada con el título, 3 noticias de normativa, veterinaria, ganadería o vida en sociedad en lenguaje llano, y cierre. Hashtag `#NoticiasQueCuentan`.

**Del blog de Petsforyou** — 17:00. Tarjeta del artículo o su reel, con enlace al artículo.

**La familia Petsforyou** — 19:00. Cloe, Zara, Mango y Maya. Tarjeta o reel.

**Ada y sus amigos** — capítulo el viernes a las 13:00, avance el jueves a las 13:00. Uno por semana; si un capítulo no está listo, esa semana no se publica relleno. Serie animada 3D generada escena a escena. Lleva portada de sección, puesta con `herramientas/portada_seccion.py` antes de su intro, y se monta como INTRO + escenas + CIERRE.

**Noticias de X** — hasta 2 al día, en un hueco libre a más de 1 hora de cualquier otra publicación. Salen como "HISTORIAS DE CUATRO PATAS" si son un rescate y como "NOTICIAS QUE CUENTAN" si no.

**Formatos retirados** (no se publican): Cosas de casa, Quién es quién, Las mascotas hablan, Antes y después, la frase de la semana, Frases de vida, Reels del fin de semana y las noticias de tecnología genéricas.

---

## 4. Cómo tienen que ir publicadas

**Formato.** Vertical 1080x1920 siempre. Mínimo 8 segundos; las curiosidades, de 10 a 15. La frase gancho escrita en pantalla desde el primer segundo. Todo reel nuevo se monta a pantalla completa con `herramientas/montar_reel.py`: la foto ocupa toda la pantalla con zoom lento, fundido entre fotos cada 3,5-4,5 segundos, subtítulos grandes abajo frase a frase, y sin recuadro blanco. La tarjeta blanca de `tarjeta.py` se dejó de usar el 16/10 porque no funcionaba en Instagram y Facebook; las que ya estaban programadas se dejaron como estaban.

**Textos.** Pregunta sencilla al final para que la gente comente, 3 a 5 hashtags, sin párrafos largos en Reels y Shorts. Nada de relleno ni de datos inventados.

**Redes.** Instagram (@petsforyou8), Facebook, TikTok, YouTube, Pinterest, X y Threads, todo vía Upload-Post. **Todo lo que se publica en redes va también a YouTube** como Short: en los vídeos ya lo incluye el flujo de programación; los carruseles y fotos llevan además un vídeo vertical "foto con música" de 15-20 segundos que se programa aparte solo en YouTube.

**Música** (en `audio/`), según la historia: héroes `musica-heroe-epica.mp3`, abandono `musica-abandono-triste.mp3`, superación `musica-superacion-inspiradora.mp3`, historias tiernas `musica-historias-emocionante.mp3`, curiosidades `musica-curiosidades-pegadiza.mp3`. Reutilizables: `musica-noticias.mp3` y `musica-curiosidades.mp3`.

**Reglas de marca.** María no aparece en cámara y no se colabora con protectoras. Todo el contenido se produce con IA, fotos de producto y los flujos de Make y GitHub.

---

## 5. Cómo se publica, técnicamente

El vídeo se sube a `videos/` del repositorio público `petsforyou/imagenes` y se programa pasando su URL `raw.githubusercontent.com` a un escenario de Make, que llama a Upload-Post. Upload-Post se queda una copia interna, así que después no expone la URL original, solo el nombre del archivo.

Escenarios de Make que publican (equipo 2485997):

| Escenario | Qué hace |
|---|---|
| 7510594 🎬 Programar vídeo en redes | Vídeo vertical en las 7 redes. Entradas: video, texto, titulo_corto, texto_pinterest, fecha (Madrid), clave |
| 8122808 🧵 Vídeo solo en X y Threads | Para añadir X y Threads a algo ya programado sin duplicar |
| 7741886 ▶️ Vídeo solo en YouTube | El Short de los carruseles y fotos |
| 7503726 Programar foto en redes | Foto en Instagram, Facebook, TikTok y Pinterest |
| 7509757 / 7845744 / 7523163 Carruseles | Carrusel de 5 o 3 fotos |
| 7633245 Historia en Instagram y Facebook | Stories |
| 7611336 / 8116203 / 7541069 / 7540970 | Vídeo solo en Instagram, solo en TikTok, pin solo en Pinterest, foto solo en Instagram |
| 7510162 🗑️ Cancelar publicación programada | Cancela por job_id. **Es irreversible y borra la copia del vídeo** |
| 7241074 Consultar historial | Lo ya publicado. Solo devuelve los 10 más recientes de casi mil, y no acepta parámetros |
| 7611317 Consultar programadas | Todo lo que viene. `scheduled_date` en UTC, `original_scheduled_str` en hora de Madrid |

Para montar material: 7530987 lanza el workflow de carrusel en GitHub, 7584059 el de foto con música, 7613303 el de foto con música por lotes, 7615772 el del avance del capítulo, 7616806 el de montaje de la serie. Para leer y escribir en el repo: 7530826 (consulta a la API de GitHub) y 7584043 (escribir archivo, PUT).

Dos cosas que conviene saber. **La hora de una publicación programada no se puede cambiar**: hay que cancelarla y volver a programarla con el archivo otra vez, y al reprogramar se pierden los textos por plataforma que tuviera guardados. Y **X tiene un tope diario de coste**: cuando se pasa, devuelve `cost_cap_reached` en el precheck y esa red se queda sin publicar mientras el resto sale bien.

---

## 6. Quién prepara cada cosa y cuándo

Desde el 11/10 las publicaciones del calendario las preparan y programan solas estas tareas programadas de Claude. Horas de Madrid.

| Hueco | Tarea | Cuándo corre |
|---|---|---|
| Curiosidad diaria y fotos de las 11:00 | 🔁 Curiosidades | Domingos 10:56, cubre 14 días |
| Historias de cuatro patas | 🦸 Historias de cuatro patas | Lunes y jueves 9:37 |
| Producto útil del miércoles y guía del domingo | 🛍️ Producto de la semana | Lunes 9:47 |
| Capítulo de Ada del viernes | 🎬 Capítulo semanal de Ada y sus amigos | Miércoles 9:00 |
| Avance de Ada del jueves | 🎞️ Avance del capítulo | Jueves 10:07 |
| Noticias de animales de X | 🐾 Noticias de mascotas en X | Diaria, 21:52 |
| Repesca en Instagram de lo publicado sin Instagram | 📷 Repescar en Instagram | Diaria, 21:43 |
| Repaso semanal en Slack | Ritmo de publicación en redes | Viernes 19:00 |

Además, citadas en el `CLAUDE.md` pero fuera de las tareas de Claude (probablemente workflows de GitHub): `pfy-publicaciones-de-manana`, que cada día a las 20:00 manda a María por correo las publicaciones del día siguiente por si quiere cancelar algo, y `pfy-informe-semanal-redes`, informe de los lunes con histórico en `estadisticas/redes-semanal.csv`. Si esa segunda funciona, se solapa con el repaso de los viernes.

**Todo se prepara la víspera.** Por eso es normal que la cola de los próximos días esté vacía: no es un fallo. Lo único que se prepara con antelación es el capítulo de Ada, que se monta el miércoles para el viernes.

---

## 7. De qué materiales se sirve

**Repositorio público `petsforyou/imagenes`**, que es el almacén y la norma a la vez:

- `CLAUDE.md` — las reglas vigentes
- `calendario/` — el calendario del mes
- `videos/` — los mp4 ya montados, que son lo que Upload-Post descarga
- `carruseles/` — las láminas de los carruseles, una carpeta por lista
- `fotos/`, `clips/`, `refs/`, `reels/`, `avances/`, `frases/`, `perfil/` — material por tipo
- `audio/` — las músicas
- `herramientas/` — los guiones de montaje: `montar_reel.py`, `tarjeta.py`, `carrusel_noticias.py`, `portada_seccion.py`, `mascotas_hablan.py`, `perfil_petsforyou.py`, y `colas/`
- `estadisticas/` — Search Console, SEO, el registro de noticias de X (`noticias-x.txt`) y el histórico semanal de redes

**Repositorio privado `petsforyou/montaje-serie`**: `lista/cola-productos.json`, la cola de productos con huecos, reservas, estado y rueda. Los productos solo de Aosom y Timelesstools, que son los dos proveedores probados con pedido real y almacén en la UE.

**Data store 191417 de Make**: las fichas de las escenas de Ada, con su estado (espera, generar-escena, enviado, listo), su prompt de imagen, su texto y sus referencias de personaje.

**Shopify**: precio, stock y enlace de cada producto, comprobados el mismo día. Si el calendario da un precio distinto del de Shopify, manda Shopify.

**ElevenLabs**: imágenes nuevas (`bytedance-seedream-5-pro`, unos 818 créditos por imagen) y las voces fijas de los personajes de Ada. Hay un tope: por debajo de 200.000 créditos no se genera ninguna imagen salvo para Ada, y por debajo de 100.000 tampoco para Ada. Se comprueba antes con el escenario 7918693. Kling se quedó sin créditos.

**vidIQ**: lo usa el repaso de los viernes para medir qué funciona en YouTube y la tarea de historias para comparar titulares. Ojo: YouTube Analytics va con dos o tres días de retraso.

---

## 8. Estado a 23 de octubre y qué hay que decidir

El ritmo se está cumpliendo. Esta semana salieron las curiosidades, las historias, el producto diario, el consejo del miércoles y el capítulo de Ada ("La invitación de Halloween", primera parte del especial de Halloween). La guía en carrusel del domingo está programada para el 25. Lo mejor de la semana: la historia de Clark y el niño de 6 años, con 2.224 visualizaciones, 220 me gusta y 11 comentarios. Lo peor, la serie de Ada, que no pasa de 10 visualizaciones por capítulo.

Cuatro cosas abiertas:

1. **El calendario del repo está desfasado** y contradice al `CLAUDE.md` en la parrilla, en las Historias y en el tope de productos. Hay que reescribirlo o marcarlo como superado.
2. **El `CLAUDE.md` se contradice consigo mismo** en la hora de Historias de cuatro patas (22:00 o 20:30) y del Producto del día (20:30 o 20:00).
3. **Holywin**: seis publicaciones programadas del 26 al 31 y el especial de Ada el día 30, contra la decisión de suspenderlo desde el 26.
4. **Las mascotas hablan**, formato retirado, salió el miércoles 21 y sigue programado el sábado 24 a las 13:00.

Y una pendiente de la primera semana del calendario que solo puede hacer María desde el móvil: cambiar el nombre de usuario de Instagram, poner la biografía nueva en las tres redes, fijar las 3 mejores publicaciones y dar a la app de Meta de Make los permisos `instagram_manage_insights` y `pages_read_engagement`, sin los cuales no se puede medir cuántos seguidores trae cada publicación.

La reevaluación del calendario es el **lunes 9 de noviembre**.
