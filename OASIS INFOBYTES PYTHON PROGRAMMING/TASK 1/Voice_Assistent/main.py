import pyttsx3
import speech_recognition as sr
from google_search import google_search_info
from youtube_search import youtube_search_and_play
from facts import interesting_fact
from jokes import tell_joke

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(message):
    """Convert text to speech."""
    engine.say(message)
    engine.runAndWait()

# Speech recognition setup
recognizer = sr.Recognizer()

def listen():
    """Capture and process user's voice input."""
    with sr.Microphone() as source:
        recognizer.energy_threshold = 10000
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("I didn't catch that. Could you please repeat?")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech service.")
            return ""

def google_search_task():
    """Perform a Google search based on user input."""
    speak("What should I search for?")
    query = listen()
    if query:
        speak(f"Searching for {query}.")
        title, details = google_search_info(query)
        if title and details:
            speak(f"Here's what I found: {title}. {details}")
        else:
            speak("I couldn't find anything useful for that query.")
    else:
        speak("I need a search term to proceed.")

def youtube_task():
    """Search and play a YouTube video."""
    speak("What would you like to watch or listen to on YouTube?")
    query = listen()
    if query:
        speak(f"Playing {query} on YouTube.")
        youtube_search_and_play(query)
    else:
        speak("Could you please repeat that? I didn't understand.")

def share_fact():
    """Share an interesting fact."""
    speak("Here's something you might find interesting.")
    fact = interesting_fact()
    speak(fact)

def tell_a_joke():
    """Tell a joke to the user."""
    speak("Let me tell you a joke.")
    joke = tell_joke()
    speak(joke)

def assistant():
    """Main assistant logic."""
    speak("Hi there! I'm SAM, your virtual assistant. How may I assist you?")
    while True:
        user_input = listen()
        if not user_input:
            continue

        if "search" in user_input or "find" in user_input:
            google_search_task()
        elif "play" in user_input or "youtube" in user_input:
            youtube_task()
        elif "fact" in user_input:
            share_fact()
        elif "joke" in user_input or "laugh" in user_input:
            tell_a_joke()
        elif "exit" in user_input or "quit" in user_input:
            speak("Goodbye! Have a wonderful day.")
            break
        else:
            speak("I'm not sure how to help with that. Could you try rephrasing?")

if __name__ == "__main__":
    assistant()
