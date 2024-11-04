document.addEventListener("DOMContentLoaded", function() {
    const customizeCookiesButton = document.getElementById("customizeCookies");
    const modal = document.getElementById("customize-cookies-modal");
    const closeModal = document.querySelector(".close_cookies");
    const cookieForm = document.getElementById("cookie-preferences-form");
    const marketingCookiesCheckbox = document.getElementById("marketing-cookies");
    const cookieBox = document.querySelector(".wrapper2");
    const buttons = document.querySelectorAll(".button");

    // Funkcia na načítanie Google Analytics 4
    function loadGoogleAnalytics() {
        if (!window.ga4Initialized) {
            // Načítanie gtag.js
            const gtagScript = document.createElement('script');
            gtagScript.async = true;
            gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-N0MJRLXRKS';
            document.head.appendChild(gtagScript);

            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-N0MJRLXRKS', {
                'anonymize_ip': true,
                'cookie_flags': 'SameSite=None; Secure'
            });

            window.ga4Initialized = true;
        }
    }

    // Funkcia na odstránenie Google Analytics 4
    function unloadGoogleAnalytics() {
        // Odstránenie gtag.js
        const gtagScripts = document.querySelectorAll('script[src*="googletagmanager.com/gtag/js"]');
        gtagScripts.forEach(script => script.remove());

        // Vyčistenie dataLayer
        window.dataLayer = [];
        window.ga4Initialized = false;
    }

    // Funkcia na zobrazenie modalu
    function showModal() {
        if (modal) {
            modal.style.display = "block";
        }
    }

    // Funkcia na skrytie modalu
    function hideModal() {
        if (modal) {
            modal.style.display = "none";
        }
    }

    // Funkcia na získanie hodnoty cookie
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    // Funkcia na nastavenie cookie
    function setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = `${name}=${value}; expires=${expires}; path=/; SameSite=Lax`;
    }

    // Inicializovať stav checkboxu podľa uložených cookies
    function initializeCookieSettings() {
        const marketingCookie = getCookie("marketingCookies");
        if (!marketingCookie) {
            marketingCookiesCheckbox.checked = true;
        } else if (marketingCookie === "accepted") {
            marketingCookiesCheckbox.checked = true;
            loadGoogleAnalytics();
        } else {
            marketingCookiesCheckbox.checked = false;
            unloadGoogleAnalytics();
        }
    }

    // Funkcia na vykonanie kódov na zobrazenie cookie boxu
    function executeCodes() {
        if (getCookie("cookieBy") === "toto_sperky") return;
        if (cookieBox) {
            cookieBox.classList.add("show");

            buttons.forEach((button) => {
                button.addEventListener("click", () => {
                    if (cookieBox) {
                        cookieBox.classList.remove("show");
                    }

                    if (button.id === "acceptBtn") {
                        setCookie("cookieBy", "toto_sperky", 30);
                        setCookie("marketingCookies", "accepted", 30);
                        loadGoogleAnalytics();
                    } else if (button.id === "declineBtn") {
                        setCookie("cookieBy", "toto_sperky", 30);
                        setCookie("marketingCookies", "declined", 30);
                        unloadGoogleAnalytics();
                    } else if (button.id === "customizeBtn") {
                        showModal();
                    }
                });
            });
        }
    }

    // Event listener pre otvorenie modalu
    if (customizeCookiesButton) {
        customizeCookiesButton.addEventListener("click", showModal);
    }

    // Event listener pre zatvorenie modalu
    if (closeModal) {
        closeModal.addEventListener("click", hideModal);
    }

    // Event listener pre klik mimo modalu na zatvorenie
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            hideModal();
        }
    });

    // Event listener pre odoslanie formulára
    if (cookieForm) {
        cookieForm.addEventListener("submit", function(event) {
            event.preventDefault();
            const marketingCookies = marketingCookiesCheckbox.checked ? "accepted" : "declined";
            const currentCookieValue = getCookie("marketingCookies");

            if (currentCookieValue !== marketingCookies) {
                setCookie("cookieBy", "toto_sperky", 30);
                setCookie("marketingCookies", marketingCookies, 30);
                if (marketingCookies === "accepted") {
                    loadGoogleAnalytics();
                } else {
                    unloadGoogleAnalytics();
                }
            }
            hideModal();
        });
    }

    // Inicializácia na načítanie nastavení cookies
    initializeCookieSettings();

    // Event listener pre načítanie stránky
    window.addEventListener("DOMContentLoaded", executeCodes);
});