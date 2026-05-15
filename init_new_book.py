import os
import shutil
import sys

def create_new_book(book_name, num_chapters):
    root_dir = os.path.abspath(f"../{book_name.lower().replace(' ', '_')}")
    if os.path.exists(root_dir):
        print(f"Error: Directory {root_dir} already exists.")
        return
    
    os.makedirs(root_dir)
    print(f"Created root directory: {root_dir}")

    # 1. Copy ALL workflows and skills
    if os.path.exists(".agents"):
        shutil.copytree(".agents", f"{root_dir}/.agents")
        print("Copied all workflows and skills to new book.")

    # 2. Copy shared web assets (style and script)
    if os.path.exists("shared"):
        shutil.copytree("shared", f"{root_dir}/shared")
        print("Copied shared web assets (CSS/JS) to new book.")
    else:
        # Create minimal shared if it doesn't exist
        os.makedirs(f"{root_dir}/shared", exist_ok=True)
        with open(f"{root_dir}/shared/style.css", "w") as f:
            f.write("/* Main Styles */\nbody { font-family: 'Inter', sans-serif; }\n")
        with open(f"{root_dir}/shared/script.js", "w") as f:
            f.write("// Multi-language logic\nfunction setLanguage(lang) { document.body.className = 'lang-' + lang; }\n")

    # 3. Create Root Index (Library)
    root_index_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{book_name} - Biblioteca</title>
    <link rel="stylesheet" href="shared/style.css">
</head>
<body class="lang-es">
    <h1>{book_name}</h1>
    <div class="library-grid">
"""
    for i in range(num_chapters + 1):
        chap_name = f"{i:02d}_capitulo_{i}"
        root_index_content += f'        <a href="{chap_name}/web/index.html">Capítulo {i}</a><br>\n'
    
    root_index_content += """    </div>
    <script src="shared/script.js"></script>
</body>
</html>"""
    
    with open(f"{root_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(root_index_content)
    print("Created main index.html (Library).")

    # 4. Create libro_maestro.tex template (with elegantimage)
    maestro_content = r"""\documentclass[12pt,paper=6in:9in,pagesize=pdftex,oneside,openany]{book}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-tabla]{babel}
\usepackage{ebgaramond}
\usepackage[tracking=true]{microtype}
\usepackage{lettrine}
\usepackage{geometry}
\geometry{paperwidth=6in, paperheight=9in, top=0.8in, bottom=1in, inner=0.85in, outer=0.65in, footskip=0.5in}
\usepackage{titlesec}
\usepackage{xcolor}
\definecolor{gold}{HTML}{C5A059}

\newcommand{\chapterornament}{%
  \vspace{1em}
  \begin{tikzpicture}
    \draw[gold, line width=1pt] (0,0) -- (3,0);
    \fill[gold] (3.2,0) +(0,0.1) -- +(0.1,0) -- +(0,-0.1) -- +(-0.1,0) -- cycle;
    \draw[gold, line width=1pt] (3.4,0) -- (6.4,0);
  \end{tikzpicture}
  \vspace{1em}
}

\titleformat{\chapter}[display]{\centering\normalfont\color{gold}}{\Large\MakeUppercase{\chaptertitlename} \thechapter}{10pt}{\Huge\scshape\lsstyle}[\vspace{0.5ex}\chapterornament]
\titlespacing*{\chapter}{0pt}{-20pt}{40pt}
\titleformat{\section}{\normalfont\Large\scshape\color{gold}}{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\thepage}
\usepackage{graphicx}
\usepackage{caption}
\captionsetup{font=it, labelformat=empty}
\usepackage{setspace}
\setstretch{1.15}
\usepackage{wrapfig}
\usepackage{mdframed}

\newmdenv[
  topline=false, bottomline=false, rightline=false,
  linewidth=2pt, linecolor=gold, backgroundcolor=white,
  leftmargin=10pt, innerleftmargin=10pt, innerrightmargin=0pt,
  skipabove=15pt, skipbelow=15pt
]{elegantquote}

% Imágenes Elegantes (Bordes redondeados y marco dorado)
\usepackage{tikz}
\newsavebox{\picbox}
\newcommand{\elegantimage}[2][0.85\textwidth]{%
  \begin{figure}[ht]
    \centering
    \sbox{\picbox}{\includegraphics[width=#1]{#2}}%
    \begin{tikzpicture}
      \useasboundingbox (0,0) rectangle (\wd\picbox,\ht\picbox);
      \begin{scope}
        \clip[rounded corners=3mm] (0,0) rectangle (\wd\picbox,\ht\picbox);
        \node[anchor=south west, inner sep=0pt] at (0,0) {\usebox{\picbox}};
      \end{scope}
      \draw[rounded corners=3mm, draw=gold, line width=2pt] (0,0) rectangle (\wd\picbox,\ht\picbox);
    \end{tikzpicture}
  \end{figure}
}
\newcommand{\inlineelegantimage}[2][\linewidth]{%
  \sbox{\picbox}{\includegraphics[width=#1]{#2}}%
  \begin{tikzpicture}
    \useasboundingbox (0,0) rectangle (\wd\picbox,\ht\picbox);
    \begin{scope}
      \clip[rounded corners=3mm] (0,0) rectangle (\wd\picbox,\ht\picbox);
      \node[anchor=south west, inner sep=0pt] at (0,0) {\usebox{\picbox}};
    \end{scope}
    \draw[rounded corners=3mm, draw=gold, line width=2pt] (0,0) rectangle (\wd\picbox,\ht\picbox);
  \end{tikzpicture}%
}

\widowpenalty10000
\clubpenalty10000

\title{\Huge\scshape """ + book_name + r"""}
\author{\Large Tu Nombre}
\date{\today}

\begin{document}
\frontmatter
\begin{titlepage}
    \centering
    \vspace*{2cm}
    {\Huge\scshape\color{gold} """ + book_name + r""" \par}
    \vspace{4cm}
    {\Large Tu Nombre \par}
\end{titlepage}

\clearpage
\tableofcontents
\mainmatter

"""
    
    # 5. Generate Chapters (HTML and LaTeX)
    for i in range(num_chapters + 1):
        chap_name = f"{i:02d}_capitulo_{i}"
        chap_dir = os.path.join(root_dir, chap_name)
        latex_dir = os.path.join(chap_dir, 'latex')
        web_dir = os.path.join(chap_dir, 'web')
        web_assets_dir = os.path.join(web_dir, 'assets')
        
        os.makedirs(latex_dir, exist_ok=True)
        os.makedirs(web_assets_dir, exist_ok=True)
        
        # HTML Template for Chapter
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Capítulo {i}: {book_name}</title>
    <link rel="stylesheet" href="../../shared/style.css">
</head>
<body class="lang-es">
    <div class="lang-selector-elegant">
        <button onclick="setLanguage('es')">ES</button>
        <button onclick="setLanguage('en')">EN</button>
    </div>
    <main class="main-content">
        <h1 class="chapter-title"><span class="es">Capítulo {i}</span><span class="en">Chapter {i}</span></h1>
        <div class="story-block fade-in">
            <p class="es">Contenido en español...</p>
            <p class="en">Content in English...</p>
        </div>
    </main>
    <script src="../../shared/script.js"></script>
</body>
</html>"""
        with open(os.path.join(web_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # LaTeX Template for Chapter
        tex_file = os.path.join(latex_dir, f"capitulo_{i:02d}.tex")
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(f"\\chapter{{Título del Capítulo {i}}}\n\n")
            f.write(f"\\lettrine[lines=3, nindent=0.5em, findent=0.2em]{{E}}{{}}ste es el inicio del capítulo {i}.\n")
        
        maestro_content += f"\\input{{{chap_name}/latex/capitulo_{i:02d}.tex}}\n"

    maestro_content += "\n\\end{document}\n"

    with open(os.path.join(root_dir, 'libro_maestro.tex'), 'w', encoding='utf-8') as f:
        f.write(maestro_content)
    
    # 6. Copy the LaTeX updater script
    if os.path.exists("update_latex_chapters.py"):
        shutil.copy("update_latex_chapters.py", f"{root_dir}/update_latex_chapters.py")

    print(f"✅ Libro '{book_name}' generado exitosamente con {num_chapters} capítulos.")
    print(f"Arquitectura Web-First completada en: {root_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 init_new_book.py \"Nombre del Libro\" num_capitulos")
        sys.exit(1)
    
    name = sys.argv[1]
    chapters = int(sys.argv[2])
    create_new_book(name, chapters)
