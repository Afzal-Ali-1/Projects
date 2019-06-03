__author__ = 'Afzal'
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)#we can use here voices[1] to get female voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("I am Jarvis ,How can I help you ? ,Afzal")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold= 1#Seconds of non-speaking audio before a phrase is complete
        audio=r.listen(source)#press ctrl and click listen to read doc in pycharm
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except BaseException as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query
if __name__=="__main__":
    speak("Afzal is cool")
    wishme()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)