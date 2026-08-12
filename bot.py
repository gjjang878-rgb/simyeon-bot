import os
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

TOKEN = os.environ["BOT_TOKEN"]

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        if member.is_bot:
            continue

        name = member.first_name

        message = (
            "🌑 WELCOME TO 深淵\n\n"
            f"{name}님, 심연에 오신 것을 환영합니다.\n\n"
            "공지 확인 후 활동 부탁드립니다.\n"
            "끝을 알 수 없는 곳, 深淵"
        )

        await update.message.reply_text(message)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
)

app.run_polling()
