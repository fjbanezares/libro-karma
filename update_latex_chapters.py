import os
import re
from bs4 import BeautifulSoup

def clean_text(text):
    if not text: return ""
    text = text.replace('\n', ' ').strip()
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('&', '\\&').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#')
    text = text.replace('Nhân Quả', 'Nhan Qua')
    text = text.replace('ả', 'a').replace('â', 'a').replace('ư', 'u').replace('ơ', 'o').replace('ế', 'e').replace('ố', 'o').replace('ề', 'e').replace('ĩ', 'i').replace('ệ', 'e').replace('ộ', 'o').replace('ầ', 'a')
    text = re.sub(r'<strong>(.*?)</strong>', r'\\textbf{\1}', text)
    text = text.replace('«', '``').replace('»', "''")
    return text

def extract_images(soup):
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('assets/'):
            images.append(src.replace('assets/', ''))
    return images

def generate_latex_00(chap_dir, soup):
    # Custom parser for chapter 00 since it lacks standard .moral and .parable blocks
    title_span = soup.select_one('.chapter-title span.es')
    subtitle_span = soup.select_one('.subtitle span.es')
    title = clean_text(title_span.text) if title_span else "Introducción"
    subtitle = clean_text(subtitle_span.text) if subtitle_span else ""

    latex_content = f"\\chapter[{title}]{{{title}\\\\ \\large {subtitle}}}\n\n"
    
    # Hero image for chap 00 is intro.png
    if os.path.exists(f"{chap_dir}/web/assets/intro.png"):
        latex_content += f"\\elegantimage{{{chap_dir}/web/assets/intro.png}}\n\n"
        
    paragraphs = soup.select('.story-block p.es')
    if len(paragraphs) > 0:
        p1 = clean_text(paragraphs[0].text)
        first_letter = p1[0]
        rest_of_text = p1[1:]
        latex_content += f"\\lettrine[lines=3, nindent=0.5em, findent=0.2em]{{{first_letter}}}{{}}{rest_of_text}\n\n"
    
    if len(paragraphs) > 1:
        latex_content += f"{clean_text(paragraphs[1].text)}\n\n"

    latex_content += "\\section{El Hilo Conductor de las Tradiciones}\n"
    if len(paragraphs) > 2:
        latex_content += f"{clean_text(paragraphs[2].text)}\n\n"
        
    quotes = soup.select('blockquote.es')
    if len(quotes) > 0:
        latex_content += f"\\textit{{{clean_text(quotes[0].text)}}}\n\n"
        
    if os.path.exists(f"{chap_dir}/web/assets/seed_harvest.png"):
        latex_content += f"\\elegantimage{{{chap_dir}/web/assets/seed_harvest.png}}\n\n"
        
    if len(quotes) > 1:
        latex_content += f"\\textit{{{clean_text(quotes[1].text)}}}\n\n"
        
    if len(paragraphs) > 3:
        latex_content += f"{clean_text(paragraphs[3].text)}\n\n"
        
    latex_content += "\\section{La Tercera Ley de Newton del Alma}\n"
    if len(paragraphs) > 4:
        latex_content += f"{clean_text(paragraphs[4].text)}\n\n"
        
    conn_paragraphs = soup.select('.connection-info p.es')
    if len(conn_paragraphs) > 0:
        latex_content += f"{clean_text(conn_paragraphs[0].text)}\n\n"
        
    latex_content += "\\begin{center}\n$\\vec{F}_{A} = -\\vec{F}_{B}$\n\\end{center}\n\n"
    
    if len(conn_paragraphs) > 1:
        latex_content += f"{clean_text(conn_paragraphs[1].text)}\n\n"
        
    if os.path.exists(f"{chap_dir}/web/assets/newton_soul.png"):
        latex_content += f"\\elegantimage{{{chap_dir}/web/assets/newton_soul.png}}\n\n"
        
    latex_content += "\\section{El Entrelazamiento y la Memoria}\n"
    if len(paragraphs) > 5:
        latex_content += f"{clean_text(paragraphs[5].text)}\n\n"
        
    if len(conn_paragraphs) > 2:
        latex_content += f"{clean_text(conn_paragraphs[2].text)}\n\n"
        
    if os.path.exists(f"{chap_dir}/web/assets/quantum_entanglement.png"):
        latex_content += f"\\elegantimage{{{chap_dir}/web/assets/quantum_entanglement.png}}\n\n"
        
    latex_content += "\\section{El Propósito de este Libro}\n"
    if len(paragraphs) > 6:
        latex_content += f"{clean_text(paragraphs[6].text)}\n\n"
    if len(paragraphs) > 7:
        latex_content += f"{clean_text(paragraphs[7].text)}\n\n"
        
    moral_tag = soup.select_one('.moral span.es')
    if not moral_tag:
        moral_tag = soup.select_one('.moral')
    if moral_tag:
        latex_content += f"\\vspace{{1em}}\n\\begin{{center}}\n    \\textbf{{\\Large {clean_text(moral_tag.text)}}}\n\\end{{center}}\n\\vspace{{1em}}\n\n"
        
    return latex_content

def generate_latex_for_chapter(chap_dir):
    html_path = os.path.join(chap_dir, 'web', 'index.html')
    if not os.path.exists(html_path):
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    if chap_dir.startswith("00_"):
        latex_content = generate_latex_00(chap_dir, soup)
    else:
        # Standard Chapter parsing
        title_span = soup.select_one('.chapter-title span.es')
        subtitle_span = soup.select_one('.subtitle span.es')
        
        title = clean_text(title_span.text) if title_span else "Capítulo"
        subtitle = clean_text(subtitle_span.text) if subtitle_span else ""

        # Intro text (Story block that is NOT a parable)
        intro_paragraphs = []
        intro_block = soup.select_one('.story-block:not(.parable-block)')
        if intro_block:
            for p in intro_block.select('p.es'):
                intro_paragraphs.append(clean_text(p.text))
        
        # Parable
        parable_title = ""
        parable_paragraphs = []
        parable_block = soup.select_one('.parable-block') or soup.select_one('.story-block h3.es').parent if soup.select_one('.story-block h3.es') else None
        if parable_block:
            p_title_tag = parable_block.select_one('h3.es')
            if p_title_tag:
                parable_title = clean_text(p_title_tag.text)
            for p in parable_block.select('p.es'):
                parable_paragraphs.append(clean_text(p.text))

        # Temple Interpretation / Connection Info
        interp_text = ""
        conn_info = soup.select_one('.connection-info')
        if conn_info:
            interp_p = conn_info.select_one('p.es')
            if interp_p:
                interp_text = clean_text(interp_p.text)

        moral_tag = soup.select_one('.moral span.es') or soup.select_one('.moral')
        moral = clean_text(moral_tag.text) if moral_tag else ""

        trans_box = soup.select_one('.translation-box')
        analysis_text = ""
        if trans_box:
            for p in trans_box.select('p.es'):
                if 'Análisis:' in p.text or '<strong>Análisis:</strong>' in str(p):
                    strong_tag = p.find('strong')
                    if strong_tag and 'Análisis' in strong_tag.text:
                        strong_tag.extract()
                    analysis_text = clean_text(p.text)
                    break

        latex_content = f"\\chapter[{title}]{{{title}\\\\ \\large {subtitle}}}\n\n"
        
        images = extract_images(soup)
        seen_images = set()

        # Hero image (Top)
        hero_candidates = ['juxtaposition', 'hero', 'intro', 'art']
        extensions = ['.png', '.jpg', '.jpeg']
        found_hero = False
        for cand in hero_candidates:
            for ext in extensions:
                filename = cand + ext
                if filename in images and filename not in seen_images:
                    latex_content += f"\\elegantimage{{{chap_dir}/web/assets/{filename}}}\n\n"
                    seen_images.add(filename)
                    found_hero = True
                    break
            if found_hero: break

        # Intro text (Part 1 with Lettrine, others follow)
        if intro_paragraphs:
            p1 = intro_paragraphs[0]
            first_letter = p1[0]
            rest_of_text = p1[1:]
            latex_content += f"\\lettrine[lines=3, nindent=0.5em, findent=0.2em]{{{first_letter}}}{{}}{rest_of_text}\n\n"
            for p in intro_paragraphs[1:]:
                latex_content += f"{p}\n\n"

        # Temple interpretation
        if interp_text:
            latex_content += f"\\section{{Interpretación del Templo}}\n{interp_text}\n\n"

        # Parable
        if parable_title and parable_paragraphs:
            latex_content += f"\\section{{{parable_title}}}\n"
            latex_content += "\\begin{elegantquote}\n"
            for p in parable_paragraphs:
                latex_content += f"\\textit{{{p}}}\n\n"
            latex_content += "\\end{elegantquote}\n\n"
            
            # Middle image (After Parable)
            mid_candidates = ['art', 'hero_v1', 'hero_v2', 'juxtaposition']
            found_mid = False
            for cand in mid_candidates:
                for ext in extensions:
                    filename = cand + ext
                    if filename in images and filename not in seen_images:
                        latex_content += f"\\elegantimage{{{chap_dir}/web/assets/{filename}}}\n\n"
                        seen_images.add(filename)
                        found_mid = True
                        break
                if found_mid: break

        # Moral
        if moral:
            latex_content += f"\\vspace{{1em}}\n\\begin{{center}}\n    \\textbf{{\\Large {moral}}}\n\\end{{center}}\n\\vspace{{1em}}\n\n"
        
        # Art image (Bottom)
        art_candidates = ['art', 'hero_v1', 'hero_v2']
        found_art = False
        for cand in art_candidates:
            for ext in extensions:
                filename = cand + ext
                if filename in images and filename not in seen_images:
                    latex_content += f"\\elegantimage{{{chap_dir}/web/assets/{filename}}}\n\n"
                    seen_images.add(filename)
                    found_art = True
                    break
            if found_art: break
        
        # Translation image and Analysis (Wrapped)
        pasaje_img = None
        for ext in ['.jpg', '.png', '.jpeg']:
            filename = 'pasaje_original' + ext
            if filename in images and filename not in seen_images:
                pasaje_img = filename
                break

        if pasaje_img and analysis_text:
            latex_content += f"\\section{{Análisis Kármico y Traducción}}\n"
            latex_content += f"\\begin{{wrapfigure}}{{r}}{{0.5\\textwidth}}\n"
            latex_content += f"  \\vspace{{-1.5em}}\n"
            latex_content += f"  \\begin{{center}}\n"
            latex_content += f"  \\inlineelegantimage[0.45\\textwidth]{{{chap_dir}/web/assets/{pasaje_img}}}\n"
            latex_content += f"  \\end{{center}}\n"
            latex_content += f"  \\vspace{{-1.5em}}\n"
            latex_content += f"\\end{{wrapfigure}}\n"
            latex_content += f"{analysis_text}\n\n"
            seen_images.add(pasaje_img)
        elif analysis_text:
            latex_content += f"\\section{{Análisis Kármico}}\n{analysis_text}\n\n"

    # Write to file
    out_dir = os.path.join(chap_dir, 'latex')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"capitulo_{chap_dir.split('_')[0]}.tex")
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    print(f"Updated {out_file}")

# Process chapters 00 to 22
for i in range(0, 23):
    prefix = f"{i:02d}_"
    for d in os.listdir('.'):
        if d.startswith(prefix) and os.path.isdir(d):
            generate_latex_for_chapter(d)
