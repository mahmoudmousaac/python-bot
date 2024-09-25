import time
import json
import telebot

##TOKEN DETAILS
TOKEN = "TRON"


from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# أدخل توكن البوت الخاص بك هنا
TOKEN = '7547855450:AAHkhYG91DCDc7JtBnCNZ91_397dpfSOxd0'
CHANNEL_USERNAME = '@ho_dev'

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_member = context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        update.message.reply_text('مرحبًا! يمكنك استخدام البوت.')
    else:
        update.message.reply_text(
            'يجب عليك الاشتراك في القناة أولاً: ' + CHANNEL_USERNAME
        )

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
