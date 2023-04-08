import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.token)


places = ['Холл', 'Столовая', 'Амфитеатр', 'Переговорные', 'Галерея', 'Кабинеты']
language_data = {}


@bot.message_handler(commands=['lang'])
def set_lang(message):
    user = message.chat.id
    if user not in language_data.keys():
        language_data[user] = 'en'
    else:
        if language_data[user] == 'ru':
            language_data[user] = 'en'
        else:
            language_data[user] = 'ru'
    bot.send_message(message.chat.id, f'Язык успешно сменён на {language_data[user]}')


@bot.message_handler(commands=['restart', "help", 'start', "↩ Назад"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("💬 Меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="Приветствую {0.first_name}, я бот-гид по Новгородской технической школе. \nПусть я пока только начинаю свою работу, но уже могу немало.".format(
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
    text = 'Мы небольшая команда разработчиков из Великого Новгорода под названем "Случается". Связь с нами - t.me/+geI14xdOI-RiYjhi'
    bot.send_message(message.chat.id,
                     text=text.format(
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
                     text="Что нужно тебе, странник?".format(
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


@bot.message_handler(func=lambda message: message.text == "Что такое НТШ")
def about_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    text='НТШ это - Инновационная образовательная площадка эпохи цифровой экономики. Ведущие компании региона, лаборатории ' \
         'мирового уровня и студенты НТШ вместе решают задачи новой промышленной революции в сфере ключевых технологий.' \
         '\nВ школе ведется переподготовка кадров для высокотехнологичных предприятий России и создаются новые модели бизнеса.'
    bot.send_message(message.chat.id,
                     text=text.format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "Фотографии")
def photos_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="фоточки".format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "Лабаратории НТШ")
def otdels_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    text = """В НТШ 16 различных лабораторий:
1. Медицинская информатика (https://novtechschool.ru/lab6)
2. Нейротехнологии (https://novtechschool.ru/lab11)
3. Биобанк, геномный инжиринг (https://novtechschool.ru/lab3)
4. Промышленный дизайн (https://novtechschool.ru/lab13)
5. Мехатроника и робототехника (https://novtechschool.ru/lab5)
6. Автономный транспорт (https://novtechschool.ru/lab10)
7. BIM-технологии (https://novtechschool.ru/lab15)
8. Интеллектуальная электроника (https://novtechschool.ru/lab4)
9. Новые материалы (https://novtechschool.ru/lab12)
10. Микро- и нанотехнологии (https://novtechschool.ru/lab7)
11. Неразрушающий контроль (https://novtechschool.ru/lab2)
12. Виртуальная и дополненная реальность (AR/VR) (https://novtechschool.ru/lab8)
13. Кибер-безопасность (https://novtechschool.ru/lab14)
14. Техническое зрение (https://novtechschool.ru/lab16)
15. Прототипирование (https://novtechschool.ru/lab17)
16. Искусственный интеллект (https://novtechschool.ru/lab19)
Заинтересовала какая-то лаборатория? Нажми на ее номер в списке для получения подробностей."""
    bot.send_message(message.chat.id,
                     text=text.format(
                         message.from_user), reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "История НТШ")
def history_of_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text='18 сентября 2019 года Владимиру Путину был представлен проект, а уже спустя два месяца, 13 ноября, был '
                          'заложен первый камень. Более подробно вы можете увидеть по нажатию кнопки) (https://novtechschool.ru/chronicle)'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Об ИНТЦ Валдай")
def about_ntsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В меню")
    text = """Направления научно-технологической деятельности, осуществляемой на территории интеллектуального научно-технического центра   
Разработка и создание новых, в том числе портативных, источников энергии
Разработка биомедицинских клеточных технологий
Разработка и создание мобильной сети связи 5-го поколения
Разработка и создание интернета вещей (приборы, устройства, системы, программные платформы)"""
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text=text.format(
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
    btn1 = types.KeyboardButton("Предоставить местоположение", request_location=True)
    btn2 = types.KeyboardButton("В меню")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Я могу построить Вам маршрут до НТШ!', reply_markup=markup)


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


@bot.message_handler(content_types=['location'])
def handle_loc(message):
    a_cord = message.location.longitude
    b_cord = message.location.latitude
    u = f'https://yandex.ru/maps/?mode=routes&rtext={b_cord}%2C{a_cord}~58.538431%2C31.278384'
    bot.send_message(message.chat.id, f'Ваш маршурт до НТШ:\n{u}')


print('Started')
bot.infinity_polling() 
