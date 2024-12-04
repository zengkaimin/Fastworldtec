document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    const messagesContainer = document.querySelector('.messages-container');
    
    // Function to show message
    function showMessage(type, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        
        const messageContent = document.createElement('p');
        messageContent.textContent = content;
        
        const closeBtn = document.createElement('button');
        closeBtn.className = 'close-btn';
        closeBtn.innerHTML = '&times;';
        closeBtn.onclick = function() {
            messageDiv.remove();
        };
        
        messageDiv.appendChild(messageContent);
        messageDiv.appendChild(closeBtn);
        messagesContainer.appendChild(messageDiv);
        
        // Automatically remove message after 5 seconds
        setTimeout(() => {
            messageDiv.classList.add('fade-out');
            setTimeout(() => messageDiv.remove(), 500);
        }, 5000);
    }
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;
        submitButton.textContent = 'Sending...';
        submitButton.disabled = true;
        
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const formData = new FormData(form);
        
        fetch(window.location.href, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showMessage('success', 'Thank you for your message! We will get back to you soon. 🎉');
                form.reset();
            } else {
                showMessage('error', data.message || 'Oops! Something went wrong. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showMessage('error', 'Sorry, we couldn\'t send your message. Please try again later.');
        })
        .finally(() => {
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        });
    });
});
