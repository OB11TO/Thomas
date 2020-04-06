import pyttsx3
import os
import random
import webbrowser
import time
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *
import sys
import keyboard
from Funchin import *
from cmd import *


# Глобальные переменные
text = ''
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
adress = ''
j = 0
task_number = 0
# Имя голосового помошника
ndel = ['Alexa', 'Алекса', 'Алекс']



# Описания функций комманд
def add_file(x): # история запросов
    file = open('commands.txt', 'a',encoding = 'UTF-8')
    if x != '':
        file.write(x+'\n')
    file.close()

def clear_task(): #удаляет ключевые слова
    global text,ndel
    for z in ndel:
        text = text.replace(z,'').strip()
        text = text.replace('  ',' ').strip()

def comparison(x): # осуществляет поиск самой подходящей под запрос функции
    global commands,j,add_file
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(x,commands[i])
        if (k > 50)&(k > j):
            ans = commands[i]
            j = k
    if (ans != 'Спасибо!')& (ans != 'Приветик'):
        add_file(ans)
    return(str(ans))



# распознавание
def talk():
    global text, clear_task
    text = ''
    with sr.Microphone() as sourse:
        print('Здравстуй OB11TO: ')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse, phrase_time_limit=3)
        try:
            text = (r.recognize_google(audio, language="ru-RU")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        os.system('cls')
        lb['text'] = text
        clear_task()

# выполнение команд
def cmd_exe():
    global cmds, engine, comparison, check_searching, task_number, text, lb
    text = comparison(text)
    print(text)
    check_searching()
    if (text in cmds):
        if (text != 'Приветик') & (text!= 'как тебя зовут') & (text != 'кто ты') & (text != 'Спасибо') & (text != 'покажи список команд'):
            os.system("echo Одну секунду | RHVoice-test -p Anna")

        cmds[text]()
    elif text == '':
        pass
    else:
        print('Команда не найдена!')
    task_number += 1
    if (task_number % 10 == 0):
        os.system("echo У тебя будет еще вопрос? | RHVoice-test -p Anna")
    engine.runAndWait()
    engine.stop()


# основной бесконечный цикл
def main():
    global text, talk, cmd_exe, j
    try:
        talk()
        if text != '':
            cmd_exe()
            j = 0
    except(UnboundLocalError):
        pass
    except(TypeError):
        pass



# раздел создания интерфейса
os.system("echo Alexa к вашим услугам! | RHVoice-test -p Anna")
root = Tk()
root.geometry('250x350')
root.configure(bg = 'black')
root.title('Alexa')
root.resizable(False, False)

lb = Label(root, text = text)
lb.configure(bg = 'gray')
lb.place(x = 25, y = 25, height = 25, width = 200)

but1 = Button(root, text = 'Вопрос?', command = main)
but1.configure(bd = 1, font = ('Castellar', 25), bg = 'gray')
but1.place(x = 50, y = 160, height = 50, width = 150)

but2 = Button(root, text = 'Выход', command = quit)
but2.configure(bd = 1, font = ('Castellar',25), bg = 'gray')
but2.place(x = 50, y = 220, height = 50, width = 150)

root.mainloop()
