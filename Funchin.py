import pyttsx3
import os
import webbrowser
import time
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *
import sys
import requests


# Глобальные переменные
text = ''
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
adress = ''
j = 0
task_number = 0



def hello(): #функция приветствия
    os.system("echo Приветик. OBIITO. Есть вопросы ? | RHVoice-test -p Anna")

def plans():
    os.system("echo Моя задача будет состоять в том, чтобы помочь управлять системой Умный дом.\
                    В настоящее время мы работаем над виртуальной частью программного обеспечения.\
                    Мы также работаем над оптимизацией всех существующих функций в коде.\
                    В дальнейшем мы планируем работать над технической частью проекта.\
                    Она будет состоять из создания элементов умного дома с использованием микроконтроллеров Arduino.\
                    В конечном итоге виртуальная и техническая части проекта будут объединены.\
                    Моя конечная цель будет достигнута.| RHVoice-test -p Anna")

def alexa():
    os.system("echo Меня зовут Alexa. Я простой голосовой помошник, \
                    предназначенный для упрощения пользования системой Линукс.\
                    Создал меня разработчик OBITO. Будут ли вопросы ко мне? | RHVoice-test -p Anna")

def time(): #  узнает время
     import datetime
     now = datetime.datetime.now()
     os.system("echo Сейчас %d %d | RHVoice-test -p Anna" % (now.hour, now.minute))


def clear_analis(): # очистка файла с историей запросов
    file = open('commands.txt', 'w', encoding = 'UTF-8')
    file.close()
    os.system("Файл аналитики был очищен! | RHVoice-test -p Anna")


def github():  # открывает гитхаб
    os.system("echo Открываю твою страницу Гитхаба | RHVoice-test -p Anna")
    webbrowser.open('https://github.com/OB11TO')

def brows(): # открывает браузер
    os.system("echo Открываю | RHVoice-test -p Anna")
    webbrowser.open('https://google.ru')


def ovk(): # открывает вк
    os.system("echo Вк открыт  | RHVoice-test -p Anna")
    webbrowser.open('https://vk.com/feed')

def youtube(): # открывает ютюб
    os.system("echo Открываю youtube | RHVoice-test -p Anna")
    webbrowser.open('https://www.youtube.com')

def update(): # проверка обновления
	os.system('sudo apt-get update')

def upgrade(): # установка обновлений
	os.system('sudo apt-get upgrade')

def shut(): # выключает компьютер
    global quit
    os.system('sudo shutdown -h now')
    quit()

def playLILPump(): #включает пампа
    os.system("echo Включаю Лил пампа | RHVoice-test -p Anna")
    webbrowser.open('https://www.youtube.com/watch?v=DPxL7dO5XPc')

def musik(): # включает музыку
    webbrowser.open('https://vk.com/')

def web_search(): # осуществляет поиск в интернете по запросу (adress)
    global adress
    webbrowser.open('https://yandex.ru/yandsearch?clid=2028026&text={}&lr=11373'.format(adress))

def check_translate():
    global text
    word = text
    word = word.replace('переведи','').strip()
    webbrowser.open('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text={}'.format(word))
    text = ''

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


def weather():
    url = 'https://wttr.in'
    weather_parameters = {
        '1': '',
        'T': '',
        'M': '',
        'lang':'ru'
        }
    response = requests.get(url, params=weather_parameters)
    print(response.text)
    os.system("echo Ваш прогноз погоды | RHVoice-test -p Anna")

def quit(): # функция выхода из программы
    global engine
    os.system("echo Обращайтесь OBIITO | RHVoice-test -p Anna")
    engine.stop()
    os.system('cls')
    exit(0)
