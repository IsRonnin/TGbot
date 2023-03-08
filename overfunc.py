from tokn import TOKEN
from telebot import types
import telebot

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
