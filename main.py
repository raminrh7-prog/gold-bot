from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# متغیر جهانی برای ذخیره آخرین قیمت
LAST_PRICE = None

# وقتی کاربر /start را می‌زند
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💰 آخرین قیمت آبشده اتحادیه", callback_data="price")]]
    await update.message.reply_text(
        "برای مشاهده آخرین قیمت آبشده اتحادیه کلیک کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# وقتی کاربر دکمه را می‌زند
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global LAST_PRICE
    q = update.callback_query
    await q.answer()
    if LAST_PRICE:
        await q.message.reply_text(f"💰 آخرین قیمت طلای ۱۸ عیار:\n{LAST_PRICE} تومان")
    else:
        await q.message.reply_text("❌ هنوز قیمت دریافت نشده است.")

# آپدیت کردن قیمت (GitHub Actions آن را فراخوانی می‌کند)
async def update_price_handler(update_price):
    global LAST_PRICE
    LAST_PRICE = update_price

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
