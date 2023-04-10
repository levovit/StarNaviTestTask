import telebot
try:
    from handlers import bot
    bot.infinity_polling()
except telebot.apihelper.ApiTelegramException:
    # if you don't provide token - service will just exit
    pass
