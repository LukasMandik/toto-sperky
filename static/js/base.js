document.addEventListener("DOMContentLoaded", function() {
    // Získajte názov aktuálneho súboru
    const currentPath = window.location.pathname;
  
    // Podmienka na kontrolu, či sme na hlavnej stránke
    if (currentPath === "/") {
        // Nastavenie pre hlavnú stránku
        if (window.matchMedia('(min-width: 768px)').matches) {
            gsap.registerPlugin(ScrollTrigger);
  
            gsap.to(".main_navbar", {
                backgroundColor: "#FBF8F5",
                boxShadow: "0px 3px 10px rgba(43, 43, 43, 0.1)",
                duration: 0.2,
                ease: "power2.out",
                scrollTrigger: {
                    trigger: ".main_image_container",
                    start: "center -25% ",
                    end: "center -25%",
                    scrub: false,
                    // markers: true,
                    toggleActions: "restart none none reverse",
                }
            });
        }
    } else {
        // Nastavenie pre ostatné stránky
        if (window.matchMedia('(min-width: 768px)').matches) {
            gsap.registerPlugin(ScrollTrigger);
  
            gsap.to(".main_navbar", {
                backgroundColor: "#FBF8F5",
                boxShadow: "0px 3px 10px rgba(43, 43, 43, 0.1)",
                duration: 0.2,
                ease: "power2.out",
                scrollTrigger: {
                    trigger: ".wrapper",
                    start: "center 50svh ",
                    end: "center 0svh",
                    scrub: false,
                    // markers: true,
                    toggleActions: "restart none none reverse",
                }
            });
        }
    }
  });


document.addEventListener("DOMContentLoaded", function() {

    let hamburger = document.querySelector(".hamburger");
    let menu = document.querySelector(".menu");

    hamburger.addEventListener("click", function(){
        menu.classList.toggle("active");
    });

});

document.addEventListener("DOMContentLoaded", function() {
    let hamburger = document.querySelector(".hamburger");
    let toggle = document.querySelector("#toggle");

    hamburger.addEventListener("click", function() {
        toggle.classList.toggle("active");
        if (toggle.classList.contains("active")) {
            document.body.style.overflow = 'hidden';
            // document.body.style.position = 'fixed';
            document.body.style.width = '100%';
        } else {
            document.body.style.overflow = '';
            document.body.style.position = '';
            document.body.style.width = '';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
  
    gsap.registerPlugin(ScrollTrigger);
    gsap.utils.toArray('.starterline').forEach((elem) => {
        let line = elem.querySelector('.line');
        var lineLength = line.getTotalLength();
        line.style.strokeDasharray = lineLength;
        line.style.strokeDashoffset = lineLength;
  
        let Timeline = gsap.timeline({
            ease: "elastic",

            scrollTrigger: {
                trigger: elem,
                start: "top 0svh",
                end: "bottom -100svh",
                scrub: true,
                // markers:true,
            }
        });
  
        Timeline
        .to(line,{strokeDashoffset: 0})
    });
  });


  document.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname;
    const menuItems = document.querySelectorAll('.startermenu li a');

    menuItems.forEach(item => {
        const section = item.getAttribute('data-section');
        if ((currentPath === '/' && section === 'home') || 
            currentPath.includes(section.toLowerCase()) || 
            (currentPath.includes('product') && section === 'Gallery')) {
            item.classList.add('active2');
        } else {
            item.classList.remove('active2');
        }
    });
});




document.addEventListener("DOMContentLoaded", function() {
    const customizeCookiesButton = document.getElementById("customizeCookies");
    const modal = document.getElementById("customize-cookies-modal");
    const closeModal = document.querySelector(".close_cookies");
    const cookieForm = document.getElementById("cookie-preferences-form");
    const marketingCookiesCheckbox = document.getElementById("marketing-cookies");

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

    // Nastaviť stav checkboxu podľa uložených cookies
    if (!document.cookie.includes("marketingCookies=")) {
        marketingCookiesCheckbox.checked = true;
    } else if (document.cookie.includes("marketingCookies=accepted")) {
        marketingCookiesCheckbox.checked = true;
        loadGoogleAnalytics();
    } else {
        marketingCookiesCheckbox.checked = false;
        unloadGoogleAnalytics();
    }

    customizeCookiesButton.addEventListener("click", function() {
        modal.style.display = "block";
    });

    closeModal.addEventListener("click", function() {
        modal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });

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
        modal.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const cookieBox = document.querySelector(".wrapper2");
    const buttons = document.querySelectorAll(".button");
    const modal = document.getElementById("customize-cookies-modal");
    const closeModal = document.querySelector(".close_cookies");
    const cookieForm = document.getElementById("cookie-preferences-form");
    const marketingCookiesCheckbox = document.getElementById("marketing-cookies");

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

    const executeCodes = () => {
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
                    modal.style.display = "block";
                }
            });
        });
    };

    closeModal.addEventListener("click", function() {
        modal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    cookieForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const marketingCookies = marketingCookiesCheckbox.checked ? "accepted" : "declined";
        document.cookie = "cookieBy=toto_sperky; path=/; max-age=" + 60 * 60 * 24 * 30;
        document.cookie = "marketingCookies=" + marketingCookies + "; path=/; max-age=" + 60 * 60 * 24 * 30;
        if (marketingCookies === "accepted") {
            loadGoogleAnalytics();
        } else {
            unloadGoogleAnalytics();
        }
        modal.style.display = "none";
    });

    window.addEventListener("load", executeCodes);
});