$(document).ready(function() {

let hamburger = document.querySelector(".hamburger");
let menu = document.querySelector(".menu");

	hamburger.addEventListener("click", function(){
		menu.classList.toggle("active");
	})

})



$(document).ready(function() {

        $(document).ready(function() {
            let hamburger = document.querySelector(".hamburger");
            let toggle = document.querySelector("#toggle");

            hamburger.addEventListener("click", function() {
                toggle.classList.toggle("active");
                if (toggle.classList.contains("active")) {
                    document.body.style.overflow = 'hidden';
                    document.body.style.position = 'fixed';
                    document.body.style.width = '100%';
                } else {
                    document.body.style.overflow = '';
                    document.body.style.position = '';
                    document.body.style.width = '';
                }
            });
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
    gsap.utils.toArray('.second_home_container').forEach((elem) => {
        let lines = elem.querySelectorAll('.background_wrapper');
  
        lines.forEach((line) => {
            let Timeline = gsap.timeline({
                ease: "slowMo.ease",
                scrollTrigger: {
                    trigger: line,
                    start: "top 100svh",
                    end: "bottom 50svh",
                    scrub: true,
                    // markers: true,
                    // toggleActions: "restart none none reverse",
                }
            });
  
            Timeline.from(line, { backgroundPositionX: "200", rotation:"120deg"});
        });
    });
  });

  // $(document).ready(function() {
  // // Inicializuj ScrollTrigger
  // gsap.registerPlugin(ScrollTrigger);

  // // Vytvor animáciu s ScrollTrigger
  // gsap.to('.logo_dot', {
  //   rotation: "-=360_cw",
  //   transformOrigin: "7220px 2000px",
  //   duration: 3,
  //   ease: 'power2.inOut',
  //   repeat: 100000,
  //   scrollTrigger: {
  //     trigger: '.starterdot', // Bod, kde sa spustí animácia
  //     start: 'top 580svh',     // Začiatok triggeru (keď je 80% prvku v zornom poli)
  //     end: 'bottom 190svh',    // Koniec triggeru
  //     scrub: 1,             // Skrúbovací efekt pri posúvaní
  //     toggleActions: 'play none none none', // Akcie pri spustení
  //     markers: true,
  //   },
  // });

  // });





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
  
    gsap.utils.toArray('.logo_svg_container_footer').forEach((elem) => {
      // Predpokladáme, že každý prvok má niečo ako čiaru alebo iný element na animovanie
      let line = elem.querySelectorAll('.logo_dot'); // Prvok, ktorý budeme animovať
  
      // Vytvoríme GSAP časovú os
      let timeline = gsap.timeline({
        ease: "bounce",
        repeat: 100, // Opakovanie nekonečne
        yoyo: true, // Animácia sa opakuje opačným smerom
      });
  
      // Pridáme animáciu na Timeline
      timeline
        .from(line[0], { rotation: "-=360_cw", transformOrigin: "7220px 2000px", duration: 260 }, 0)
        .from(line[1], { rotation: "-=360_cw", transformOrigin: "7620px 2000px", duration: 527 }, 0)
        .from(line[2], { rotation: "-=360_cw", transformOrigin: "-5370px -4250px", duration: 211 }, 0)
        .from(line[3], { rotation: "-=360_cw", transformOrigin: "4020px 6220px", duration: 220}, 0);
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
  
    gsap.utils.toArray('.line_center_detail_product').forEach((elem) => {
      let line = elem.querySelector('.line');
      let lineLength = line.getTotalLength();
  

      line.style.strokeDasharray = lineLength;
      line.style.strokeDashoffset = lineLength; 

      let Timeline = gsap.timeline({
        scrollTrigger: {
          trigger: elem,
          easy:"linear",
          start: "top 700svh",
          end: "bottom 700svh",
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
        let lines = elem.querySelectorAll('.text_home_about_jewelry p.first_text, .text_home_about_jewelry p.last_text');
  
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


//   $(document).ready(function() {
//     gsap.utils.toArray('.gallery_container .container').forEach((elem) => {
//         let lines = elem.querySelectorAll('.box a');
  
//         let Timeline = gsap.timeline({
//             scrollTrigger: {
//                 trigger: elem,
//                 start: "center 100svh",
//                 end: "center 100svh",
//                 scrub: false,
//                 toggleActions: "restart none none reverse",
//                 markers: true,
//             }
//         });
  
//         lines.forEach((line) => {
//             Timeline.to(line, { className: '+=hover' }, 0.5); // pridanie triedy 'hover'
//         });
//     });
// });


  
// $(document).ready(function() {
//   // Funkcia na detekciu šírky obrazovky
//   function isMobileScreen() {
//       return window.matchMedia("(max-width: 768px)").matches;
//   }

//   if (isMobileScreen()) {
//       let links = gsap.utils.toArray('.box');

//       links.forEach((link) => {
//           link.addEventListener('click', function(event) {
//               if (!link.classList.contains('hover')) {
//                   event.preventDefault(); // Zabraňuje predvolenému správaniu (navigácia)
//                   links.forEach(l => l.classList.remove('hover')); // Odstráni 'hover' z ostatných prvkov
//                   link.classList.add('hover'); // Pridá triedu 'hover'
//               } else {
//                   link.classList.remove('hover'); // Odstráni triedu 'hover' pri druhom kliknutí
//               }
//           });
//       });

//       window.addEventListener('scroll', function() {
//           links.forEach((link) => {
//               link.classList.remove('hover'); // Odstráni triedu 'hover' pri skrolovaní
//           });
//       });
//   }
// });



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
  $(document).ready(function() {

    gsap.set(".box2", {
      x: (i) => i * 155
    });
    
    
    gsap.to(".box2", {
      duration: 40,
      ease: "linear",
      x: "+=775", //move each box 500px to right
      modifiers: {
        x: gsap.utils.unitize(x => parseFloat(x) % 775) //force x value to be between 0 and 500 using modulus
      },
      repeat: -1
    });
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
$(document).on("click", ".hamburger", function() {
  if ($(".menu").hasClass("active")) {
  const Container = document.querySelectorAll('.switch-box');
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
  gsap.utils.toArray('.container_home').forEach((elem) => {
      let lines = elem.querySelectorAll('.container_home .box_home');

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

          Timeline.from(line, { opacity: 0, y: 20 });
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


// $(document).ready(function() {
//   gsap.utils.toArray('.starter').forEach((elem) => {
//       let lines = elem.querySelectorAll('.main_image_container img');

//       lines.forEach((line) => {
//           let Timeline = gsap.timeline({
//               ease: "ease.inOut",
//               scrollTrigger: {
//                   trigger: line,
//                   start: "top 50svh",
//                   end: "bottom -500svh",
//                   scrub: true,
//                   // markers: true,
//                   // toggleActions: "restart none none reverse",
//               }
//           });

//           // Timeline.to(line, {width: 270, y: 350 , rotate: -3},0,0)
//           // Timeline.to(line, {  });
//           Timeline.to(line, { width: 330, y: 380})
//           // Timeline.to(line, {  });
//       });
//   });
// });






    
  

      

      

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

// document.addEventListener('DOMContentLoaded', function() {
//   if ('ontouchstart' in window || navigator.maxTouchPoints) {
//       document.querySelectorAll('.container .box').forEach(function(box) {
//           box.classList.remove('hover');
//       });
//   }
// });