print("Hello. I am Maya, your very own AI assistant. Nice to meet you!")
print("How can I help Today?")
from datetime import datetime
today=datetime.now()

import speech_recognition as sr
import pyttsx3

# Create a Recognizer instance
recognizer = sr.Recognizer()

# Capture audio input from the microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio_data = recognizer.listen(source)

# Perform speech recognition using Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data)
    print("You:", text)
    if text=='what is the date':
        theday="Today is "+ str(today.strftime("%A")) + ' ' + str(today.strftime("%B")) + ' ' + str(today.strftime("%d")) + ' ' + str(today.strftime("%Y"))
        print(theday)
    else:
        theday="Developer is still woriking on it. Stick around for a while!"
except sr.UnknownValueError:
    theday="Sorry, could not understand audio."
    print(theday)
except sr.RequestError as e:
    theday="Error: Could not request results from Google Speech Recognition service;"
    print(theday)



speeker= pyttsx3.init()#initiation
speeker.setProperty('rate', 150)
speeker.setProperty('volume', 0.9)

speeker.say(theday)
print("done1")

speeker.runAndWait()
print("done2")
