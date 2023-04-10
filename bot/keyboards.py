from telebot import types
from strings import STRINGS


def get_main_menu_keyboard():
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_keyboard.row(STRINGS['signup_user_btn'])
    menu_keyboard.row(STRINGS['create_random_posts_btn'], STRINGS['random_likes_btn'])
    menu_keyboard.row(STRINGS['read_config_btn'])
    return menu_keyboard

