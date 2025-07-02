import telebot  #импорт библиотеки для работы с ботом
from telebot import types #из библиотеки импотируем классы и модули для работы с клавиатурой
import random 

bot = telebot.TeleBot("My_token :)") #создаем бота

@bot.message_handler(commands = ['start']) #функция message_handler - обрабочик (обрабатывает команду /start)
def start(message):
    print(message)

    bot.send_message(message.chat.id, "Привет!👋 \nЯ бот 🤖 для игры в КАМЕНЬ-НОЖНИЦЫ-БУМАГА! \n\nДавай сыграем! \n\nНапишите /play: ") #Бот пишет нам

@bot.message_handler(commands = ["play"]) #Обрабока на команду /play
def handler_message(message):

        #Создаем клавиатуру и кнопки
        keyboard_choose = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_stone = types.KeyboardButton("Камень 🗿")
        but_paper = types.KeyboardButton("Бумага 📄")
        but_scissors = types.KeyboardButton("Ножницы ✂️")
        #Добавляем кнопки
        keyboard_choose.add(but_paper, but_scissors, but_stone)
        
        bot.send_message(message.chat.id, "Выберете элемент: ", reply_markup=keyboard_choose)

@bot.message_handler(func = lambda message : True)
def play_handler(message):

    #Создаем список с вариантами для бота
    list = ["Камень 🗿", "Бумага 📄", "Ножницы ✂️"]
    bot_choose = random.choice(list)
    
    #Основная логика
    if message.text == "Камень 🗿":
        bot.send_message(message.chat.id, f"Вы выбрали - Камень 🗿 \n\nБот выбрал - {bot_choose}")
        if message.text == bot_choose:
            bot.send_message(message.chat.id, "Ничья ⚖️")
        elif bot_choose == "Ножницы ✂️":
            bot.send_message(message.chat.id, "Вы победили! ✅")
        elif bot_choose == "Бумага 📄":
            bot.send_message(message.chat.id, "Вы проиграли ❌")
    elif message.text == "Бумага 📄":
        bot.send_message(message.chat.id, f"Вы выбрали - Бумага 📄 \n\nБот выбрал - {bot_choose}")
        if message.text == bot_choose:
            bot.send_message(message.chat.id, "Ничья ⚖️")
        elif bot_choose == "Ножницы ✂️":
            bot.send_message(message.chat.id, "Вы проиграли ❌")
        elif bot_choose == "Камень 🗿":
            bot.send_message(message.chat.id, "Вы победили! ✅")
    elif message.text == "Ножницы ✂️":
        bot.send_message(message.chat.id, f"Вы выбрали - Ножницы ✂️ \n\nБот выбрал - {bot_choose}")
        if message.text == bot_choose:
            bot.send_message(message.chat.id, "Ничья ⚖️")
        elif bot_choose == "Бумага 📄":
            bot.send_message(message.chat.id, "Вы победили! ✅")
        elif bot_choose == "Камень 🗿":
            bot.send_message(message.chat.id, "Вы проиграли ❌")
    else:
        bot.send_message(message.chat.id, "Я Вас не понимаю!")
    

bot.polling(non_stop = True)