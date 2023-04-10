import telebot
try:
    from handlers import bot
    bot.polling()
except telebot.apihelper.ApiTelegramException:
    # if you don't provide token - service will just exit
    pass
