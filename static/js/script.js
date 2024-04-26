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
  
    hamburger.addEventListener("click", function(){
      toggle.classList.toggle("active");
    })
  
  })



  $(document).ready(function() {
    // Check if screen width is greater than 748px using media query
    if (window.matchMedia('(min-width: 768px)').matches) {
      gsap.registerPlugin(ScrollTrigger);
  
      gsap.to(".main_navbar", {
        // height: 100,
        backgroundColor: "rgba(251, 251, 251, 1)",
        duration: 0.4,
        ease: "power2.out",
        scrollTrigger: {
          trigger: ".endpoint",
          start: "center 390svh ",
          end: "center 390svh",
          // toggleClass: "black",
          scrub: false,
          // markers: true,
          // pin: true,
          toggleActions: "restart none none reset ",
          // play pause resume reverse restart reset complete
        }
      });
    }
  });
  
  // $(document).ready(function() {


  //     gsap.utils.toArray('.startermenu').forEach((elem) => {
  //         let lines = elem.querySelectorAll('.main_navbar .menu ul li a');
    
  //         let Timeline = gsap.timeline({
  //           scrollTrigger: {
  //               trigger: elem,
  //               start: "botton 600svh",
  //               end: "top 600svh",
  //               scrub: false,
  //               toggleActions: "restart none none reverse",
  //               markers: true,
  //           }
  //         });
      
  //         lines.forEach((line) => {
  //           Timeline.to(line, { x: 40,duration: 0.35 });
  //         });
  //       });
    
  // });



  
  // $(document).on("click", ".hamburger", function() {
  //   if ($(".menu").hasClass("active")) {
  //     gsap.utils.toArray('.startermenu').forEach((elem) => {
  //       let lines = elem.querySelectorAll('.main_navbar .menu ul li');
     
  //       let Timeline = gsap.timeline({
  //         scrollTrigger: {
  //           trigger: elem,
  //           start: "botton 600svh",
  //           end: "top 600svh",
  //           scrub: false,
  //           toggleActions: "play none none reverse",
  //           // markers: true,
  //         }
  //       });
  //         Timeline.from(lines, { x: 40, stagger: 0.05});
  //       });
  //   }
  // });
    
  // $(document).on("click", ".hamburger", function() {
  //   if ($(".menu").hasClass("active")) {
  //     gsap.utils.toArray('.startermenu').forEach((elem) => {
  //       let lines = elem.querySelectorAll('.main_navbar .menu ul li');
     
  //       let Timeline = gsap.timeline({
  //         scrollTrigger: {
  //           trigger: elem,
  //           start: "botton 600svh",
  //           end: "top 600svh",
  //           scrub: false,
  //           toggleActions: "play none none reverse",
  //           // markers: true,
  //         }
  //       });
  //         Timeline.from(lines, { x: 40, stagger: 0.05});
  //       });
  //   }
  // });
  


  $(document).on("click", ".hamburger", function() {
    if ($(".menu").hasClass("active")) {
    const Container = document.querySelectorAll('.main_navbar .menu ul li');
  
  // Create an animation loop using GSAP
  gsap.from(Container, {
    x: -340,
    opacity: 0, 
    // y: 2,
    // rotate: 1,
    stagger: 0.03,  
    duration: 1, 
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
  delay: 0.5, 
  opacity: 0, 
  // y: 2,
  // rotate: 1,
  stagger: 0.03,  
  duration: 0.8, 
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
  const svgContainer = document.querySelector('.svg_container');

// Create an animation loop using GSAP
gsap.to(svgContainer, {
  x: 10, // Move horizontally by 10 pixels
  // y: 2,
  // rotate: 1,  
  duration: 2, // Animation duration in seconds
  repeat: -1, // Repeat indefinitely
  yoyo: true, // Reverse the animation direction back and forth
  ease: 'power2.inOut' // Smooth easing function
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
                  scrub: false,
                  // markers: true,
                  toggleActions: "restart none none reverse",
              }
          });

          Timeline.to(line, { opacity: 1, y: 0 });
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

          Timeline.to(line, { backgroundPosition: "47% 60%" });
      });
  });
});


$(document).ready(function() {
  gsap.utils.toArray('.starter').forEach((elem) => {
      let lines = elem.querySelectorAll('.main_image_container img');

      lines.forEach((line) => {
          let Timeline = gsap.timeline({
              ease: "ease.inOut",
              scrollTrigger: {
                  trigger: line,
                  start: "top 50svh",
                  end: "bottom -500svh",
                  scrub: true,
                  // markers: true,
                  // toggleActions: "restart none none reverse",
              }
          });

          // Timeline.to(line, {width: 270, y: 350 , rotate: -3},0,0)
          // Timeline.to(line, {  });
          Timeline.to(line, { width: 330, y: 380})
          // Timeline.to(line, {  });
      });
  });
});





$(document).ready(function() {

    var scroll = new SmoothScroll('a[href*="#"]', {
      speed: 800, // nastavte rychlost scrollování podle potřeby
      easing: 'easeInOutCubic',
    });

  });

    
  

      

      