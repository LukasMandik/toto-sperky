document.addEventListener('DOMContentLoaded', function() {
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
  document.addEventListener("DOMContentLoaded", function() {
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

  document.addEventListener("DOMContentLoaded", function() {
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

  document.addEventListener("DOMContentLoaded", function() {
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

  document.addEventListener("DOMContentLoaded", function() {
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