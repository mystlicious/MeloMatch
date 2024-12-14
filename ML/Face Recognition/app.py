from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
import tensorflow as tf
import base64

app = Flask(__name__)

# Load model ekspresi wajah
model = tf.keras.models.load_model('/model/model_mobile80.h5')

# Fungsi preprocessing gambar
def preprocess_image(image_data):
    # Decode base64 image
    image_data = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)  # Ubah ke grayscale
    img_resized = cv2.resize(img, (256, 256))  # Resize ke ukuran model
    img_normalized = img_resized / 255.0  # Normalisasi
    img_stacked = np.stack((img_normalized,) * 3, axis=-1)  # Tambah channel RGB
    return img_stacked.reshape(1, 256, 256, 3)

# Route utama untuk menampilkan halaman HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk prediksi gambar
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image_data = data['image']
    
    # Preprocess gambar
    processed_image = preprocess_image(image_data)
    
    # Prediksi menggunakan model
    prediction = model.predict(processed_image)
    expression = "Sad" if prediction[0][0] > 0.95 else "Happy"
    
    return jsonify({'expression': expression})

if __name__ == '__main__':
    app.run(debug=True)
