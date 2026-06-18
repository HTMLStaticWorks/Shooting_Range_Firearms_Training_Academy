document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggler (Dark/Light Mode)
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    
    // Check local storage for theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-bs-theme', savedTheme);
        updateThemeIcon(savedTheme);
    } else {
        // Check system preference
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (prefersDark) {
            htmlElement.setAttribute('data-bs-theme', 'dark');
            updateThemeIcon('dark');
        }
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const currentTheme = htmlElement.getAttribute('data-bs-theme') || 'light';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            htmlElement.setAttribute('data-bs-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeToggleBtn) return;
        const icon = themeToggleBtn.querySelector('i');
        if (icon) {
            if (theme === 'dark') {
                icon.classList.remove('bi-moon-fill');
                icon.classList.add('bi-sun-fill');
            } else {
                icon.classList.remove('bi-sun-fill');
                icon.classList.add('bi-moon-fill');
            }
        }
    }

    // 2. RTL Toggler
    const rtlToggleBtn = document.getElementById('rtl-toggle');
    
    // Check local storage for dir
    const savedDir = localStorage.getItem('dir');
    if (savedDir) {
        htmlElement.setAttribute('dir', savedDir);
        // Also update the language if needed
        htmlElement.setAttribute('lang', savedDir === 'rtl' ? 'ar' : 'en');
    }

    if (rtlToggleBtn) {
        rtlToggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const currentDir = htmlElement.getAttribute('dir') || 'ltr';
            const newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
            
            htmlElement.setAttribute('dir', newDir);
            htmlElement.setAttribute('lang', newDir === 'rtl' ? 'ar' : 'en');
            localStorage.setItem('dir', newDir);
            
            // Adjust AOS for RTL if needed or reload to cleanly re-calc
            // window.location.reload(); 
        });
    }

    // 3. Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
});
