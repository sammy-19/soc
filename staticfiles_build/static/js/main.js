// static/js/main.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM fully loaded and parsed"); // Check if JS file is running

    // --- Element References (Define elements needed by multiple sections first) ---
    const mainNav = document.querySelector('#main-nav');
    const navbarToggler = document.querySelector('.navbar-toggler');

    const volunteerPopup = document.getElementById('volunteer-popup');
    const closeVolunteerPopupButton = document.getElementById('close-volunteer-popup');
    const openVolunteerPopupButton = document.getElementById('open-volunteer-popup');

    const donatePopup = document.getElementById('donate-info-popup');
    const closeDonatePopupButton = document.getElementById('close-donate-popup');
    const donatePopupTriggers = document.querySelectorAll('.trigger-donate-popup');

    const overlay = document.getElementById('cm-overlay'); // Shared overlay

    // --- Check if elements were found ---
    console.log("Volunteer Popup:", volunteerPopup); // Should not be null if HTML exists
    console.log("Donate Popup:", donatePopup); // Should not be null if HTML exists
    console.log("Overlay:", overlay); // Should not be null if HTML exists

    // --- Generic Popup Functions ---
    function openPopup(popupElement) {
        if (popupElement && overlay) {
            console.log("Opening popup:", popupElement.id); // Debug log
            popupElement.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        } else {
            console.error('Cannot open popup: Popup element or overlay not found.', popupElement, overlay);
        }
    }

    function closePopup(popupElement) {
        if (popupElement && overlay) {
            console.log("Closing popup:", popupElement.id); // Debug log
            popupElement.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        } else {
            console.error('Cannot close popup: Popup element or overlay not found.', popupElement, overlay);
        }
    }

    // --- Hamburger Menu ---
    if (navbarToggler && mainNav) {
        console.log("Attaching hamburger listener");
        navbarToggler.addEventListener('click', function() {
            mainNav.classList.toggle('is-active');
            const isExpanded = mainNav.classList.contains('is-active');
            navbarToggler.setAttribute('aria-expanded', isExpanded);
            const icon = navbarToggler.querySelector('i');
            if (icon) {
                icon.className = isExpanded ? 'fa fa-times' : 'fa fa-bars'; // Simpler toggle
            }
        });
        // Close nav if clicking outside (optional)
        document.addEventListener('click', function(event) {
            const isClickInsideNav = mainNav.contains(event.target);
            const isClickOnToggler = navbarToggler.contains(event.target);
            if (!isClickInsideNav && !isClickOnToggler && mainNav.classList.contains('is-active')) {
                mainNav.classList.remove('is-active');
                navbarToggler.setAttribute('aria-expanded', 'false');
                const icon = navbarToggler.querySelector('i');
                if (icon) { icon.className = 'fa fa-bars'; }
            }
        });
    } else {
        console.warn("Hamburger toggler or nav not found.");
    }

    // --- Volunteer Popup Listeners ---
    if (openVolunteerPopupButton && volunteerPopup) {
        console.log("Attaching volunteer open listener");
        openVolunteerPopupButton.addEventListener('click', () => openPopup(volunteerPopup));
    } else {
         console.warn("Volunteer open button or popup element not found.");
    }
    if (closeVolunteerPopupButton && volunteerPopup) {
         console.log("Attaching volunteer close listener");
        closeVolunteerPopupButton.addEventListener('click', () => closePopup(volunteerPopup));
    }

    // --- Direct Donation Popup Listeners ---
    if (donatePopupTriggers.length > 0 && donatePopup) {
         console.log(`Attaching ${donatePopupTriggers.length} direct donate listeners`);
        donatePopupTriggers.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                 console.log("Direct donate button clicked");
                openPopup(donatePopup);
            });
        });
    } else {
         console.warn("Donate trigger buttons or donate popup element not found.");
    }
    if (closeDonatePopupButton && donatePopup) {
        console.log("Attaching donate close listener");
        closeDonatePopupButton.addEventListener('click', () => closePopup(donatePopup));
    }

    // --- Shared Overlay Listener ---
    if (overlay) {
         console.log("Attaching overlay listener");
        overlay.addEventListener('click', () => {
            if (volunteerPopup && volunteerPopup.classList.contains('active')) {
                closePopup(volunteerPopup);
            }
            if (donatePopup && donatePopup.classList.contains('active')) {
                 closePopup(donatePopup);
            }
        });
    } else {
        console.warn("Overlay element not found.");
    }

     // --- Shared Escape Key Listener ---
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
             if (volunteerPopup && volunteerPopup.classList.contains('active')) {
                closePopup(volunteerPopup);
            }
            if (donatePopup && donatePopup.classList.contains('active')) {
                 closePopup(donatePopup);
            }
        }
    });

    // --- Feedback Form Handler (Example - Keep if needed) ---
    const feedbackForm = document.getElementById('feedback-form');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function(event) {
            console.log('Feedback form submitted (default action may occur)');
        });
    }

    // --- Volunteer Form Handler (Example - Keep if needed) ---
     const volunteerForm = document.getElementById('volunteer-form');
     if (volunteerForm) {
         volunteerForm.addEventListener('submit', function(event) {
             console.log('Volunteer form submitted (default action may occur)');
         });
     }

    // --- Banner Slider Logic ---
    const slideDataElement = document.getElementById('slide-data');
    console.log("Slide data element:", slideDataElement); // Check if the script tag is found

    if (slideDataElement) {
        let slides = [];
        try {
             slides = JSON.parse(slideDataElement.textContent);
             console.log("Parsed slides:", slides); // See the parsed data
        } catch(e) { console.error("Error parsing slide data:", e); }

        // Define Static Slides (Ensure static paths are correct)
        const staticSlides = [
             { title: "Become a Volunteer", text: "There are many ways to get involved, offering opportunities to use your unique talents, learn new skills, and meet like-minded people. Your contribution of time, no matter how small, helps us reach our goals and serve the community more effectively. Ready to lend a hand? Find out how you can become a volunteer today!", image_url: "/static/images/banners/volunteer.jpg", button_text: "I Want to Volunteer", button_link: "#", button_action: "volunteer" },
             { title: "Contact Us", text: "Have questions...?", image_url: "/static/images/banners/contact_banner.jpg", button_text: "Get In Touch", button_link: "/contact/", button_action: "link" }, // Use actual URL path
             { title: "Send Feedback", text: "Help us improve...", image_url: "/static/images/banners/feedback_banner.jpg", button_text: "Leave Feedback", button_link: "#feedback-form", button_action: "scroll" }
        ];
        console.log("Static slides defined:", staticSlides);

        // Combine slides
        slides = slides.concat(staticSlides);
        console.log("Total slides:", slides.length, slides);

        // Slider DOM Elements
        const bannerSection = document.querySelector('.banner');
        const bannerTitle = document.getElementById('banner-title');
        const bannerText = document.getElementById('banner-text');
        const bannerButton = document.getElementById('banner-button');
        const prevButton = document.getElementById('prev');
        const nextButton = document.getElementById('next');

        // Check if banner elements exist
        console.log("Banner Section:", bannerSection);
        console.log("Banner Title:", bannerTitle);
        console.log("Banner Text:", bannerText);
        console.log("Banner Button:", bannerButton);
        console.log("Prev Button:", prevButton);
        console.log("Next Button:", nextButton);


        let currentSlideIndex = 0;
        let slideInterval;

        // Functions (showSlide, nextSlide, prevSlide, startSliderInterval - Keep from previous response)
        function showSlide(index) {
             if (!slides || slides.length === 0 || !bannerSection || !bannerTitle || !bannerText || !bannerButton) {
                 console.error("Missing slide data or banner elements for slider showSlide.");
                 return;
             }
             currentSlideIndex = (index + slides.length) % slides.length;
             const slide = slides[currentSlideIndex];
             console.log("Showing slide", currentSlideIndex, slide); // Debug log

             bannerTitle.style.opacity = 0; bannerText.style.opacity = 0; bannerButton.style.opacity = 0;

             if (slide.image_url) {
                 bannerSection.style.backgroundImage = `url(${slide.image_url})`;
             } else {
                  bannerSection.style.backgroundImage = `url('/static/images/banners/default_banner.jpg')`; // Check default path
             }

             setTimeout(() => {
                 bannerTitle.textContent = slide.title || "";
                 bannerText.innerHTML = slide.text || "";
                 bannerButton.textContent = slide.button_text || "Learn More";
                 bannerButton.href = slide.button_link || "#";
                 bannerButton.dataset.action = slide.button_action || 'link';
                 bannerButton.style.display = slide.button_text ? 'inline-block' : 'none';
                 bannerTitle.style.opacity = 1; bannerText.style.opacity = 1; bannerButton.style.opacity = 1;
             }, 250);
         }
         function nextSlide() { showSlide(currentSlideIndex + 1); }
         function prevSlide() { showSlide(currentSlideIndex - 1); }
         function startSliderInterval() {
             clearInterval(slideInterval);
             if (slides.length > 1) { slideInterval = setInterval(nextSlide, 12000); } // Reset to 12 secs
         }


        // Event Listener for the Dynamic Banner Button
        if (bannerButton) {
            console.log("Attaching banner button listener");
            bannerButton.addEventListener('click', function(event) {
                const action = bannerButton.dataset.action;
                console.log("Banner button clicked! Action:", action); // Debug log

                if (action === 'Open Donate Popup' || action === 'donate') { // Check both raw and display value
                    event.preventDefault();
                    console.log("Attempting to open Donate popup from banner");
                    openPopup(donatePopup);
                } else if (action === 'Open Volunteer Popup' || action === 'volunteer') {
                     event.preventDefault();
                     console.log("Attempting to open Volunteer popup from banner");
                     openPopup(volunteerPopup);
                } else if (action === 'scroll') {
                     const targetElement = document.querySelector(bannerButton.getAttribute('href'));
                     if (targetElement) {
                         event.preventDefault();
                         console.log("Attempting to scroll to:", bannerButton.getAttribute('href'));
                         targetElement.scrollIntoView({ behavior: 'smooth' });
                     } else {
                          console.warn("Scroll target not found:", bannerButton.getAttribute('href'));
                     }
                } else if (bannerButton.getAttribute('href') === '#') {
                     event.preventDefault();
                }
                // If action is 'link', default behavior is allowed
            });
        } else {
             console.warn("Banner button not found");
        }

        // Initialize Slider
        if (slides && slides.length > 0) {
            console.log("Initializing slider...");
            showSlide(0);
            startSliderInterval();

            if (nextButton) { nextButton.addEventListener('click', () => { nextSlide(); startSliderInterval(); }); }
            if (prevButton) { prevButton.addEventListener('click', () => { prevSlide(); startSliderInterval(); }); }

            if (slides.length <= 1) {
                 if (prevButton) prevButton.style.display = 'none';
                 if (nextButton) nextButton.style.display = 'none';
            }
        } else {
            console.warn("No slides available to initialize slider.");
            // Handle no slides case... (default text etc.)
            if(bannerTitle) bannerTitle.textContent = "Welcome to Saving Our Community";
            if(bannerText) bannerText.textContent = "Learn more about our work.";
            if(bannerButton) bannerButton.style.display = 'none';
            if (prevButton) prevButton.style.display = 'none';
            if (nextButton) nextButton.style.display = 'none';
        }
    } else {
        console.log("Slide data element not found on this page. Slider not initialized.");
    } // End if (slideDataElement)

}); // End DOMContentLoaded