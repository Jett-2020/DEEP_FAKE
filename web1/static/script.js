const sr = ScrollReveal({
    distance: '65px',
    duration: 2600,
    delay: 450,
    reset: true
});

sr.reveal('.hero-text', { delay: 200, origin: 'top' });
sr.reveal('.hero-img', { delay: 450, origin: 'top' });
sr.reveal('.icons', { delay: 500, origin: 'left' });

document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();

    const formData = new FormData();
    const videoFile = document.getElementById('videoInput').files[0];
    formData.append('video', videoFile);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        document.getElementById('result').innerText = result.message;
    } catch (error) {
        console.error('Error:', error);
    }
};

document.getElementById('analyzeButton').onclick = async function() {
    try {
        const response = await fetch('/analyze', {
            method: 'POST'
        });

        const result = await response.json();
        document.getElementById('result').innerText = result.message;
    } catch (error) {
        console.error('Error:', error);
    }
};
