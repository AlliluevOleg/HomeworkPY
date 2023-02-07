import telebot
import random

bot = telebot.TeleBot(
    "token", parse_mode=None)
game_start = False
x = None


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    global game_start
    global x
    if game_start:
        if message.text.isdigit():
            number = int(message.text)
            if number > x:
                bot.reply_to(message, 'Введите число поменьше')
            elif number < x:
                bot.reply_to(message, 'Введите число побольше')
            elif number == x:
                game_start = False
                bot.reply_to(message, f'Поздравляю ты угадал {x}')
            else:
                bot.reply_to(message, 'не понятно. повторите')
        else:
            bot.reply_to(message, 'введите число...')

    if message.text == 'играть':
        if not game_start:
            game_start = True
            x = random.randint(1, 1000)
            bot.reply_to(message, 'игра началась')
        else:
            bot.reply_to(message, 'игра уже идет')
    
    elif message.text == 'вычислить':
        bot.reply_to(message,'введите выражение')
        bot.register_next_step_handler(message, calc)
        
def calc(message):
    bot.reply_to(message, f'otvet {eval(message.text)}')

bot.infinity_polling()
