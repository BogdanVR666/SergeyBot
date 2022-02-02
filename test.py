from Bot import Bot
import config

Sergey = Bot(answers=config.answers)

print(Sergey.GetAnswer(input(">>")))