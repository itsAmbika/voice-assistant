import speech_recognition as sr
import pyttsx3


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Sorry, I didn’t catch that.")
        return "None"

    return query

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def listen_and_save(filename="assets/user_input.wav"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        # Save the raw audio to a .wav file
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry, I couldn’t understand."

# Use the function
query = take_command()

if 'time' in query:
    from datetime import datetime
    time = datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

elif 'joke' in query:
    speak("Why don’t scientists trust atoms? Because they make up everything!")

elif 'task' in query:
    speak("tell me the task its date and time so that i can add in todo list")
    
else:
    speak("Sorry, I can’t do that yet.")

