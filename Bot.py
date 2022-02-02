from random import choice as random_choice
from random import randint as random_integer
import re
from time import sleep as wait
from time import strftime as time
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

WEATHER_TOKEN: str = "4052ee0b6353371d1b7acdc7bfe593a8"

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM(WEATHER_TOKEN, config_dict)
manager = owm.weather_manager()


def rps_result(player1, player2):
    equal = 'ничья'
    more = 'победа'
    less = 'поражение'
    if player1 == 1:
        if player2 == 1:
            return equal
        elif player2 == 2:
            return more
        elif player2 == 3:
            return less

    if player1 == 2:
        if player2 == 1:
            return less
        elif player2 == 2:
            return equal
        elif player2 == 3:
            return more

    if player1 == 3:
        if player2 == 1:
            return more
        elif player2 == 2:
            return less
        elif player2 == 3:
            return equal


def get_weather(sity: str) -> dict:
    observation = manager.weather_at_place(sity)
    weather = observation.weather
    weather_detailed = weather.detailed_status
    temp = weather.temperature('celsius')['temp'],
    temp_min = weather.temperature('celsius')['temp_min'],
    temp_max = weather.temperature('celsius')['temp_max']
    return {'weather': weather_detailed, 'temp': float(temp[0]), 'temp_min': float(temp_min[0]),
            'temp_max': float(temp_max)}


def rock_paper_scissors(player_choice: int):  # Rock, paper, scissors
    s_player_choice = random_integer(1, 3)  # Second Player Choice
    rps_data = {1: 'камень',
                2: 'ножницы',
                3: 'бумага', }
    result = rps_result(player_choice, s_player_choice)
    return f'Ваш выбор: {rps_data[player_choice]}\nВыбор Оппонента: {rps_data[s_player_choice]}\nРезультат: {result}'


class Bot:
    def __init__(self, answers=dict(None)):
        self.answers = answers

    def get_answer(self, question: str) -> str:
        for i in list(self.answers.keys()):
            if question in i:
                if type(answer := self.answers[i]) == str:
                    return answer
                elif type(answer) == tuple:
                    return random_choice(answer)
        else:
            return 'я тебя не понял'

    def add_q_and_a(self, question: str, answer: str) -> None:
        if question in self.answers:
            if type(self_answer := self.answers[question]) == str:
                self_answer = (self_answer, answer)
                return None

            elif type(self_answer) == tuple:
                self_answer = (*self_answer, answer)
                return None
        else:
            self.answers[question] = answer

    def set_answer(self, question, answer):
        for i in list(self.answers.keys()):
            if question in i:
                self.answers[question] = answer
            else:
                raise ValueError(f"This bot has no question '{question}'")
