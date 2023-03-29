import os
import webbrowser
import sys
import subprocess
import os
import pygame
import re
import yt_dlp
import winshell as winshell
import voice
import random
import string
import requests
import json
import re
import pyglet
import asyncio
from datetime import datetime
import math
def youtube():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://www.youtube.com', new=2)


def browser():
    webbrowser.open('https://www.google.com', new=2)


# Установка pygame.mixer
pygame.mixer.init()

def stop_music():
    print('остоновила')
    pygame.mixer_music.stop()
    print('готово')

def music():
    # Получение текущей директории
    dir_path = os.getcwd()

    # Перемещение в директорию с музыкой
    os.chdir(dir_path + "/music")

    # Получение списка всех файлов в директории
    music_files = os.listdir()

    # Проигрывание каждой песни по очереди
    while True:
        for file in music_files:
            # Проверка, что файл - это музыка
            if file.endswith(".mp3"):
                print("Playing", file)
                pygame.mixer.music.load(file)
                pygame.mixer_music.set_volume(0.3)
                pygame.mixer.music.play()
                while pygame.mixer_music.get_busy():
                    return


def time():
    time = datetime.now()
    print(time.hour, time.minute, time.second)
    voice.speaker(f'{str(time.hour)}часов, {str(time.minute)}минут и {str(time.second)} секунды')

week_day = {
    'Monday':'понедельник',
    'Tuesday':'вторник',
    'Wednesday':'среда',
    'Thursday':'четверг',
    'Friday':'пятница',
    'Saturday':'суббота',
    'Sunday':'воскресенье',
}
def time_day():
    time = datetime.now()
    day = datetime.today().strftime("%A")
    print(day)
    print(time.day)
    voice.speaker(f"Дураста! сегодня же {str(time.day)} число, а день недели {str(week_day[day])}")


def time_month():
    time = datetime.now()
    print(time.month)
    voice.speaker(f'ну ты конечно и даешь сейчас {str(time.month)}')


def time_year():
    time = datetime.now()
    print(time.year)
    voice.speaker(f'ну вы конечно и выдали, сейчас же идёт {str(time.year)}')

numbers_for_translate = {
    1:'один',
    2:'два',
    3:'три',
    4:'четыре',
    5:'пять',
    6: 'шест',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одинадцать',
    12: 'двенадцать',
    13: 'тренадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
}
def weather():
    # вставьте свой API-ключ вместо 'YOUR_API_KEY'
    api_key = 'dc4b0ae9e71d7cb1805e6679f58276ab'
    # получаем IP-адрес пользователя
    ip_address = requests.get('https://api.ipify.org').text
    response = requests.get(url=f'http://ip-api.com/json/{ip_address}').json()
    city_name = response['city']
    # создаем URL-запрос на получение погоды для заданного города
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

    # отправляем запрос и получаем ответ
    response = requests.get(url)

    # преобразуем полученные данные в формат JSON
    data = response.json()

    # извлекаем нужную информацию из данных о погоде
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    temp = math.trunc(int(temperature)) # 3.98 >> 3
    # выводим информацию о погоде на экран
    print(f'Температура в городе {city_name}: {temperature}°C')
    print(f'Описание погоды: {description}')
    voice.speaker(f'Температура {numbers_for_translate[temp]} градуса.') # 3 >> три


def offpc():
    # Эта команда отключает ПК под управлением Windows

    # os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def directory():
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    os.makedirs("C://Users/user/desktop/" + name)


def trash():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)


def offBot():
    '''Отключает бота'''
    sys.exit()




def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
