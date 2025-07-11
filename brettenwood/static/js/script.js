document.addEventListener('DOMContentLoaded', function () {
    // ==================== Mobile Menu Toggle ====================
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('nav'); // Changed from navLinks to nav for better semantics
    const navLinks = document.querySelectorAll('.nav-link');

    function toggleMenu() {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        hamburger.setAttribute('aria-expanded', hamburger.classList.contains('active'));
    }

    // Enhanced event listeners for mobile support
    hamburger.addEventListener('click', toggleMenu);
    hamburger.addEventListener('touchstart', function (e) {
        e.preventDefault();
        toggleMenu();
    });

    // Close menu when clicking links
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (hamburger.classList.contains('active')) {
                toggleMenu();
            }
        });
    });

    // Close menu when tapping outside
    document.addEventListener('click', function (e) {
        if (navMenu.classList.contains('active') &&
            !e.target.closest('nav') &&
            !e.target.classList.contains('hamburger')) {
            toggleMenu();
        }
    });

    // ==================== Existing Smooth Scrolling ====================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                if (hamburger.classList.contains('active')) {
                    toggleMenu();
                }

                setTimeout(() => {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }, 100);
            }
        });
    });

    // ==================== Existing Portfolio Modal ====================
    window.openModal = function (imageSrc, location, description) {
        const modal = document.getElementById('imageModal');
        const modalImg = document.getElementById('expandedImage');
        const caption = document.getElementById('caption');

        modalImg.src = imageSrc;
        caption.innerHTML = `<h3>${location}</h3><p>${description}</p>`;
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';

        modalImg.addEventListener('touchstart', function (e) {
            e.stopPropagation();
        });
    };

    window.closeModal = function () {
        const modal = document.getElementById('imageModal');
        modal.classList.remove('show');
        document.body.style.overflow = '';
    };

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('modal')) {
            closeModal();
        }
    });

    document.addEventListener('touchstart', function (event) {
        if (event.target.classList.contains('modal')) {
            closeModal();
        }
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });

    // ==================== Existing Scroll Animations ====================
    let lastScrollPosition = 0;
    let ticking = false;

    const animateOnScroll = function () {
        const elements = document.querySelectorAll('.feature-card, .system-card, .gallery-square, .review-card');
        const windowHeight = window.innerHeight;

        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;

            if (elementPosition < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });

        ticking = false;
    };

    const animatedElements = document.querySelectorAll('.feature-card, .system-card, .gallery-square, .review-card');
    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });

    window.addEventListener('scroll', function () {
        lastScrollPosition = window.scrollY;

        if (!ticking) {
            window.requestAnimationFrame(function () {
                animateOnScroll(lastScrollPosition);
                ticking = false;
            });
            ticking = true;
        }
    });

    animateOnScroll();

    // ==================== Existing Brand Filtering ====================
    document.querySelectorAll('.brand-btn').forEach(btn => {
        btn.addEventListener('touchstart', function (e) {
            e.preventDefault();
            this.click();
        });

        btn.addEventListener('click', function () {
            const buttons = document.querySelectorAll('.brand-btn');
            const cards = document.querySelectorAll('.system-card');
            const selectedBrand = this.dataset.brand;

            buttons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            cards.forEach(card => {
                const cardBrand = card.dataset.brand;
                const shouldShow = selectedBrand === 'all' || cardBrand === selectedBrand;

                if (shouldShow) {
                    card.style.display = 'block';
                    void card.offsetWidth;
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // ==================== Existing Mobile UX Improvements ====================
    document.addEventListener('dblclick', function (e) {
        e.preventDefault();
    }, { passive: false });

    function setVh() {
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
    }

    setVh();
    window.addEventListener('resize', setVh);
});
