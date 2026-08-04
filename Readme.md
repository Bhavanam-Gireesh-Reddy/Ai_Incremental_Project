# MarketPulse AI

A demo web application that bundles multiple AI/ML features in one place. Use it to try forecasting (ARIMA, SARIMA, LSTM), sentiment analysis (BERT + baseline), RAG-based document Q&A, LangChain agents, image generation, audio generation, and computer vision demos (object detection). The application exposes a simple web UI and API endpoints for each feature so non-technical users and developers can prototype and demo AI capabilities quickly.

---

## Problem statement

Teams and learners often need a single, easy way to try different AI features without wiring many separate demos. This project solves that by providing a single web app that accepts common inputs (text, images, product IDs), runs the right model or agent, and returns clear outputs (forecasts, classification labels, chat answers, generated images/audio, detection results). It is meant for demos, education, and quick prototyping.

---

## Key features

- Forecasting: ARIMA, SARIMA, and LSTM models for sales forecasting.
- NLP & Sentiment: Baseline logistic regression + transformer-based sentiment (BERT-like models).
- RAG (Retrieval-Augmented Generation): ingest documents, build vector store, and answer questions using a generator.
- LangChain Agents: tool-using agents that can call vision, forecasting, or other tools.
- Chatbots: simple chat UI backed by RAG or LangChain agents.
- Vision: image generation, audio generation, and object detection (uses saved model weights).
- Deep learning demos: CNN and transfer-learning image classification pipelines.

---

## Repository layout (important)

```
app.py                   # FastAPI app: routes pages and API endpoints
requirements.txt         # pip dependencies
templates/               # HTML pages (index, chatbot, arima, lstm, langchain, etc.)
static/                  # CSS, logos, generated media, detection outputs
uploads/                 # temp files uploaded by users
Forecaster/              # forecasting code (arima, sarima, lstm)
LangChain/               # LangChain agent wrapper and CLI
LANGRAPH/                # LangGraph integration code
chatbot/                 # RAG/chatbot wrapper (chatbot.script -> agent)
deep_learning/           # CNN & transfer learning training / prediction
ml_tech/                 # classical ML scripts (decision tree, svm, random forest)
nlp_sentiment/           # sentiment training and orchestration
rag/                     # RAG pipeline (loader, chunking, vectorizer, retriever, generator)
vision/                  # image generation, audio, detector code and models
```

---

## How it fits together (runtime flow)

- `app.py` is the single entry point. It serves HTML pages from `templates/` and provides API endpoints.
- Each endpoint imports and calls a small script inside the matching folder. For example:
  - Forecast endpoints call `Forecaster.scripts.forecast_sales`.
  - Chatbot endpoints call `chatbot.script.run_chatbot` or `LANGRAPH.scripts.run_chatbot`.
  - RAG uses `rag/pipeline.py` to ingest documents and answer questions.
  - Vision endpoints call code in `vision/src` (object detector, image/audio generators).

---

## Quick setup and run (shortest path)

1. Clone the repository:

```bash
git clone https://github.com/Bhavanam-Gireesh-Reddy/Ai_Incremental_Project.git
cd Ai_Incremental_Project
```

2. Create a Python virtual environment and activate it:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file with provider keys if you plan to use them:

```
GEMINI_API_KEY=your_key_here
HF_TOKEN=your_hf_token_here
```

5. (Optional) Run setup scripts for components that expect artifacts:

```bash
python nlp_sentiment/scripts.py      # train baseline logreg model and build artifacts
# For RAG: place documents under rag/data or call the pipeline ingestion from code
```

6. Start the web app:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 in your browser.

---

## Important API endpoints (examples)

- Chatbot: POST /chatbot
  - Body: { "message": "Your question" }

- LangChain agent (form + optional image): POST /langchain-agent
  - Form fields: message (text), image (file, optional)

- Sentiment (BERT): POST /sentiment-bert
  - Body: { "text": "I love this product" }

- Image generation: POST /generate-image
  - Body: { "prompt": "a red dress on a runway" }

- Object detection: POST /detect-object
  - Upload an image file via multipart/form-data

- Forecasting:
  - POST /forecast-arima  (Body: {"product_id": "P100", "days": 30})
  - POST /forecast-lstm
  - POST /forecast-sarima

---

## Notes and limitations

- Some demos require large model downloads (transformers, image-generation) or pre-saved artifacts (object detector weights at `vision/model/best.pt`, vector DB under `rag/chroma_db`, trained logistic model under `nlp_sentiment/models`). If those artifacts are missing, either run the provided scripts to create them or place them in the expected paths.
- For good performance on heavy models (training or large inference), use a machine with a GPU.
- Keep API keys private. Do not commit `.env` with secrets.

---

## Suggested small improvements before demoing to others

- Add `README.md` (this file) to the repository root (done).
- Add `.env.example` listing environment variables needed.
- Add a small `demo-data/` folder with a couple of example documents for RAG and a small image sample for vision demos.
- Consider a `docker-compose.yml` to simplify dependency management and environment consistency.

---

## Author / Contact

Project owner: Bhavanam-Gireesh-Reddy
Repository: https://github.com/Bhavanam-Gireesh-Reddy/Ai_Incremental_Project
