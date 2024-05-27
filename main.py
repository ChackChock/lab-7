from random import shuffle
from telebot.types import Message
import telebot

bot = telebot.TeleBot("5383955971:AAFz8yVLVXrO5A1MOwM0dA-U9Ym_rb3Q6kM")

# commit 3: 1 line
# commit 1: 2 line
questions = [
    "Столица России?",
    "Самое большое озеро в мире?",
    "Самая популярный спорт в мире?",
    "Как называется переменная, принадлежащая классу?",
]
answers = [
    ["Москва", "Египет", "Лондон", "Париж"],
    ["Каспийское море", "Виктория", "Гурон", "Байкал"],
    ["Футбол", "Гольф", "Хоккей", "Бадминтон"],
    ["Метод", "Переменная", "Свойство", "Поле"],
]
# commit 2: 1 line
current_question = 0
money = 100

# commit 6: 1 line
@bot.message_handler(commands=["start"])
def process_start_command(message: Message):
    answers_copy = answers[current_question].copy()
    shuffle(answers_copy)
    msg = questions[current_question] + "\n" + "\n".join(answers_copy)
    bot.send_message(
        message.from_user.id,
        "Вас приветствует бот-викторина!\nВот ваш первый вопрос:\n\n" + msg,
    )

# commit 7: 1 line
@bot.message_handler()
def process_message(message: Message):
    global current_question, money
    # commit 7: 2 line
    text = message.text.lower()
    if text == answers[current_question][0].lower():
        money *= 2
        bot.send_message(message.from_user.id, "Это правильный ответ!")
    else:
        money /= 4
        bot.send_message(message.from_user.id, "Это неверный ответ!")

    current_question += 1
    if current_question == len(questions):
        current_question = 0
        bot.send_message(message.from_user.id, f"Ваш выигрыш: {money} евро.")
    else:
        answers_copy = answers[current_question].copy()
        shuffle(answers_copy)
        msg = questions[current_question] + "\n" + "\n".join(answers_copy)
        bot.send_message(message.from_user.id, msg)

# commit 6: 3 line
bot.polling(none_stop=True, interval=0)
