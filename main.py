import os
import telebot

bot = telebot.TeleBot("7937720717:AAFrNdb4lTKa25AzN36qWQyHWCdoCytqtT8")

@bot.massage_handler(commands=["start"])
def send_welcome(massage):
    bot.reply_to(massage, "Hello I'm Gimazer Telegram Bot 😍")

    @bot.massage_handler(command=["channels"])
    def send_massage(massage):
        bot.send_massage(massage, "Meme channel - t.me/athal_hub")

        bot.polling()