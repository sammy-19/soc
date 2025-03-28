
document.addEventListener("DOMContentLoaded", function() {

    const navbarToggler = document.querySelector('.navbar-toggler');
    const mainNav = document.querySelector('#main-nav');

    if (navbarToggler && mainNav) {
        navbarToggler.addEventListener('click', function() {
            // Toggle the .is-active class on the nav menu
            mainNav.classList.toggle('is-active');

            // Toggle aria-expanded attribute for accessibility
            const isExpanded = mainNav.classList.contains('is-active');
            navbarToggler.setAttribute('aria-expanded', isExpanded);

            // Optional: Change icon on toggle (e.g., bars to times)
            const icon = navbarToggler.querySelector('i');
            if (icon) {
                if (isExpanded) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times'); // Font Awesome close icon
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });

        // Optional: Close dropdown if clicking outside of it
        document.addEventListener('click', function(event) {
            const isClickInsideNav = mainNav.contains(event.target);
            const isClickOnToggler = navbarToggler.contains(event.target);

            if (!isClickInsideNav && !isClickOnToggler && mainNav.classList.contains('is-active')) {
                mainNav.classList.remove('is-active');
                navbarToggler.setAttribute('aria-expanded', 'false');
                 const icon = navbarToggler.querySelector('i');
                 if (icon) {
                     icon.classList.remove('fa-times');
                     icon.classList.add('fa-bars');
                 }
            }
        });
    }


     // --- NEW: Volunteer Popup Logic ---
     const openPopupButton = document.getElementById('open-volunteer-popup');
     const closePopupButton = document.getElementById('close-volunteer-popup');
     const volunteerPopup = document.getElementById('volunteer-popup');
 
     if (openPopupButton && closePopupButton && volunteerPopup) {
         // Function to open the popup
         function openPopup() {
             volunteerPopup.classList.add('active');
             document.body.style.overflow = 'hidden'; // Prevent background scrolling
         }
 
         // Function to close the popup
         function closePopup() {
             volunteerPopup.classList.remove('active');
             document.body.style.overflow = ''; // Restore background scrolling
         }
 
         // Event listener for the open button
         openPopupButton.addEventListener('click', openPopup);
 
         // Event listener for the close button
         closePopupButton.addEventListener('click', closePopup);
 
         // Event listener to close popup when clicking outside the content area
         volunteerPopup.addEventListener('click', function(event) {
             // Check if the click target is the modal background itself
             if (event.target === volunteerPopup) {
                 closePopup();
             }
         });
 
          // Optional: Close popup on 'Escape' key press
         document.addEventListener('keydown', function(event) {
             if (event.key === 'Escape' && volunteerPopup.classList.contains('active')) {
                 closePopup();
             }
         });
     }
 
     // --- NEW: Optional: Basic Feedback Form Handling (Example) ---
     const feedbackForm = document.getElementById('feedback-form');
     if (feedbackForm) {
         feedbackForm.addEventListener('submit', function(event) {
             // You might want more sophisticated handling here,
             // perhaps using Fetch API to submit asynchronously
             // and show a success message without page reload.
             console.log('Feedback form submitted');
             // Example: Show a simple alert after submission (replace with better UX)
             // event.preventDefault(); // Uncomment this to stop default submission
             // alert('Thank you for your feedback!');
             // feedbackForm.reset(); // Optionally clear the form
         });
     }

      // --- NEW: Banner Slider Logic ---
    /*
    const slideDataElement = document.getElementById('slide-data');

    // Only run slider logic if the slide data script tag exists (i.e., on the homepage)
    if (slideDataElement) {
        const slides = JSON.parse(slideDataElement.textContent);
        const bannerSection = document.querySelector('.banner'); // The section with the background
        const bannerTitle = document.getElementById('banner-title');
        const bannerText = document.getElementById('banner-text');
        const bannerButton = document.getElementById('banner-button');
        const prevButton = document.getElementById('prev');
        const nextButton = document.getElementById('next');

        let currentSlideIndex = 0;
        let slideInterval;

        function showSlide(index) {
            if (!slides || slides.length === 0 || !bannerSection) return;

            // Ensure index is within bounds
            currentSlideIndex = (index + slides.length) % slides.length;

            const slide = slides[currentSlideIndex];

            // --- Fade Out Content (Optional but smoother) ---
            if (bannerTitle) bannerTitle.style.opacity = 0;
            if (bannerText) bannerText.style.opacity = 0;
            if (bannerButton) bannerButton.style.opacity = 0;
             // --- Update Background ---
            // Add transition effect via CSS on .banner
            bannerSection.style.backgroundImage = `url(${slide.image_url})`;


            // --- Update Content (after a short delay for fade out) ---
            setTimeout(() => {
                if (bannerTitle) {
                     bannerTitle.textContent = slide.title;
                     bannerTitle.style.opacity = 1; // Fade In
                }
                if (bannerText) {
                    // Use innerHTML if your text includes line breaks (<br>)
                    bannerText.innerHTML = slide.text; // Use innerHTML to render <br> from linebreaksbr
                    bannerText.style.opacity = 1; // Fade In
                }
                if (bannerButton) {
                    bannerButton.textContent = slide.button_text || "Donate Now"; // Default text
                    bannerButton.href = slide.button_link || "#"; // Default link
                    bannerButton.style.display = slide.button_text ? 'inline-block' : 'none'; // Hide if no text
                    bannerButton.style.opacity = 1; // Fade In
                }
            }, 250); // Adjust delay ms (should be less than CSS transition time)
        }

        function nextSlide() {
            showSlide(currentSlideIndex + 1);
        }

        function prevSlide() {
            showSlide(currentSlideIndex - 1);
        }

        function startSliderInterval() {
            // Clear existing interval before starting a new one
            clearInterval(slideInterval);
            if (slides && slides.length > 1) { // Only interval if more than one slide
                 slideInterval = setInterval(nextSlide, 5000); // 5 seconds
            }
        }

        // --- Initialize Slider ---
        if (slides && slides.length > 0) {
            showSlide(0); // Show the first slide initially
            startSliderInterval(); // Start automatic sliding

            // --- Event Listeners ---
            if (nextButton) {
                nextButton.addEventListener('click', () => {
                    nextSlide();
                    startSliderInterval(); // Restart interval on manual navigation
                });
            }
            if (prevButton) {
                prevButton.addEventListener('click', () => {
                    prevSlide();
                    startSliderInterval(); // Restart interval on manual navigation
                });
            }
        } else {
            // Hide controls if no slides or only one slide
             if (prevButton) prevButton.style.display = 'none';
             if (nextButton) nextButton.style.display = 'none';
        }
    } */
 
     // ---  Basic Volunteer Form Handling (Example) ---
      const volunteerForm = document.getElementById('volunteer-form');
      if (volunteerForm) {
          volunteerForm.addEventListener('submit', function(event) {
              console.log('Volunteer form submitted');
              // Similar to feedback form, consider AJAX submission.
              // event.preventDefault(); // Uncomment to stop default submission
              // alert('Thank you for your application! We will be in touch.');
              // volunteerForm.reset(); // Optionally clear form
              // closePopup(); // Optionally close popup after submission
          });
      }

      // --- Donation Info Popup Logic ---
    const donatePopupTriggers = document.querySelectorAll('.trigger-donate-popup'); // Get all trigger buttons
    const donatePopup = document.getElementById('donate-info-popup');
    const closeDonatePopupButton = document.getElementById('close-donate-popup');
    const donateOverlay = document.getElementById('cm-overlay'); // Reuse overlay if desired, or create a specific one

    function openDonatePopup() {
        if (donatePopup && donateOverlay) {
            donatePopup.classList.add('active');
            donateOverlay.classList.add('active'); // Show overlay
            document.body.style.overflow = 'hidden';
        }
    }

    function closeDonatePopup() {
         if (donatePopup && donateOverlay) {
            donatePopup.classList.remove('active');
            donateOverlay.classList.remove('active'); // Hide overlay
            document.body.style.overflow = '';
        }
    }

    // Add listeners to all trigger buttons
    if (donatePopupTriggers.length > 0 && donatePopup) {
        donatePopupTriggers.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault(); // Prevent default link behavior
                openDonatePopup();
            });
        });

        // Listener for the close button inside the popup
        if (closeDonatePopupButton) {
            closeDonatePopupButton.addEventListener('click', closeDonatePopup);
        }

        // Listener for the overlay (if reusing the main overlay)
        if (donateOverlay) {
            donateOverlay.addEventListener('click', function(event) {
                // Only close if the donate popup is the one active
                // (Add more robust checks if multiple popups can interfere)
                if(donatePopup.classList.contains('active')) {
                    closeDonatePopup();
                }
            });
        }

         // Optional: Close on 'Escape' key press
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && donatePopup.classList.contains('active')) {
                closeDonatePopup();
            }
        });
    }

    // Get all the navigation links and the content sections
    const navLinks = document.querySelectorAll(".flex-wrapper h3");
    const sections = document.querySelectorAll(".statement");

    // Hide all sections except the first one (page1) on page load
    sections.forEach((section, index) => {
        if (index !== 0) {
            section.style.display = "none";
        }
    });

    // Add click event listeners to the nav links
    navLinks.forEach((link, index) => {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default link behavior

            // Remove 'active' class from all links
            navLinks.forEach(link => link.classList.remove("active"));
            // Add 'active' class to the clicked link
            this.classList.add("active");

            navLinks.forEach(link => link.classList.add('inactive'));
            this.classList.remove('inactive');

            // Hide all sections
            sections.forEach(section => section.style.display = "none");
            // Show the corresponding section
            sections[index].style.display = "block";
        });
    });
});

