console.log("JS CARGADO");

// =========================
// MENU RESPONSIVE
// =========================
function toggleMenu() {

    const navLinks = document.getElementById("navLinks");
    const toggleBtn = document.querySelector(".nav-toggle");

    if(navLinks){
        const isOpen = navLinks.classList.toggle("active");
        if(toggleBtn){
            toggleBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
            toggleBtn.textContent = isOpen ? "✕" : "☰";
        }
    }
}

// Cierra el menú móvil al tocar un link, o al tocar fuera del menú
document.addEventListener("DOMContentLoaded", function(){

    const navLinks = document.getElementById("navLinks");
    const toggleBtn = document.querySelector(".nav-toggle");

    if(!navLinks) return;

    navLinks.querySelectorAll("a").forEach(function(link){
        link.addEventListener("click", function(){
            navLinks.classList.remove("active");
            if(toggleBtn){
                toggleBtn.setAttribute("aria-expanded", "false");
                toggleBtn.textContent = "☰";
            }
        });
    });

    document.addEventListener("click", function(e){
        if(!navLinks.classList.contains("active")) return;
        const clickedInsideMenu = navLinks.contains(e.target);
        const clickedToggle = toggleBtn && toggleBtn.contains(e.target);
        if(!clickedInsideMenu && !clickedToggle){
            navLinks.classList.remove("active");
            if(toggleBtn){
                toggleBtn.setAttribute("aria-expanded", "false");
                toggleBtn.textContent = "☰";
            }
        }
    });

    document.addEventListener("keydown", function(e){
        if(e.key === "Escape" && navLinks.classList.contains("active")){
            navLinks.classList.remove("active");
            if(toggleBtn){
                toggleBtn.setAttribute("aria-expanded", "false");
                toggleBtn.textContent = "☰";
            }
        }
    });

});

// =========================
// HERO SLIDER
// =========================
const slides = document.querySelectorAll(".slide");

let currentSlide = 0;

function showSlide(index){

    if(!slides.length) return;

    slides.forEach(slide=>{
        slide.classList.remove("active");
    });

    slides[index].classList.add("active");

    console.log("Mostrando slide:", index + 1);
}

function nextSlide(){

    currentSlide++;

    if(currentSlide >= slides.length){
        currentSlide = 0;
    }

    showSlide(currentSlide);
}

function prevSlide(){

    currentSlide--;

    if(currentSlide < 0){
        currentSlide = slides.length - 1;
    }

    showSlide(currentSlide);
}

// GLOBALES
window.nextSlide = nextSlide;
window.prevSlide = prevSlide;

// AUTO HERO
if(slides.length > 0){

    showSlide(currentSlide);

    setInterval(()=>{
        nextSlide();
    },4000);
}

// =========================
// FILOSOFÍA SLIDER
// =========================
const filoSlides = document.querySelectorAll(".filo-slide");

let filoIndex = 0;

function showFilo(index){

    if(!filoSlides.length) return;

    filoSlides.forEach(slide=>{
        slide.classList.remove("active");
    });

    filoSlides[index].classList.add("active");

    console.log("Filosofía:", index + 1);
}

function nextFilo(){

    filoIndex++;

    if(filoIndex >= filoSlides.length){
        filoIndex = 0;
    }

    showFilo(filoIndex);
}

function prevFilo(){

    filoIndex--;

    if(filoIndex < 0){
        filoIndex = filoSlides.length - 1;
    }

    showFilo(filoIndex);
}

// GLOBALES
window.nextFilo = nextFilo;
window.prevFilo = prevFilo;

// =========================
// EQUIPOS DE ENTRENAMIENTO SLIDER
// =========================
const entrenoSlides = document.querySelectorAll(".entreno-slide");

let entrenoIndex = 0;

function showEntreno(index){

    if(!entrenoSlides.length) return;

    entrenoSlides.forEach(slide=>{
        slide.classList.remove("active");
    });

    entrenoSlides[index].classList.add("active");

    console.log("Equipos de entrenamiento:", index + 1);
}

function nextEntreno(){

    entrenoIndex++;

    if(entrenoIndex >= entrenoSlides.length){
        entrenoIndex = 0;
    }

    showEntreno(entrenoIndex);
}

function prevEntreno(){

    entrenoIndex--;

    if(entrenoIndex < 0){
        entrenoIndex = entrenoSlides.length - 1;
    }

    showEntreno(entrenoIndex);
}

// GLOBALES
window.nextEntreno = nextEntreno;
window.prevEntreno = prevEntreno;
