import telebot
import config
import random
from telebot import types
import massive
import sqlite3
"""
conn = sqlite3.connect('data/db_shawarma.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('SELECT name, name_shawarma FROM characters menu_shawarma'),
                   (user_id, user_name, user_surname, username))
    conn.commit()


SELECT *
FROM menu_shawarma
WHERE weapon = 'pistol';
"""

#Клавиатура для приветствия
item1 = types.KeyboardButton("Пожелать хорошего дня!☺️☺️☺️")
item2 = types.KeyboardButton("Сделать заказ!🧾🌯🔥")
item3 = types.KeyboardButton("Кинуть кости🎲🎲🎲")
markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
markup.add(item1, item2, item3)

#Клавиатура для выбора двух направлений
button_menu_shawarma_hall_1 = ("Выбрать из меню🧾")
button_menu_shawarma_hall_2 = ("Собрать свою🌯")
button_menu_shawarma_hall_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_menu_shawarma_hall_0.add(button_menu_shawarma_hall_1,
                                button_menu_shawarma_hall_2)

#Клавиатура меню с готовой шаурмой
button_menu_shawarma_0 = massive.menu
button_menu_shawarma_next_step = ("Готово")
markup_menu_shawarma = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
markup_menu_shawarma.add(button_menu_shawarma_0 [0],
                         button_menu_shawarma_0 [1],
                         button_menu_shawarma_0 [2],
                         button_menu_shawarma_0 [3],
                         button_menu_shawarma_next_step)


#Клавиатура для лаваша
button_lavash_0 = massive.lavash
button_lavash_next_step = ("Далее :\n"
                           "Мясо")
button_lavash = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_lavash.add(button_lavash_0[0],
                  button_lavash_0[1],
                  button_lavash_0[2],
                  button_lavash_0[3],
                  button_lavash_next_step)


#Клавиатура для мяса
button_meat_0 = massive.meat
button_meat_next_step = ("Далее :\n"
                           "Овощи")
button_meat = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_meat.add(button_meat_0 [0],
                button_meat_0 [1],
                button_meat_0 [2],
                button_meat_0 [3],
                button_meat_next_step)


#Клавиатура для овощей
button_components_0 = massive.produce
button_components_next_step = ("Далее :\n"
                               "Соус")
button_components = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
button_components.add(button_components_0 [0],
                      button_components_0 [1],
                      button_components_0 [2],
                      button_components_0 [3],
                      button_components_0 [4],
                      button_components_0 [5],
                      button_components_0 [6],
                      button_components_0 [7],
                      button_components_0 [8],
                      button_components_0 [9],
                      button_components_0 [10],
                      button_components_next_step)


#Клавиатура для выбора соуса
button_souce_0 = massive.souce
button_souce_next_step = ("Далее :\n"
                          "На сколько поджарить лаваш")
button_souce = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_souce.add(button_souce_0[0],
                 button_souce_0[1],
                 button_souce_0[2],
                 button_souce_0[3],
                 button_souce_0[4],
                 button_souce_0[5],
                 button_souce_0[6],
                 button_souce_0[7],
                 button_souce_0[8],
                 button_souce_next_step)

#Клавиатура для выбора уровня поджарки лаваша
button_hot_0 = massive.hot
button_hot_next_step = ("Готово")
button_hot = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_hot.add(button_hot_0[0],
               button_hot_0[1],
               button_hot_0[2],
               button_hot_next_step)





markup_choice = {
    'button_lavash', 'False'
    'button_meat', 'False'
    'button_components', 'False'
    'button_souce', 'False'
    'button_hot', 'False'
}




'''@bot.message_handler(content_types=['text'])
def welcome(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Пожелать хорошего дня!☺️☺️☺️':
            bot.send_message(message.chat.id, 'И вам прекрасного дня!🔥🔥🔥')
            sti_nice = open ('good_day.mp4', 'rb')
            bot.send_animation(message.chat.id, sti_nice)
        elif message.text == "Сделать заказ!🧾🌯🔥" :
            bot.send_message(message.chat.id, 'Будем рады принять ваш заказ!', reply_markup=types.ReplyKeyboardRemove())#сделать чтоб после этого ответа выскочило меню
        elif message.text == "Кинуть кости🎲🎲🎲" :
            sti_luck = open('kubik.mp4', 'rb')
            bot.send_animation(message.chat.id, sti_luck)
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        else:
            bot.send_message(message.chat.id, 'Не балуйтесь, лучше киньте кости)')

def menu(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_menu_1 = types.KeyboardButton("Выбрать из меню🧾")
    button_menu_2 = types.KeyboardButton("Собрать свою🌯")
    markup.add(button_menu_1, button_menu_2)
    if message.chat.type == 'private':
        if message.text == 'Выбрать из меню🧾':
            bot.send_message(message.chat.id, 'И вам прекрасного дня!🔥🔥🔥',
                             reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Собрать свою🌯" :
            bot.send_message(message.chat.id, 'Будем рады принять ваш заказ!,',
                             reply_markup=types.ReplyKeyboardRemove())
        else:
            pass




def menu_shawarma(message: types.Message):
    button_menu_shawarma_0 = menu[0]
    button_menu_shawarma_1 = menu[1]
    button_menu_shawarma_2 = menu[2]
    button_menu_shawarma_3 = menu[3]
    markup_menu_shawarma = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu_shawarma.add(button_menu_shawarma_0,button_menu_shawarma_1,
                             button_menu_shawarma_2,button_menu_shawarma_3)
    if message.chat.type == 'private':
        if message.text == button_menu_shawarma_0:
            bot.send_message(message.chat.id, 'Добавлено🔥',
                             reply_markup=types.ReplyKeyboardRemove())
        elif message.text == button_menu_shawarma_1:
            bot.send_message(message.chat.id, 'Добавлено🔥',
                             reply_markup=types.ReplyKeyboardRemove())
        elif message.text == button_menu_shawarma_2:
            bot.send_message(message.chat.id, 'Добавлено🔥',
                             reply_markup=types.ReplyKeyboardRemove())
        elif message.text == button_menu_shawarma_3:
            bot.send_message(message.chat.id, 'Добавлено🔥',
                             reply_markup=types.ReplyKeyboardRemove())
        else:
            pass


'''
