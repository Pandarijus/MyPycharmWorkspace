import speech_recognition as sr
import pyttsx3 as tts

recogniser = sr.Recognizer()

while True:

    try:

        with sr.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic,duration=0.1)
            audio = recogniser.listen(mic)
            text = recogniser.recognize_google(audio)
            text = text.lower()

            print(text)
    except:
        recogniser = sr.Recognizer()
        continue

