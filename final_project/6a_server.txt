"""Flask web deployment for the Watson NLP emotion detector."""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    """Render the emotion detection browser interface."""
    return render_template("index.html")


@app.route("/healthz")
def healthz():
    """Return a lightweight deployment health response."""
    return jsonify({"status": "ok"})


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze the submitted text and return the requested sentence format."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text_to_analyze)
    except RuntimeError as error:
        return jsonify({"error": str(error)}), 503

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)