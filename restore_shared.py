import re

# Update shared/style.css
with open("shared/style.css", "r") as f:
    css = f.read()

# Replace Visibility Control block
old_vis = """/* Visibility Control */
body.lang-es .en {
    display: none !important;
}

body.lang-en .es {
    display: none !important;
}"""

new_vis = """/* Toggle switch languages */
body:not(.lang-es) .es,
body:not(.lang-en) .en,
body:not(.lang-it) .it,
body:not(.lang-zh) .zh,
body:not(.lang-ar) .ar,
body:not(.lang-ru) .ru,
body:not(.lang-de) .de,
body:not(.lang-fr) .fr,
body:not(.lang-ja) .ja,
body:not(.lang-pt) .pt {
    display: none !important;
}

body.lang-ar {
    direction: rtl;
}"""

# Wait, check if old_vis is there exactly
if "body.lang-es .en" in css:
    css = css.replace(old_vis, new_vis)
    with open("shared/style.css", "w") as f:
        f.write(css)
    print("Updated style.css")

# Update shared/script.js
with open("shared/script.js", "r") as f:
    js = f.read()

# Replace setLanguage class logic
js = re.sub(r"document\.body\.className\.replace\([^)]+\)", "document.body.className.replace(/lang-(es|en|it|zh|ar|ru|de|fr|ja|pt)/g, '')", js)

# Replace langInfo dictionary
old_lang_info = """const langInfo = {
        'es': { flag: '🇪🇸', label: 'Castellano' },
        'en': { flag: '🇬🇧', label: 'English' }
    };"""

new_lang_info = """const langInfo = {
        'es': { flag: '🇪🇸', label: 'Castellano' },
        'en': { flag: '🇬🇧', label: 'English' },
        'it': { flag: '🇮🇹', label: 'Italiano' },
        'zh': { flag: '🇨🇳', label: '中文' },
        'ar': { flag: '🇦🇪', label: 'العربية' },
        'ru': { flag: '🇷🇺', label: 'Русский' },
        'de': { flag: '🇩🇪', label: 'Deutsch' },
        'fr': { flag: '🇫🇷', label: 'Français' },
        'ja': { flag: '🇯🇵', label: '日本語' },
        'pt': { flag: '🇵🇹', label: 'Português' }
    };"""

if "    const langInfo = {" in js:
    # Just replace it
    js = re.sub(r'const langInfo = {[^}]+};', new_lang_info, js)

# Update the Arabic audio replacement from the other session?
# "Fixing Arabic text in JavaScript for the audio button"
# In script.js:
# if (lang === 'ar') titleSpan.textContent = "الاستماع إلى القصة المكتوبة";
# Let's add that under `if (audioPlayer)` logic.

# In script.js:
#             titleSpan.textContent = 'Listen to Spoken Story';
#         }

js = js.replace("""            titleSpan.textContent = 'Listen to Spoken Story';
        }""", """            titleSpan.textContent = 'Listen to Spoken Story';
        } else if (lang === 'it') {
            titleSpan.textContent = 'Ascolta la Storia Parlata';
        } else if (lang === 'zh') {
            titleSpan.textContent = '聆听语音故事';
        } else if (lang === 'ar') {
            titleSpan.textContent = 'الاستماع إلى القصة المكتوبة';
        } else if (lang === 'ru') {
            titleSpan.textContent = 'Слушать аудио сказку';
        } else if (lang === 'de') {
            titleSpan.textContent = 'Hören Sie die gesprochene Geschichte';
        } else if (lang === 'fr') {
            titleSpan.textContent = 'Écouter l\\'histoire parlée';
        } else if (lang === 'ja') {
            titleSpan.textContent = '音声ストーリーを聞く';
        } else if (lang === 'pt') {
            titleSpan.textContent = 'Ouvir a História Falada';
        }""")

with open("shared/script.js", "w") as f:
    f.write(js)
print("Updated script.js")
