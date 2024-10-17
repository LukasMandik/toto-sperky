document.addEventListener('DOMContentLoaded', function() {
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
  
  

  document.addEventListener('DOMContentLoaded', function() {
    gsap.registerPlugin(ScrollTrigger);
  
    gsap.utils.toArray('.line_center').forEach((elem) => {
      let line = elem.querySelector('.line');
      let lineLength = line.getTotalLength();
  
      line.style.strokeDasharray = lineLength;
      line.style.strokeDashoffset = lineLength; 

      let Timeline = gsap.timeline({
        scrollTrigger: {
          trigger: elem,
          easy: "linear",
          start: "top 500svh",
          end: "bottom 300svh",
          scrub: true,
          // markers: true,
          // toggleActions: "restart none none reverse",  
        }
      });
      Timeline.to(line, { strokeDashoffset: 0 });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
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
      Timeline.to(line, { strokeDashoffset: 0 });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    gsap.registerPlugin(ScrollTrigger);
  
    gsap.utils.toArray('.line_center_short').forEach((elem) => {
      let line = elem.querySelector('.line');
      let lineLength = line.getTotalLength();
  
      line.style.strokeDasharray = lineLength;
      line.style.strokeDashoffset = lineLength; 
  
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
  
      Timeline.to(line, { strokeDashoffset: 0 });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
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

  document.addEventListener('DOMContentLoaded', function() {
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

  document.addEventListener('DOMContentLoaded', function() {
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

  document.addEventListener('DOMContentLoaded', function() {
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

  document.addEventListener('DOMContentLoaded', function() {
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

document.addEventListener("DOMContentLoaded", function() {
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
  
  
document.addEventListener("DOMContentLoaded", function() {
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

document.addEventListener("DOMContentLoaded", function() {
    gsap.utils.toArray('.third_home_container').forEach((elem) => {
        let lines = elem.querySelectorAll('.carusel');
  
        let Timeline = gsap.timeline({
          scrollTrigger: {
              trigger: elem,
              start: "center 790svh",
              end: "center 790svh",
              scrub: false,
              toggleActions: "restart none none reverse",
            //   markers: true,
          }
      });
  
      lines.forEach((line) => {
        Timeline.from(line, { opacity: 0, y: 20,scale: 0.9,duration: 0.35});
      });
    });
  });  

document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.querySelector('.carusel');
  const images = carousel.querySelectorAll('.carusel a .carousel_items');

  function updateImageScales() {
      const carouselRect = carousel.getBoundingClientRect();
      const carouselCenter = carouselRect.left + carouselRect.width / 2;
      const tolerance = carouselRect.width * 0.1; // 10% tolerance

      images.forEach(img => {
          const imgRect = img.getBoundingClientRect();
          const imgCenter = imgRect.left + imgRect.width / 2;
          const distanceFromCenter = Math.abs(carouselCenter - imgCenter);
          const maxDistance = (carouselRect.width / 2) - tolerance;

          let scale;
          if (distanceFromCenter < tolerance) {
              scale = 1.17;
          } else {
              scale = 1.17 - ((distanceFromCenter - tolerance) / maxDistance * 0.1);
              scale = Math.max(scale, 1); // Ensure the scale doesn't go below 1
          }

          img.style.transform = `scale(${scale})`;
      });
  }

  carousel.addEventListener('scroll', updateImageScales);
  window.addEventListener('resize', updateImageScales);

  updateImageScales(); // Initial call to set the scales
});