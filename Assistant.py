import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5') # for using inbuilt voice in windows 
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour < 12:
        speak("heyyy Good Morning !") 
    elif hour >= 12 and hour < 18:
        speak("heyyy Good Afternoon !")
    elif hour >= 18 and hour < 22:
        speak("heyyy Good Evening !")
    else:    
        speak("heyyy Good Night !")

    speak("Indienri Here, How can I help you Sir!")

def tasktodo():
  # Takes Commands from User  
     r = sr.Recognizer()
     with sr.Microphone() as mic:
         print("Listening.....")
         r.pause_threshold = 0.7   # seconds of non-speaking audio before a phrase is considered complete
         r.energy_threshold = 500  # minimum audio energy to consider for recording
         audio = r.listen(mic)   
     try:
        print("Recognizing.....")
        task = r.recognize_google(audio, language='en-in')
        print("User said : ", task)          
     except :
        #print(error)
        print("Sorry, Say that again Please!")
        return "None"
     return task
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saurabhpowar1823@gmail.com', 'SaurabhP@1452')
    server.sendmail('saurabhpowar1823@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    list = ["hello","good morning", "hi", "good afternoon", "good evening", "good night", "hola"]
    wishme()

    while True:
        task = tasktodo().lower()
        
                
        if "who is" in task:
            speak('searching...')
            try:
                task = task.replace("wikipedia", "")    
                results = wikipedia.summary(task, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry I'm not able to search at the moment")
        elif "how are you" in task:
            speak("I'm Wonderful, Tell me how can I help you")
        elif "what is" in task:
            speak('searching...')
            try:
                task = task.replace("wikipedia", "")    
                results = wikipedia.summary(task, sentences=1)
                print(results)
                speak(results)
            except:
                speak("Sorry I'm not able to search at the moment")
        
        elif "youtube" in task:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")            
        elif "google" in task:
            speak("Opening google")
            webbrowser.open("google.com")
        elif "weather" in task:
            webbrowser.open("today's weather")
        elif "play music" in task:
            music = 'F:\\Untitled'
            songs = os.listdir(music)
            speak("Playing music")
            os.startfile(os.path.join(music,songs[0]))
        
        elif "the time now" in task:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}") 
            
        elif "news" in task:
            webbrowser.open('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
        elif "open vs code" in task:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in task:
            try:
                speak("What should I say")
                content = tasktodo()
                to = "saurabhpowar1823@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except:
                speak("Sorry I'm not able to send mail at the moment")
        
        elif 'play untitled' in task:
            webbrowser.open('https://www.youtube.com/watch?v=2KsrtJ3VtZs')

        elif "quit" in task:
            exit()
        else:
            print("Sorry I can't do that")





