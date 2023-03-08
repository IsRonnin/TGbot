import telebot
from telebot import types
from tokn import *

bot = telebot.TeleBot(TOKEN)

def videos(message):
    markup = types.InlineKeyboardMarkup()
    [markup.add(types.InlineKeyboardButton(text=key, url=videos_l[key])) for key in videos_l.keys()]
    bot.send_video(message.chat.id, 'https://media.giphy.com/media/B6odR0DhsStfW/giphy.gif')
    bot.send_message(message.chat.id, text="Лови эти *прекрасные свежие* видео!", reply_markup=markup, parse_mode= 'Markdown')

def home_work(message):
    markup = types.InlineKeyboardMarkup()
    [markup.add(types.InlineKeyboardButton(text=key, url=home_work_l[key])) for key in home_work_l.keys()]
    bot.send_video(message.chat.id, 'https://media.giphy.com/media/ExMGjbktr4phe/giphy.gif')
    bot.send_message(message.chat.id, text="Лови эту *прекрасную свежую* домашку!", reply_markup=markup, parse_mode= 'Markdown')

commands = {"Домашка": home_work, "Видео": videos}


videos_l = {"Установка джанги": "https://youtu.be/5nqyiSZ4G9k", "Запись 3 веба 2 модуля": "https://youtu.be/AR_xd7kbRas", 
            "настройка среды": "https://youtu.be/_HmBBaIb2VI", "Как сжать дз?": "https://youtu.be/JvmqW3DLb4k",
            "Как залить дз на лмс?": "https://youtu.be/ym_0md8PNj4"}

home_work_l = {"Дз за 1 модуль": "https://github.com/IsRonnin/Module_1_hometasks",
               "Дз за 2 модуль": "https://github.com/IsRonnin/HomeWorks_module2",
               "Игра за 1 модуль": "https://github.com/IsRonnin/Game"}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    [markup.add(types.KeyboardButton(key)) for key in commands.keys()]
    bot.send_video(message.chat.id, 'https://media.giphy.com/media/xT77XZrTKOxycjaYvK/giphy.gif')
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Я бот для помощи вам созданный от скуки... Как думаете я нужен? Отызвы писать -> IsRonnin's".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    try:
        answ = commands[message.text]
        if type(answ) is str:
            bot.send_message(message.chat.id, text=answ)
        else:
            answ(message)
    except Exception as e:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


        '''
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        [markup.add(types.KeyboardButton(key)) for key in commands.keys()]
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для перенаправления вас.".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


        
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
'''
bot.polling(none_stop=True)

