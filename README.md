# 🗣️ Reading Score – Real-Time Reading Accuracy App (Django + Whisper)

**Reading Score** is a real-time web app that helps users improve their reading fluency by transcribing spoken input and comparing it to a reference text. Built using **Django**, **WebSockets**, and **OpenAI's Whisper (small model)**, the app streams microphone audio from the browser, transcribes it, and computes a reading accuracy score.

---

## 🚀 Features

- 📄 Upload any `.txt` file as the reading target
- 🎙️ Speak live from your browser using the microphone
- 🔁 Audio is streamed to the backend in chunks via **WebSocket**
- 🧠 Transcribed in real-time using **Whisper-small**
- 📊 Compared with original text to compute an accuracy score
- ✅ Displays:
  - Reference text
  - Transcription result
  - Reading accuracy percentage

---

## 🛠️ Tech Stack

| Component      | Tech Used                     |
|----------------|-------------------------------|
| Framework      | Django (ASGI-enabled)         |
| Realtime Layer | Django Channels + WebSocket   |
| Transcription  | OpenAI Whisper (small)        |
| Frontend       | HTML + JavaScript (MediaRecorder) |
| Scoring        | `jiwer`, `difflib`, or custom |

---

## 📂 Project Structure

reading-score/
├── myhome/ # Django project root
├── upload-audio/ # Main Django app
│ ├── consumers.py # WebSocket logic
│ ├── views.py # Text upload & result display
│ ├── templates/ # HTML templates
│ ├── static/ # JavaScript (mic, WebSocket)
│ └── routing.py # ASGI WebSocket routes
├── manage.py
├── reuirement.txt # ⚠️ Rename to requirements.txt
└── db.sqlite3

yaml
Copy
Edit

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/marwaai/reading-score.git
cd reading-score
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

bash
Copy
Edit
mv reuirement.txt requirements.txt
4. Install ffmpeg (required by Whisper)
bash
Copy
Edit
sudo apt install ffmpeg  # Or use brew/choco for macOS/Windows
▶️ Running the App
1. Apply migrations
bash
Copy
Edit
python manage.py migrate
2. Start the ASGI server
bash
Copy
Edit
daphne myhome.asgi:application
# or, with uvicorn
# uvicorn myhome.asgi:application
Open http://localhost:8000 in your browser.

📊 How It Works
User uploads a .txt file (e.g. "The cat sat on the mat.")

User clicks Record and reads the text aloud

Django backend receives audio  and chunks by librosa then transcribes each using Whisper-small
then it send by websocket to the same page
Once complete, the final transcript is compared to the .txt  and give transcription with score (precentage of correct char compare to original).
