from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
await update.message.reply_text("سلام! من فعال هستم.")

if __name__ == "__main__":
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
