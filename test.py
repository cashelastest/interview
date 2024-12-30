import telebot
from DB import insert_data

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    bot.send_message(message.chat.id,insert_data(username))


if __name__ =="__main__":
    bot.polling(non_stop=True)