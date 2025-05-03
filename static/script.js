// This script can be used for dynamic menu item highlighting or adding interactivity.
document.querySelectorAll('.menu-item').forEach(item => {
  item.addEventListener('click', () => {
    document.querySelector('.menu-item.active').classList.remove('active');
    item.classList.add('active');
  });
});

document.addEventListener("DOMContentLoaded", function () {
  let images = [
      "/static/images/main-slider/kirti-mandir.jpg",
      "/static/images/main-slider/India.jpg",
      "/static/images/main-slider/carousel-2.jpg",
      "/static/images/main-slider/Sun-Temple-Banner.jpg",
      "/static/images/main-slider/Dwarkadhish Temple30.jpg",
      "/static/images/main-slider/Dwarkadhish-Temple-1.jpg",
      "/static/images/main-slider/carousel-1.jpg",
      "/static/images/main-slider/pavagadhtemplefrontview.jpg",
      "/static/images/main-slider/1.jpg"
  ];

  let index = 0;
  let imgElement = document.getElementById("slideshow");

  setInterval(function () {
      index = (index + 1) % images.length;
      imgElement.style.transform = "scale(1.1)"; // Zoom-in effect
      setTimeout(() => {
          imgElement.src = images[index];
      }, 500);
  }, 3000);
});

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
  thumbnail.style.display = 'none';
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


const feedbacks = [
  {
      name: "Patel Dhyan",
      role: "Backend Designer",
      img: "profile1.jpg",
      feedback: "I really had my doubts at first. I asked for a quote online, and the next day I was contacted by a sales representative. The quote came out high, so the salesman did a good job to find me a good deal."
  },
  {
      name: "Sara Johnson",
      role: "Marketing Manager",
      img: "profile2.jpg",
      feedback: "The service was exceptional. The process was smooth, and the support team guided me through every step. Highly recommended!"
  },
  {
      name: "Mark Smith",
      role: "Product Designer",
      img: "profile3.jpg",
      feedback: "Fantastic experience! The team was professional, and I got exactly what I was looking for. Will definitely work with them again."
  }
];

let index = 0;

document.querySelector(".next-btn").addEventListener("click", () => {
  index = (index + 1) % feedbacks.length; // Go to the next feedback (loop back to first after last)
  updateFeedback();
});

document.querySelector(".prev-btn").addEventListener("click", () => {
  index = (index - 1 + feedbacks.length) % feedbacks.length; // Go to previous feedback (loop back to last after first)
  updateFeedback();
});

function updateFeedback() {
  const clientImg = document.getElementById("client-img");
  const clientName = document.getElementById("client-name");
  const clientRole = document.getElementById("client-role");
  const clientFeedback = document.getElementById("client-feedback");

  clientImg.src = feedbacks[index].img;
  clientName.textContent = feedbacks[index].name;
  clientRole.textContent = feedbacks[index].role;
  clientFeedback.textContent = feedbacks[index].feedback;
}