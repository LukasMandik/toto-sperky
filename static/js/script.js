$(document).ready(function() {

let hamburger = document.querySelector(".hamburger");
let menu = document.querySelector(".menu");

	hamburger.addEventListener("click", function(){
		menu.classList.toggle("active");
	})

})





  $(document).ready(function() {
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


  



  



$(document).ready(function() {
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





  $(document).ready(function() {
    gsap.registerPlugin(ScrollTrigger);
  
    gsap.utils.toArray('.starterdot').forEach((elem) => {
      // Predpokladáme, že každý prvok má niečo ako čiaru alebo iný element na animovanie
      let line = elem.querySelectorAll('.logo_dot'); // Prvok, ktorý budeme animovať

  
        // Vytvoríme GSAP časovú os s ScrollTrigger
        let timeline = gsap.timeline({
          ease: "power2.inOut",
          scrollTrigger: {
            trigger: elem, // Bod, kde sa spustí animácia
            start: 'top 280svh',    // Začiatok triggeru
            end: 'bottom 190svh',   // Koniec triggeru
            scrub: 1,               // Skrúbovacie posúvanie
            // markers: true,   
            // toggleActions: "restart none none reverse",   
          },
        });
  
        // Pridáme animáciu na Timeline
        timeline
        .from(line[0], { rotation: "-=360_cw", transformOrigin: "7220px 2000px", duration: 3},0,0, ">")
        .from(line[1], { rotation: "-=360_cw", transformOrigin: "7620px 2000px", duration: 4}, "<")
        .from(line[2], { rotation: "-=360_cw", transformOrigin: "-5370px -4250px", duration: 4},0,0, "=") // Rotácia elementu s offsetom
        .from(line[3], { rotation: "-=360_cw", transformOrigin: "4020px 6220px", duration: 5},0,0,"<"); // Rotácia elementu s offsetom
      
    });
  });
  
  

  $(document).ready(function() {
    gsap.registerPlugin(ScrollTrigger);
  
    gsap.utils.toArray('.line_center').forEach((elem) => {
      let line = elem.querySelector('.line');
      let lineLength = line.getTotalLength();
  

      line.style.strokeDasharray = lineLength;
      line.style.strokeDashoffset = lineLength; 

      let Timeline = gsap.timeline({
        scrollTrigger: {
          trigger: elem,
          easy:"linear",
          start: "top 500svh",
          end: "bottom 300svh",
          scrub: true,
          // markers: true,
          // toggleActions: "restart none none reverse",  
        }
      });
      Timeline
        .to(line, { strokeDashoffset: 0 })
    });
  });

  $(document).ready(function() {
    gsap.registerPlugin(ScrollTrigger);
  
    gsap.utils.toArray('.line_center_about_me').forEach((elem) => {
      let line = elem.querySelector('.line');
      let lineLength = line.getTotalLength();
  

      line.style.strokeDasharray = lineLength;
      line.style.strokeDashoffset = lineLength; 

      let Timeline = gsap.timeline({
        scrollTrigger: {
          trigger: elem,
          easy:"linear",
          start: "top 600svh",
          end: "bottom 600svh",
          scrub: false,
          // markers: true,
          toggleActions: "restart none none reverse",  
        }
      });
      Timeline
        .to(line, { strokeDashoffset: 0 })
    });
  });
  $(document).ready(function() {
    gsap.registerPlugin(ScrollTrigger);
  
    gsap.utils.toArray('.line_center_short').forEach((elem) => {
      let line = elem.querySelector('.line');
      let lineLength = line.getTotalLength();
  
      // Nastavte strokeDasharray a počiatočný offset
      line.style.strokeDasharray = lineLength;
      line.style.strokeDashoffset = lineLength; // Začne od stredu
  
      // Vytvorte časovú os pre animáciu
      let Timeline = gsap.timeline({
        scrollTrigger: {
          trigger: elem,
          easy:"linear",
          start: "top 600svh",
          end: "bottom 300svh",
          scrub: true,
          // markers: true,
          // toggleActions: "restart none none reverse",  
        }
      });
  
      // Animačný efekt, ktorý zobrazí čiaru od stredu po oba konce
      Timeline
        .to(line, { strokeDashoffset: 0 }) // Záporná hodnota pre animáciu oboma smermi
    });
  });


  $(document).ready(function() {
    gsap.utils.toArray('.text_home_about_jewelry').forEach((elem) => {
        let lines = elem.querySelectorAll('.text_home_about_jewelry h1.first_text, .text_home_about_jewelry h2.last_text');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 610svh",
              end: "center 620svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, x: -150,duration: 0.45 });
      });
    });
  });

  $(document).ready(function() {
    gsap.utils.toArray('.text_home_about_jewelry').forEach((elem) => {
        let lines = elem.querySelectorAll('.text_home_about_jewelry .ellipse_group');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 610svh",
              end: "center 620svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, x: 150,duration: 0.35 },0.2,0);
      });
    });
  });


  $(document).ready(function() {
    gsap.utils.toArray('.second_home_container').forEach((elem) => {
        let lines = elem.querySelectorAll('.second_home_container .text_home_about_jewelry .ellipse_group .ellipse-1');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 610svh",
              end: "center 120svh",
              scrub: true,
              // toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, {x: 5,duration: 0.35 });
      });
    });
  });
  $(document).ready(function() {
    gsap.utils.toArray('.second_home_container').forEach((elem) => {
        let lines = elem.querySelectorAll('.second_home_container .text_home_about_jewelry .ellipse_group .ellipse-2');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 610svh",
              end: "center 120svh",
              scrub: true,
              // toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, {y: 5,duration: 0.35 });
      });
    });
  });
  $(document).ready(function() {
    gsap.utils.toArray('.second_home_container').forEach((elem) => {
        let lines = elem.querySelectorAll('.second_home_container .text_home_about_jewelry .ellipse_group .ellipse-3');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 610svh",
              end: "center 120svh",
              scrub: true,
              // toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, {scale: 1.03, x: -5,duration: 0.35 });
      });
    });
  });

  $(document).ready(function() {
    gsap.utils.toArray('.home_buttons').forEach((elem) => {
        let lines = elem.querySelectorAll('.home_buttons .btn');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 610svh",
              end: "center 620svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, y: 20,duration: 0.35, width: 80});
      });
    });
  });
  $(document).ready(function() {
    gsap.utils.toArray('.text-about-me1').forEach((elem) => {
        let lines = elem.querySelectorAll('.text-about-me1 p');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 750svh",
              end: "center 750svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, y: 20,scale: 0.9,duration: 0.35},0.5,0);
      });
    });
  });

  $(document).ready(function() {
    gsap.utils.toArray('.content-about-me').forEach((elem) => {
        let lines = elem.querySelectorAll('.image_neckless img');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 1450svh",
              end: "center 1450svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, {
           opacity: 0,
           y: 20, 
           duration: 0.35,
           },0.8,0);
      });
    });
  });
  $(document).ready(function() {
    gsap.utils.toArray('.container_about_me').forEach((elem) => {
        let lines = elem.querySelectorAll('.image_neckless');
  
        lines.forEach((line) => {
            let Timeline = gsap.timeline({
                ease: "slowMo.ease",
                scrollTrigger: {
                    trigger: line,
                    start: "top 650svh",
                    end: "bottom 0svh",
                    scrub: true,
                    // markers: true,
                    // toggleActions: "restart none none reverse",
                }
            });
  
            Timeline.to(line, { scale: 1.25,});
        });
    });
  });

  $(document).ready(function() {
    gsap.utils.toArray('.text-about-me').forEach((elem) => {
        let lines = elem.querySelectorAll('.text-about-me p');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 650svh",
              end: "center 650svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, y: 20,scale: 0.9,duration: 0.35});
      });
    });
  });
  $(document).ready(function() {
    gsap.utils.toArray('.content-about-me').forEach((elem) => {
        let lines = elem.querySelectorAll('.carousel');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 650svh",
              end: "center 650svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, y: 20,scale: 0.9,duration: 0.35});
      });
    });
  });
  $(document).ready(function() {
    gsap.utils.toArray('.third_home_container').forEach((elem) => {
        let lines = elem.querySelectorAll('.carusel');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 790svh",
              end: "center 790svh",
              scrub: false,
              toggleActions: "restart none none reverse",
              // markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, y: 20,scale: 0.9,duration: 0.35});
      });
    });
  });
  
  $(document).on("click", ".hamburger", function() {
    if ($(".menu").hasClass("active")) {
    const Container = document.querySelectorAll('.main_navbar .menu .menu_search');
  // Create an animation loop using GSAP
  gsap.from(Container, {
    x: -340,
    delay: 0, 
    opacity: 0, 
    // y: 2,
    // rotate: 1,
    stagger: 0.03,  
    duration: 0.6, 
    // repeat: -1,
    // yoyo: true, 
    ease: 'power2.inOut' // Smooth easing function
  });
  }
  });



  $(document).on("click", ".hamburger", function() {
    if ($(".menu").hasClass("active")) {
    const Container = document.querySelectorAll('.main_navbar .menu ul li');
  
  // Create an animation loop using GSAP
  gsap.from(Container, {
    x: -340,
    // delay: 0.4, 
    opacity: 0, 
    // y: 2,
    // rotate: 1,
    stagger: 0.03,  
    duration: 0.7, 
    // repeat: -1,
    // yoyo: true, 
    ease: 'power2.inOut' // Smooth easing function
  });
}
});

$(document).on("click", ".hamburger", function() {
  if ($(".menu").hasClass("active")) {
  const Container = document.querySelectorAll('.main_navbar .menu .connections_container p');
// Create an animation loop using GSAP
gsap.from(Container, {
  x: -340,
  delay: 0.3, 
  opacity: 0, 
  // y: 2,
  // rotate: 1,
  stagger: 0.03,  
  duration: 0.6, 
  // repeat: -1,
  // yoyo: true, 
  ease: 'power2.inOut' // Smooth easing function
});
}
});
  
  $(document).ready(function() {
  
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
        // .to(dot,{ opacity: 0 })
            // .to(line[1], { opacity: 0 },"+=");
    });
  });

$(document).ready(function() {
  gsap.utils.toArray('.starter2').forEach((elem) => {
      let lines = elem.querySelectorAll('.main_title_container h1 ,.main_title_container h2');

      let Timeline = gsap.timeline({
        scrollTrigger: {
            trigger: elem,
            start: "center 610svh",
            end: "center 620svh",
            scrub: false,
            toggleActions: "restart none none reverse",
            // markers: true,
        }
    });

    lines.forEach((line) => {
      Timeline.from(line, { opacity: 0, x: 100,duration: 0.35 });
    });
  });
});

$(document).ready(function() {
  gsap.utils.toArray('.starter').forEach((elem) => {
      let lines = elem.querySelectorAll('.title_home_container h2');

      let Timeline = gsap.timeline({
        scrollTrigger: {
            trigger: elem,
            start: "center 610svh",
            end: "center 620svh",
            scrub: false,
            toggleActions: "restart none none reverse",
            // markers: true,
        }
    });

    lines.forEach((line) => {
      Timeline.from(line, { opacity: 0, x: 100,duration: 0.35 });
    });
  });
});


$(document).ready(function() {
  gsap.utils.toArray('.starter').forEach((elem) => {
      let lines = elem.querySelectorAll('.main_image_container');

      lines.forEach((line) => {
          let Timeline = gsap.timeline({
              ease: "slowMo.ease",
              scrollTrigger: {
                  trigger: line,
                  start: "top -0svh",
                  end: "bottom -600svh",
                  scrub: true,
                  // markers: true,
                  // toggleActions: "restart none none reverse",
              }
          });

          Timeline.to(line, { backgroundPosition: "64% 30%" });
      });
  });
});


$(document).ready(function() {
  gsap.utils.toArray('body').forEach((elem) => {
      let lines = elem.querySelectorAll('.main_image_container');

      lines.forEach((line) => {
          let Timeline = gsap.timeline({
              ease: "slowMo.ease",
              scrollTrigger: {
                  trigger: line,
                  start: "top -0svh",
                  end: "bottom -600svh",
                  scrub: true,
                  // markers: true,
                  // toggleActions: "restart none none reverse",
              }
          });

          Timeline.to(line, { y: -300 });
      });
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


