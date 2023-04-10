import os
from dotenv import load_dotenv
import telebot
from telebot.types import Message

from utils.user_utils import create_n_users
from utils.post_utils import create_up_to_n_posts_per_user
from keyboards import get_main_menu_keyboard
from strings import STRINGS
from models import USERS


load_dotenv()

API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def send_menu(message: Message):
    bot.send_message(message.chat.id, STRINGS['start_msg'], reply_markup=get_main_menu_keyboard())


@bot.message_handler(func=lambda message: message.text == STRINGS['signup_user_btn'])
def create_n_users_handler(message: Message):
    user_num = os.getenv("NUMBER_OF_USERS")
    users = create_n_users(int(user_num))
    users_string = "\n".join([f'👻{u.username}' for u in users])
    msg_text = f'created {user_num} users:\n' \
               f'{users_string}'
    bot.send_message(message.chat.id, msg_text)


@bot.message_handler(func=lambda message: message.text == STRINGS['create_random_posts_btn'])
def create_random_posts_handler(message: Message):
    max_posts = int(os.getenv("MAX_POSTS_PER_USER"))
    posts = create_up_to_n_posts_per_user(max_posts)
    posts_per_user = '\n'.join([f'user👻 {u.username} created {len(u.posts)} posts📃' for u in USERS.values()])
    template_txt = f'created {len(posts)} posts\n' \
                   f'{posts_per_user}'
    bot.send_message(message.chat.id, template_txt)


