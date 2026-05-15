# Skill / Workflow: Generación de Libro PDF para KDP con Arquitectura "Web-First"

Este documento detalla el procedimiento estándar y los algoritmos para generar un libro PDF premium y elegantemente maquetado para su venta en Amazon KDP (tamaño 6x9 pulgadas), utilizando como única "fuente de verdad" una arquitectura HTML multi-idioma.

## 1. Arquitectura "Web-First" Automatizada

No debes empezar los libros desde cero ni construir el LaTeX manualmente. Utiliza siempre el script generador de ecosistemas.

### Script: `init_new_book.py`
Este script funciona como un *scaffolding*. Al ejecutarlo, genera toda la infraestructura necesaria para un nuevo libro:
1.  **Hereda las habilidades:** Copia de forma recursiva toda la carpeta `.agents/` para conservar los *workflows* y directrices.
2.  **Hereda los estilos web:** Copia la carpeta `shared/` con el diseño en CSS y el selector de idiomas en JS.
3.  **Genera la Biblioteca Global:** Crea un `index.html` maestro en la raíz.
4.  **Genera el esqueleto de capítulos:** Para el número de capítulos que especifiques, crea el directorio base, la carpeta `web/` con su HTML multi-idioma bilingüe preconfigurado, y la carpeta `latex/`.
5.  **Genera el `libro_maestro.tex`:** Inyecta automáticamente todas las macros de estilo (bordes, capitulares, ornamentos) y preconfigura todos los `\input{}`.

## 2. El Compilador: `update_latex_chapters.py`

La escritura del libro se realiza exclusivamente en HTML (`web/index.html` de cada capítulo). El script `update_latex_chapters.py` es el compilador que transforma el ecosistema web al formato LaTeX.

**Características del Compilador:**
-   **Escaneo Inteligente de Imágenes:** Lee de forma dinámica todas las etiquetas `<img>` del HTML y las posiciona cronológicamente en el LaTeX sin duplicados, manejando tanto el "Hero Image" como las imágenes secundarias.
-   **Limpieza de Caracteres Especiales:** Translitera caracteres especiales (como los tonos del alfabeto vietnamita) a equivalentes latinos que `pdflatex` pueda compilar sin problemas.
-   **Mapeo de Estructuras:** Extrae automáticamente las secciones (`.story-block`, `.moral`, `blockquote`) y las asigna a sus correspondientes entornos premium en LaTeX.

## 3. Elementos de Diseño Premium (LaTeX)

El archivo `libro_maestro.tex` incluye un arsenal de diseño editorial de alta calidad para impresionar en KDP:

1.  **Tipografía:** `EB Garamond` clásica. Tamaño de papel 6x9 (superventas KDP) con márgenes asimétricos (lomo más grueso).
2.  **Imágenes Elegantes (`\elegantimage`):** Las fotos ya no se pegan sin más. Este macro usa `TikZ` para **redondear las esquinas (3mm)** de la imagen y dibujar un **grueso marco dorado**, convirtiéndolas en verdaderas láminas encuadernadas.
3.  **Alineación Flotante (`wrapfig` y `\inlineelegantimage`):** Para imágenes que no deben ocupar una página entera (como las tiras horizontales de traducciones o pasajes originales), se utiliza un macro inline envuelto en `wrapfigure`, permitiendo que el análisis escrito fluya elegantemente a un lado de la imagen.
4.  **Letras Capitulares (`\lettrine`):** El inicio de cada capítulo se embellece con una gran letra capitular de 3 líneas de altura. *(Nota: Únicamente la primera letra es capital, el resto de la palabra fluye en formato de texto normal).*
5.  **Citas Elegantes (`elegantquote`):** Las parábolas y fragmentos citados se envuelven en un entorno `mdframed` especial. Carece de recuadros completos pero presenta una gruesa línea dorada en el margen izquierdo, aportando distinción sin asfixiar la lectura.
6.  **Ornamentos de Capítulo:** Debajo de cada título principal se dibuja un sutil separador geométrico dorado (líneas con un rombo central) utilizando `TikZ`, sumando a la estética clásica.

## 4. Flujo de Trabajo (Resumen)

Para crear y mantener un libro bajo este ecosistema:
1.  **Crear el repositorio:** En una nueva carpeta, usa un script (basado en `init_new_book.py`) para montar la base.
2.  **Escribir:** Añade el contenido bilingüe (HTML) en los `web/index.html` correspondientes a cada capítulo. Asegúrate de añadir las imágenes a `web/assets/`.
3.  **Sincronizar:** Ejecuta `python3 update_latex_chapters.py`.
4.  **Compilar:** Ejecuta `pdflatex libro_maestro.tex` (dos veces para actualizar el índice).
5.  **Revisar:** Abre `libro_maestro.pdf` para admirar un libro completamente estandarizado y hermoso.
