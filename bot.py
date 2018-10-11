import os
import telebot
import random
from telebot import apihelper
from telebot.types import Message

# Configuration
TG_PROXY = 'https://103.241.156.250:8080'
TG_BOT_TOKEN = '684607438:AAGZsyi2_YxZ99SgNNY0ndOKSqM8ZWwYfhI'

# Set proxy
apihelper.proxy = {'http': TG_PROXY}

# Init bot
bot = telebot.TeleBot(TG_BOT_TOKEN)

anekdote = """Царь позвал к себе Иванушку-дурака и говорит:
– Если завтра не принесешь двух говорящих птиц – голову срублю.
Иван принес филина и воробья. Царь говорит:
– Ну, пусть что-нибудь скажут.
Иван спрашивает:
– Воробей, почем раньше водка в магазине была?
Воробей:
– Чирик.
Иван филину:
– А ты, филин, подтверди.
Филин:
– Подтверждаю."""

# /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, anekdote)

message_uhu = "Угу"
message_agree = "Подтверждаю"
talks = [message_uhu,
         message_agree]

# Plain message
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message,random.choice(talks))

# Polling
while True:
    try:
        bot.polling(none_stop=True,timeout=123)
    except Exception as e:
        logger.error(e)
        time.sleep(15)
