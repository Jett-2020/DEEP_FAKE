document.getElementById('uploadButton').addEventListener('click', function() {
    const fileInput = document.getElementById('videoUpload');
    const resultDiv = document.getElementById('result');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('video', file);

        fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.textContent = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.textContent = 'An error occurred while analyzing the video.';
        });
    } else {
        resultDiv.textContent = 'Please select a video file to upload.';
    }
});
