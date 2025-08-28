import requests
import json

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(URL, json=Input_json, headers=Headers)
    formatted_text = json.loads(response.text)
    formatted_response = formatted_text['emotionPredictions'][0]

    anger_score = formatted_response['emotion']['anger']
    disgust_score = formatted_response['emotion']['disgust']
    fear_score = formatted_response['emotion']['fear']
    joy_score = formatted_response['emotion']['joy']
    sadness_score = formatted_response['emotion']['sadness']

    emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
                'joy': joy_score, 'sadness': sadness_score,}

    dominant_emotion = max(emotions, key=emotions.get)      
    
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
            'joy': joy_score,'sadness': sadness_score, 'dominant_emotion': dominant_emotion}


