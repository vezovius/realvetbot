from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    update.message.reply_text("سلام! من فعال هستم.")

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
