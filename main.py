import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.token)


places = ['Холл', 'Столовая', 'Амфитеатр', 'Переговорные', 'Галерея', 'Кабинеты']
language_data = {}


@bot.message_handler(commands=['restart', "help", 'start', "↩ Назад"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💬 Меню")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Приветствую {0.first_name}, я бот-гит по Новгородской технической школе. \nПусть я пока только начинаю свою работу, но уже могу немало.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "❓ О Стартап Type")
def about_startup_type(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    text = """Startup Tour 2023 в Великом Новгороде!
28 апреля на площадке Новгородской технической школы пройдет Startup Tour 2023 —
масштабная конференция Фонда «Сколково», посвященная технологиям в креативных индустриях.
Эксперты обсудят развитие ключевых творческих индустрий региона и перспективы CreativeTECH-
бизнеса в России, разберут кейсы и поделятся практическими советами, которые будут полезны
для продвижения креативно-технологических проектов.
Не упустите шанс узнать о CreativeTECH-трендах первыми!
Расписание:
9:00-10:00 Регистрация
9:30-10:00 Кофе-брейк
10:00-10:15 Открытие
10:15-18:00 Основной познавательный трек, Прикладной предпринимательский трек, Выставка\n
Регистрируйтесь прямо сейчас. https://startup-tour.ru/"""
    bot.send_message(message.chat.id,
                     text=text.format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "🙍‍🙍 ‍Авторы бота")
def autors(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="инфа о  нас, там ккуар кодик какой нибудь и всякое такое, там теги на нас".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "В меню" or message.text == "💬 Меню")
def return1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("❓ О Стартап Type")
    btn = types.KeyboardButton("О НТШ")
    btn1 = types.KeyboardButton("Навигатор")
    btn2 = types.KeyboardButton("О ИНТЦ Валдай")
    btn4 = types.KeyboardButton("🙍‍🙍 ‍Авторы бота")
    markup.add(btn0, btn, btn1, btn2, btn4)
    bot.send_message(message.chat.id,
                     text="Что нужно вам?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "О НТШ")
def about_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Что такое НШТ")
    btn1 = types.KeyboardButton("Фотографии")
    btn2 = types.KeyboardButton("Отделы НТШ")
    btn3 = types.KeyboardButton("История НТШ")
    btn4 = types.KeyboardButton("В меню")
    markup.add(btn, btn1, btn2, btn3,btn4)
    bot.send_message(message.chat.id,
                     text="Что конкретно вам интересно?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Что такое НШТ")
def about_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="текст о нтш, его создании и т.д.".format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "Фотографии")
def photos_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="фоточки".format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "Отделы НТШ")
def otdels_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="отделы нтш сс фоточками или без  и т.д.".format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "История НТШ")
def history_of_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="История НТШ текст или ссыль".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "О ИНТЦ Валдай")
def about_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="текст о ИНТЦ валдай,  и т.д.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Навигатор")
def nav(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Как добраться до НТШ?")
    btn1 = types.KeyboardButton("Навигатор по НТШ")
    btn2 = types.KeyboardButton("В меню")
    markup.add(btn, btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Где вы в данный момент".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Как добраться до НТШ?")
def how_to_go_to_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="[хз че тут].".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Навигатор по НТШ")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расположение входов")
    btn2 = types.KeyboardButton("Планы корпусов")
    btn3 = types.KeyboardButton("Карта Стартап Тура")
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


@bot.message_handler(func=lambda message: message.text == "Карта Стартап Тура")
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_photo(message.chat.id, open('resources/places.jpg', 'rb'), "Карта Стартап Тура", reply_markup=markup)


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
    markup.add(types.InlineKeyboardButton('Ближайший туалет', callback_data='apf_' + 'Ближайший туалет' + '_' + place_from))
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, text=f"Из {place_from}... \nКуда вам надо?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('apf_'))
def callback_inline(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    place_to, place_from = call.data[4:].split('_')
    bot.send_message(call.message.chat.id, text=f"Гена на маршрут из {place_from} в {place_to}")


print('Started')
bot.infinity_polling() 
