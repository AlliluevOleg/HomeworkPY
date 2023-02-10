import telebot

bot = telebot.TeleBot("5596841647:AAH7k4P7Xi4gZMvVMC_42W0SnPICDb2srR8")

def send_anwer(id, question, answer):
    bot.send_message(id, f'{question}\n Ответ {answer} ')

data = open('questions.txt', 'r', encoding='utf - 8')
question_list = data.readlines()
data.close

for row in question_list:
    split_row = row.split('--')
    id = split_row[0]
    question = split_row[1]
    print(question[:-1])
    answer = input('ВВедите ответ: ')
    if answer != 'пропустить':
        send_anwer(id, question, answer)
    print('__________')
