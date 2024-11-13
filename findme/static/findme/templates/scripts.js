{% load static %}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        var form = event.target;
        var formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest', // Indicates that the request is AJAX
                'X-CSRFToken': form.querySelector('input[name="csrfmiddlewaretoken"]').value // CSRF token for security
            }
        })
        .then(response => {
            if (response.ok) {
                // Redirect to home page
                window.location.href = "home.html";
            } else {
                // Display error message
                return response.json().then(data => {
                    document.getElementById('response-message').innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('response-message').innerHTML = '<div class="alert alert-danger">There was an error submitting the form.</div>';
        });
    });
});
