// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {

    // Select all <a> elements that link to the glossary page
    //const glossaryLinks = document.querySelectorAll('a[href^="https://lpi.oregonstate.edu/mic/glossary#"]');
    const glossaryLinks = document.querySelectorAll('a[href^="../glossary#"]');

    // Iterate over each link and add event listeners for mouseover and mouseout
    glossaryLinks.forEach(link => {

       // When the mouse hovers over the link
        link.addEventListener('mouseover', function() {
            const word = this.getAttribute('href').split('#')[1];

           // Fetch the definition from the API
            fetch(`http://localhost:5000/definition/${word}`)
                .then(response => response.json())
                .then(data => {

// If a definition is received, show the popup with the definition
                    if (data.definition) {
                        showPopup(this, data.definition);
                    }
                })
                .catch(error => console.log('Error fetching definition:', error));
        });

        // When the mouse pointer leaves the link
        link.addEventListener('mouseout', function() {
            hidePopup();
        });
    });

    // Function to show the popup with the definition
    function showPopup(element, definition) {
        let popup = document.getElementById('glossary-popup');
        // Create the popup element if it doesn't exist
        if (!popup) {
            popup = document.createElement('div');
            popup.id = 'glossary-popup';
            document.body.appendChild(popup);
        }

        // Set the text of the popup to the definition
        popup.textContent = definition;
        // Position and display the popup near the word
        popup.style.position = 'absolute';
        popup.style.display = 'block'
        popup.style.backgroundColor = 'white';
        popup.style.border = '1px solid #ddd';
        popup.style.padding = '10px';
        popup.style.zIndex = '1000';
        popup.style.maxWidth = '200px';
        popup.style.left = `${element.getBoundingClientRect().left}px`;
        popup.style.top = `${element.getBoundingClientRect().bottom + window.scrollY}px`;
    }
 
    // Function to hide the popup
    function hidePopup() {
        const popup = document.getElementById('glossary-popup');
        if (popup) {
            popup.style.display = 'none';
        }
    }
});
