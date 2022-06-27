import os
import sys
import webbrowser
import requests
import subprocess


def browser():
    webbrowser.open('https://40r.ru')
    print('браузер запущен')


def game():
    subprocess.Popen('C:/')
    print('игра')


def weather():
    print('погода')


def offpc():
    #os.system('shutdown /s')
    print('выключаю ПК')


def offbot():
    sys.exit()


def passive():
    pass
