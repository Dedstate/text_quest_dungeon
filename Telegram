from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from random import choice, randint
from hero import Hero, items

token = "5067951585:AAGrKQ22qnO3TDH8KBk-Z35oT3IcAEFCznY"
bot = Bot(token)
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context ):
    username = update.message.from_user['username']
    context.bot.send_message(update.effective_chat.id, f'Привет, о славный {username}')
    context.bot.send_message(update.effective_chat.id, f'Этот мир погряз в боли и отчаянии и только ты можешь с этим справиться!')
    start_button = [
        [InlineKeyboardButton("Начать приключение!", callback_data='start')]]

    update.message.reply_text('Готов ли ты дать им отпор', reply_markup=InlineKeyboardMarkup(start_button))
    context.user_data['hero'] = Hero(username)
    print(context.user_data['hero'])


def button_check(update, context):
    query = update.callback_query
    if query.data == "start":
        adventure = [
            [InlineKeyboardButton("Пошарить вокруг", callback_data='search')], [InlineKeyboardButton("В поисках приключений!", callback_data='enemy')]]
        context.bot.send_message(update.effective_chat.id, "Сделай свой выбор", reply_markup=InlineKeyboardMarkup(adventure))
    elif query.data == "search":
        print(context.user_data['hero'])
        new_item = choice(items)
        if new_item == 'монеток':
            new_money = choice([1, 3, 5, 10])
            context.user_data['hero'].money += new_money
            context.bot.send_message(update.effective_chat.id, f'Неплохой улов! Я обнаружил {new_money} монет, да я богат!')
        else:
            context.user_data['hero'].add_equip(new_item)
            context.bot.send_message(update.effective_chat.id, f'Неплохой улов! Я обнаружил {new_item}')
    elif query.data == "enemy":
        battle = [
            [InlineKeyboardButton('Подкрасться сзади', callback_data='a stab in the back')],
            [InlineKeyboardButton('Подготовить засаду', callback_data='ambush')],
            [InlineKeyboardButton('Подготовить засаду', callback_data='ambush')]
        ]
        #случайная вероятность, понадобиться чуть позже
        # num = randint(1, 100)
        # if num <= 70:
        #     ...



start_handler = CommandHandler('start', start)
button_check_handler = CallbackQueryHandler(button_check)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_check_handler)

updater.start_polling()
updater.idle()
