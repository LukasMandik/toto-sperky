$(document).ready(function() {

    let hamburger = document.querySelector(".hamburger");
    let menu = document.querySelector(".menu");

    hamburger.addEventListener("click", function(){
        menu.classList.toggle("active");
        console.log("Hamburger menu bolo kliknuté");
    });

});

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




$(document).ready(function() {
    var bodyWrapper = document.querySelector('.footer_hide_element');
    
        bodyWrapper.style.clipPath = 'ellipse(69% 100% at center 0)';
        // bodyWrapper.style.webkitClipPath = 'ellipse(350% 100% at 50% 0%)';
    
    });
