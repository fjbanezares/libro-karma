document.addEventListener('DOMContentLoaded', () => {
    initLayout();
    initLanguage();
    initScroll();
});

function initLayout() {
    const body = document.body;
    const toggleBtns = document.querySelectorAll('.toggle-btn');
    const overlay = document.querySelector('.sidebar-overlay');
    const langTrigger = document.querySelector('.lang-current-trigger');
    const langMenu = document.querySelector('.lang-dropdown-menu');

    // Desktop/Sidebar collapse state
    const isCollapsed = localStorage.getItem('karmaSidebarCollapsed') === 'true';
    if (window.innerWidth > 1024 && isCollapsed) {
        body.classList.add('sidebar-collapsed');
    }

    // Toggle menu logic
    toggleBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (window.innerWidth <= 1024) {
                body.classList.toggle('sidebar-open');
            } else {
                body.classList.toggle('sidebar-collapsed');
                localStorage.setItem('karmaSidebarCollapsed', body.classList.contains('sidebar-collapsed'));
            }
        });
    });

    // Language Dropdown logic
    if (langTrigger && langMenu) {
        langTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            langMenu.classList.toggle('show');
        });
    }

    // Close language menu on document click
    document.addEventListener('click', () => {
        if (langMenu) langMenu.classList.remove('show');
    });

    // Sidebar Close logic: ONLY via overlay or toggle button in mobile
    // (Removed the global document listener that closed sidebar-open on any click)

    // Sidebar overlay click
    if (overlay) {
        overlay.addEventListener('click', () => {
            body.classList.remove('sidebar-open');
        });
    }

    // Highlight current page
    updateActiveNavLink();
}

function updateActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkHref = link.getAttribute('href');
        if (!linkHref) return;

        // Simplify: if the link is in the current path, it's active
        // Get the folder name from the link (e.g. "09_frio_egoismo")
        const linkParts = linkHref.split('/');
        const folder = linkParts.find(p => p.match(/^\d{2}_/));

        if (folder && currentPath.includes(folder)) {
            link.classList.add('active');
        } else if ((linkHref.includes('index.html') || linkHref === '/') &&
            (currentPath.endsWith('/') || currentPath.endsWith('index.html')) &&
            !currentPath.includes('_')) {
            link.classList.add('active');
        }
    });
}

function initLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    let lang = urlParams.get('lang') || localStorage.getItem('karmaLang') || 'es';
    setLanguage(lang);
}

function setLanguage(lang) {
    document.body.className = document.body.className.replace(/lang-(es|en|it|zh|ar|ru|de|fr|ja|pt)/g, '') + ` lang-${lang}`;
    localStorage.setItem('karmaLang', lang);

    // Update UI Indicators
    const langInfo = {
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

    const currentTrigger = document.querySelector('.lang-current-trigger');
    if (currentTrigger && langInfo[lang]) {
        currentTrigger.innerHTML = `<span class="flag">${langInfo[lang].flag}</span> <span>${langInfo[lang].label}</span>`;
    }

    // Update Dropdown Items Active State
    document.querySelectorAll('.lang-opt').forEach(opt => {
        const bl = opt.getAttribute('data-lang');
        opt.classList.toggle('active', bl === lang);
    });

    // Persist language on all navigation links
    const links = document.querySelectorAll('.nav-link, .logo-link, .chapter-card');
    links.forEach(link => {
        try {
            const href = link.getAttribute('href');
            if (!href || href.startsWith('#') || href.startsWith('mailto:')) return;

            const url = new URL(href, window.location.href);
            url.searchParams.set('lang', lang);

            // Use setAttribute to keep relative paths intact
            const base = href.split('?')[0];
            link.setAttribute('href', base + url.search);
        } catch (e) { }
    });
}

function initScroll() {
    const progress = document.querySelector('.scroll-progress');
    const heroImg = document.getElementById('hero-img');
    const fadeElements = document.querySelectorAll('.fade-in');

    const handleScroll = () => {
        const scrolled = window.scrollY;

        // Parallax Effect
        if (heroImg) {
            heroImg.style.transform = `scale(${1 + scrolled * 0.0004}) translateY(${scrolled * 0.1}px)`;
            heroImg.style.opacity = 1 - (scrolled / window.innerHeight);
        }

        // Win Progress line
        const winH = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const width = (scrolled / winH) * 100;
        if (progress) progress.style.width = width + "%";

        // Scroll Fade-in reveal
        fadeElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.85) {
                el.classList.add('is-visible');
            }
        });
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll();
}
