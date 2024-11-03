$(document).ready(function() {
    const customizeCookiesButton = document.getElementById("customizeCookies");
    const modal = document.getElementById("customize-cookies-modal");
    const closeModal = document.querySelector(".close_cookies");
    const cookieForm = document.getElementById("cookie-preferences-form");
    const marketingCookiesCheckbox = document.getElementById("marketing-cookies");
    const cookieBox = document.querySelector(".wrapper2");
    const buttons = document.querySelectorAll(".button");

    // Funkcia na načítanie Google Analytics
    function loadGoogleAnalytics() {
        // Načítanie Universal Analytics
        (function(i,s,o,g,r,a,m){
            i['GoogleAnalyticsObject']=r;
            i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)
            }, i[r].l=1*new Date();
            a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];
            a.async=1;
            a.src=g;
            m.parentNode.insertBefore(a,m)
        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-XXXXX-Y', 'auto');
        ga('send', 'pageview');

        // Načítanie gtag.js
        const gtagScript = document.createElement('script');
        gtagScript.async = true;
        gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-N0MJRLXRKS';
        document.head.appendChild(gtagScript);

        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-N0MJRLXRKS');
    }

    // Funkcia na odstránenie Google Analytics
    function unloadGoogleAnalytics() {
        // Odstránenie Universal Analytics
        if (window.ga) {
            window.ga('remove');
            delete window.ga;
        }

        // Odstránenie gtag.js
        const gtagScripts = document.querySelectorAll('script[src*="googletagmanager.com/gtag/js"]');
        gtagScripts.forEach(script => script.remove());

        // Vyčistenie dataLayer
        window.dataLayer = [];
    }

    // Funkcia na zobrazenie modalu
    function showModal() {
        modal.style.display = "block";
    }

    // Funkcia na skrytie modalu
    function hideModal() {
        modal.style.display = "none";
    }

    // Inicializovať stav checkboxu podľa uložených cookies
    function initializeCookieSettings() {
        if (!document.cookie.includes("marketingCookies=")) {
            marketingCookiesCheckbox.checked = true;
        } else if (document.cookie.includes("marketingCookies=accepted")) {
            marketingCookiesCheckbox.checked = true;
            loadGoogleAnalytics();
        } else {
            marketingCookiesCheckbox.checked = false;
            unloadGoogleAnalytics();
        }
    }

    // Event listener pre otvorenie modalu
    customizeCookiesButton.addEventListener("click", showModal);

    // Event listener pre zatvorenie modalu
    closeModal.addEventListener("click", hideModal);

    // Event listener pre klik mimo modalu na zatvorenie
    window.addEventListener("click", function(event) {
        if (event.target == modal) {
            hideModal();
        }
    });

    // Event listener pre odoslanie formulára
    cookieForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const marketingCookies = marketingCookiesCheckbox.checked ? "accepted" : "declined";
        const currentCookieValueArray = document.cookie.split('; ').find(row => row.startsWith('marketingCookies='));
        let currentCookieValue = "";
        if (currentCookieValueArray) {
            currentCookieValue = currentCookieValueArray.split('=')[1];
        }

        if (currentCookieValue !== marketingCookies) {
            document.cookie = "marketingCookies=" + marketingCookies + "; path=/; max-age=" + 60 * 60 * 24 * 30;
            if (marketingCookies === "accepted") {
                loadGoogleAnalytics();
            } else {
                unloadGoogleAnalytics();
            }
        }
        hideModal();
    });

    // Funkcia na vykonanie kódov na zobrazenie cookie boxu
    function executeCodes() {
        if (document.cookie.includes("cookieBy=toto_sperky")) return;
        cookieBox.classList.add("show");

        buttons.forEach((button) => {
            button.addEventListener("click", () => {
                cookieBox.classList.remove("show");

                if (button.id === "acceptBtn") {
                    document.cookie = "cookieBy=toto_sperky; path=/; max-age=" + 60 * 60 * 24 * 30;
                    document.cookie = "marketingCookies=accepted; path=/; max-age=" + 60 * 60 * 24 * 30;
                    loadGoogleAnalytics();
                } else if (button.id === "declineBtn") {
                    document.cookie = "cookieBy=toto_sperky; path=/; max-age=" + 60 * 60 * 24 * 30;
                    document.cookie = "marketingCookies=declined; path=/; max-age=" + 60 * 60 * 24 * 30;
                    unloadGoogleAnalytics();
                } else if (button.id === "customizeBtn") {
                    showModal();
                }
            });
        });
    }

    // Inicializácia na načítanie nastavení cookies
    initializeCookieSettings();

    // Event listener pre načítanie stránky
    window.addEventListener("DOMContentLoaded", executeCodes);
});