import os
from dotenv import load_dotenv
import telebot

from utils.user_utils import create_n_users
from keyboards import get_main_menu_keyboard
from strings import STRINGS


load_dotenv()

API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def send_menu(message):
    bot.send_message(message.chat.id, STRINGS['start_msg'], reply_markup=get_main_menu_keyboard())


@bot.message_handler(func=lambda message: message.text == STRINGS['signup_user_btn'])
def get_users_count(message):
    user_num = os.getenv("NUMBER_OF_USERS")
    users = create_n_users(int(user_num))
    users_string = "\n".join([f'👻{u.username}' for u in users])
    msg_text = f'created {user_num} users:\n' \
               f'{users_string}'
    bot.send_message(message.chat.id, msg_text)
