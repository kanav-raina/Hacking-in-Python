import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import smtplib

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak('I am an AI created by Kanav Raina')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing')
        query=r.recognize_google(audio,language='en-in')
        print("User said : {0}".format(query))
    except Exception as e:
        print('say that again please...')
        return 'None'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','password')
    server.sendmail('your email',to,content)
    server.close()




if __name__=='__main__':
    #speak('Time to play the game')
    #wishMe()
    #takeCommand()
    query='email'
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences=2)
        speak('Accordint to wikipedia')
        speak(results)
    elif 'google' in query:
        webbrowser.open('google.com')
    elif 'youtube' in query:
        webbrowser.open('youtube.com')
    elif 'stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    elif 'play' in query:
        music_dir='/home/kanav/Music/'
        songs = os.listdir(music_dir)
        #print(songs[2])
        subprocess.call(['vlc',os.path.join(music_dir,songs[2])])
    elif 'time' in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        time='The time is {0}'.format(strtime)
        speak(time)
    elif 'visual studio' in query:
        subprocess.call('code')
    elif 'email' in query:
        try:
            speak('What should i say')
            content='sending email from ai bot'
            to='enteremail@gmail.com'
            sendEmail(to,content)
            speak('Email has been sent')
        except Exception as e:
            print(e)
            speak('Email not sent')

