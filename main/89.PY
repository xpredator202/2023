import tkinter
import pyttsx3
import JarisAI 
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import time 
import sys 
import pyjokes
import pywhatkit
import urllib.parse
import pprint
import random
import requests
import wolframalpha
import pyautogui
import pyaudio
from PIL import Image
import config
import warnings

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
GREETINGS = ["hello ally","ally","wake up ally","you there ally","time to work ally","hey ally","ok ally","are you there"]
GREETINGS_RES= ["always there for you ","i am ready", "your wish is my command","how can i help you","i am online and ready to go"]
EMAIL_DIC ={
    'myself':'xpredator2021@gmail.com',
    'my offical email' : 'xpredator2021@gmail.com',
    'my second email' : 'ammsh8060@gmail.com',
}

app_id = config.wolframalpha_id 

def computational_intelligence(question):
    try: 
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
    except:
        speak(f"sorry{userName} i couldn't fetch your question's answer please try again later")
        return None

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! sparsh")
        print("Good Morning! sparsh")

    elif hour>=12 and hour<18:
        speak("Good AfterNoon! Sparsh")
        print("Good AfterNoon! Sparsh")
    else:
        speak("Good Evening! sparsh")
        print("Good Eveining! sparsh")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........... ")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in',)
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please ..... ")
        return "None"
    return query

obj = JarvisAI.JarvisAssistant(sync=True, token='71dd94xsxsxse48471ec7af2a733acfb', disable_msg=False, load_chatbot_model=True,high_accuracy_chatbot_model=False,chatbot_model=False,chatbot_large=True,backend_tts_api='pyttsx3')


speak("hello there,")
speak("pls tell me what should i call you")
userName= takecommand()
speak("ok, i will call you"+userName)
speak("by the way that's a nice name")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    
        if 'time' in query:
            time_c = obj.tell_time()
            print(time_c)
            speak(userName+f"the time is{time_c}")
    
        elif query in GREETINGS:
          speak(random.choice(GREETINGS_RES))
        
        elif 'open' in query:
          obj.website_opner ={
              'wikipedia':'https://www.wikipedia.org/',
                          'insta| instagram':'https://instagram.com/',
                         'facebook':'https://facebook.com/',
                         'save file':'https://www.instagram.com/sparsh.comm/saved/',
                         'typing |typing pratice |type rush |game ':'https://www.typerush.com/account.html?play=1',
                         'git hub':'https://www.github.com/',
                         'mail':'https://www.gmail.com/',
                         'amazon':'https//www.amazon.in/', 
                         'message':'https://www.instagram.com/direct/inbox/',
                         'youtube':'https://www.youtube.com/',

          }
          domain = query.split(' ')[-1]
          open_result = obj.website_opener(domain)
          speak(f'alright !! opening{domain}')
          print(open_result)
        
        if 'weather' in query:
          city = query.split(' ')[-1]
          weather_res = obj.weather(city=city)
          print(weather_res)
          speak(weather_res)

        elif 'buzzing'in query or 'news' in query or 'headlines' in query:
          news_res = obj.news()
          speak('source: The Times Of India')
          print('Source: The Times Of India')
          speak('Todays headlines are ....')
          print('Today Headlines are......')
          for index, articles in enumerate(news_res):
              pprint.pprint(articles['title'])
              speak(articles['title'])
              if index == len(news_res)-2:
                  break
          speak('These were the top headlines')

        elif 'search google for'in query:
          obj.search_anything_google(query)
        
        elif'play music' in query or "hit some music"in query or "play some music"in query or 'mind fresh':
          music_dir = "dir"
          songs = os.listdir(music_dir)
          for song in songs:
              os.startfile(os.path.join(music_dir,song))

        elif ' youtube' in query:
          video = query.split(' ')[1]
          speak(f"okay{userName} now i am playing{video}on youtube")
          pywhatkit.playonyt(video)
        
        
        elif'calculate' in query:
           question = query
           answer = computational_intelligence(question)
           speak(answer)

        elif'what is' in query or "who is"in query:
          question = query
          answer = computational_intelligence(question)
          speak(answer)

        elif "what do i have"in query or "do i have plans" in query or "am i busy" in query:
          obj.google_Calendar_events(query)

        elif "make a note" in query or " write this down" in query or " remember this" in query:
          speak("what would you like me to write down")
          note_text = takecommand()
          obj.take_note(note_text)
          speak("i've made a note of that")
        
        elif"close the note" in query or "close notepade" in query:
         speak(f"okey{userName},closing notepad")
         os.system("taskill /f /im notepad++.exe")

        elif "joke" in query:
         joke = pyjokes.get_joke()
         print(joke)
         speak(joke)
       
        elif " system"in query:
          sys_info = obj.system_info()
          print(sys_info)
          speak(sys_info)
        
        elif" where is" in query:
          place = query.split('where is',)[1]
          current_loc, target_loc, distance = obj.location(place)
          city = target_loc.get('city','')
          state = target_loc.get('state','')
          country = target_loc.get('country','')
          time.sleep(1)
          try:

            if city: 
                res = f"{place} is in {state} state and country{country}. It is {distance} km away from your current location"
                print(res)
                speak(res)
            else :
                res = f"{place} is a state in {country}. It is {distance} km away from your current location"
                print(res)
                speak(res)
          except:
            res = f"sorry{userName} , I couldn't get the co-ordinates of the location yoru requested. Pls try again"
            speak(res)
            
        elif 'swtch the window'in query or 'switch window' in query or 'change window' in query or 'change screen' in query:
            speak(f"okay{userName}, switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif ' where i am'in query or 'current location' in query or 'where am i' in query:
            try: 
                city,state,country = obj.my_location()
                print(city, state, country)
                speak(f"you are currently in{city} city which is in {state}state and country{country}")
            except:
                speak(f"sorry {userName} i coundn't fetch your current location . Plee try again")
        
        elif 'take screenshot' in query or "take a screenshot" in query or 'capture the screen'in query or 'take a ss'in query or 'take ss' in query:
            speak("by what name do you want me to save the screenshot?")
            name = takecommand()
            speak(f"alright{userName}, taking the screen shot")
            img = pyautogui.screenshot()
            name = f"{name}.png"
            img.save(name)
            speak("The screenshot has been succesfully captured")

        elif "show me the screenshot" in query:
            try:
                img = Image.open("C://Users//Manav sharma//Pictures//Screenshots//"+name)
                img.show(img)
                speak(f"Here it is{userName}")
                time.sleep(2)

            except IOError:
                speak(f"sorry{userName}, i am unable to display the screenshot")

        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak(f"{userName}, all the files in this folder are now hidden")
        
        elif "visible" in query or "make files visisble" in query:
            os.system("attrib -h /s /d")
            speak(f"{userName}, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
        
        elif'area of rectangle' in query:
            speak("let me prepare my self")
            speak("now first")
            speak("tell me the length of the object")
            query1 = takecommand()
            q=int(query1)
            speak("now, tell me the breath of the object")
            query2=takecommand()
            qq=int(query2)
            qqq=q*qq
            speak(qqq)
            print(qqq)

        elif'area of square' in query:
            speak(f"ok {userName}what is the number")
            query1=takecommand()
            w=int(query1)
            ww=w*w
            speak(f"the area of this square is{ww}, {userName}")
            print(f"the area of this square object is {ww},{userName}")
        
        elif'area of trapezium' in query:
            speak(f"ok {userName} tell me the first base of this trapezoid object")
            query1= takecommand()
            e=int(query1)
            speak(f"ok i got the first base ,now{userName}tell me the 2 base of this trapezoid object")
            query2=takecommand()
            ee=int(query2)
            speak(f"now tell me the Height of this trapezoid object")
            query3=takecommand()
            eee=int(query3)
            eeee=e+ee/2*eee
            speak(f"the area of this trapezium object is {eeee},{userName}")
            print(f"the area of this trapezium object is {eeee}, {userName}")

        elif 'area of triangle' in query:
            speak(f"ok {userName} tell me the base of the triangular object")
            query1 =takecommand()
            r=int(query1)
            speak(f"ok i got the base{userName}, now tell me the height of the object")
            query2 =takecommand()
            rr=int(query2)
            rrr=r*rr/2
            speak(f"the area of this object is {rrr}, {userName}")
            print(f"the area of this object is {rrr}, {userName}")

        elif'area of circle'in query:
            speak(f"ok {userName}tell me the radius of the circle")
            query1=takecommand()
            t=int(query1)
            tt=22/7*t*t
            speak(f"the area of this object is {tt},{userName}")
            print(f"the area of this object is {tt},{userName}")

        elif'area of the cylinder'in query:
            speak(f"ok {userName} , then tell me the radius of the object")
            query1=takecommand()
            y=int(query1)
            speak("ok now tell me the height of the object ")
            query2=takecommand()
            yy=int(query2)
            yyy=2*22/7*y*yy+2*22/7*y*y
            speak(f"the area of this object is {yyy},{userName}")
            print(f"the area of this object is {yyy}, {userName}")
        
        elif'area of the cube'in query:
            speak(f"ok{userName}, then tell me the edge of the object")
            query1=takecommand()
            u=int(query1)
            uu=6*u*u
            speak(f"the area of this object is{uu},{userName}")
            print(f"the area of this object is{uu},{userName}")


        elif "goodbye" in query or "offline"in query or "bye"in query or "i have to go " in query:
            speak(f"alright {userName}, going offline . it was nice working with you")
            sys.exit()
if __name__ == "__main__":
     while True:
            try:
                fingers, hand_type, cv2, img, cap = obj.jarvisai_detect_hands()
                # print(fingers, hand_type)
                cv2.putText(img, 'Up four fingers of right hand to wake up assistant', (50, 200),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.imshow("img", img)
                cv2.waitKey(1)
                if fingers == [1, 1, 1, 1, 0] and hand_type == 'Right':
                    cv2.destroyAllWindows()
                    cap.release()
                    wishMe()
                if fingers == [0, 1, 1, 1, 1] and hand_type == 'Left':
                    cv2.destroyAllWindows()
                    cap.release()
                    city = "Indore"
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    takecommand(weather_res)
            except:
                obj.jarvisai_configure_hand_detector(camera=0, detectionCon=0.7, maxHands=2,
                                                     cam_display=True, cam_height=720, cam_width=1280)
