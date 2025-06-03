# Voice Assistant (Python)

A simple desktop voice assistant project built in Python using `pyttsx3` and `SpeechRecognition`.

## 🗓️ Week 1 Progress

- Set up Python virtual environment (`venv`)
- Installed key libraries: `pyttsx3`, `speechrecognition`, `pyaudio`
- Tested voice output with basic "Hello Ambika" speech
- Initialized Git and pushed project to GitHub

## 🚀 How to Run
  ```bash
python assistant.py
```



# 🗣️ Voice Assistant – Week 2 Update

This week, we extended our basic voice assistant to understand **voice commands** using **Speech Recognition** and respond using **Text-to-Speech (TTS)**.

---

## ✅ What was added in Week 2

- Integrated the `speech_recognition` library to take voice input from the microphone.
- Added the ability to understand basic commands like:
  - Asking for the current time
  - Telling a simple joke
  - Responding when the input is unknown
- Organized code using functions for better readability.

---

## 🧠 Technologies & Libraries Used

- `pyttsx3`: Text-to-Speech engine for offline speaking
- `speech_recognition`: For converting voice to text
- `datetime`: To fetch current system time

---

##  How to Run

1. Activate your virtual environment:
   ```bash
   .\venv\Scripts\activate   # Windows PowerShell
## Speak your command:

Say "What time is it?" → It replies with the current time.

Say "Tell me a joke" → It tells a joke.

Say anything else → It replies it can’t do that yet.
