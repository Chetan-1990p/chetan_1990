import datetime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')

    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evining')
    speak('I am jarvis sir. please tell me how may I help you')
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
     print("listening...")
     r.pause_threshold=1
     audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
 wishme()
 takecommand()
 while True:
     query=takecommand().lower()
     if'wikipedia'in query:
         speak('searching wikipedia...')
         query = query.replace('wikipedia...',"")
         results = wikipedia.summary(query,sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in query:
         webbrowser.open("youtube.com")

     elif 'google' in query:
         webbrowser.open("google")

     elif 'stackover' in query:
         webbrowser.open("stackover")

     elif 'crome browser' in query:
         webbrowser.open("crome brower")

     elif'play music' in query:
         music_dir = 'E:\songs'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

     elif 'the time' in query:
         strTime=datetime.datetime.now().strftime("%H:,%M:%S")
         speak(f"sir,the time is {strTime}")







