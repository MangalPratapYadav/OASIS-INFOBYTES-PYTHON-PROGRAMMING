import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text.lower()
        except:
            return ""
