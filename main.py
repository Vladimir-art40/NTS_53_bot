import telebot
import config
from config import places
from telebot import types


bot = telebot.TeleBot(config.token)


language_data = {}


@bot.message_handler(commands=['start'])
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Навигатор по НТШ")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Поехали", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Навигатор по НТШ")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расположение входов")
    btn2 = types.KeyboardButton("Планы корпусов")
    btn3 = types.KeyboardButton("Места проведения")
    btn4 = types.KeyboardButton("Как дойти...")
    btn5 = types.KeyboardButton("В меню")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Навигатор по НТШ\nЧто вам нада?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Расположение входов")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_photo(message.chat.id, open('resources/inputs.jpg', 'rb'), 'Расположение входов в НТШ', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Планы корпусов")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("I Корпус")
    btn2 = types.KeyboardButton("II Корпус")
    btn3 = types.KeyboardButton("В меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Выберите корпус", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "I Корпус")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_photo(message.chat.id, open('resources/corp1.jpg', 'rb'), "План I корпуса НТШ", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "II Корпус")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_photo(message.chat.id, open('resources/corp2.jpg', 'rb'), "План II корпуса НТШ", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Места проведения Стартап Тура")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_photo(message.chat.id, open('resources/places.jpg', 'rb'), "Места проведения ", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Как дойти...")
def echo_message(message):
    markup = types.InlineKeyboardMarkup()
    for place in places:
        markup.add(types.InlineKeyboardButton(place, callback_data='apl_' + place))
    
    bot.send_message(message.chat.id, text="Где вы сейчас?", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data.startswith('apl_'))
def callback_inline(call):
    place_from = call.data[4:]
    
    markup = types.InlineKeyboardMarkup()
    for place in places:
        if place == place_from:
            continue
        markup.add(types.InlineKeyboardButton(place, callback_data='apf_' + place + '_' + place_from))
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, text=f"Из {place_from}... \nКуда вам надо?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('apf_'))
def callback_inline(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    place_to, place_from = call.data[4:].split('_')
    bot.send_message(call.message.chat.id, text=f"Гена на маршрут из {place_from} в {place_to}")


print('Started')
bot.infinity_polling()
