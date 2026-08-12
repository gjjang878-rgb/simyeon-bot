import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

TOKEN = os.environ["BOT_TOKEN"]

# Render Web Service용 웹 서버
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


# 새 멤버 입장 시 자동 인사
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.new_chat_members:
        return

    for member in update.message.new_chat_members:
        if member.is_bot:
            continue

        name = member.first_name

        message = (
            "🌑 WELCOME TO 深淵\n\n"
            f"{name}님, 심연에 오신 것을 환영합니다.\n"
            "📢 공지 확인 후 활동 부탁드립니다.\n\n"
            "끝을 알 수 없는 곳, 深淵"
        )

        await update.message.reply_text(message)


def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome
        )
    )

    app.run_polling()


if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    run_bot()
