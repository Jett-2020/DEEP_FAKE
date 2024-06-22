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
