"""Required unit tests for the EmotionDetection package."""

from __future__ import annotations

import pytest

from EmotionDetection import emotion_detector
import EmotionDetection.emotion_detection as detector_module


STATEMENTS_AND_EMOTIONS = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]


class FakeResponse:
    """Watson-compatible response used for deterministic unit tests."""

    def __init__(self, scores):
        self.scores = scores

    def raise_for_status(self):
        return None

    def json(self):
        return {"emotion_prediction": {"emotion": self.scores}}


@pytest.mark.parametrize(
    ("statement", "expected_emotion"),
    STATEMENTS_AND_EMOTIONS,
)
def test_emotion_detector(statement, expected_emotion, monkeypatch):
    """Each required statement returns its expected dominant emotion."""
    scores = {emotion: 0.01 for emotion in ("anger", "disgust", "fear", "joy", "sadness")}
    scores[expected_emotion] = 0.91
    monkeypatch.setattr(
        detector_module.requests,
        "post",
        lambda *args, **kwargs: FakeResponse(scores),
    )

    result = emotion_detector(statement)

    assert result["dominant_emotion"] == expected_emotion