#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import datetime
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import pyowm
from PySide2 import QtCore, QtGui, QtWidgets
import sys
import wolframalpha
import wikipedia
import pyautogui
from time import sleep


opts = {
    'alias':('tom','thomas'),
    'tbr':('start'),
    'cmds':{
    "ctimes": ('what time','now is the time','hour','show time','time','what time'),
    'stupid': ('tell a joke', 'make me laugh'),
    'pogoda':('weather', 'show the weather', 'weather','what is the weather now', 'pagoda'),
    'search':('search','Google search','Google' 'look for','google','find'),
    'yt':('youtube'),
    'ali':('ali','aliexpress'),
    'ctd':('exit')
    }
}

# WEATHER
owm = pyowm.OWM('c17e34503b50a20cb2ccef7213239d58',language="en-US" )
place = 'Rostov-on-Don'
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp_max"]

def weath():
    if temp < 10 :
        speak("Dress as warm as possible , it is very cold outside!")
    elif temp < 20 :
        speak("Dress warmly!")
    else:
        speak("The temperature is normal, Dress to your taste!")


# GOOGLE
def srch():
  r = sr.Recognizer()
  with sr.Microphone(device_index = 3) as source:
    print("Tell me what to look for...")
    audio  = r.listen(source)

  query = r.recognize_google(audio, language="en-US").lower()
  print('You said: '+ query.lower())

  webbrowser.open('https://www.google.com/search?client=avast&q='+query.lower())

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="en-US").lower()
        print("Recognized: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Браниаку
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()


            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("Golos ne Raspoznan!")
    except sr.RequestError as e:
        speak("Sar! Proverty podkluchenie k inety")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):


    if cmd == 'ctimes':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Now" + str(now.hour) + ":" + str(now.minute))

    elif 'pogoda' in cmd:
      speak("WEATHER" + str(temp ) + ' gradusov, ' + w.get_detailed_status())
      weath()

    elif 'search' in cmd:
        srch()

    elif 'yt' in cmd:
        webbrowser.open('https://www.youtube.com/')
        speak('okey!')

    elif 'ctd' in cmd:
        pyautogui.hotkey('win','d')


    else:
        speak("Ne ponimau!")
# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 3) # по умолчанию index = 1

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!


#Распознает время и в соответствии с временем говорит приветствие
now = datetime.datetime.now()
welcome =  now.hour


# Функция времени

days = {0: u"ponedelnik", 1: u"vtornik", 2: u"sreda", 3: u"chetverk", 4: u"pyatnicha", 5: u"subbota", 6: u"voskreseniye"}
today = datetime.datetime.today()


if 13 > welcome :

  speak('Good day ')
  webbrowser.open('C:\\Users\\USER\\Music\\motivation\\rokki_balboa_motivacija_-_rocky_balboa_(zf.fm).mp3')
  speak("Now" + ' '+ days[datetime.date.today().weekday()] +'. time '+ str(now.hour) + ":" + str(now.minute) )
  speak("Weather" + str(temp ) + ' gradusov, ' + w.get_detailed_status())
  weath()

elif welcome <= 17:
  speak('Hi bro, kak dela')

elif welcome >= 18:
  speak("Hi bro, kak dela")

speak("Tom slushaet")

stop_listening = r.listen_in_background(m, callback)
while True:
  time.sleep(0.1) # infinity loop
