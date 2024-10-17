

window.addEventListener('load', function() {
  
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

window.addEventListener('load', function() {
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
window.addEventListener('load', function() {
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
  











