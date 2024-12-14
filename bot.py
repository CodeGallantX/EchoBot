from config import TOKEN
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# TOKEN
print(f"SECRET_TOKEN: {TOKEN}")

# /start command
async def start(update: Update, context):
    await update.message.reply_text("Hello! I am EchoBot. Send me any message and I'll echo it back.")

# user messages
async def echo(update: Update, context):
    user_message = update.message.text(f"You said: {user_message}")

# help
async def help(update: Update, context):
    await.update.message.reply_text("Use `/start` to greet me or send any message to get a reply.")

# Main function
def main():
    application  ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
    