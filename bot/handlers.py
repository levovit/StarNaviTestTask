import os
from dotenv import load_dotenv
import telebot
from telebot.types import Message

from keyboards import get_main_menu_keyboard
from strings import STRINGS
from models import USERS, POSTS
from utils.user_utils import create_n_users
from utils.post_utils import create_up_to_n_posts_per_user
from utils.like_utils import like_up_to_n_posts_per_user


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
    template_txt = f'created {user_num} <b>users:</b>\n' \
                   f'{users_string}'
    bot.send_message(message.chat.id, template_txt, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == STRINGS['create_random_posts_btn'])
def create_random_posts_handler(message: Message):
    max_posts = int(os.getenv("MAX_POSTS_PER_USER"))
    posts = create_up_to_n_posts_per_user(max_posts)
    posts_per_user = '\n\n'.join([f'👻<b>user</b> {u.username}\n '
                                  f'created <b>{len(u.posts)}</b> posts📃' for u in USERS.values()])
    template_txt = f'created <b>{len(posts)}</b> posts\n' \
                   f'{posts_per_user}'
    bot.send_message(message.chat.id, template_txt, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == STRINGS['random_likes_btn'])
def create_random_posts_handler(message: Message):
    max_likes = int(os.getenv("MAX_LIKE_PER_USER"))
    like_count = like_up_to_n_posts_per_user(max_likes)
    posts = POSTS.values()
    likes_per_post = '\n'.join([f'👍<b>{p.like_count}</b> likes for post: <b>{p.title}</b>' for p in posts])
    template_txt = f'Total placed <b>{like_count}</b> likes✍️\n' \
                   f'{likes_per_post}'
    bot.send_message(message.chat.id, template_txt, parse_mode="HTML")

