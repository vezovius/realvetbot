from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من فعال هستم.")

app.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    app.run_polling()