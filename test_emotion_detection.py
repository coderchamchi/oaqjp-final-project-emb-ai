"""
Unit tests for the emotion_detector function.
"""
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for EmotionDetection package.
    """
    def test_emotion_detector(self):
        """
        Tests dominant emotion detection for joy, anger, and disgust.
        """
        # Test case for joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test case for anger
        result_2 = emotion_detector("I am really angry about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test case for disgust
        result_3 = emotion_detector("I am disgusted by this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

if __name__ == '__main__':
    unittest.main()
