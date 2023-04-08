from telebot import types
from texts import *


def btm_markup(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == 'ru':
        markup.add(types.KeyboardButton(menu_ru))
    else:
        markup.add(types.KeyboardButton(menu_en))
    return markup


def gen_markup(data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for p in data:
        markup.add(types.KeyboardButton(p))
    return markup


def main_markup(lang):
    if lang == 'ru':
        return gen_markup(main_menu_ru)
    else:
        return gen_markup(main_menu_en)


def hi_nav_markup(lang):
    if lang == 'ru':
        return gen_markup(hi_nav_menu_ru)
    else:
        return gen_markup(hi_nav_menu_en)


def nav_markup(lang):
    if lang == 'ru':
        return gen_markup(nav_menu_ru)
    else:
        return gen_markup(nav_menu_en)


def ants_markup(lang):
    if lang == 'ru':
        return gen_markup(ants_menu_ru)
    else:
        return gen_markup(ants_menu_en)


def ask_loc_markup(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == 'ru':
        markup.add(types.KeyboardButton(ask_location_menu_ru[0], request_location=True))
        markup.add(types.KeyboardButton(ask_location_menu_ru[1]))
    else:
        markup.add(types.KeyboardButton(ask_location_menu_en[0], request_location=True))
        markup.add(types.KeyboardButton(ask_location_menu_en[1]))
    return markup


def select_build_markup(lang):
    if lang == 'ru':
        return gen_markup(select_build_menu_ru)
    else:
        return gen_markup(select_build_menu_en)

