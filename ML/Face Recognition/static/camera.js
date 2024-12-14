const video = document.getElementById('camera');
const captureButton = document.getElementById('capture');
const predictButton = document.getElementById('predict');
const resultText = document.getElementById('result');

let canvas, capturedImage;

// Akses kamera
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Gagal mengakses kamera: ", err);
    });

// Fungsi untuk menangkap gambar
captureButton.addEventListener('click', () => {
    canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    capturedImage = canvas.toDataURL('image/jpeg'); // Simpan gambar

    alert('Gambar berhasil diambil. Klik Predict untuk menganalisis.');
});

// Fungsi untuk mengirim gambar ke server Flask
predictButton.addEventListener('click', () => {
    if (!capturedImage) {
        alert('Ambil gambar terlebih dahulu.');
        return;
    }

    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify({ image: capturedImage }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        resultText.textContent = `Ekspresi: ${data.expression}`;
    })
    .catch(err => console.error('Error:', err));
});
