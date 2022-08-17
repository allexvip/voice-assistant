import os
import sys
import webbrowser
import requests
import subprocess
import pyttsx3
import datetime
from words import data_set, TRIGGERS
import random
from bs4 import BeautifulSoup
import keyboard
import sounddevice as sd

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи

in_Speak = False


def speaker(text):
    in_Speak = True
    engine.say(text)
    engine.runAndWait()
    in_Speak = False


def ican(text):
    questions = list(data_set.keys())
    questions.pop(0)
    speaker(f"Я отвечаю на следующие фразы: {', '.join(questions)}")


def writeText(text_data):
    keyboard.write(text_data)
    speaker(f"окей")


def browser(text):
    webbrowser.open('https://yandex.ru')
    print('браузер запущен')


def game(text):
    subprocess.Popen(r'C:\Users\Alex\AppData\Roaming\Telegram Desktop\Telegram.exe')
    print('игра')


def weather(text):
    print('погода')


def offpc(text):
    os.system('shutdown /s')
    print('выключаю ПК')


def offbot(text):
    sys.exit()


def showAudioDeviceList(text):
    print(sd.query_devices())


def gettime(text):
    now = datetime.datetime.now()
    hour = now.hour
    minutes = str(now.minute)
    if len(minutes) < 2:
        minutes = '0' + minutes
    speaker(f"В Москве {hour} {minutes}")


def runanekdot(text):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.52'
    }

    url = 'https://www.anekdot.ru/random/anekdot/'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    anekdot = soup.find_all('div', class_="text")
    anekdot_list = []
    i = 0
    for article in anekdot:
        if i == 5:
            break
        else:
            i = i + 1
        anekdot_text = article.text.strip().replace(".", ",")
        print(anekdot_text)
        speaker(anekdot_text)
        anekdot_list.append(anekdot_text)
    # anekdot_text = random.choice(anekdot_list)
    # print(anekdot_text)
    # speaker(anekdot_text)


def runexchange(text):
    pass


def passive(text):
    pass
