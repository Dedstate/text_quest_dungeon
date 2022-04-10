from random import choice, randint

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    Updater,
    MessageHandler,
    Filters,
)

from hero import Hero, items
from tokens import TOKEN


HELLO = 0
BUTTON_CHECK = 1


def start(update, context):
    username = update.message.from_user["username"]
    context.bot.send_message(
        update.effective_chat.id, f"Привет, о славный {username}"
    )
    context.bot.send_message(
        update.effective_chat.id,
        "Этот мир погряз в боли и отчаянии и только ты можешь с этим "
        "справиться!",
    )
    start_button = [
        [InlineKeyboardButton("Начать приключение!", callback_data="start")]
    ]
    update.message.reply_text(
        "Готов ли ты дать им отпор",
        reply_markup=InlineKeyboardMarkup(start_button),
    )
    context.user_data["hero"] = Hero(username)
    context.user_data["enemy"] = Hero("Георгий")
    return HELLO


def hello(update, context):
    query = update.callback_query
    if query.data == "start":
        adventure = [
            [InlineKeyboardButton("Пошарить вокруг", callback_data="search")],
            [
                InlineKeyboardButton(
                    "В поисках приключений!", callback_data="enemy"
                )
            ],
        ]
        context.bot.send_message(
            "Сделай свой выбор",
            reply_markup=InlineKeyboardMarkup(adventure),
        )
    elif query.data == "search":
        new_item = choice(items)
        if new_item == "монеток":
            new_money = choice([1, 3, 5, 10])
            context.user_data["hero"].money += new_money
            context.bot.send_message(
                update.effective_chat.id,
                f"Неплохой улов! Я обнаружил {new_money} монет, да я богат!",
            )
        else:
            context.user_data["hero"].add_equip(new_item)
            context.bot.send_message(
                update.effective_chat.id,
                f"Неплохой улов! Я обнаружил {new_item}",
            )
    elif query.data == "enemy":
        variety = [
            [
                InlineKeyboardButton(
                    "Подкрасться со спины",
                    callback_data="sneak up from behind",
                )
            ],
            [
                InlineKeyboardButton(
                    "Подготовить засаду", callback_data="ambush"
                )
            ],
            [InlineKeyboardButton("Пойти напролом", callback_data="go ahead")],
        ]
        context.bot.send_message(
            update.effective_chat.id,
            "Сделай свой выбор",
            reply_markup=InlineKeyboardMarkup(variety),
        )
        return BUTTON_CHECK


print("Привет")


def battle(update, context):
    query = update.callback_query
    if query.data == "sneak up from behind":
        perc = randint(1, 100)
    if perc >= 65:
        ...


enemy_equip = [
    "стальной меч",
    "мешок монет",
    "геройский щит",
    "комплект путешественника",
]
new_equip_f_enemy = choice(enemy_equip)
rand_money = randint(10, 100)


bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
button_check_handler = MessageHandler(Filters.text, hello)
conversation_handler = ConversationHandler(
    entry_points=[start_handler],
    states={HELLO: [start_handler], BUTTON_CHECK: [button_check_handler]},
    fallbacks=[],
    allow_reentry=True,
)

dispatcher.add_handler(conversation_handler)

updater.start_polling()
updater.idle()
