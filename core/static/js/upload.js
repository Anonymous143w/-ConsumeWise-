async function uploadImage(imageData) {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value; // Ensure you have this in your HTML
    try {
        const response = await fetch('/upload-image/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken, // Include the CSRF token for POST requests
            },
            body: JSON.stringify({ image: imageData }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error('Error uploading image:', error);
        alert('Error uploading image!');
    }
}
