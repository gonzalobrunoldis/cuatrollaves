document.addEventListener('DOMContentLoaded', function() {
    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevents the default form submission
            
            // Collect form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
        
            // Prepare data to send
            const formData = { name, email, message };
        
            // Send data using fetch
            fetch('/submit-contact', {  // Ensure this matches Flask route
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while submitting the form.');
            });
        });        
    }
});