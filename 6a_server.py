"""
This module implements the Flask server for the Emotion Detection application.
"""
from flask import Flask, render_template, request

app = Flask("Emotion Detector")

def emotion_detector(text_to_analyse):
    """
    Mock emotion detector for local demonstration.
    Simulates Watson NLP API response.
    """
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    # Mock scores based on keywords for demo
    text_lower = text_to_analyse.lower()

    if any(w in text_lower for w in ['happy', 'glad', 'joy', 'love', 'great']):
        emotions = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.96, 'sadness': 0.01}
    elif any(w in text_lower for w in ['angry', 'anger', 'hate', 'furious']):
        emotions = {'anger': 0.95, 'disgust': 0.02, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01}
    elif any(w in text_lower for w in ['disgust', 'disgusted', 'gross']):
        emotions = {'anger': 0.01, 'disgust': 0.94, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.02}
    elif any(w in text_lower for w in ['fear', 'scared', 'afraid']):
        emotions = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.95, 'joy': 0.01, 'sadness': 0.02}
    elif any(w in text_lower for w in ['sad', 'unhappy', 'cry', 'miss']):
        emotions = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.96}
    else:
        emotions = {'anger': 0.05, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.80, 'sadness': 0.05}

    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    return emotions


@app.route("/emotionDetector")
def detect_emotion():
    """
    Flask route to evaluate the emotion of the given text.
    """
    text_to_analyze = request.args.get('textToAnalyse')

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

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
    Renders the main index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)