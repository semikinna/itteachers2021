import telebot
bot = telebot.TeleBot('AAECVpHX58Os_W4yBFl2AnifDH99nCa0C08')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('7-11 класс', '8 класс', '9 класс', ' 10 класс')



if message.text.lower() == '7-11 класс':
        bot.send_message(message.chat.id, '1 урок 8.30 - 9.10 ; 2 урок 9.30 - 10.15; 3 урок 10.35 - 11.15; 4 урок 11.30 - 12.15 ; 5 урок 12.30 - 13.15; 6 урок 13.30 - 14.15; 7 урок 14.30 - 15.10')
    elif message.text.lower() == '8 класс':
        bot.send_message(message.chat.id, '1 урок 8.15 - 9.00 ; 2 урок 9.15 - 10.00; 3 урок 10.20 - 11.05; 4 урок 11.20 - 12.05 ; 5 урок 12.30 - 13.15; 6 урок 13.20 - 14.00; 7 урок 14.20 - 15.00')
   elif message.text.lower() == '9 класс':
        bot.send_message(message.chat.id, '1 урок  ; 2 урок 9.30 - 10.15; 3 урок 10.35 - 11.15; 4 урок 11.30 - 12.15 ; 5 урок 12.30 - 13.15; 6 урок 13.30 - 14.15; 7 урок 14.30 - 15.10 ; 8 урок 15.25 - 16.10')
    elif message.text.lower() == '10 класс':
        bot.send_message(message.chat.id, '1 урок  ; 2 урок 9.15 - 10.00; 3 урок 10.20 - 11.05; 4 урок 11.20 - 12.05 ; 5 урок 12.20 - 13.00; 6 урок 13.20 - 14.00; 7 урок 14.20 - 15.00 ; 8 урок 15.15 - 16.00')
    elif message.text.lower() == 'я тебя люблю':


bot.polling(none_stop=True)
