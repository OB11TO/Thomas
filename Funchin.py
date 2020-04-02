import os
import webbrowser
import time
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *
import sys
import keyboard



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

def time():
     import datetime
     now = datetime.datetime.now()
     os.system("echo Сейчас время %d часа %d минут| RHVoice-test -p Anna" % (now.hour, now.minute))


def clear_analis(): # очистка файла с историей запросов
    file = open('commands.txt', 'w', encoding = 'UTF-8')
    file.close()
    os.system("Файл аналитики был очищен! | RHVoice-test -p Anna")


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
