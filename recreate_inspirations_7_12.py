import os
import re
from deep_translator import GoogleTranslator

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

common_titles = {
    "es": "La Inspiración Original", "en": "The Original Inspiration", "it": "L'Ispirazione Originale", 
    "zh": "最初的灵感", "ar": "الإلهام الأصلي", "ru": "Оригинальное вдохновение", 
    "de": "Die Ursprüngliche Inspiration", "fr": "L'Inspiration Originale", 
    "ja": "元のインスピレーション", "pt": "A Inspiração Original"
}

common_descs = {
    "es": "La historia que hemos generado para este capítulo está inspirada por este pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la fotografía original.",
    "en": "The story we generated for this chapter is inspired by this passage from the original scene of the \"Tranh Nhân Quả\" (Karma Illustrations) murals at the Linh Ung Temple in Da Nang, captured in the original photograph.",
    "it": "La storia che abbiamo generato per questo capitolo è ispirata a questo passaggio della scena originale dei murales «Tranh Nhân Quả» del Tempio Linh Ung a Da Nang, catturato nella fotografia originale.",
    "zh": "我们为本章生成的故事灵感来自于岘港灵应寺“Tranh Nhân Quả”（因果图）壁画原始场景的这一段，在原始照片中被捕捉下来。",
    "ar": "القصة التي أنشأناها لهذا الفصل مستوحاة من هذا المقطع من المشهد الأصلي لجداريات \"Tranh Nhân Quả\" في معبد Linh Ung في دا نانغ، والتي تم التقاطها في الصورة الأصلية.",
    "ru": "История, которую мы создали для этой главы, вдохновлена этим фрагментом оригинальной сцены фресок «Tranh Nhân Quả» в храме Линь Унг в Дананге, запечатленном на оригинальной фотографии.",
    "de": "Die Geschichte, die wir für dieses Kapitel generiert haben, ist von dieser Passage der ursprünglichen Szene der Wandmalereien „Tranh Nhân Quả“ im Linh Ung-Tempel in Da Nang inspiriert, die auf dem Originalfoto festgehalten wurde.",
    "fr": "L'histoire que nous avons générée pour ce chapitre est inspirée de ce passage de la scène originale des fresques « Tranh Nhân Quả » du temple Linh Ung à Da Nang, capturée sur la photographie originale.",
    "ja": "私たちがこの章のために作成した物語は、ダナンのリンウン寺にある「Tranh Nhân Quả」（カルマのイラスト）壁画の元のシーンのこの一節からインスピレーションを得ており、元の写真に収められています。",
    "pt": "A história que geramos para este capítulo foi inspirada nesta passagem da cena original dos murais «Tranh Nhân Quả» no Templo Linh Ung em Da Nang, capturada na fotografia original."
}

intro_texts = {
    "es": "Como se puede apreciar en el pasaje extraído del mural, la causa y su efecto kármico están descritos originalmente en vietnamita y con una breve traducción al inglés. A continuación, te ofrecemos su traducción detallada en los distintos idiomas:",
    "en": "As can be seen in the passage extracted from the mural, the cause and its karmic effect are originally described in Vietnamese with a brief English translation. Below, we offer the detailed translation in different languages:",
    "it": "Come si può vedere nel passaggio estratto dal murale, la causa e il suo effetto karmico sono originariamente descritti in vietnamita con una breve traduzione in inglese. Di seguito offriamo la traduzione dettagliata in diverse lingue:",
    "zh": "正如壁画所见，原因及其业报原本用越南语描述并配有简短英文翻译。以下是各种语言的详细翻译：",
    "ar": "كما يمكن رؤيته في المقطع المقتبس من اللوحة الجدارية، فإن السبب وتأثيره الكارمي موصوفان في الأصل باللغة الفيتنامية مع ترجمة إنجليزية موجزة. نقدم أدناه الترجمة التفصيلية بلغات مختلفة:",
    "ru": "Как видно из отрывка, взятого из фрески, причина и кармический эффект изначально описаны на вьетнамском языке с кратким английским переводом. Ниже мы предлагаем подробный перевод на разные языки:",
    "de": "Wie in der aus dem Wandgemälde entnommenen Passage zu sehen ist, werden die Ursache und ihre karmische Wirkung ursprünglich auf Vietnamesisch mit einer kurzen englischen Übersetzung beschrieben. Nachfolgend bieten wir die detaillierte Übersetzung in verschiedenen Sprachen an:",
    "fr": "Comme on peut le voir dans le passage extrait de la fresque, la cause et son effet karmique sont décrits à l'origine en vietnamien avec une brève traduction en anglais. Ci-dessous, nous proposons la traduction détaillée dans différentes langues :",
    "ja": "壁画から抽出された一節に見られるように、原因とそのカルマ的影響は元々ベトナム語で説明されており、短い英訳が添えられています。以下に、さまざまな言語での詳細な翻訳を示します。",
    "pt": "Como pode ser visto na passagem extraída do mural, a causa e seu efeito cármico são originalmente descritos em vietnamita com uma breve tradução para o inglês. Abaixo, oferecemos a tradução detalhada em diferentes idiomas:"
}

mural_trans = {
    "07_manos_del_mal": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Usar las manos para actos malvados.<br>Efecto: Renace como una especie sin manos.",
                         "en": "<strong>Recreated Translation:</strong><br>Cause: Using hands to do evil things.<br>Effect: Brings rebirth as species without hands."},
    "08_pedestal_soberbia": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Ser arrogante e irrespetuoso con los demás.<br>Efecto: Trae bajo estatus social.",
                             "en": "<strong>Recreated Translation:</strong><br>Cause: Being arrogant and disrespectful towards others.<br>Effect: Brings low social status."},
    "09_frio_egoismo": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Ser tacaño y no ayudar en la vida anterior.<br>Efecto: Renace como un pobre abandonado.",
                        "en": "<strong>Recreated Translation:</strong><br>Cause: Being stingy and unhelpful in the previous life.<br>Effect: Brings rebirth as a poor and neglected."},
    "10_infierno_sombras": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Ser un ladrón y asesino en la vida anterior.<br>Efecto: Trae renacimiento en el infierno y sufrimiento por fuego y cuchillos.",
                            "en": "<strong>Recreated Translation:</strong><br>Cause: Being a thief and murderer in the previous life.<br>Effect: Brings rebirth into hell and suffering from fire and knives."},
    "11_mirada_desprecio": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Mirar a los demás con desprecio.<br>Efecto: Trae enfermedades graves y soledad.",
                            "en": "<strong>Recreated Translation:</strong><br>Cause: Looking down on others.<br>Effect: Brings severe disease and loneliness."},
    "12_peso_injusticia": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Tratar mal a los empleados.<br>Efecto: Conduce a un rápido final de las bendiciones y a la pobreza.",
                           "en": "<strong>Recreated Translation:</strong><br>Cause: Treating employees poorly.<br>Effect: Brings a quick end to blessing and poverty."}
}

an_es = {
    "07_manos_del_mal": "El uso de la fuerza para la maldad y la violencia atrae inexorablemente la pérdida de los medios para actuar. El Karma arrebata para que el alma aprenda desde la impotencia el valor sagrado de la protección y la caricia.",
    "08_pedestal_soberbia": "Despreciar al prójimo desde la arrogancia genera una deuda cósmica que se cobra sometiendo al espíritu a posiciones sociales de inmensa precariedad, para recordar que todos somos iguales en la esencia.",
    "09_frio_egoismo": "El egoísmo y la tacañería aíslan al alma en una celda de frío espiritual, obligándola a renacer en condiciones de abandono absoluto para que finalmente aflore la sed de dar.",
    "10_infierno_sombras": "Quien siembra dolor extremo, robo y asesinato, atrae hacia sí mismo un sufrimiento ardiente y cortante, un verdadero infierno personal diseñado para disolver su insensibilidad de piedra.",
    "11_mirada_desprecio": "La mirada de desprecio y la burla hacia el infortunio ajeno corrompen nuestro ser interior, manifestándose tarde o temprano en enfermedades severas y repulsión social prolongada.",
    "12_peso_injusticia": "Tratar con injusticia y maldad a quienes nos sirven consume velozmente nuestras bendiciones materiales, hundiendo el destino en la ruina para enseñarnos el respeto sagrado hacia el trabajador."
}

chapters = ["07_manos_del_mal", "08_pedestal_soberbia", "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"]

def get_trans(text_es, lang_code, g_code):
    try:
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

# Translate mural trans
for chap_k, d in mural_trans.items():
    es_t = d["es"]
    for code, g_code in lang_map.items():
        if code not in d:
             d[code] = get_trans(es_t, code, g_code)

def translate_analysis(es_text):
    results = {"es": es_text, "en": get_trans(es_text, "en", "en")}
    for code, g_code in lang_map.items():
        results[code] = get_trans(es_text, code, g_code)
    return results

for chap in chapters:
    filepath = f"{chap}/web/index.html"
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove the final-art block BEFORE moral
    # We look for <div class="final-art fade-in" ...> ... </div> just preceding <div class="moral...
    pattern_redundant = re.compile(r'<div class="final-art fade-in"[^>]*>\s*<img src="assets/hero\.png"[^>]*>\s*</div>\s*(?=<div class="moral fade-in">)', re.IGNORECASE)
    content = pattern_redundant.sub('', content)

    # If it is not placed before moral, let's just make sure it's gone if it's there
    # But wait, there might be another final-art. We ONLY want to remove it IF it shows hero.png 
    # and is before moral. The regex above takes care of it because it checks img src is hero.png.

    # 2. Insert the original-inspiration block
    # Check if we already have it to avoid dups
    if '<div class="original-inspiration fade-in"' not in content:
        all_titles = "".join([f'<h3 class="{k}" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: \'Cinzel\', serif;">{v}</h3>\n' for k,v in common_titles.items()])
        all_descs = "".join([f'<p class="{k}" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">{v}</p>\n' for k,v in common_descs.items()])
        intros = "".join([f'<p class="{k}" style="color: #bbb; margin-bottom: 1.5rem; font-style: italic;">{v}</p>\n' for k,v in intro_texts.items()])
        m_trans = "".join([f'<p class="{k}" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197, 160, 89, 0.1); padding: 1rem; border-left: 3px solid var(--gold);">{v}</p>\n' for k,v in mural_trans[chap].items()])
        
        # Vietnamese Translation
        vt_text = GoogleTranslator(source='es', target='vi').translate(mural_trans[chap]["es"].replace('<strong>Traducción Recreada:</strong><br>', '').replace('<br>', ' | '))
        vietnamese_html = f'<p style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: \'EB Garamond\', serif; font-size: 1.2rem;"><strong>🇻🇳 Tiếng Việt:</strong><br>{vt_text}</p>'
        
        # Analysis
        an_all = translate_analysis(f"<strong>Análisis:</strong> {an_es[chap]}")
        an_html = "".join([f'<p class="{k}" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;">{v}</p>\n' for k,v in an_all.items()])

        replacement = f"""
            <div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197, 160, 89, 0.3);">
                {all_titles}
                {all_descs}
                <center>
                    <img src="assets/pasaje_original.jpg" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>
                <div class="translation-box" style="background: rgba(0, 0, 0, 0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">
                    {intros}
                    {vietnamese_html}
                    {m_trans}
                    <hr style="border-color: rgba(197, 160, 89, 0.2); margin-block: 2rem;">
                    {an_html}
                </div>
            </div>
    """
        # Insert before linktree
        content = re.sub(r'(<div class="linktree-subtle fade-in")', replacement + r'\1', content)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {chap} successfully.")
