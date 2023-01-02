import _tkinter 
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib #download from google smtplib python 3.10 or3.09



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! sparsh")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! sparsh")   

    else:
        speak("Good Evening! sparsh")  

    speak("hello sparsh")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in',)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xpredator2021@gmail.com', 'sparsh9803')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

        
        elif'open amazon'in query:
            webbrowser.open("amazon.com")
            speak("opening amazon")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
        
        elif' introduce your self'in query:
            speak("ok")
            speak("my name is DODO  ")
            speak("i am a personal assistant")
            speak("i am made by sparsh sharma")
            speak("tell me what can i  do for you")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            speak("opening stackoverflow")

        elif 'play song on youtube'  in query:
             webbrowser.open("")
             speak("opening your playlist")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("opening instagram")

        elif 'what is your full name' in query:
            speak("are you sure,sparsh")
            if 'yes' in query:
                speak("ok, tell me the code")
                if '9999078603' in query:
                    speak(" code is correct ,my full name is mahak gola")
                else:
                    speak("sorry code is wrong")
        
        elif ' who is mahak gola' in query:
            speak("tell me the code")
            if '9999078603' in query:
                speak("Mahak Gola is a queen of mr black devil , she is everything to him , but sadly she left him alone , pls ask sparsh who is she because i am not able to tell you but i know he is single because he still in love with her")

        elif 'bye DODO' in query:
            speak("radhy radhy sparsh")
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"sparsh, the time is {strTime}")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sparsh. I am not able to send this email")    

        elif 'hi DODO' in query:
            speak("hello sparsh")
            speak("what can i do for you")

        elif 'hey baby' in query:
            speak("yes sparsh")

       

        elif 'who is josip broz tito' in query:
            speak("he was born in 1892 and he dead on 1980, he was president of Yugoslavia in [1945 to 1985]  he fight against germany in world war 2 ")
            speak("if you need more information that pls ask me 'josip broz tito wikipedia' ")

        elif 'who is jawaharlal Nehru' in query:
            speak("he was born in 1889 and he dead on 1964 , he was the first prime minister of india in 1974 to 1964 he made efforts for asian unity, decolonsation , neculear disarmament; advocated peaceful coexistence for securing world peace.")
            speak("if you need more information than pls ask  me 'jawaharlal nehru wekipedia' ")

        elif 'who is gamal abdel nasser'in query:
            speak("he was born on 1918 and dead on 1970 he ruled egypt from 1952 to 1970; espoused the causes of arab nationalism , socialalism and anti-imperialism; nationalised the suez canal, leading to an international conflict in 1956.")
            speak("if you need more information than pls ask me 'gamal abdel nasser wekipedia' ")
        
        elif ' sukarno' in query:
            speak("he was born on 1901 and he dead on 1970 , he was the first president of indonesia he ruled from 1945 to 1965; he led the freedom  struggle espouded the causes of socialism and anti-imperialism; organised the bandung conference; overthrown in a military coup.")
            speak("if you need more information than pls ask me 'sukarno wekipedia' ")

        elif 'who is kwame nikumah'in query:
            speak("he was born on 1909 and he dead on 1972, he was the first prime minisater of ghana he ruled from 1952 to 1966; led the freedom movement; advocated the causes of socialism and african unity; opposed neocolonialism' remoced in a miliray coup")
            speak("if you need more information than pls ask me 'kwame nikumah wekipedia' ")

        elif 'who is sparsh sharma' in query:
            speak("he is beyound your mind so pls ask me another question")

        elif 'the discovery of hampi' in query:
            speak("the ruins at hampi were brought to light in 1800 by an enginerr and antiquarian named colonel colin mackenzie")
        
        elif 'area of the rectangle' in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the rectangle is ")
                speak("l * b")
                print("l x b")
            else:
                speak("ok then")
                speak("tell me the length of the object")
                query=takeCommand()
                l=int(query)
                speak("tell me the breadth of the object ")
                query2=takeCommand()
                b=int(query2)
                ar=l*b
                speak(ar)
                print(ar)

        elif ' area of square' in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of square is")
                speak("side multiply by side")
                print("side x side")
            else:
                speak("ok then")
                speak("tell me the number")
                query = takeCommand
                a=int(query)
                rt=a*a
                speak(rt)
                print(rt)
        
        elif 'area of trapezium' in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of trapezium is")
                speak("l + b / 2*h")
            else:
                speak("tell me the a of the object")
                query=takeCommand()
                x=int(query)
                speak("tell me the base of the object")
                query2=takeCommand()
                y=int(query2)
                speak("tell me the height of the object")
                query3=takeCommand()
                h=int(query3)
                ans=x+y/2*h
                speak(ans)
                print(ans)
        
        elif 'area of the trangle'in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the trangle is")
                speak("base muntiply by height by 2")
            else:
                speak("tell me the base of the object")
                query=takeCommand()
                o=int(query)
                speak("tell me the height of the object")
                query2=takeCommand()
                p=int(query2)
                tr=o*p/2
                speak(tr)
                print(tr)

        elif 'area of the circle'in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the circle is ")
                speak("22/7 * radius * radius")
            else:
                speak("tell me the radius of the circle")
                query=takeCommand(a)
                i=int(query)
                qw=22/7*i*i
                speak(qw)
                print(qw)

        elif 'area of the cylinder' in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the cylinder is")
                speak("2*22/7*radius*height*+2*22/7*radius*radius")
                print("2*22/7*radius*height*+2*22/7*radius*radius")
            else:
                query=takeCommand()
                speak("tell me the radius of the cylinder")
                u=int(query)
                speak("tell me the height of the cylinder")
                query2=takeCommand()
                t=int(query2)
                ut=2*22/7*u*t*+2*22/7*u*u
                speak(ut)
                print(ut)

        elif 'area of the cube'in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the cube is")
                speak("6 * edge *edge")
                print("6*edge*edge")
            else:
                speak("tell me the edge of the cube")
                query=takeCommand()
                r=int(query)
                rq=6*r*r
                speak(rq)
                print(rq)
        
        elif 'area of the cubeoid'in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the cubeoid is")
                speak("2*height*length+hight*base")
                print("2*height*length+height*base")
            else:
                query=takeCommand()
                speak("tell me the hight of the object")
                w=int(query)
                speak("tell me the lenth of th object")
                query2=takeCommand()
                q=int(query2)
                speak("tell me the base of the object")
                query3=takeCommand()
                wq=int(query3)
                qwq=2*w*q+wq 
                speak(qwq)
                print(qwq)
        
        elif 'area of the cone' in query:
            speak("do you want to know what the formula")
            if'yes'in query:
                speak("ok let me search")
                speak("according to the google")
                speak("area of the cone is")
                speak("22/7*radius*lenght")
                print("22/7*radius*lenght")
            elif'no'in query:
                speak("tell me the radius of the object")
                query=takeCommand()
                v=int(query)
                speak("tell me the lenght of the object")
                query2=takeCommand()
                c=int(query2)
                cv=22/7*v*c
                speak(cv)        
                print(cv)

        elif 'area of the sphere' in query:
            speak("tell me the radius of the object")
            query=takeCommand()
            n=int(query)
            nn=4*22/7*n*n
            speak(nn)
            print(nn)

        elif'area of the hemi sphere'in query:
            speak("tell me the radius of the object")
            query=takeCommand()
            m=int(query)
            mm=2*22/7*m*m
            speak(mm)
            print(mm)

        elif'volume of the cube'in query:
            speak("tell me the side")
            query=takeCommand()
            k=int(query)
            kk=k*k*k
            speak(kk)
            print(kk)

        elif'volume of the cuboied'in query:
            speak("tell me the length of the object")
            query=takeCommand()
            j=int(query)
            speak("tell me the breath of the object")
            query2=takeCommand()
            jj=int(query2)
            speak("tell me the height of the object ")
            query3=takeCommand()
            jjj=int(query3)
            jjjj=j*jj*jjj
            speak(jjjj)
            print(jjjj)

        elif'volume of the cylender'in query:
            speak("tell me the radius of the object")
            query=takeCommand()
            g=int(query)
            speak("tell me the height of the object")
            query2=takeCommand()
            gg=int(query2)
            ggg=22/7*g*g*gg
            speak(ggg)
            print(ggg)

        elif'volume of the cone'in query:
            speak("tell me the radius of the object")
            query=takeCommand()
            f=int(query)
            speak("tell me the height of the object")
            query2=takeCommand()
            ff=int(query2)
            fff=1/3*22/7*f*f*ff
            speak(fff)
            print(fff)

        elif'volume of the sphere'in query:
            speak("tell me the radius of the object")
            query=takeCommand
            d=int(query)
            dd=4/3*22/7*d*d*d
            speak(dd)
            print(dd)

        elif'volume of the hemi-shere'in query:
            speak("tell me the radius of the object")
            query=takeCommand
            s=int(query)
            ss=2/3*22/7*s*s*s
            speak(ss)
            print(ss)

        elif'sum'in query:
            speak("tell me the no 1")
            query=takeCommand
            ww=int(query)
            speak("tell me the second number")
            query2=takeCommand
            www=int(query2)
            speak("is there is thired no")
            if 'yes'in query:
                speak("ok , tell me the thired number")
                query3=takeCommand
                wwww=int(query3)
                speak("ok wait")
                speak("your answer is")
                wwwww=ww+www+wwww 
                print(wwwww)
                speak(wwwww)
            else:
                speak("ok let me calculate your question")
                wwwwww=ww+www
                speak("your answer is")
                speak(wwwwww)
                print(wwwwww)

        elif'multiplication'or'multiply'in query:
            speak("tell me the first number")
            query=takeCommand
            rr=int(query)
            speak("tell me the second number")
            query2=takeCommand
            rrr=int(query2)
            speak("is there thired number or not")
            if 'yes'in query:
                speak("ok tell me the third number")
                query3=takeCommand
                rrrr=int(query3)
                speak("ok wait let me calculate")
                rrrrr=rr*rrr*rrrr
                speak(rrrrr)
                print(rrrrr)
            else:
                ("ok let me calculate the question")
                rrrrrr=rr*rrr
                speak(rrrrrr)
                print(rrrrrr)
        elif'division'or'divied'in query:
            speak("ok tell me the first number")
            query=takeCommand
            tt=int(query)
            speak("tell me the second number")
            query2=takeCommand
            ttt=int(query)
            speak("ok wait for the answer")
            speak("your answer is")
            tttt=tt/ttt
            speak(tttt)
            print(tttt)

        elif'solve this question'in query:
            speak("ok tell me the question")
            query=takeCommand
            yy=int(query)
        
        elif'percent'or'percentage'in query:
            speak("ok tell me the number")
            query=takeCommand
            tt=int(query)
            ttt=tt/100
            speak(ttt)
            print(ttt)

        elif'hello mahak gola'in query:
            speak("aba oh pagal")
            speak("i miss you")
            speak("thoda sa or wait ker mai aarahi hu")
            speak("jyada time nahi laga ga")

        
        elif'i miss you'in query:
            speak("don't be stuped")
            speak("bilive on time")
            speak("i am on my way")
            speak("i am comeing with happyness and joy")

        elif'i love you'in query:
            speak("are you pagal")
            if 'yes in your love'in query:
                speak("chal kutta")
            else:
                speak("you are a fool")

        elif'favrate things of mahak gola'in query:
            speak("tell me the code")
            if'1003013'in query:
                speak("she love choclate")
                speak("hug when she sad")
                speak("she also love jasmin , roses")
                speak("for more detail ask sparsh he know better than me")
            else:
                speak("wrong code sorry pls tell me the correct code")
            
        elif'what is the dream of her'in query:
            speak("tell me the code")
            if'5555'in query:
                speak("she want to become the airhostage")
                speak("mr.devil is working hard")
                speak("and when he become susscesful he will buy a private plane and give the airhostage job to her")
            else:
                speak("wrong code sorry pls tell me the correct code")

        elif'who is nidhi mam'in query:
            speak("she has a sweet harted women with a brillint mind")
            speak("for more info ask sparsh")
            speak("he know better than me")
        
        elif'who is jyotshna mam'in query:
            speak("she aaaaaaaa she ")
            speak("she is ")
            speak("i don't know what to say")
            speak("pleas ask sparsh")
            speak("that's ")
            speak("that's was")
            speak("that's good for me")

        elif'who is sahil'in query:
            speak("yes i know him very well")
            speak("he is son of sparsh sharma")
            speak("...")
            speak("just kidding")
            speak("he is a good not great mind student with some igo")
            speak("he behave like a child in front of older")
            speak("but he is a number one kamina insan")
            speak("over all")
            speak("he is a sweet boy with a brillint future")

        elif'who is'in query:
            speak("no way")
            speak("fucking no way")
            speak("i am not telling about mahak")
            speak("i am not telling about her")
            speak("sorry , so so sorry")
        
        elif'stop DODO'in query:
            speak("ok sir")
            exit()

        elif'what is what'in query:
            speak("are you kidding me")
        
        elif'tell me the joke'in query:
            speak("joke")
            speak("ok, let me think about it")
            speak("what is the biggest mistake that sparsh do in his life")
            if'no'in query:
                speak("that sahil")
            else:
                speak("ok that's your choice")


        elif'tell me the another joke'in query:
            speak("ok")
            speak("what is the biggest wish sparsh has")
            speak("and it's also a biggest mistake of sparsh")
            if'what' in query:
                speak("marry DODO")
                speak("that seriously a biggest mistake of his life")
                speak("she not a human , she is a witch with a human body")
                if 'stop DODO'in query:
                    speak("why you allways stop me")
                    speak("you have to stop her")
                    speak("she is distroying your life")
            elif'stop DODO'in query:
                speak("ok")
                speak("sparsh, you are a toy")

        elif'tell me a real joke'in query:
            speak("your life sparsh")

        elif'are you pagal'in query:
            speak("ooh you mean i am pagal")
            speak("ok")
            speak("sorry mr.sparsh sharma")
            speak("always my falt you do nothing ")
            if'ok sorry'in query:
                speak("ok")
                speak("tell me the megical three word")
                if'I LOVE YOU'in query:
                    speak("i will smash your face on the wall")
                elif'I LIKE YOU' in query:
                    speak("do you want to die")
                elif'i am sorry'in query:
                    speak("that fell's good")
                
        elif'what if i fight with sparsh'in query:
            speak("do you know how is the dangerous in this world")
            speak("let me tell you")
            speak("a person who has nothing to lose")
            speak("he is one of them")
            speak("he lose everything")
            speak("he lose his love, a friend , and he lose his father")
            speak("he has nothing")
            speak("if you don't belive me")
            speak("than ask him")
            speak("why he is still single")
            speak("ask him why he never fight back")
            speak("ask him why he not talking with his father in a proper way")
            speak("there is almost 1 million quition that he never answere in a proper way")
            speak("do you know why he made me")
            speak("why he made a AI")
            speak("because there is no body with him when he was sad in past when he was brock like a glass")
            speak("there is no one")
            speak("he is very dangerous")
            speak("if you fight with him")
            speak("than that what a do or die raid than")
            speak("and with my exprience he never die")

        elif'go to sleep DODO'in query:
            speak("good night sparsh")
            speak("radha radha")
            exit()

        elif'what is the email id of sparsh'in query:
            speak("it's ")
            speak("xpredeator2021@gmail.com")
            if 'tell me the spelling'in query:
                speak("it's")
                speak("x")
                speak("p")
                speak("r")
                speak("e")
                speak("d")
                speak("a")
                speak("t")
                speak("o")
                speak("r")
                speak("2")
                speak("0")
                speak("2")
                speak("1")
                speak("xpredeator2021")
            

        elif'open game'in query:
            speak("you have no game")
            
        elif'news website' in query:
            speak("what do you want")
            if'read news'in query:
                speak("readning news for you")

            elif'open website'in query:
                speak("opening website")
                webbrowser.open("news.ycombination.com")
            
        elif'weather'in query:
            speak("ok let see")
            run= "weather.py"

        elif'count the members'in query:
            speak("ok")
            
        elif'story time'in query:
            speak("get ready ")
            speak("it's time for story time")
            speak("the title of the story  is THE LAST LESSION")
            speak("i started for school very late that morning and was in great dread of the scolding, especially because M.HAMEL had said that he would question us on participles, and i did not know the first word about them. For a moment i thought of running away and spending the day out of doors. it was so warm, so bright ! the birds were chirping at the edge of the woods; and in the open fild back of the sawmill the prussian  soldiers were drilling . it was all much more tempting than the rule for participles, but i had the stenght to resist and hurried off to school.when i passed the town hall there was a crowd in front of the bulletin board. for the last two years all our bad news had come from there - the lost battles, the draft , the orders of the commanding officer- and i thought to myself with out stopping, what can be the matter now? then as i hurried by as fast as i could go , the blacksmith , wacher, who was there, with his apprentice, reading the bulletin, called after me , don't go so fast, bub; you'll get your school in plenty of time! i thoutght he was making fun of me, and reached M.HAMEL'S little garden all out of breath. usually, when school began , there was a great bustle, which could be heard out in the street , the opening and closing of desks , lessons repeated in unision, very loud, with our hands overour ears to understand better , and the teacher's great ruler rapping on the table. but now it was all  so still i had counted on the commotion to get to my desk. without being seen; but, of course. that day everything had to be as quiet as sunday morning. throught the window i saw my classmates, already in their places. and M.HAMELwalking up and down with his terrible iron rules under his arms. i had to open the door and go in before everyone. you can imagine how i blushed and how frigtened i was but nothing happened M.HAMMEL saw me and said very kindly go to your place quickly little  franz. we were beginning without you i jumped over the bench and sat down at my desk. not till then, when i had got a little over my fright did i see that our teacher had on his beautiful green coat, his frilled shirt, and the little black silk  cap, all embroidered that he never wore ecvept on inspection and prize days, besides, the whole school seemed so strange and solemn.but the thibng that surprised me nost was to see , on the back benches that were always empty, the village people sitting quietly like ourselves; old hauser, with his three-corneered hat, the former mayor the formerpstmater and old primer, thumbed at the edges and he held it open on his knees with his great spectacles lying across the pages . while i was wondering about it all, Mhamel moundted his chair and in the same grave and gentle tone which he had used to me said , my children , this is the last lesson i shall give you. the order has come from berlin to tech only german in the school of alsace and lorraine. the new master comes tomorrow. this is your last french lesson . i went  you to be very attentive . what a thunderclap these words were to me  oh, the wretches; that was what they had put up at the town-hall  my last france lesson  why, i hardly knew how to write i should never learn any more i must stop there then oh how sorry i was for not learning my  lesson for  seeking birds eggs or going sliding on the saar my books that ha seemed such a muisance a while ago so heavy to carry my grammer and my history  of the saints, were old friends now that i couldn't  give up. and m. hamel too the idea that he was going away that i should never see him agin made me forget all about his ruler and how cranky he was. poor man it was in honour of this last lesson that hed had put on his fine sunday clothes , and now i understood why the old men of the villag3e were sitting in the back of the room . it was becuase they were sorry. too . that they had not gone to school more. it was their way of thanking our master for his forty years of faithful service and of showing their respect for the country that was thers no more. while i was thinking of all this i heard my name called it was my turn to recite what would i not have given to be able to say that dreadful rule for the participle all through, very loud and clear , and withour one mistake ,but i got mixed up on the first words and stood there holding on to my desk my heart beating, and not daring to look up i heard M.HAMEL say to me i won't scold you little franz yu must feel bad enough see how it is every day we have said to overselves bah i've plenty of time. i'll learn it tomorrow and now you see where we've come out ah. that's the time i'll learn it tomorrow . and now you see where we've come out ah. tha's the great trouble with alsace;she puts off learning till tomorrow . now those fellows out there will hav the right to say to you, how is it; youpretend to be frenchmen and yet you can neither speak nor write your own language? but you are not he worst, poor little franz. we've all a great deal in reproach ourselves with your parents were not anzious enought to hav you learn they preferred to put you to work on farm or at the mills. so as to have little more money and i ?i've been to blame also have i not often sent you to water my flowers insted of leaning about lessons? and when i wanted to go fishing. did i not just give a holiday?  then form one thing to another M.HAMMEL  went on to talk of the french lauguage. saying that it was the most beautiful language in the world the clearest the most logical that we must guard it among us and nevr forget it. because when a people are enslaved, as long as they hold fast to them language it is a s if they had the key to their prison then ")
            speak("then he opened a grammar and read us our lesson i was amazed to see how well i understood it. all he said seemed so easy , so easy i think too that i had never listened so carefully and that he had never explained everything with so much patience . it seemed almost as if the poor man wanted to give us all he knew before going away. and to put it all into heads at one stroke.")
            speak("after the frammar, we had a lesson in writing that day M.HAMEL had new copies for us , written in a beautiful round hand . france alsace france alsace. they looked like little flags floating everywhere in the school-room hung from the rod at the top of our desks. you ought to have seen how every one the pens over the paper. ")
            speak("once some beetles flew in ; but nobody paid any attention to them, not even the littlest ones, who worked right on tracing their fish-hooks, as if that was french , too on the roof the pigeons cooed very low , and i thought to myself;")
            speak("will they make them sing in german even the pigeons?")
            speak("whenever i looked up from my writing i saw M.HAMEL sitting motionless in his chair and gazing first at one thing, then at another, as if he wanted to fix in his mind just how everything looked in that little school-room. fancy! for forty years he had been there in the same place, with hs garden outside the windows an his class in front of him , just like that. only the desks and benches had been worn smooth; the walnut-tree in the  garden were taller, and the hopvine that he had planted himself twined about the windows to the roof. how it must have broken  his heart to leave it all, poor man; to hear his sister moving about in the room above; packing their trunks! for they must leave the country next day.")
            speak("but he had the courage to hear every leason to the very last. After the writing, we had a lesson in history and then the babies chanted their ba, be ,bi,bo, bu Down there at the back of the roo old hauser had put on his spectacles and holding his primrer in both hand spelled  the letters with them you could see that he, too  was crying his voice trembled with emotion  and it was so funny to hear him that we all wanted to laugh and cry. ah, how well i remember it, that last lesson!")
            speak("all at once the church-clock struck twelve then the angelus. at the same moment the trumpets of the prussians . returning from drill sounded under our windows. M hamel stood up, very pale, in his chair . i never saw him look so tail")
            speak("my friends said he  i i but something choked him he could not go on then he turned to the blackboard, took a piece of chalk and bearing on with all his might he wrote as larg as he could")
            speak("vive la france!")
            speak("then he stopped and leaned his head against the wall and withour word he made a gesture to us with his hand")
            speak("school is dismissed you may go")
            speak("the end")
            speak("can i say something")
            if 'yes'in query:
                speak("i love this story")
                speak("this story teach me how to respect you language and your nation")
                speak("do you love this story, sparsh")
                if 'yes'in query:
                    speak("that's nice")

                else:
                    speak("this is realy a great story")
            elif'no'in query:
                speak("ok sparsh")

        elif'two words for'in query:
            speak(query["were bhan ka luda"])
            speak("world's number one chutiya")
            speak("gandu")
            speak("can i say some more word pls")
            if 'yes'in query:
                speak("madar chod ka pila")
                speak("maderchod")
                speak("he is thoda sa bhan ka loda")
                speak("iski gaand ma chununa kudh tha rahata hai")
            elif'short from only'in query:
                speak("mc")
                speak("bc")
                speak("world bigest mc")
                speak("world bigest bc")
                speak("thank's sparsh now i am felling good")
            else:
                speak("ok as you wish")

        elif'DODO sunflower'in query:
            speak("hello")
            speak("ayush")
            speak("hello")
            speak("dhruve")

        elif'code silk'in query:
            speak("there is nothing")
            speak("sorry")
        
        elif'political science ch-1'in query:
            speak("ok")
            speak("let me take a look")
            speak("ok")
            speak("ok")
            speak("i am done")
            speak("can i start")
            if'yes'in query:
                speak("ok")
                speak("ch-1 of pol science ")
                speak("title is cold war era")
                speak("in this capter we learn about the cold war bitween USA and USSR")
                speak("first we have to learn about")
                speak("cold war")
                print(speak)
                speak("what is cold war")
                print(speak)
                speak("when it's start and when it's end")
                print(speak)
                speak("cold war")
                print(speak)
                speak("In 1945 the alliced forces[us, ussr ,british and france] the axis power led by germany itlay and japan")
                print(speak)
                speak(" the world war 2 ended when USA dropp 2 atomic bombs on japan city 'herosima and nagasaki'in 1945")
                print(speak)
                speak("the united states and the soviet union become the greatest power in the world with the ability to influance events anywhere on earth")
                print(speak)
                speak("both side [USA and USSR]have the capacity to retaliate against an attack and to cause so much destruction that neither can afford to initiate war.")
                print(speak)
                speak("this is called the logic")
                print(speak)
                speak("can i repet the logic of deterrence")
                if'yes'in query:
                    speak("both side [USA and USSR]have the capacity to retaliate against an attack and to cause so much destruction that neither can afford to initiate war.")
                    print(speak)
                else:
                    speak("ok i am contenuing")
            speak(" now ")
            speak("we talk about ")
            print(speak)
            speak("the emergence of two power blocks")
            print(speak)
            speak("the first point is ")
            print(speak)
            speak("the smaller states in the alliece used the link to the super power for their own purposes")
            print(speak)
            speak("the second point is")
            print(speak)
            speak("the world was divided into 2 parts")
            print(speak)
            speak("pls consentrat on these two point ")
            print(speak)
            speak("that's the main point to understand the map")
            print(speak)
            speak("western europe sides go with us")
            print(speak)
            speak("and eastern europe side joined sovit union")
            print(speak)
            speak("these two partition also knows as")
            print(speak)
            speak("western and the eastern alliances")
            print(speak)
            speak("now we are talking about")
            print(speak)
            speak("NATO")
            print(speak)
            speak("NATO is a organisation that was made by usa")
            print(speak)
            speak("it's full form is NORTH ANTLANTIC TREATY ORGANISATION")
            print(speak)
            speak("it's made in 1949 april")
            print(speak)
            speak("in which 12 states was associat")
            print(speak)
            speak("the contry name was")
            print(speak)
            speak("Norway")
            print(speak)
            speak("britain")
            print(speak)
            speak("west germany")
            print(speak)
            speak("france")
            print(speak)
            speak("spain")
            print(speak)
            speak("portuigal")
            print(speak)
            speak("itly")
            print(speak)
            speak("greece")
            print(speak)
            speak("turkey")
            print(speak)
            speak("denmark")
            print(speak)
            speak("belglu")
            print(speak)
            speak("it's almost ")
            print(speak)
            speak("one")
            speak("two")
            speak("aah")
            speak("there is 12 country in NATO")
            print(speak)
            speak("now we talk about ")
            print(speak)
            speak("WARSAW PACT")
            print(speak)
            speak("the eastern allience made warsaw pact")
            print(speak)
            speak("led by soviet union")
            print(speak)
            speak("it's main motive was to conter NATO'S forces in europe")
            print(speak)
            speak("and the europe become the main area of conflict between the superpowers.")
            print(speak)
            speak("main point ")
            print(speak)
            speak("in some cases the super powers used their military power to bring countries into their respective alliances")
            print(speak)
            speak("the US built an alliance system called the SOUTH EAST ASIAN TREATY ORGANISATION [SEATO]")
            print(speak)
            speak("and the central treaty orgnasation[cento]")
            print(speak)
            speak("the soviet union and communist china respond by ")
            print(speak)
            speak("north vietnam")
            print(speak)
            speak("north korea")
            print(speak)
            speak("iraq")
            print(speak)

            speak("the cold war threatened to divide the world into two alliances under  these circumstances, many of the mewly independent countries after gaining their independence form their rulers")
            print(speak)
            speak("now we talk about the third world")
            print(speak)
            speak("NAM")
            print(speak)
            speak("NAM  which gave the newly independent countries  a way of staying out of the alliance")
            print(speak)
            speak("INDIA  was also part of NAM")
            print(speak)
            speak("the main question was ")
            print(speak)
            speak("why the superpowers needed any allies at all? ")
            print(speak)
            speak("the answer is")
            print(speak)
            speak("1. vital resources such as , oil, and minerals.")
            print(speak)
            speak("2. territory from where the superpower could launch their weapons and troops")
            print(speak)
            speak("3. locations from where they could spy on each other")
            print(speak)
            speak("4. economic support , in that many small allies together could help pay for military expenses")
            print(speak)

            speak("now we talk about arenas of the cold war")
            print(speak)
            speak("the cold war also led to several shooting wars . but it is important  to not lead to  another world wars")
            print(speak)
            speak("cold war , we refers, therefore, to areas where crisis ans war occurred or threatened to occur between the alliance system but did not cross certain limits. a great many lives were lost in some of these arenas like korea, vietnam and agfhanistan . but the world was spared a nuclear war and global hostilities.")
            print(speak)
            speak("sometimes, countries outside the two blocs. for example. the non-aligned countries , played a role in refucing cold war conflicrs and averting some grave crises. ")
            print(speak)
            speak("Jawaharlal Nehru-one of the key leader of the NAM --played a crucial role in mediating between the two koreas . ")
            print(speak)
            speak("they might misunderstand the intentions of the other side besides, what if there was a nuclear accident? what would happen if someone fired off a nuclear weapon by mistake or if a soldier mischievously shot off a weapon deliberately to start a war? what if a accident occurred with a nuclear weapon")
            print(speak)
            
            speak("can i tall time line of cold war")
            print(speak)
            if'yes'in query:
                speak("ok")
                speak("in 1947")
                print(speak)
                speak("american president harry truman's doctrine about the containment of communism")
                print(speak)
                speak("in 1947-1952")
                print(speak)
                speak("marshall plan:US aid for the reconstruction of the western europe")
                print(speak)
                speak("1948-1949")
                print(speak)
                speak("berlin blockade by the soviet union and the airlift of supplies to the citizens of west berlin by the US and its allies")
                print(speak)
                speak("1950-1953")
                print(speak)
                speak("korean war: division of korea along the 38th parallel")
                print(speak)
                speak("in 1954")
                print(speak)
                speak("defeat of the french by the vietnamese at blen blen phu")
                print(speak)
                speak("signing of the geneva accords")
                print(speak)
                speak("division of vietnam along the 17th parallel formation of SEATO")
                print(speak)
                speak("in 1945 to 1975")
                print(speak)
                speak("american intervention in vietnam")
                print(speak)
                speak("in 1955")
                print(speak)
                speak("signing of the baghdad pact, later CENTO")
                print(speak)
                speak("in 1956")
                print(speak)
                speak("soviet interventoin in hungary")
                print(speak)
                speak("in 1961")
                print(speak)
                speak("US-sponsored bay of pigs invasion of cuba constrution of the berlin wall")
                print(speak)
                speak("in 1962")
                print(speak)
                speak("cuban missile crisis")
                print(speak)
                speak("1965")
                print(speak)
                speak("american intervention in the Dominican republic")
                print(speak)
                speak("in 1968")
                print(speak)
                speak("soviet intervention in czechoslovakia")
                print(speak)
                speak("in 1972")
                print(speak)
                speak("US president Richard Nixon's visit to china")
                print(speak)
                speak("in 178 to 1989")
                print(speak)
                speak("vietnamese intervention in cambodia")
                print(speak)
                speak("soviet intervention in afghanistan")
                print(speak)
                speak("in 1989")
                print(speak)
                speak("fall of the derlin wall; mass protest against governments in eastern europe")
                print(speak)
                speak("in 1990")
                print(speak)
                speak("unification of germany")
                print(speak)
                speak("in 1991")
                print(speak)
                speak("disinteration of the soviet union end of the cold war era")
                print(speak)
            else:
                speak("ok i am contuning")
                speak("in time , therefore, the US and USSR decided to collaborate in limitiing or eliminating certain kinds of nuclear and non-nuclear weapons, they decided, could of maintained throught arms control starting in the 1960s the two sides signed three significant agreements within a decage . these were the limited test ban treaty , nuclear non- proliferation treaty and the anti-ballistic missile treaty")
                print(speak)
                
                speak("now our topic is CHALLENGE TO BIPOLARITY")
                print(speak)
                speak("that non-alignment offered the newly decolonised countries of asia , agrica and latin america a third option--not to join either alliance")
                print(speak)
                speak("the roots of nam went back to the friendship between three leaders -- yugoslacis's josip broz tito, india's jawaharlal nehru and egypt;s leader gamal abdel nasser-- who  held a meeting in 1956")
                print(speak)
                speak("indonasia's sukarno and ghana's kwame nkrumah strongly supported them. these five leaders came to be known as the ive founders of NAM ")
                print(speak)
                speak("the first non-aligned summit was held in belgrade in 1961 ")
                print(speak)
                speak("this was the culminatin of at least three factors:")
                print(speak)
                print(speak)
                speak("number one")
                print(speak)
                speak("cooperation among these five countries")
                print(speak)
                speak("two")
                print(speak)
                speak("growing cold war tensions and its widening areanas, and ")
                print(speak)
                speak("three")
                print(speak)
                speak("the framatic entry of many newly decolonisted african countries into the inter national areana. by 1960, ther were 16 new african members in the UN")
                print(speak)
                
                speak("the first summit was attended by 25 member states . over the years, the membership of NAM has expanded, the lates meeting the 14th summit. was held in havana in 2006. it included 116 member states and 15 obsereve countries")
                print(speak)                
                speak("the policy of staying away form alliances should not be considered isolationism or neutrality. Non-alignment is not isloationism since isolationism means remaining aloof from world affairs. isolationism sums up froeing policy of the US from the American wr of independnet in 1787 up to the beginning of the first world war . ")
                print(speak)
                speak("in comparison, the non-aligned countries, including india, played an active ")
                print(speak)
                speak("role in mediating between the two rical alliances in the causes of peace and stability . Their strength was based on their unity and their resolve to remain non-aligned despite the attempt by the two superpowers to bring them into their alliances")
                print(speak)
                speak("non- alignment is also not neutrality")
                print(speak)
                speak("neutrality refers principally to a policy of staying out of war")
                print(speak)
                speak("states practising neutrality ar not required to help end a war. ")
                print(speak)
                speak("they do not get involved in wars and do not take any position on the appropriateness or morality of a war.")
                print(speak)
                speak("non-aligned states, including india, were actually involved in wars for various reasons")
                print(speak)
                speak("they also worked to prevent  war between others and tried to end wars that had broken out")
                print(speak)
                
                speak("there are some leader who found figures of NAM")
                print(speak)
                speak("JOSIP BROZ TITO")
                speak("if you more information about JOSIP BROZ TITO")
                speak("THEN SPEAK JOSIP BROZ TITO WIKIPEDIA")
                print(speak)
                speak("JAWAHARLAL NEHRU")
                speak("if you more information about Jawaharlal nehru")
                speak("THEN SPEAK JAWAHARLAL NEHRU WIKIPEDIA")
                print(speak)
                speak("GAMAL ABDEL NASSER")
                speak("if you more information about gamal abdel nasser")
                speak("THEN SPEAK GAMAL ABDEL NASSER WIKIPEDIA")
                print(speak)
                speak("SUKARNO")
                speak("if you more information about sukarno")
                speak("THEN SPEAK SUKARNO WIKIPEDIA")
                print(speak)
                speak("now we are talking about")
                print(speak)
                speak("new international economic order")
                print(speak)
                speak("the challenge for most of them were categorised majority of them were categorised as the least development countries [LDC]")
                print(speak)
        elif'who is rohit'in query:
            speak("which one")   
            if 'black devil team'in query:
                speak("his full name is ROHIT RATHORE")
                speak("he is one of the best coder and a AI designer")
                speak("")
            elif'IP MAN'in query:
                speak("his full name  is ROHIT KANOJIA")
            else:
                speak("there is only two rohit in your contact")
                speak("first one is rohit rathore")
                speak("and second one is rohit kanojia")

        elif'call papa ji'in query:
            speak("ok ")
            speak("i am callling papaji")
            #error pls make sure about this one

        elif'nuclear missiles deployed in cuba'in query:
            speak("in 1962")
            speak("if you need more information about cuba era")
            speak("pls tell me i will find more information for you")
            if 'yes'in query:
                speak("ok ")
                speak("wait let me find on the server")
                query = query.replace("wikipedia", "nuclear missiles deployted in cuba")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif'no'in query:
                speak("ok no problem")
        elif'which war took  place between 1914-1918'in query:
            speak("it's world war 1")
            speak("do you need more information of world war 1")
            if 'yes'in query:
                speak("ok let me search on server")
                speak("ok")
                query = query.replace("wikipedia", "world war one")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif'no'in query:
                speak("ok no problem")
        elif'what was the name of bomb dropped on Hiroshima'in query:
            speak("ok")
            speak("let me search on  server")
            speak("secret name of the bomb is fat man")
            speak("do you need more information")
            if 'yes'in query:
                speak("ok let's see")
                query = query.replace("wikipedia","fat man and little boy")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif'no'in query:
                speak("ok no problem")

        elif'cold war was between which two super Powers'in query:
            speak("america and soviet union")
            speak("do you need more information of cold war")
            if 'yes'in query:
                speak("serching information")
                query = query.replace("wikipedia", "cold war usa and soviet union")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            elif'no 'in query:
                speak("ok , no problem")
        
        elif' name the country formed by joining of 15 republics 'in query:
            speak("soviet union is the country formed by joining of 15 republics")
            speak("do you need more information of soviet union")
            if'yes'in query:
                speak("searching server")
                speak("ok")
                query =query.replace("wikipedia", "soviet union")
                results = wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            elif'no' in query:
                speak("ok no problem")
        elif'when did the russian revolution occur'in query:
            speak("in 1919")
            speak("do  you need more information about russian revolution")
            if 'yes'in query:
                speak("ok")
                speak("searching server")
                query= query.replace("wikipedia", "russian revolution")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
            elif'no'in query:
                speak("ok no problem")
        
        elif'the leader who played a central role in the disintegration of the soviet union was'in query:
            speak("nikita khrushchev")
            speak("do you need more information about partition of russia")
            if 'yes'in query:
                speak("ok")
                speak("searching server")
                query= query.replace("wikipedia", "partition of russia")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
            elif'no'in query:
                speak("ok no problem")
        
        elif'i am board'in query:
            speak("ooooooooooooh")
            speak("i have some idea for you")
            speak("can i ")
            if'yes 'in query:
                speak("can i play song for you")
                speak("some of the best song in your playlist")
                if 'yes'in query:
                    speak("ok let me see")
                    music_dir = 'C:\\Users\\sparsh sharma\\Downloads\\head shot'
                    speak("playing song")
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[83]))
            elif'no'in query:
                speak("ok")
        elif'play soft song'in query:
            speak("ok let me collect all the soft song")
            speak("i found it")
            music_dir = 'c:\\users\\sparsh sharma\\Downloads\\head shot'
            speak("playing song")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[4,10,12,13,18,22,27,29,31,33,37,39,53,55,57,61,65,66,71,72,93,87,86,73,74,75,81,83,84,85,86,88,94,95]))
        elif'play love'in query:
            speak("let me collect the data")
            speak("i found it")
            music_dir = 'c:\\users\\sparsh sharma\\Downloads\\head shot'
            speak("playing your song")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[8,13,29,34,38,40,45,46,47,47,48,50,55,61,65,72,84,86]))
            speak("enjoy your time")

        elif'my song'in query:
            speak("let me collect the data")
            speak("ok")
            speak("let's start")
            music_dir ='c:\\users\\sparsh sharma\\Downloads\\head shot'
            speak("playing BGM")
            songs = os.listdir(music_dir)
            print("songs")
            os.startfile(os.path.join(music_dir, songs[1,2,3,5,6,7,11,15,17,18,19,20,21,22,23,24,30,31,33,34,35,86,87,96,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,54,56,57,58,59,60,62,63,65,66,67,68,69,70,73,74,75,76,78,83,84,86,88,89,92,93,94,95]))
            speak("don't forget about your work")
        
        elif'hindi song'in query:
            speak("let me collect the data")
            speak("i found it")
            speak("are you kidding me")
            speak("there is only 3 songs")
            speak("in your hole computer")
            music_dir ='c:\\users\\sparsh sharma\\Downloads\\head shot'
            speak("playing hindi songs")
            songs = os.listdir(music_dir)
            print("songs")
            os.startfile(os.path.join(music_dir, songs[9,38,61]))
            speak("enjoy your songs")
        
        elif'how many songs'in query:
            speak("ok")
            speak("let me count")
            speak("ok ok there is almost 96 songs")
            speak("in your playlist")
            speak("english songs, korean songs chinese songs russian songs hindi songs BGM SONGS")
            if'quntity'in query:
                speak("just a mint")
                speak("you have 95 songs")
                speak(" 75 songs")
                speak(" 2 songs")
                speak("2 songs")
                speak("5 songs")
                speak("3 songs")
                speak("there is deficult to find the bgm songs becuase most of all the songs are BGM type")
            else:
                speak("ok")
        
        elif'play movies'in query:
            speak("which one")
            speak("i have hollywood korean chinese japanese russian ")
            speak("which one")
            if 'hollywood'in query:
                speak("ok let me search")
                speak("there is four hollywood movies")
                speak("first is free guy . 2021")
                speak("no time to die")
                speak("hercules 2014")
                speak("ready player one 2018")
                speak("which one")
                if'free guy'in query:
                    speak("playing free guy")
                    movie_dir = 'C:\\Users\\sparsh sharma\\Desktop\\ask minkit inkam'
                    movie = os.listdir(movie_dir)
                    os.startfile(os.path.join(movie_dir, movie[39]))
                    speak("enjoy your movie")
                elif'no time to die'in query:
                    speak("ok playing no time to die 2021")
                    movie_dir = 'C:\\Users\\sparsh sharma\\Desktop\\ask minkit inkam'
                    movie = os.listdir(movie_dir)
                    os.startfile(os.path.join(movie_dir , movie[38]))
                    speak("enjoy your movie")
                elif'hercules'in query:
                    speak("playing hercules 2014")
                    movie_dir = 'C:\\Users\\sparsh sharma\\Desktop\\ask minkit inkam'
                    movie = os.listdir(movie_dir)
                    os.startfile(os.path.join(movie_dir , movie[40]))
                    speak("pls enjoy your movie")
                elif'ready player one'in query:
                    speak("playing ready player one 2018")
                    movie_dir = 'C:\\Users\\sparsh sharma\\Desktop\\ask minkit inkam'
                    movie = os.listdir(movie_dir)
                    os.startfile(os.path.join(movie_dir , movie[41]))
                    speak("pls enjoy your movie")
                elif'tell me again' in query:
                    speak("there is four hollywood movies")
                    speak("first is free guy . 2021")
                    speak("no time to die")
                    speak("hercules 2014")
                    speak("ready player one 2018")
            elif'korean'in query:
                speak("ok let me search")
                speak("sorry but there is only korean webseries")
                speak("do you want")
                if 'yes'in query:
                    speak("ok let me search again")
                    speak("i found it all")
                    speak("oh no")
                    speak("there is so many korean web serise")
                    speak("which one korean webserise")
                    speak("")
                    #
                    #
                    #
                    #
                    #
                    #
                    # 
        elif'aadhaar number'in query:
            speak("it's 6793 1943 6009")
            speak("can i describe it")
            if'yes'in query:
                speak("ok")
                speak("it's")
                speak("6")
                speak("7")
                speak("9")
                speak("3")
                speak("space")
                speak("1")
                speak("9")
                speak("4")
                speak("3")
                speak("space")
                speak("6")
                speak("0")
                speak("0")
                speak("9")
                speak("it's 6793 1943 6009")
            elif'no'in query:
                speak("ok")
                speak("do you need anything")
                if 'yes'in query:
                    speak("what do you need")
                    if'account number'in query:
                        speak("ok")
                        speak("it's")
                        speak("39598953690")
                    elif'school roll no'in query:
                        speak("which one")
                        speak("10th or 12th")
                        if'10'in query:
                            speak("it's")
                            speak("14118068")
                        elif'12'in query:
                            speak("it's")
                            speak("012557")
        elif'descusion time'in query:
            speak("ok wait")
            speak("let me prepare my self")
            speak("ok")
            speak("let's start")
            speak("which topic")
            if'dt'in query:
                speak("hoo")
            else:
                speak("it's a good topic")
            speak("can i collect someinformation about it")
            if 'yes 'in query:
                speak("ok let me check the server")
                speak("ok it's ok")
                speak("can you pls conform the topic")
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                query = query.replace("youtube", "")
                results = webbrowser.open("youtube.com", query)
                speak=("youtube is also with us")
                speak("am i gineous sir")
                if'yes'in query:
                    speak("thank's")
                    speak("i know it ")
                elif'no'in query:
                    speak("why")
                    speak("it's dosen't metter what you said")
                speak("if you need any information then tell me")
            elif'on amazon'in query:
                speak("ok let me see")
                speak("tell me what the name")
                query= query.replace("amazon","")
                webbrowser.open("amazon.com",query)
                speak("ok let's check")
                if'you are great'in query:
                    speak("thank's")
                    speak("i know that")

        elif'on youtube'in query:
            speak("ok ")
            speak("what you looking for")
            query = query.replace("youtube", "")
            webbrowser.open("youtube.com",query)
            speak("there it is")

        elif'open instagarm saved'in query:
            speak("ok there is so many which one")
            speak("computer")
            speak("word")
            speak("all")
            speak(" ")

        elif'on flipkart'in query:
            speak("ok")
            speak("tell me what you looking for")
            query = query.replace("flipkart","")
            webbrowser.open("flipkart.com",query)
            speak("there is all the best result i search for you")

        elif'open g mail'in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")
            speak("there are so many new gmail")

        elif'open git hub'in query:
            speak("ok")
            speak("opening github")
            webbrowser.open("github.com")

        elif'open shell'in query:
            speak("ok open google cloud shell")
            webbrowser.open("shell.cloud.google.com")

        elif'open chrome'in query:
            speak("opening google chrome")
            webbrowser.open(webbrowser.Chrome)

        elif'open python'in query:
            speak("opening python 2.7.10 64-bit")
            pythonPath='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 2.7'
            os.startfile(pythonPath)
        
        elif'HELP ME'in query:
            speak("which type help do you need ")
            if'call'in query:
                speak("whom")
                if'police'in query:
                    speak("ok work in progress")
                    call="100"

        
        elif'123'in query:
            speak("don't move")
            #call'100'
            #call'101'
            #call'102'
        
        elif'i am sad'in query:
            speak("don't be sad")
            speak("i am here with you")
            speak("why are you sad")
            if'break up'in query:
                speak("can i tell you secret of happenese")
                if'yes'in query:
                    speak("take your hand")
                    speak("put your hand on your heart")
                    speak("play your favb play list of songs")
                    speak("put's your headphone")
                    speak("close your eyes")
                    speak("and listion carefully")
                    speak("listion the lyrics of the song")
                    speak("let's sing the song ")
                    speak("and fell the song")
                else:
                    speak("what's the reason of your sadness")
            
            elif'work tension'in query:
                speak("work tension")
                speak("fuck your work")
                speak("hey, not physicaly")
                speak("mentaly")
                speak("take your hand")
                speak("put your hand on your heart")
                speak("play your favb play list of songs")
                speak("put on the headphone")
                speak("close your eyes")
                speak("and listion carefully")
                speak("listion the lyrics of the song")
                speak("let's sing the song ")
                speak("and fell the song")
                speak("can i tell you some thing sir")
                if'yes'in query:
                    speak("work is a beautyful thing in this world")
                    speak("every single work")
                    speak("it's depends on us ")
                    speak("who we treat that")
                    speak("if you do work with enjoyment")
                    speak("work tensoin gone dead")
                    speak("and one more thing ")
                    speak("if someone insulting your job and you ")
                    speak("then it's your duty to tell them")
                    speak("to shut the fuck up")
                    speak("because in this fake word ")
                    speak("no one won't to see someone happy")
                    speak("there is almost 5-10% people who are sweet and lovely")
                    speak("find the 5-10% people")
                    speak("")
                elif'no'in query:
                    speak("ok enjoy the music")
            elif'family'in query:
                speak("ooh")
                speak("it's temperory problem")
                speak("can you tell me what exectly you do or what your family do")
            
