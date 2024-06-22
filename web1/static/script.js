const sr = ScrollReveal({
    distance: '65px',
    duration: 2600,
    delay: 450,
    reset: true
});

sr.reveal('.hero-text', { delay: 200, origin: 'top' });
sr.reveal('.hero-img', { delay: 450, origin: 'top' });
sr.reveal('.icons', { delay: 500, origin: 'left' });

document.getElementById('uploadButton').addEventListener('click', function () {
    const videoInput = document.getElementById('videoUpload');
    const file = videoInput.files[0];
    const messageDiv = document.getElementById('message');

    if (!file) {
        messageDiv.innerHTML = "Please select a video file.";
        return;
    }

    const formData = new FormData();
    formData.append('video', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        messageDiv.innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        messageDiv.innerHTML = "An error occurred while uploading the video.";
    });
    
});
document.addEventListener('DOMContentLoaded', function() {
    const videoUpload = document.getElementById('videoUpload');
    const uploadButton = document.getElementById('uploadButton');
    const sendEmailButton = document.getElementById('sendEmailButton');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const resultSection = document.getElementById('resultSection');
    const resultText = document.getElementById('resultText');

    // Initialize EmailJS with your Service ID
    emailjs.init('service_9jy7y17'); // Replace with your actual EmailJS User ID

    uploadButton.addEventListener('click', function() {
        const file = videoUpload.files[0];
        
        if (!file) {
            alert('Please select a video file.');
            return;
        }

        const formData = new FormData();
        formData.append('video', file);

        // Display loading spinner
        loadingSpinner.classList.remove('hidden');

        // Simulate backend processing delay
        setTimeout(function() {
            // Simulated analysis result
            const analysisResult = 'Deepfake analysis completed successfully.';

            // Hide loading spinner
            loadingSpinner.classList.add('hidden');

            // Show result section
            resultSection.classList.remove('hidden');
            resultText.textContent = analysisResult;
        }, 2000); // Simulate 2 seconds processing time (adjust as needed)
    });

    sendEmailButton.addEventListener('click', function() {
        const email = prompt('Enter recipient email:');
        
        if (!email) {
            alert('Email is required to send the report.');
            return;
        }

        const pdfUrl = 'C:/Users/ajogd/OneDrive/Desktop/report.pdf'; // Replace with actual PDF URL

        // Prepare the email parameters
        const emailParams = {
            to_email: email,
            message: 'Please find attached the deepfake analysis report.',
            pdf_url: pdfUrl
        };

        // Send email using EmailJS
        emailjs.send('your_service_id', 'your_template_id', emailParams)
            .then(function(response) {
                console.log('Email sent:', response);
                alert(`Report sent to ${email} successfully.`);
            }, function(error) {
                console.error('Email error:', error);
                alert('Failed to send email.');
            });
    });
});

