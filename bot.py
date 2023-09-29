import telebot
import sqlite3 as sql

# База Данных
con = sql.connect("data.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(id TEXT)")

# Ваш бот
token = "6580851166:AAENR66Ri4Y73gFmjKgUYInB0P2njNRjf3c"
bot = telebot.TeleBot(token)

# ID Вашего канала
chan_id = -1001964634300

# Клавиатура для проверки подписки
keyboard = telebot.types.InlineKeyboardMarkup()
subscribe = telebot.types.InlineKeyboardButton(text="Join to VIP GROUP✔️", url="https://t.me/+pSJ0Rf7j07RiOGY6")
check = telebot.types.InlineKeyboardButton(text="💸EARN NOW💸", callback_data="check")
keyboard.add(check)
keyboard.add(subscribe)


# Не нужная хуйня, вписал просто для видимости
menu = telebot.types.ReplyKeyboardMarkup(True, True)
menu.add("https://amar-inc-dm.vercel.app 👈")


@bot.message_handler(commands=["start"])
def start(message):
    new_cur = con.cursor()  # Create a new cursor
    users = new_cur.execute("SELECT id FROM users WHERE id = ?", (message.chat.id,)).fetchone()
    con.commit()
    new_cur.close()  # Close the cursor
    if users is None:  # Если юзер ещё не в БД
        bot.send_message(message.chat.id, "To earn 5000 today you need to tap button EARN NOW", reply_markup=keyboard)
    else:  # Уже в бд
        bot.send_message(message.chat.id, "🥳You got access to use AVIATOR PREDICTION bot bot tap here to get it now✅ https://amar-inc-dm.vercel.app?gnat=1241219257274093 👈", reply_markup=menu)


# Тут мы чекаем подписку
@bot.callback_query_handler(func=lambda call: True)
def c_listener(call):
    if call.data == "check":
        new_cur = con.cursor()  # Create a new cursor
        x = bot.get_chat_member(chan_id, call.message.chat.id)
        if x.status == "member" or x.status == "creator" or x.status == "administrator":
            bot.send_message(call.message.chat.id, "🥳You got access to use AVIATOR PREDICTION bot bot tap here to get it now✅ https://amar-inc-dm.vercel.app?gnat=1241219257274093 👈", reply_markup=menu)
            new_cur.execute("INSERT INTO users VALUES(?)", (call.message.chat.id,))
            con.commit()
        else:
            bot.send_message(call.message.chat.id, "Firstly join to group, than tap to EARN NOW button😇", reply_markup=keyboard)
        new_cur.close()  # Close the cursor


if __name__ == "__main__":
    bot.polling()
