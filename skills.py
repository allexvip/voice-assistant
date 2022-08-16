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

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def ican(text):
    questions = list(data_set.keys())
    questions.pop(0)
    speaker(f"Могу ответить на следующие вопросы: {', '.join(questions)}")

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
    print(os.system('python - m sounddevice'))


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
    for article in anekdot:
        #print(article.text.strip())
        # speaker(article.text.strip())
        anekdot_list.append(article.text.strip())
    anekdot_text = random.choice(anekdot_list)
    print(anekdot_text)
    speaker(anekdot_text)

def runexchange(text):
    pass

def passive(text):
    pass
