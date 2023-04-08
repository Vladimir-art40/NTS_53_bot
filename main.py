import telebot
import config
from telebot import types
from texts import *
from markups import *


bot = telebot.TeleBot(config.token)

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

    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, f'{lang_switch_ru} {language_data[user]}')
    else:
        bot.send_message(message.chat.id, f'{lang_switch_en} {language_data[user]}')


@bot.message_handler(commands=['restart', "help", 'start'])
def start(message):
    if message.chat.id not in language_data.keys():
        language_data[message.chat.id] = 'ru'

    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, hello_ru.format(message.from_user), 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, hello_en.format(message.from_user), 
                         reply_markup=btm_markup('en'))


### Main menu

@bot.message_handler(func=lambda message: message.text in [menu_ru, menu_en])
def return1(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, menu_text_ru.format(message.from_user), 
                         reply_markup=main_markup('ru'))
    else:
        bot.send_message(message.chat.id, menu_text_en.format(message.from_user), 
                         reply_markup=main_markup('en'))


@bot.message_handler(func=lambda message: message.text == main_menu_ru[0] 
                     or message.text == main_menu_en[0])
def about_startup_type(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, about_startup_ru.format(message.from_user), 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, about_startup_en.format(message.from_user), 
                         reply_markup=btm_markup('en'))
    

@bot.message_handler(func=lambda message: message.text == main_menu_ru[1] 
                     or message.text == main_menu_en[1])
def about_ntsh(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, about_nts_menu_text_ru.format(message.from_user), 
                         reply_markup=ants_markup('ru'))
    else:
        bot.send_message(message.chat.id, about_nts_menu_text_en.format(message.from_user), 
                         reply_markup=ants_markup('en'))


@bot.message_handler(func=lambda message: message.text == main_menu_ru[2] 
                     or message.text == main_menu_en[2])
def nav(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, hi_nuv_text_ru, 
                         reply_markup=hi_nav_markup('ru'))
    else:
        bot.send_message(message.chat.id, hi_nuv_text_ru, 
                         reply_markup=hi_nav_markup('en'))
    
    
@bot.message_handler(func=lambda message: message.text == main_menu_ru[3] 
                     or message.text == main_menu_en[3])
def about_ntsh(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, about_intc_ru, 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, about_intc_en, 
                         reply_markup=btm_markup('en'))


@bot.message_handler(func=lambda message: message.text == main_menu_ru[4] 
                     or message.text == main_menu_en[4])
def autors(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, autors_ru.format(message.from_user), 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, autors_en.format(message.from_user), 
                         reply_markup=btm_markup('en'))

### Menu About NTS

@bot.message_handler(func=lambda message: message.text == ants_menu_ru[0]
                     or message.text == ants_menu_en[0])
def about_ntsh(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, about_nts_ru.format(message.from_user), 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, about_nts_en.format(message.from_user), 
                         reply_markup=btm_markup('en'))
    

@bot.message_handler(func=lambda message: message.text == ants_menu_ru[1]
                     or message.text == ants_menu_en[1])
def photos_ntsh(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, photos_ru.format(message.from_user), 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, photos_en.format(message.from_user), 
                         reply_markup=btm_markup('en'))
    

@bot.message_handler(func=lambda message: message.text == ants_menu_ru[2]
                     or message.text == ants_menu_en[2])
def otdels_ntsh(message):
    markup = types.InlineKeyboardMarkup()

    if language_data[message.chat.id] == 'ru':
        text = labs_nts_ru
    else:
        text = labs_nts_en

    for lab in text.split('\n'):
        name = lab.split(' (')[0]
        url = lab.split(' (')[1][:-1]
        markup.add(types.InlineKeyboardButton(name, url=url))

    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, labs_nts_text_ru, 
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, labs_nts_text_en, 
                         reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == ants_menu_ru[3]
                     or message.text == ants_menu_en[3])
def history_of_ntsh(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, history_of_nts_ru, 
                         reply_markup=btm_markup('ru'))
    else:
        bot.send_message(message.chat.id, history_of_nts_en, 
                         reply_markup=btm_markup('en'))

### Part for make request of user`s location for path to nts

@bot.message_handler(func=lambda message: message.text == hi_nav_menu_ru[0]
                     or message.text == hi_nav_menu_en[0])
def ask_location(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, nav_nts_ru, 
                        reply_markup=ask_loc_markup('ru'))
    else:
        bot.send_message(message.chat.id, nav_nts_en, 
                        reply_markup=ask_loc_markup('en'))

### Nav body

@bot.message_handler(func=lambda message: message.text == hi_nav_menu_ru[1]
                     or message.text == hi_nav_menu_en[1])
def echo_message(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, nav_of_nts_text_ru, 
                        reply_markup=nav_markup('ru'))
    else:
        bot.send_message(message.chat.id, nav_of_nts_text_en, 
                        reply_markup=nav_markup('en'))



@bot.message_handler(func=lambda message: message.text == nav_menu_ru[0] 
                     or message.text == nav_menu_en[0])
def echo_message(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_photo(message.chat.id, open('resources/inputs.jpg', 'rb'), nav_menu_ru[0], 
                    reply_markup=btm_markup('ru'))
    else:
        bot.send_photo(message.chat.id, open('resources/inputs.jpg', 'rb'), nav_menu_en[0], 
                    reply_markup=btm_markup('en'))


@bot.message_handler(func=lambda message: message.text == nav_menu_ru[1] 
                     or message.text == nav_menu_en[1])
def echo_message(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, select_build_menu_text_ru, 
                        reply_markup=select_build_markup('ru'))
    else:
        bot.send_message(message.chat.id, select_build_menu_text_en, 
                        reply_markup=select_build_markup('en'))


@bot.message_handler(func=lambda message: message.text == select_build_menu_ru[0]
                     or message.text == select_build_menu_en[0])
def echo_message(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_photo(message.chat.id, open('resources/corp1.jpg', 'rb'), first_build_plane_ru, 
                    reply_markup=btm_markup('ru'))
    else:
        bot.send_photo(message.chat.id, open('resources/corp1.jpg', 'rb'), first_build_plane_en, 
                    reply_markup=btm_markup('en'))


@bot.message_handler(func=lambda message: message.text == select_build_menu_ru[1]
                     or message.text == select_build_menu_en[1])
def echo_message(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_photo(message.chat.id, open('resources/corp2.jpg', 'rb'), second_build_plane_ru, 
                    reply_markup=btm_markup('ru'))
    else:
        bot.send_photo(message.chat.id, open('resources/corp2.jpg', 'rb'), second_build_plane_en, 
                    reply_markup=btm_markup('en'))


@bot.message_handler(func=lambda message: message.text == nav_menu_ru[2] 
                     or message.text == nav_menu_en[2])
def echo_message(message):
    if language_data[message.chat.id] == 'ru':
        bot.send_photo(message.chat.id, open('resources/places.jpg', 'rb'), map_startup_tour_ru, 
                    reply_markup=btm_markup('ru'))
    else:
        bot.send_photo(message.chat.id, open('resources/places.jpg', 'rb'), map_startup_tour_en, 
                    reply_markup=btm_markup('en'))


@bot.message_handler(func=lambda message: message.text == nav_menu_ru[3] 
                     or message.text == nav_menu_en[3])
def echo_message(message):
    markup = types.InlineKeyboardMarkup()
    for place in places_ru:
        markup.add(types.InlineKeyboardButton(place, callback_data='apl_' + place))
    
    bot.send_message(message.chat.id, text="Где вы сейчас?", 
                     reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data.startswith('apl_'))
def callback_inline(call):
    place_from = call.data[4:]
    
    markup = types.InlineKeyboardMarkup()
    for place in places_ru:
        if place == place_from:
            continue
        markup.add(types.InlineKeyboardButton(place, callback_data='apf_' + place + '_' + place_from))
    markup.add(types.InlineKeyboardButton('Ближайший туалет', callback_data='apf_' + 'Ближайший туалет' + '_' + place_from))
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, text=f"Из {place_from}... \nКуда вам надо?", 
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('apf_'))
def callback_inline(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    place_to, place_from = call.data[4:].split('_')
    bot.send_message(call.message.chat.id, text=f"{call.from_user.first_name} вот твоё полотенце из {place_from} в {place_to}")


@bot.message_handler(content_types=['location'])
def handle_loc(message):
    a_cord = message.location.longitude
    b_cord = message.location.latitude
    u = f'https://yandex.ru/maps/?mode=routes&rtext={b_cord}%2C{a_cord}~58.538431%2C31.278384'
    if language_data[message.chat.id] == 'ru':
        bot.send_message(message.chat.id, f'{path_to_nts_ru}:\n{u}')
    else:
        bot.send_message(message.chat.id, f'{path_to_nts_en}:\n{u}')


print('Started')
bot.infinity_polling() 
