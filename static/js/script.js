let hamburger = document.querySelector(".hamburger");
let menu = document.querySelector(".menu");

	hamburger.addEventListener("click", function(){
		menu.classList.toggle("active");
	})





$(document).ready(function() {
  gsap.registerPlugin(ScrollTrigger);


  gsap.to(".main_navbar", {
    y: -100,
    // backgroundColor: "rgba(5, 8, 6, 0.95)",
    duration: 0.7,
    ease: "power2.out",
    scrollTrigger: {
      trigger: ".endpoint",
      start: "top 180svh ",
      end: "center -80svh",
      // toggleClass: "black",
      scrub: false,
      // markers: true,
      // pin: true,
      toggleActions: "restart none none reverse",
    }
  })
})



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




// $(document).ready(function() {
//   gsap.registerPlugin(ScrollTrigger);
//   const title = ".sluzby_container .title_home_container h2";
  

//   gsap.from(title,{
//       duration: 2,
//       x:100,
//       stagger: 0.25,
//       opacity: 0,
//       ease: "power2.out",
//       scrollTrigger: {
//         trigger: title,
//         end: "center 500svh",
//         start: "center 700svh",
//         // markers: true,
//         scrub: false,
//         toggleActions: "restart none none reverse",
//         // play pause resume reverse restart reset complete
//     }
// })  
// })

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
      let lines = elem.querySelectorAll('.container .box');

      lines.forEach((line) => {
          let Timeline = gsap.timeline({
              ease: "elastic",
              scrollTrigger: {
                  trigger: line,
                  start: "top 550svh",
                  end: "bottom 600svh",
                  scrub: true,
                  // markers: true,
                  // toggleActions: "restart none none reverse",
              }
          });

          Timeline.to(line, { opacity: 1, y: 0 });
      });
  });
});





$(document).ready(function() {

    var scroll = new SmoothScroll('a[href*="#"]', {
      speed: 800, // nastavte rychlost scrollování podle potřeby
      easing: 'easeInOutCubic',
    });

  });

    
  

      

      