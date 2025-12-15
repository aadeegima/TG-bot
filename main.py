import os
import telebot

bot = telebot.TeleBot("8520268519:AAEzpbKfnlOff9o-PXUnN5BmXWykoYI_cm8")

@bot.massage_handler(commands=["start"])
def send_welcome(massage):
    bot.reply_to(massage, "Hello I'm Gimazer Telegram Bot 😍")

    @bot.massage_handler(command=["channels"])
    def send_massage(massage):
        bot.send_massage(massage, "Meme channel - t.me/athal_hub")


        bot.polling()
