from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext import Filters
import time
import schedule
import re
from datetime import datetime
import random



#defining your bot token here
TOKEN = "7056623611:AAEXx4bFobyREnlr7fe09GLd8QmxgaYytb8"
group_chat_id =-4018981596

def start(update, context):
    global group_chat_id
    group_chat_id = update.message.chat_id
    update.message.reply_text(f'Привет! Я бот. Chat ID группы: {group_chat_id}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("You requested help. Here are some available commands:\n"
                              "/help - Show this help message\n"
                              "/start - Start the bot")

def handle_message(update: Update, context: CallbackContext):
    global group_chat_id


    names = ['крист.*', 'аля', 'мил.*', 'юля','али.*', 'юл.*', 'эми.*', 'мам.*']
    names2 = ['посуд.*','жест.*', 'треш', 'стир.*','уборк.*','грязь','бардак','бред','убир.*']
    names3 = ['ахах.*', 'смеш.*', 'вес.*']
    names4 = ['спас.*', 'отл.*', 'клас.*']
    names5 = ['@juliettasorokina_bot', 'juli.*', 'при.*', 'пок.*', 'жиз.*', 'дел.*']
    names6 = ['день', 'сегодня', 'гада.*', 'погада']
    names7 = ['деби.*', 'урод.*', 'дура.*', 'коз.*', 'хрен.*', 'борде.*']
    # Преобразование введенного текста в нижний регистр

    text = update.message.text
    text_lower = text.lower()
    if text == '/start':
        start(update, context)
    elif text == '/help':
        help_command(update, context)
    text = update.message.text
    # Проверка, является ли сообщение командой
    if text.startswith('/'):
        return

    if any(re.search(name5, text_lower) for name5 in names5):
        send_hello_message()
    if any(re.search(name2, text_lower) for name2 in names2): # Замените 'your_bot_username' на имя вашего бота
        send_random_message()
    if any(re.search(name, text_lower) for name in names): # Замените 'your_bot_username' на имя вашего бота
        send_random_message3()
    if any(re.search(name3, text_lower) for name3 in names3):
        send_random_message1()
    if any(re.search(name4, text_lower) for name4 in names4):
        send_random_message2()
    if any(re.search(name6, text_lower) for name6 in names6):
        send_random_message4()
    if any(re.search(name7, text_lower) for name7 in names7):
        send_random_message5()
def send_hello_message():
    bot = Bot(token=TOKEN)
    message = "Привет, я снова здесь!"
    bot.send_message(group_chat_id, text=message)

def send_message1():
    print("Отправка сообщения в", datetime.now())
    bot = Bot(token=TOKEN)
    word_list = ['голубой', 'красный', 'желтый','белый', 'зеленый']
    random_word = random.choice(word_list)
    message =f"Мила, гоу к посудомойка! Желаю удачи! Цвет мелка сегодня:{random_word}"
    bot.send_message(group_chat_id, text=message)
def send_message2():
    print("Отправка сообщения в", datetime.now())
    bot = Bot(token=TOKEN)
    message = "Кристина, гоу к посудомойка! Желаю удачи!"
    bot.send_message(group_chat_id, text=message)
def send_message3():
    print("Отправка сообщения в", datetime.now())
    bot = Bot(token=TOKEN)
    message = "Юля или Кристина, гоу к посудомойка! Желаю удачи!"
    bot.send_message(group_chat_id, text=message)
# Запланировать отправку сообщения каждый день в определенное время
def send_message4():
    print("Отправка сообщения в", datetime.now())
    bot = Bot(token=TOKEN)
    message = "Юля (Кристина) у тебя два дня на уборку коридора, ванны, кухни! Не забудь про сортир и плиту! Жду отчета! Желаю удачи!"
    bot.send_message(group_chat_id, text=message)
def send_message5():
    print("Отправка сообщения в", datetime.now())
    bot = Bot(token=TOKEN)
    message = "Мила у тебя два дня на уборку коридора, ванны, кухни! Не забудь про сортир и плиту! Жду отчета! Желаю удачи!"
    bot.send_message(group_chat_id, text=message)
def send_message6():
    print("Отправка сообщения в", datetime.now())
    bot = Bot(token=TOKEN)
    message = "Кристина, у тебя два дня на уборку коридора, ванны, кухни! Не забудь про сортир и плиту! Жду отчета! Желаю удачи!"
    bot.send_message(group_chat_id, text=message)
def send_random_message():
    bot = Bot(token=TOKEN)
    word_list1 = ['Ругаетесь!', 'Не убираетесь!', 'Придираетесь!', 'Но, вы все равно, ничего так!', 'Люблю вас!','Как же я задолбалась!']
    random_word1 = random.choice(word_list1)
    message = f"{random_word1}"
    bot.send_message(group_chat_id, text=message)
def send_random_message1():
    bot = Bot(token=TOKEN)
    word_list2 = ['Ахахаха', 'Обхохочешься', 'Смешно', 'Very nice!', 'Смешные, какие!','Сделали мой день!',
                  'Целую']
    random_word2 = random.choice(word_list2)
    message = f"{random_word2}"
    bot.send_message(group_chat_id, text=message)
def send_random_message3():
    bot = Bot(token=TOKEN)
    word_list3 = ['Красотка', 'Cool girl!', 'Хорошая девочка!', 'Ты- лучшая!', 'Люблю тебя!', 'Желаю удачи!','Вау!']
    random_word3 = random.choice(word_list3)
    message = f"{random_word3}"
    bot.send_message(group_chat_id, text=message)
def send_random_message2():
    bot = Bot(token=TOKEN)
    word_list5 = ['Я очень рада!', 'И тебе спасибо!', 'Я тоже так думаю!', 'Ты уверенна?', 'Ну,ок', 'Ору', 'Согласна']
    random_word5 = random.choice(word_list5)
    message = f"{random_word5}"
    bot.send_message(group_chat_id, text=message)
def send_random_message4():
    bot = Bot(token=TOKEN)
    word_list4 = ['Все будет более чем хорошо', 'Лучше остаться дома!', 'Поработай сегодня - сделай что нибудь полезное для других!', 'Ты- лучшая, но, кажется, не сегодня ', 'Тебя ждет интересная встреча!', 'Загадай желание и оно исполниться, но только одно!','Отдохни и придумай, как бы тебе заработать!','Ты можешь поехать куда нибудь, и это будет здорово!']
    random_word4 = random.choice(word_list4)
    message = f"{random_word4}"
    bot.send_message(group_chat_id, text=message)
def send_random_message5():
    bot = Bot(token=TOKEN)
    word_list5 = ['Хоре выражаться!', 'Не ругайся!', 'Плохие слова оставь для других!', 'В чате нельзя так говорить!', 'Сейчас выйду из чата!']
    random_word5 = random.choice(word_list5)
    message = f"{random_word5}"
    bot.send_message(group_chat_id, text=message)
def main():
    #creating a bot instance
    bot = Bot(token=TOKEN)
    # creating an updater instance and pass the bot instance

    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher

    # defining the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # handling non-command messages using a filter
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    start_date = datetime(2024,4, 28, 23, 0)
    schedule.every(3).days.at(start_date.strftime("%H:%M")).do(send_message1)

    start_date1 = datetime(2024, 4, 29, 23, 0)
    schedule.every(3).days.at(start_date1.strftime("%H:%M")).do(send_message2)

    start_date2 = datetime(2024, 4, 30, 23, 0)
    schedule.every(3).days.at(start_date2.strftime("%H:%M")).do(send_message3)

    start_date3 = datetime(2024, 5, 3, 23, 30)
    schedule.every(21).days.at(start_date3.strftime("%H:%M")).do(send_message4)

    start_date4 = datetime(2024, 5, 10, 23, 30)
    schedule.every(21).days.at(start_date4.strftime("%H:%M")).do(send_message5)

    start_date5 = datetime(2024, 5, 17, 23, 30)
    schedule.every(21).days.at(start_date4.strftime("%H:%M")).do(send_message6)

    # starting the bot
    updater.start_polling()
    while True:
        schedule.run_pending()
        time.sleep(1)  # Ждем 1 секунду перед проверкой расписания


    # Отправляем приветственное сообщение при каждом запуске

if __name__ == "__main__":
    main()
