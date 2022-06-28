import os
import sys
import webbrowser
import requests
import subprocess
import pyttsx3
import datetime
from words import data_set, TRIGGERS

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def ican():
    questions = list(data_set.keys())
    questions.pop(0)
    speaker(f"Могу ответить на следующие вопросы: {', '.join(questions)}")


def browser():
    webbrowser.open('https://yandex.ru')
    print('браузер запущен')


def game():
    subprocess.Popen(r'C:\Users\Alex\AppData\Roaming\Telegram Desktop\Telegram.exe')
    print('игра')


def weather():
    print('погода')


def offpc():
    os.system('shutdown /s')
    print('выключаю ПК')


def offbot():
    sys.exit()


def showAudioDeviceList():
    print(os.system('python - m sounddevice'))


def gettime():
    now = datetime.datetime.now()
    hour = now.hour
    minutes = str(now.minute)
    if len(minutes) < 2:
        minutes = '0' + minutes
    speaker(f"В Москве {hour} {minutes}")


def passive():
    pass
