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
    check_translate()
    text = comparison(text)
    print(text)
    check_searching()
    if (text in cmds):
        if (text != 'Приветик') & (text != 'Спасибо') & (text != 'покажи список команд'):
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

def check_translate():
    global text, tr
    tr = 0
    variants = ['переведи', 'перевести', 'переводить', 'перевод']
    for i in variants:
        if (i in text)&(tr == 0):
            word = text
            word = word.replace('переведи','').strip()
            word = word.replace('перевести','').strip()
            word = word.replace('переводить','').strip()
            word = word.replace('перевод','').strip()
            word = word.replace('слово','').strip()
            word = word.replace('слова','').strip()
            webbrowser.open('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text={}'.format(word))
            tr = 1
            text = ''


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

cmds = {
    'Приветик' : hello,                         'выруби компьютер' : shut,                   'down comp' : shut,
    'Спасибо' : quit,                              'покажи  cтатистику' : pri_com,           'загугли':web_search,
    'открой браузер' : brows,                  'включи vk' : ovk,                            'открой интернет' : brows,
    'открой youtube' : youtube,                   'вруби музыку' : musik,                      'open vk' : ovk,
    'открой  стату' : pri_com,                   'включи музон' : musik,                      'очисти файл' : clear_analis,
    'покажи файл' : pri_com,                  'открой файл' : pri_com,                  'открой музыку' : musik,
    'планы' : plans,                           'на будущее' : plans,                      'что планируется' : plans,
    'открой гитхаб' : github,                     'pump' : playLILPump,                    'сколько время' : time,
    'переведи' : check_translate,                'play lil pump': playLILPump
}


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
