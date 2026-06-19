document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    }

    // 2. GSAP Animations
    if (typeof gsap !== 'undefined') {
        // Hero Section Animation
        const heroTitle = document.querySelector('.hero-title');
        const heroSubtitle = document.querySelector('.hero-subtitle');
        const heroBtns = document.querySelectorAll('.hero-btn');

        if (heroTitle && heroSubtitle) {
            const tl = gsap.timeline();
            tl.from(heroTitle, { y: 50, opacity: 0, duration: 1, ease: "power3.out", delay: 0.2 })
              .from(heroSubtitle, { y: 30, opacity: 0, duration: 0.8, ease: "power3.out" }, "-=0.5")
              .from(heroBtns, { y: 20, opacity: 0, duration: 0.6, stagger: 0.2, ease: "power2.out" }, "-=0.4");
        }

        // Counter Animations
        const counters = document.querySelectorAll('.counter-val');
        if (counters.length > 0) {
            // Using Intersection Observer to trigger GSAP counter when in view
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        const endVal = parseInt(target.getAttribute('data-target'), 10);
                        
                        let obj = { val: 0 };
                        gsap.to(obj, {
                            val: endVal,
                            duration: 2,
                            ease: "power2.out",
                            onUpdate: function() {
                                target.innerHTML = Math.round(obj.val) + '+';
                            }
                        });
                        
                        observer.unobserve(target);
                    }
                });
            }, { threshold: 0.5 });

            counters.forEach(counter => {
                observer.observe(counter);
            });
        }
    }
});
