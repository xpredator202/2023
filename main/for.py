import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say((audio))
    engine.runAndWait()

def takeCommand():
    # print("it takes microphone input from the user and returns string output")

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognizer_google(audio,language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("say that again please.........")
        return "none"
    return query



query957=takeCommand
speak("user name is "+query957)
print("user name is "+query957)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning"+query957)
        print("Good Morning"+query957)
    elif hour>=12 and hour<18:
        speak("good afternoon"+query957)
        print("Good AfterNoon"+query957)
    else:
        speak("Good Evening"+query957)
        print("Good Evening"+query957)
if __name__ =="__main__":
    wishMe()
    while True:
        # if 1:
            query = takeCommand().lower()

            # logic for executing tasks based on query
            if 'wikipedia 'in query:
                speak('searching Wikipedia......')
                print('searching Wkipeadia......')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentence =2 )
                speak("According to Wkipedia")
                print(results)
                speak(results)
            


            elif'who i am'  in query:
                speak("your are"+query957)
                print("you are"+query957)
            
            elif'what is my name' in query:
                speak("your name is"+query957)
                print("your name is"+query957)
            
            
