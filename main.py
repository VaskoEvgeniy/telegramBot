import telebot

bot = telebot.TeleBot('5954696584:AAFmpROwR6rSzoioASCHc3hHUhxh_wI4LSM')




@bot.message_handler(commands=['start', 'help'])
def start(message):
    if message.text == '/help':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} Please contact our administrator for assistance. His contact @passshaaa ')
    else:
        bot.send_message(message.chat.id, 'Hello')




bot.polling(none_stop=True)