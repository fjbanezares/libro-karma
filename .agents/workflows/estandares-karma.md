---
description: Estándares de desarrollo para el proyecto Libro del Karma (Versión 2.0 - Discreet)
---

Este flujo de trabajo define cómo mantener la interfaz "discreta y ágil" inspirada en el proyecto `libro-jesus`.

### 1. Interfaz Web (Agile & Discreet)
- **Header**: Barra superior fija con `backdrop-filter: blur`. Contiene el logo a la izquierda y controles a la derecha.
- **Menú de Capítulos**: Dropdown discreto en el header, no sidebar expansivo.
- **Idiomas**: Selector sutil con banderas que activa las clases `.es` y `.en` en el body.
- **Persistencia**: El idioma debe persistir mediante `localStorage` y parámetros de URL (`?lang=en`) al navegar entre capítulos.

### 2. Estructura de Contenido
- **Hero Section**: Imagen a pantalla completa con paralaje suave y título centrado (`Cinzel` para títulos, `EB Garamond` para cuerpo).
- **Story Container**: Máximo 700px de ancho para lectura cómoda.
- **Secciones clave**: 
  - `story-block`: Narrativa detallada.
  - `connection-info`: Explicación técnica/espiritual del mural del templo (la "Causa" y el "Efecto").
  - `moral`: Frase final impactante.

### 3. Desarrollo de Nuevos Capítulos
1. Crear carpeta `XX_nombre/`.
2. Generar imagen `juxtaposition.png` en `web/assets/`.
3. Crear `index.html` siguiendo el template "Discreet" (ver `00_introduccion/web/index.html`).
4. Actualizar el menú de navegación en `shared/script.js` si es necesario (o asegurar que el dropdown links son correctos).

### 4. LaTeX (Publicación)
- Mantener los archivos `.tex` en castellano para KDP.
- Incluir siempre la imagen y la interpretación del templo.
