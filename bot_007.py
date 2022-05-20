import telebot
#import config

TOKEN = "5314183031:AAH9L-X5OzyKu68FTDHHk4ZANtBLq3bxPyk"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])

def lololol(message):
    bot.send_message(message.chat.id, message.text)
    bot.polling(none_stop=True)

