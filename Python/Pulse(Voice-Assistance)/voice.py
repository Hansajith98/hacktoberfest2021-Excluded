import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import webbrowser
import youtube_dl
from googleapiclient.discovery import build
import os
from selenium import webdriver
from playsound import playsound


#Initializing the object for pttxs3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#voices[0] will give male vocals while voices[1] will give female
engine.setProperty('voice',voices[0].id)
youtube_api=input("Enter your api key for Youtube")


def get_url(url):
    api_key=youtube_api
    youtube=build('youtube','v3',developerKey=api_key)
    print("here")
    req=youtube.search().list(q=url,part='snippet',type='video')
    req=req.execute()
    val=(req['items'][0]['id']['videoId'])
    return ('https://youtube.com/watch?v='+val)  


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        speak('Listening..')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio)
        time.sleep(2)
        print('Recognizing...')
        print(f"user said {query} \n")
    except Exception : 
       speak('Please Say Again')
       return "none"
    return query    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
        speak('Good Morning!')
    elif hour >=12 and hour<18 :
        speak('Good Afternoon!')
    else:
        speak('Good evening!')   
    speak('Hello I am Pulse')
    time.sleep(1)
    speak('How may I help you?') 
    
    
    
if __name__ == "__main__":
    wishme()
    while True:
       query=takeCommand().lower()  
       if 'wikipedia' in query:
           speak("searching wiipedia")
           query=query.replace('wikipedia',"")
           results=wikipedia.summary(query, sentences=2)
           print(results)
           speak("according to wikipedia")
           speak(results)
       elif 'open youtube' in query:
            speak('opening')
            browser=webdriver.Chrome()
            browser.get('https://www.youtube.com/')
       elif 'song' in query:
            # speak('playing')
            
            # browser=webdriver.Chrome()
            query=query.replace('play song',"")
            url=get_url(query)
            # print('playing')
            print(url)
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '720',
            
            }],
             }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
            except:
                pass
            for file in os.listdir("./"):
                print(file)
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            playsound('song.mp3')
            speak('song finished')
       elif 'google search' in query:
            speak('searching')
            browser=webdriver.Chrome()
            query=query.replace('google search',"")
            browser.get('https://www.google.com/')
            browser.find_element_by_name("q").send_keys(query)
            time.sleep(2)
            browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]").click()
            
       elif 'exit' in query:
           speak("ok bye")
           break    
       else:
            pass
            #more to be written