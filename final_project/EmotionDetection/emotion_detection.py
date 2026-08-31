"""EmotionDetection package implementation."""

from __future__ import annotations

from typing import Any

import requests


WATSON_NLP_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_NAME = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze: str | None) -> dict[str, Any]:
    """Analyze text and return Watson's five scores and dominant emotion."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {**{name: None for name in EMOTION_NAMES}, "dominant_emotion": None}

    response = requests.post(
        WATSON_NLP_URL,
        headers={"grpc-metadata-mm-model-id": MODEL_NAME},
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    response.raise_for_status()
    emotion_scores = response.json()["emotion_prediction"]["emotion"]

    anger_score = emotion_scores["anger"]
    disgust_score = emotion_scores["disgust"]
    fear_score = emotion_scores["fear"]
    joy_score = emotion_scores["joy"]
    sadness_score = emotion_scores["sadness"]
    dominant_emotion = max(
        EMOTION_NAMES,
        key=lambda name: emotion_scores[name],
    )

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }