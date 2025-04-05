// static/js/main.js

document.addEventListener("DOMContentLoaded", function() {

    // --- Banner Slider Logic ---
    const slideDataElement = document.getElementById('slide-data');

    if (slideDataElement) {
        // Parse slides from Django template
        let slides = [];
        try {
             slides = JSON.parse(slideDataElement.textContent);
        } catch(e) {
            console.error("Error parsing slide data:", e);
        }


        // --- Define Static Slides for Specific CTAs ---
        const staticSlides = [
            {
                title: "Become a Volunteer",
                text: "Join our team and make a direct impact. Your time and skills are valuable!",
                image_url: "{% static 'images/banners/volunteer_banner.jpg' %}", // ** Replace with actual static image path **
                button_text: "I Want to Volunteer",
                button_link: "#", // Link isn't used, action is popup
                button_action: "volunteer" // Custom action type
            },
            {
                title: "Contact Us",
                text: "Have questions or suggestions? We'd love to hear from you.",
                image_url: "{% static 'images/banners/contact_banner.jpg' %}", // ** Replace with actual static image path **
                button_text: "Get In Touch",
                button_link: "{% url 'home:contact' %}", // Link to contact page
                button_action: "link"
            },
             {
                title: "Send Feedback",
                text: "Help us improve! Let us know about your experience or ideas.",
                image_url: "{% static 'images/banners/feedback_banner.jpg' %}", // ** Replace with actual static image path **
                button_text: "Leave Feedback",
                button_link: "#feedback-form", // Anchor link to form on homepage
                button_action: "scroll" // Custom action type
            }
        ];

        // Combine dynamic slides (from CMS) with static slides
        // You might want to intersperse them or add static ones at the end
        slides = slides.concat(staticSlides);

        // --- Slider DOM Elements ---
        const bannerSection = document.querySelector('.banner');
        const bannerTitle = document.getElementById('banner-title');
        const bannerText = document.getElementById('banner-text');
        const bannerButton = document.getElementById('banner-button');
        const prevButton = document.getElementById('prev');
        const nextButton = document.getElementById('next');

        let currentSlideIndex = 0;
        let slideInterval;

        // --- Functions ---
        function showSlide(index) {
            if (!slides || slides.length === 0 || !bannerSection || !bannerTitle || !bannerText || !bannerButton) {
                console.error("Missing slide data or banner elements for slider.");
                return; // Exit if essential elements are missing
            }

            currentSlideIndex = (index + slides.length) % slides.length;
            const slide = slides[currentSlideIndex];

            // Fade Out Content
            bannerTitle.style.opacity = 0;
            bannerText.style.opacity = 0;
            bannerButton.style.opacity = 0;

             // Update Background (Ensure path is correct)
            if (slide.image_url) {
                bannerSection.style.backgroundImage = `url(${slide.image_url})`;
            } else {
                 bannerSection.style.backgroundImage = `url('{% static "images/banners/default_banner.jpg" %}')`; // Fallback?
            }

            // Update Content after delay
            setTimeout(() => {
                bannerTitle.textContent = slide.title || ""; // Default empty
                bannerText.innerHTML = slide.text || ""; // Use innerHTML for line breaks
                bannerButton.textContent = slide.button_text || "Learn More";
                bannerButton.href = slide.button_link || "#";

                // Store the action type in a data attribute
                bannerButton.dataset.action = slide.button_action || 'link'; // Default to link

                // Set button visibility
                bannerButton.style.display = slide.button_text ? 'inline-block' : 'none';

                // Fade In Content
                bannerTitle.style.opacity = 1;
                bannerText.style.opacity = 1;
                bannerButton.style.opacity = 1;

            }, 250); // Delay matches CSS transition (adjust if needed)
        }

        function nextSlide() {
            showSlide(currentSlideIndex + 1);
        }

        function prevSlide() {
            showSlide(currentSlideIndex - 1);
        }

        function startSliderInterval() {
            clearInterval(slideInterval);
            if (slides.length > 1) {
                 slideInterval = setInterval(nextSlide, 5000); // 5 seconds
            }
        }

        // --- Event Listener for the Dynamic Banner Button ---
        if (bannerButton) {
            bannerButton.addEventListener('click', function(event) {
                const action = bannerButton.dataset.action;
                console.log("Banner button clicked, action:", action); // Debug log

                if (action === 'donate') { // Matches 'Open Donate Popup' display value
                    event.preventDefault();
                    openPopup(donatePopup); // Use the generic openPopup function
                } else if (action === 'volunteer') { // Matches custom action type
                     event.preventDefault();
                     openPopup(volunteerPopup); // Use the generic openPopup function
                } else if (action === 'scroll') {
                    const targetElement = document.querySelector(bannerButton.getAttribute('href')); // Get element from href (#feedback-form)
                    if (targetElement) {
                        event.preventDefault();
                        targetElement.scrollIntoView({ behavior: 'smooth' });
                    }
                    // Allow default if it's a normal link (action === 'link' or default)
                } else if (bannerButton.getAttribute('href') === '#') {
                     event.preventDefault(); // Prevent jump for placeholder links
                }
            });
        }


        // --- Initialize Slider ---
        if (slides && slides.length > 0) {
            showSlide(0);
            startSliderInterval();

            if (nextButton) {
                nextButton.addEventListener('click', () => {
                    nextSlide();
                    startSliderInterval(); // Restart interval
                });
            }
            if (prevButton) {
                prevButton.addEventListener('click', () => {
                    prevSlide();
                    startSliderInterval(); // Restart interval
                });
            }
             // Hide controls if only one slide
            if (slides.length <= 1) {
                 if (prevButton) prevButton.style.display = 'none';
                 if (nextButton) nextButton.style.display = 'none';
            }

        } else {
            // Handle case where there are no slides at all
            bannerTitle.textContent = "Welcome to Saving Our Community"; // Default content
            bannerText.textContent = "Learn more about our work.";
            bannerButton.style.display = 'none'; // Hide button
            if (prevButton) prevButton.style.display = 'none';
            if (nextButton) nextButton.style.display = 'none';
             console.log("No slides found for banner.");
        }
    } // End if (slideDataElement)

}); // End DOMContentLoaded