from telebot import TeleBot

bot = TeleBot(token="6234746672:AAFMgsAfIQ27LE1igh5FNhZswWo19xuLdiA")

def send_telegram_message(message):
    chat_id = '-1001857206392'
    bot.send_message(chat_id, message)