function imagesLoaded() {
  const images = document.getElementsByTagName("img");
  for (const img of images) {
    if (!img.complete) {
      return false;
    }
  }
  return true;
}

function hideLoadingScreen() {
  const loadingScreen = document.getElementById("loading-screen");
  if (imagesLoaded()) {
    // loadingScreen.style.opacity = "0";
    setTimeout(function () {
      loadingScreen.style.display = "none";
    }, 500);
  } else {
    setTimeout(hideLoadingScreen, 100);
  }
}

window.addEventListener("load", function () {
  hideLoadingScreen();
});





window.addEventListener("load", function () {
const loadingScreen = document.getElementById("loading-screen");
// loadingScreen.style.opacity = "0";
setTimeout(function () {
loadingScreen.style.display = "none";
}, 1000);
});