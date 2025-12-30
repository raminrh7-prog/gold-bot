import requests
from bs4 import BeautifulSoup
import re
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # برای کانال یا چت

PRICE_FILE = "price.txt"  # فایلی که GitHub Actions قیمت را ذخیره می‌کند

# تابع خواندن قیمت ذخیره شده
def read_price():
    if os.path.exists(PRICE_FILE):
        with open(PRICE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "❌ قیمت موجود نیست"

# وقتی کاربر /start را می‌زند
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💰 آخرین قیمت آبشده اتحادیه", callback_data="price")]]
    await update.message.reply_text(
        "برای مشاهده آخرین قیمت آبشده اتحادیه کلیک کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# وقتی کاربر دکمه را می‌زند
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    last_price = read_price()
    await q.message.reply_text(f"💰 آخرین قیمت طلای ۱۸ عیار:\n{last_price} تومان")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
