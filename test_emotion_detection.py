"""
Unit tests for the emotion_detector function.
"""
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for EmotionDetection package.
    """

    def _mock_response(self, emotion_scores):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "emotionPredictions": [{"emotion": emotion_scores}]
        }
        return mock_resp

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy(self, mock_post):
        mock_post.return_value = self._mock_response(
            {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.97, 'sadness': 0.01}
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger(self, mock_post):
        mock_post.return_value = self._mock_response(
            {'anger': 0.95, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01}
        )
        result = emotion_detector("I am really angry about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust(self, mock_post):
        mock_post.return_value = self._mock_response(
            {'anger': 0.01, 'disgust': 0.94, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01}
        )
        result = emotion_detector("I am disgusted by this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

if __name__ == '__main__':
    unittest.main()
