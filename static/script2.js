// document.addEventListener("DOMContentLoaded", function () {
//   var swiper = new Swiper(".swiper-container", {
//       slidesPerView: 3,  // Show 3 slides at once
//       spaceBetween: 30,
//       loop: true,
//       navigation: {
//           nextEl: ".swiper-button-next",
//           prevEl: ".swiper-button-prev",
//       },
//       breakpoints: {
//           1024: { slidesPerView: 3 }, // Desktop
//           768: { slidesPerView: 2 },  // Tableta
//           480: { slidesPerView: 1 }   // Mobile
//     }
//   });
// });
document.addEventListener("DOMContentLoaded", function () {
  var swiper = new Swiper(".swiper-container", {
      slidesPerView: 3,  // Show 3 slides at once
      spaceBetween: 30,
      loop: true,
      navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
      },
      breakpoints: {
          1024: { slidesPerView: 3 }, // Desktop
          768: { slidesPerView: 2 },  // Tablet
          480: { slidesPerView: 1 }   // Mobile
 }
});
});

function playVideo() {
    const video = document.getElementById('culture-video');
    const thumbnail = document.querySelector('.video-thumbnail');
    const cancelButton = document.querySelector('.cancel-button');
  
    // Set the correct YouTube embed URL with autoplay
    video.src = "https://www.youtube.com/embed/MNvUFMv1O9U?autoplay=1";
  
    // Show the video and cancel button
    video.style.display = 'block';
    cancelButton.style.display = 'block';
  
    // Hide the thumbnail
    thumbnail.style.display='none';
  }
function cancelVideo() {
    const video = document.getElementById('culture-video');
    const thumbnail = document.querySelector('.video-thumbnail');
    const cancelButton = document.querySelector('.cancel-button');
  
    // Hide the video and cancel button
    video.style.display = 'none';
    cancelButton.style.display = 'none';
  
    // Show the thumbnail
    thumbnail.style.display = 'inline-block';
  
    // Stop the video by removing the src
    video.src = "";
  }