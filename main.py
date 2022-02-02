import re
import telebot
from time import strftime, sleep
from Bot import Bot
import config

Sergey = Bot(answers=config.answers)

SergeyTelegram = telebot.TeleBot(config.BOT_TOKEN, parse_mode='HTML')

print('Bot running...')

@SergeyTelegram.message_handler(commands=['start'])
def StartCommand(message):
    sleep(1)
    SergeyTelegram.send_message(message.chat.id, 'Привет. Меня зовут Сергей, и я создан специально для тебя. У меня ты можешь спросить погоду, время, поговорить со мной')

@SergeyTelegram.message_handler(regexp=r'(?:подо|)жди \d \w')
def RPS(message):
    SergeyTelegram.reply_to(message, "Хорошо")
    if 'сек' in (text:=message.text.split())[2]:
        sleep(int(text[1]))
    elif 'мин' in text[2]:
        sleep(int(text[1])*60)
    elif "час" in text[2]:
        sleep(int(text[1])*3600)
    elif re.search('д[е|]н[ь|я|ей]', text[2]):
        sleep(int(text[1])*86400)
    SergeyTelegram.send_message(message.chat.id, 'Подождал, что нибудь еще?')

@SergeyTelegram.message_handler(content_types=['text'])
def Answers(message):
    UserText = message.text.lower()
    Answer = Sergey.GetAnswer(UserText)
    print(message.from_user.first_name, message.from_user.last_name)
    print(UserText)
    print(Answer)
    SergeyTelegram.send_message(message.chat.id, Answer)

try:
    SergeyTelegram.infinity_polling()
except KeyboardInterrupt:
    print("Operation stopped by user")