"""
This module implements the emotion detector function
by calling the Watson NLP Emotion Predict API.
"""
import requests

def emotion_detector(text_to_analyse):
    """
    Calls the Watson NLP Emotion Predict API, parses the response,
    and returns formatted emotion scores along with the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        
        # Handle status code 400 (Task 7 requirement)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
        formatted_response = response.json()
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    except requests.exceptions.RequestException:
        # Graceful handling for other HTTP/connection errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

if __name__ == "__main__":
    result = emotion_detector("I am so happy today!")
    print(result)
