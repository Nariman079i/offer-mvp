from telebot import TeleBot

bot = TeleBot(token="5669809910:AAE7J0MTxS1dvwGpht_6k5x3FyWVbsD61jI")

def send_telegram_message(message):
    chat_id = '-931952874'
    bot.send_message(chat_id, message)