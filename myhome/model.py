# Install needed packages if not installed:
# pip install sounddevice librosa soundfile noisereduce git+https://github.com/openai/whisper.git

import os
import librosa
import soundfile as sf
import whisper
import noisereduce as nr
import numpy as np

# Load Whisper model
model = whisper.load_model("small")# or "base", "tiny", etc.


# 🎚️ Split and denoise audio
def chunk_and_denoise(filename, chunk_duration=5, sample_rate=16000):
    print("🔍 Loading and splitting audio...")
    y, sr = librosa.load(filename, sr=sample_rate)
    print(y)
    total_duration = librosa.get_duration(y=y, sr=sr)
    print(f"📦 Total duration: {total_duration:.2f} seconds")

    chunk_samples = int(chunk_duration * sr)
    chunks = []

    for i in range(0, len(y), chunk_samples):
        chunk = y[i:i + chunk_samples]

        print(f"🔇 Reducing noise for chunk {i // chunk_samples}...")
        denoised = nr.reduce_noise(y=chunk, sr=sr)

        chunk_filename = f"chunk_{i // chunk_samples}.wav"
        sf.write(chunk_filename, denoised, sr)
        chunks.append(chunk_filename)

    print(f"✅ Created {len(chunks)} cleaned chunks")
    return chunks

# 🧠 Transcribe with Whisper
def transcribe_chunks(chunks):
    print("🧠 Transcribing each chunk...")
    full_text = ""
    for i, chunk in enumerate(chunks):
        result = model.transcribe(chunk,language="en",fp16=False)
        full_text += result["text"] + " "
    return full_text.strip()
def cleanup(chunks):
    for f in chunks:
        if os.path.exists(f):
            os.remove(f)



