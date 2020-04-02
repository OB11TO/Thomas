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
import commands


# Глобальные переменные
text = ''
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
adress = ''
j = 0
task_number = 0

ndel = ['Alexa', 'Алекса', 'Алекс']

commands = ['Приветик','открой гитхаб', 'открой файл', 'down comp', 'выруби компьютер', 'Спасибо', 'покажи файл','покажи список команд',
'open vk', 'открой браузер', 'open vk', 'открой интернет', 'открой youtube', 'включи музон','вруби музыку','сколько время', 'очисти файл',
'открой стату', 'покажи cтатистику', 'покажи красивую девушку', 'открой музыку', 'переведи', 'планы', 'на будущее', 'что планируется', 'play lil pump','загугли']

# Описания функций комманд
def pri_com(): # выводит на экран историю запросов
    z = {}
    mas = []
    mas2 = []
    mas3 = []
    mas4 = []
    file = open('commands.txt', 'r', encoding = 'UTF-8')
    k = file.readlines()
    for i in range(len(k)):
        line = str(k[i].replace('\n','').strip())
        mas.append(line)
    file.close()
    for i in range(len(mas)):
        x = mas[i]
        if x in z:
            z[x] += 1
        if not(x in z):
            b = {x : 1}
            z.update(b)
        if not(x in mas2):
            mas2.append(x)
    for i in mas2:
        mas3.append(z[i])
    for i in range(1, len(mas3)+1):
        mas4.append(str(i)+') ')
    list = pd.DataFrame({
        'command' : mas2,
        'count' : mas3
    }, index = mas4)
    list.index.name = '№'
    print(list)

def plans():
    global engine
    os.system("echo Моя задача будет состоять в том, чтобы помочь управлять системой Умный дом.\
                    В настоящее время мы работаем над виртуальной частью программного обеспечения.\
                    Мы также работаем над оптимизацией всех существующих функций в коде.\
                    В дальнейшем мы планируем работать над технической частью проекта.\
                    Она будет состоять из создания элементов умного дома с использованием микроконтроллеров Arduino.\
                    В конечном итоге виртуальная и техническая части проекта будут объединены.\
                    Моя конечная цель будет достигнута.| RHVoice-test -p Anna")


def time():
     import datetime
     now = datetime.datetime.now()
     os.system("echo Сейчас время %d часа %d минут| RHVoice-test -p Anna" % (now.hour, now.minute))


def clear_analis(): # очистка файла с историей запросов
    global engine
    file = open('commands.txt', 'w', encoding = 'UTF-8')
    file.close()
    os.system("Файл аналитики был очищен! | RHVoice-test -p Anna")

def add_file(x): # история запросов
    file = open('commands.txt', 'a',encoding = 'UTF-8')
    if x != '':
        file.write(x+'\n')
    file.close()

def web_search(): # осуществляет поиск в интернете по запросу (adress)
    global adress
    webbrowser.open('https://yandex.ru/yandsearch?clid=2028026&text={}&lr=11373'.format(adress))

def check_searching(): # проверяет нужно-ли искать в интернете
    global text,wifi_name,add_file
    global adress
    global web_search
    if 'загугли' in text:
        add_file('загугли')
        adress = text.replace('загугли','').strip()
        text = text.replace(adress,'').strip()
        web_search()
        text = ''
    elif 'загугли' in text:
        add_file('загугли')
        adress = text.replace('загугли','').strip()
        text = text.replace(adress,'').strip()
        web_search()
        text = ''
    adress = ''

def clear_task(): #удаляет ключевые слова
    global text,ndel
    for z in ndel:
        text = text.replace(z,'').strip()
        text = text.replace('  ',' ').strip()

def hello(): #функция приветствия
    global engine
    os.system("echo Приветик. OBIITO. Есть вопросы ? | RHVoice-test -p Anna"),

def quit(): # функция выхода из программы
    global engine
    os.system("echo Обращайтесь OBIITO | RHVoice-test -p Anna")
    engine.stop()
    os.system('cls')
    exit(0)

def github():  # открывает гитхаб
    os.system("echo Открываю твою страницу Гитхаба | RHVoice-test -p Anna")
    webbrowser.open('https://github.com/OB11TO')

def brows(): # открывает браузер
    os.system("echo Открываю | RHVoice-test -p Anna")
    webbrowser.open('https://google.ru'.format(textSearch))


def ovk(): # открывает вк
    os.system("echo Вк открыт  | RHVoice-test -p Anna")
    webbrowser.open('https://vk.com/feed')

def youtube(): # открывает ютюб
    os.system("echo Открываю youtube | RHVoice-test -p Anna")
    webbrowser.open('https://www.youtube.com')

def shut(): # выключает компьютер
    global quit
    os.system('sudo shutdown -h now')
    quit()

def playLILPump(): #включает пампа
    os.system("echo Включаю Лил пампа | RHVoice-test -p Anna")
    webbrowser.open('https://www.youtube.com/watch?v=DPxL7dO5XPc')

def musik(): # включает музыку
    webbrowser.open('https://vk.com/')

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
