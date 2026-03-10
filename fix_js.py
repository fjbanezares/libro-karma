import os
import re

file_path = "shared/script.js"
with open(file_path, "r") as f:
    js = f.read()

# Fix 1: The document.body.className line
js = re.sub(r"document\.body\.className\.replace\([^`]+`", "document.body.className.replace(/lang-(es|en|it|zh|ar|ru|de|fr|ja|pt)/g, '') + `", js)

# Fix 2: The langInfo dictionary
old_dict = r"const langInfo = \{[\s\S]*?\};\s*const currentTrigger"
new_dict = """const langInfo = {
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
    };

    const currentTrigger"""

js = re.sub(old_dict, new_dict, js)

with open(file_path, "w") as f:
    f.write(js)
print("Fixed syntax errors in script.js")
