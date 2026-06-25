"""
This module implements the Flask server for the Emotion Detection application.
It exposes endpoints to analyze text and render the web UI.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")  # pylint: disable=invalid-name

@app.route("/emotionDetector")
def detect_emotion():
    """
    Task 7: Flask route with error handling for blank/invalid inputs.
    """
    text_to_analyze = request.args.get('textToAnalyse')
    
    # Handle empty or whitespace-only input locally
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again."
        
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    
    # If the API returned None (e.g. status code 400)
    if dominant_emotion is None:
        return "Invalid text! Please try again."
        
    return (
        f"For the given text the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
