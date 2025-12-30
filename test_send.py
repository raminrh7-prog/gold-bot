from telegram import Bot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ تست موفق ارسال پیام از GitHub Actions")
print("پیام ارسال شد!")
