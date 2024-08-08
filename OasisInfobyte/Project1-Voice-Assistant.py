import speech_recognition as sr  #library to recognizes speech using various speech recognition engines
import pyttsx3  #convert text to speech
import datetime  #handle date and time
import wikipedia  #fetch info from wikipedia
import pyaudio  #to handle audio streams fro microphone input

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()


# Define a function to respond to voice commands
def respond(command):  # take voice command as input and performs actions
    if "hello" in command:
        pyttsx3.speak("Hello! How can I help you?")
    elif "time" in command:
        pyttsx3.speak(datetime.datetime.now().strftime("%H:%M:%S"))
    elif "date" in command:
        pyttsx3.speak(datetime.datetime.now().strftime("%d:%m:%Y"))
    elif "search" in command:  #fetches summary from wikipedia and reads it aloud
        query = command.replace("search", "")
        pyttsx3.speak("searching for " + query)
        results = wikipedia.summary(query, sentences=3)
        pyttsx3.speak(results)
    elif any(stop_word in command for stop_word in ["stop", "exit", "quit", "bye", "goodbye"]):
        pyttsx3.speak("Goodbye! Have a great day!")
        exit()
    else:
        pyttsx3.speak("I didn't understand that. Please try again.")


# Define a function to speak text
def speak(text):
    engine.say(text)  # queses text to be spoken
    engine.runAndWait()


# Initialize PyAudio
p = pyaudio.PyAudio()  #creates an instance of pyaudio class to manage audio input/output

# Start listening for voice commands
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="en-IN")
            print("You said:", command)
            respond(command)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")

# Close PyAudio
p.terminate()
#ensures that pyaudio instance is properly closed when program ends.
