# Watson NLP Emotion Detector

This repository contains the completed IBM Watson NLP final-project emotion
detector. It preserves the course starter interface and adds the Python
implementation, package export, Flask service, tests, and rubric evidence.

## Task 1 — repository URL

Public repository:

https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai

## Tasks 1–8 submission index

| Task | Submission |
| --- | --- |
| 1 — Repository URL | This README and the public repository URL above |
| 2 — Application function and import test | `2a_emotion_detection.py`, `2b_application_creation.txt` |
| 3 — Output formatting | `3a_output_formatting.py`, `3b_formatted_output_test.txt` |
| 4 — Package validation | `final_project/EmotionDetection/__init__.py`, `final_project/4b_packaging_test.txt` |
| 5 — Unit tests | `final_project/test_emotion_detection.py`, `final_project/5a_unit_testing.txt`, `final_project/5a_unit_testing.png`, `final_project/5b_unit_testing_result.txt` |
| 6 — Flask deployment | `final_project/server.py`, `final_project/6a_server.txt` |
| 7 — Error handling | `7a_error_handling_function.py`, `7b_error_handling_server.py`, `7c_error_handling_interface.png` |
| 8 — Static analysis | `8a_server_modified.py`, `8b_static_code_analysis.txt` |

## Implementation

`emotion_detection.py` sends the text to the course Watson NLP
`EmotionPredict` endpoint using the
`emotion_aggregated-workflow_lang_en_stock` model. It returns `anger`,
`disgust`, `fear`, `joy`, and `sadness` scores, plus `dominant_emotion`.

The Flask application provides:

- `GET /` — browser interface
- `GET /healthz` — deployment health check
- `GET /emotionDetector?textToAnalyze=...` — customer-facing formatted emotion result
- HTTP 400 with `Invalid text! Please try again!` for missing or blank input
- HTTP 503 with an explicit error when Watson is unavailable

The final-project server is configured for localhost port 5000, as required by
the course deployment task.

## Setup and run

```bash
python3 -m pip install -r requirements.txt
python3 server.py
```

Then open `http://localhost:5000/` or request:

```text
http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20this
```

## Validation

The repository includes deterministic tests that replace only the remote HTTP
response:

```bash
uv run --no-project \
  --with 'Flask>=2.2,<4' \
  --with 'pytest>=7,<9' \
  --with 'requests>=2.31,<3' \
  pytest -q
```

Static analysis:

```bash
uv run --no-project \
  --with 'Flask>=2.2,<4' \
  --with 'pylint>=3,<4' \
  --with 'requests>=2.31,<3' \
  pylint server.py emotion_detection.py
```

Local validation passes with 7 tests and pylint 10.00/10. The course Watson
endpoint may be unavailable from a Replit development network, so the saved
local evidence does not claim live model inference. Capture a live positive
inference in the IBM course environment before submitting it as live Watson
evidence.
