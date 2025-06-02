import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry, I couldn’t understand."

command = listen()
print("You said:", command)

if "hello" in command.lower():
    speak("Hi Ambika! Nice to meet you.")
else:
    speak("I’m not sure how to respond.")





