// static/content_manager/js/cm_mobile_menu.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('CM Mobile Menu JS Loaded');

    const mobileNavToggler = document.getElementById('cm-mobile-toggler');
    // Target the UNIQUE ID of the mobile dropdown nav element
    const mobileNavDropdown = document.getElementById('cm-mobile-nav-dropdown');

    // --- Check if elements were found ---
    console.log("Mobile Toggler:", mobileNavToggler);
    console.log("Mobile Nav Dropdown:", mobileNavDropdown);
    // ----------------------------------

    if (mobileNavToggler && mobileNavDropdown) {
        console.log("Attaching mobile nav toggler listener");

        mobileNavToggler.addEventListener('click', function(event) {
            event.stopPropagation();
            console.log("Toggler clicked!");

            // Toggle the .is-active class on the mobile nav dropdown
            mobileNavDropdown.classList.toggle('is-active');
            console.log("Toggled .is-active on #cm-mobile-nav-dropdown. Current classes:", mobileNavDropdown.className);

            // Toggle aria-expanded attribute on the button
            const isExpanded = mobileNavDropdown.classList.contains('is-active');
            mobileNavToggler.setAttribute('aria-expanded', String(isExpanded));

            // Toggle icon class on the button
            const icon = mobileNavToggler.querySelector('i');
            if (icon) {
                icon.className = isExpanded ? 'fa fa-times' : 'fa fa-bars';
            }
        });

        // Close dropdown if clicking outside of it
        document.addEventListener('click', function(event) {
            // Check if the nav element itself exists before trying to check contains
            if (!mobileNavDropdown) return;

            const isClickInsideNav = mobileNavDropdown.contains(event.target);
            const isClickOnToggler = mobileNavToggler.contains(event.target);

            if (!isClickInsideNav && !isClickOnToggler && mobileNavDropdown.classList.contains('is-active')) {
                console.log("Click outside detected, closing dropdown.");
                mobileNavDropdown.classList.remove('is-active');
                mobileNavToggler.setAttribute('aria-expanded', 'false');
                const icon = mobileNavToggler.querySelector('i');
                if (icon) { icon.className = 'fa fa-bars'; }
            }
        });

        // Optional: Close dropdown on Escape key press
        document.addEventListener('keydown', function(event) {
             // Check if the nav element itself exists
             if (!mobileNavDropdown) return;

             if (event.key === 'Escape' && mobileNavDropdown.classList.contains('is-active')) {
                 console.log("Escape key pressed, closing dropdown.");
                 mobileNavDropdown.classList.remove('is-active');
                 mobileNavToggler.setAttribute('aria-expanded', 'false');
                 const icon = mobileNavToggler.querySelector('i');
                 if (icon) { icon.className = 'fa fa-bars'; }
             }
         });

    } else {
        if (!mobileNavToggler) console.warn("Mobile toggler button (#cm-mobile-toggler) not found.");
        if (!mobileNavDropdown) console.warn("Mobile nav dropdown (#cm-mobile-nav-dropdown) not found.");
    }

}); // End DOMContentLoaded