import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InputFile

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    with open("welcome_turkish.jpg", "rb") as f:
        context.bot.send_voice(chat_id=update.effective_chat.id, voice=InputFile(f))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Lütfen hayvanın türünü seçin: /kedi, /kopek veya /kus")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
