import telebot as tb
from telebot.types import InlineKeyboardMarkup as kb
from telebot.types import InlineKeyboardButton as bt
import Data
import Functions

bot = tb.TeleBot('5828159918:AAEHx2MM58mLTq0SiytXV5g1X_tV0ze0jK0', parse_mode=None)

function = Functions.Functions()



@bot.message_handler(func=lambda m: True)
def reply(message):
    user = message.from_user.id

    bot.send_message(user, function.search(message))


bot.polling()
