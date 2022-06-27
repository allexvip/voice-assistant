import os
import sys
import webbrowser
import requests
import subprocess
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи

def speaker(text):
    engine.say(text)
    engine.runAndWait()


def browser():
    webbrowser.open('https://yandex.ru')
    print('браузер запущен')


def game():
    subprocess.Popen(r'C:\Users\Alex\AppData\Roaming\Telegram Desktop\Telegram.exe')
    print('игра')


def weather():
    print('погода')


def offpc():
    # os.system('shutdown /s')
    print('выключаю ПК')


def offbot():
    sys.exit()

def show_audiodevice_list():
    print(os.system('python - m sounddevice'))

def passive():
    pass

