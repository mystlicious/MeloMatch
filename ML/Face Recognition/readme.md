# MeloMatch - Mood-Based Music Recommendation System 🎶

MeloMatch is a music recommendation system that detects facial expressions (Happy/Sad) through the camera and recommends songs based on the user's mood.

## Features
- Mood detection (Happy/Sad) using a Machine Learning model.  
- Song recommendations based on the user's mood.  
- Simple dashboard display.

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/mystlicious/MeloMatch.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MeloMatch
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Launch the application.
2. Allow camera access for facial expression detection.
3. Based on your detected mood (Happy/Sad), the system will recommend a list of songs.
4. Enjoy the music and improve your mood! 🎧

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for backend development.
- **OpenCV**: Image processing for camera input.
- **TensorFlow/Keras**: Machine Learning model for mood detection.
- **Pandas**: Data manipulation and analysis.

## Screenshots
![Landing](assets/screenshot demi.png)

## Future Plans
- Add more moods (e.g., Angry, Relaxed, Energetic).
- Improve model accuracy with data augmentation.
- Mobile app version.

---
Enjoy MeloMatch and let the music match your mood! 🎵
