// static/content_manager/js/cm_mobile_menu.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('CM Mobile Menu JS Loaded');

    const mobileNavToggler = document.getElementById('cm-mobile-toggler');
    const mobileNavDropdown = document.getElementById('cm-sidebar-nav'); // Target the nav element

    if (mobileNavToggler && mobileNavDropdown) {
        console.log("Attaching mobile nav toggler listener to button:", mobileNavToggler);
        console.log("Mobile nav dropdown element:", mobileNavDropdown);

        mobileNavToggler.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent click from immediately closing dropdown

            console.log("Toggler clicked!");

            // Toggle the .is-active class on the nav dropdown element itself
            mobileNavDropdown.classList.toggle('is-active');

            // Toggle aria-expanded attribute on the button
            const isExpanded = mobileNavDropdown.classList.contains('is-active');
            mobileNavToggler.setAttribute('aria-expanded', String(isExpanded)); // Set attribute as string

            // Toggle icon class on the button
            const icon = mobileNavToggler.querySelector('i');
            if (icon) {
                icon.className = isExpanded ? 'fa fa-times' : 'fa fa-bars';
                console.log("Icon class set to:", icon.className);
            }
        });

        // Close dropdown if clicking outside of it
        document.addEventListener('click', function(event) {
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
        if (!mobileNavDropdown) console.warn("Mobile nav dropdown (#cm-sidebar-nav) not found.");
    }

}); // End DOMContentLoaded