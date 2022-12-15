import telebot
import config
import random
from telebot import types
import button
import sqlite3
import class_user_db


bot = telebot.TeleBot(config.token)

conn = sqlite3.connect('data/db_shawarma.db', check_same_thread=False)
cursor = conn.cursor()




def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR REPLACE INTO user (user_id, user_name, user_surname, user_nickname) '
                   'VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()

def db_order(user_id: int):
    cursor.execute('INSERT OR REPLACE INTO user_order (user_id, menu_shawarma_id, ord_id, addres , time , user_name) '
                   'VALUES (?, ? , ? , ? , ? , ?)',
                   (user_id, button.button_menu_shawarma_0))
    conn.commit()


@bot.message_handler(commands=['start'])
def hello(message):
    sti = open('media/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n"
                                      "Я - <b>{1.first_name}</b>, "
                                      "бот созданный чтобы ты вкусно поел!"
                                      .format(message.from_user, bot.get_me()),
                                      parse_mode='html', reply_markup=button.markup)

    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    user_nickname = message.from_user.username

    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=user_nickname)


    @bot.message_handler(regexp="Пожелать хорошего дня!☺️☺️☺️")
    def welcome(message: types.Message):
        bot.send_message(message.chat.id, 'И вам прекрастного дня!🔥🔥🔥')
        sti_nice = open('media/good_day.mp4', 'rb')
        bot.send_animation(message.chat.id, sti_nice)

    @bot.message_handler(regexp="Кинуть кости🎲🎲🎲")
    def welcome(message: types.Message):
        sti_luck = open('media/kubik.mp4', 'rb')
        bot.send_animation(message.chat.id, sti_luck)
        bot.send_message(message.chat.id, str(random.randint(0, 100)))

    @bot.message_handler(regexp="Сделать заказ!🧾🌯🔥")
    def hall(message: types.Message):
        bot.send_message(message.chat.id, 'Будем рады принять ваш заказ!',
                         reply_markup=button.button_menu_shawarma_hall_0)


#============================THE 1ST LINE=============================================


@bot.message_handler(regexp=str(button.button_menu_shawarma_hall_1))
def menu(message: types.Message):
    bot.send_message(message.chat.id, 'Выберите из списка:',
                     reply_markup=button.markup_menu_shawarma)

    @bot.message_handler(regexp=button.button_menu_shawarma_0[0])
    def chicken(message: types.Message):
        bot.send_message(message.chat.id, 'Добавлено🔥',)


    @bot.message_handler(regexp=button.button_menu_shawarma_0[1])
    def beef(message: types.Message):
        bot.send_message(message.chat.id, 'Добавлено🔥',)

    @bot.message_handler(regexp=button.button_menu_shawarma_0[2])
    def pork(message: types.Message):
        bot.send_message(message.chat.id, 'Добавлено🔥',)

    @bot.message_handler(regexp=button.button_menu_shawarma_0[3])
    def turkey(message: types.Message):
        bot.send_message(message.chat.id, 'Добавлено🔥',)

    @bot.message_handler(regexp=button.button_menu_shawarma_next_step)
    def turkey(message: types.Message):
        bot.send_message(message.chat.id, 'Ожидайте заказ🔥🔥🔥',
                         reply_markup=types.ReplyKeyboardRemove())





'''
    @bot.message_handler(regexp=str(button.markup_menu_shawarma))
    def menu_shawarma(message: types.Message):
        try:
            if message.text == str(button.button_menu_shawarma_0):
                if message.text == str(button.button_menu_shawarma_0[0]):
                    bot.send_message(message.chat.id, 'Добавлено🔥',
                                     reply_markup=types.ReplyKeyboardRemove())
                elif message.text == str(button.button_menu_shawarma_0[1]):
                    bot.send_message(message.chat.id, 'Добавлено🔥',
                                     reply_markup=types.ReplyKeyboardRemove())
                elif message.text == str(button.button_menu_shawarma_0[2]):
                    bot.send_message(message.chat.id, 'Добавлено🔥',
                                     reply_markup=types.ReplyKeyboardRemove())
                elif message.text == str(button.button_menu_shawarma_0[3]):
                    bot.send_message(message.chat.id, 'Добавлено🔥',
                                     reply_markup=types.ReplyKeyboardRemove())
                elif message.text == str(button.button_menu_shawarma_next_step):
                    bot.send_message(message.chat.id, 'Ожидайте!🔥🔥🔥')
                else:
                    bot.send_message(message.chat.id, 'Нет такого блюда')
            else:
                return()
        except Exception as e:
            print(repr(e))
'''
#============================THE 2ND LINE==============================================



@bot.message_handler(regexp = button.button_menu_shawarma_hall_2)
def menu(message: types.Message):
    bot.send_message(message.chat.id, 'Выбирайте поочереди, пока не соберется '
                                      'шаверма мечты:)\nНачнём с лаваша:',
                     reply_markup=button.button_lavash)

    @bot.message_handler(regexp=button.button_lavash_next_step)
    def lavash(message: types.Message):
        bot.send_message(message.chat.id, 'Теперь выберите мясо:',
                         reply_markup=button.button_meat)

    @bot.message_handler(regexp=button.button_meat_next_step)
    def meat(message: types.Message):
        bot.send_message(message.chat.id, 'Теперь выберите овощи:',
                         reply_markup=button.button_components)

    @bot.message_handler(regexp=button.button_components_next_step)
    def components(message: types.Message):
        bot.send_message(message.chat.id, 'Теперь выберите соус:',
                         reply_markup=button.button_souce)

    @bot.message_handler(regexp=button.button_souce_next_step)
    def souce(message: types.Message):
        bot.send_message(message.chat.id, 'Теперь выберите уровень прожарки лаваша:',
                         reply_markup=button.button_hot)

    @bot.message_handler(text=button.button_hot_next_step)
    def hot(message: types.Message):
        bot.send_message(message.chat.id, 'Готово🔥',
                         reply_markup=types.ReplyKeyboardRemove())

#============================ORDER========================






#=========================END=============================
'''
    @bot.message_handler(content_types=['text'])
    def menu(message: types.Message):
        bot.send_message(message.chat.id, 'Добавлено🔥', reply_markup=button.button_meat)

        @bot.message_handler(content_types=['text'])
        def menu(message: types.Message):
            bot.send_message(message.chat.id, 'Добавлено🔥', reply_markup=button.button_components)

            @bot.message_handler(content_types=['text'])
            def menu(message: types.Message):
                bot.send_message(message.chat.id, 'Добавлено🔥', reply_markup=button.button_souce)

                @bot.message_handler(content_types=['text'])
                def menu(message: types.Message):
                    bot.send_message(message.chat.id, 'Добавлено🔥', reply_markup=types.ReplyKeyboardRemove())



'''



#=======================
if __name__ == '__main__':
    bot.infinity_polling()