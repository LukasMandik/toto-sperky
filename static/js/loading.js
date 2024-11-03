function mediaLoaded() {
    const images = document.getElementsByTagName("img");
    const videos = document.getElementsByTagName("video");

    for (const img of images) {
      if (!img.complete) {
        return false;
      }
    }

    for (const video of videos) {
      if (video.readyState < 4) { // HAVE_ENOUGH_DATA
        return false;
      }
    }

    return true;
}

function hideLoadingScreen() {
    const loadingScreen = document.getElementById("loading-screen");
    if (mediaLoaded()) {
      // loadingScreen.style.opacity = "0";
      setTimeout(function () {
        loadingScreen.style.display = "none";
      }, 50);
    } else {
      setTimeout(hideLoadingScreen, 10);
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
    }, 10);
});
