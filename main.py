import os
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من فعال هستم.")

def send_photo(update: Update, context: CallbackContext):
    # اطمینان حاصل کنید فایل در همان مسیر پروژه وجود دارد
    photo_path = "welcome_turkish.jpg"
    if os.path.exists(photo_path):
        with open(photo_path, "rb") as photo:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
    else:
        update.message.reply_text("فایل عکس پیدا نشد.")

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("photo", send_photo))

    updater.start_polling()
    updater.idle()
