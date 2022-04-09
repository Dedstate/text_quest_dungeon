from wsgiref.simple_server import software_version
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
    context.user_data['enemy'] = Hero("Георгий")
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
    elif query.data == 'enemy':
        variety = [
            [InlineKeyboardButton('Подкрасться со спины', callback_data='sneak up from behind')],
            [InlineKeyboardButton('Подготовить засаду', callback_data='ambush')],
            [InlineKeyboardButton('Пойти напролом', callback_data='go ahead')]
        ]
        context.bot.send_message(update.effective_chat.id, "Сделай свой выбор", reply_markup=InlineKeyboardMarkup(variety))

    if query.data == "sneak up from behind":
        perc = randint(1, 100)
        if perc >= 65:
            context.user_data['enemy'].hp -= 35
            num = 0
            while num <= 1:
                if num == 0:
                    battle = [
                    [InlineKeyboardButton('Защищаться', callback_data='defense')],
                    [InlineKeyboardButton('Атаковать', callback_data='attack')],
                    ]
                    context.bot.send_message(update.effective_chat.id, "Сделай свой выбор", reply_markup=InlineKeyboardMarkup(battle))
                    if query.data == "attack":
                        context.user_data['enemy'].get_attack(context.user_data['hero'].damage)
                        if context.user_data['enemy'].hp <= 0:
                            if "мешок монет" == new_equip_f_enemy:
                                context.send_message(f"Я получил {rand_money} монет, да я сын маминой подруги!")
                            else:
                                context.send_message(f"Я получил {new_equip_f_enemy}, а я хорош!")
                    if query.data == "defense":
                        context.user_data['hero'].hp += context.user_data['enemy'].damage + 10
                        if context.user_data['hero'].hp > 100:
                            context.user_data['hero'].brony += context.user_data['hero'].hp % 100
                            context.user_data['hero'].hp = 100
                else:
                    context.user_data['hero'].get_attack(context.user_data['enemy'].damage)
                num = (num + 1) % 2



    context.user_data['hero'].add_equip(choice(enemy_equip))

enemy_equip = ["стальной меч", "мешок монет", "геройский щит",  "комплект путешественника"]
new_equip_f_enemy = choice(enemy_equip)
rand_money = randint(10, 100)

start_handler = CommandHandler('start', start)
button_check_handler = CallbackQueryHandler(button_check)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_check_handler)

updater.start_polling()
updater.idle()