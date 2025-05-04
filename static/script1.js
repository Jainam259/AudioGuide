document.addEventListener("DOMContentLoaded", function () {
  let currentIndex = 0;
  const images = document.querySelectorAll(".slider img");
  const totalImages = images.length;

  function showNextImage() {
      images[currentIndex].classList.remove("active");
      currentIndex = (currentIndex + 1) % totalImages;
      images[currentIndex].classList.add("active");
  }

  // Initialize the slider
  images[currentIndex].classList.add("active");

  // Change image every 3 seconds
  setInterval(showNextImage, 3000);
});
