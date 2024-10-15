

  

  document.addEventListener('DOMContentLoaded', function() {
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
  











