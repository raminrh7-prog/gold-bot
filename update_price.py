import requests
from bs4 import BeautifulSoup
import re
from telegram import Bot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def get_gold_price():
    try:
        url = "https://www.tala.ir/price/18k"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "fa-IR,fa;q=0.9"
        }
        r = requests.get(url, headers=headers, timeout=10)
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text(separator=" ")
        match = re.search(r"آخرین\s*قیمت\s*[:\-]?\s*([\d,]+)", text)
        return match.group(1) if match else None
    except Exception as e:
        print("ERROR:", e)
        return None

def main():
    price = get_gold_price()
    if price:
        print(f"Sending price: {price}")
        bot = Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=f"💰 آخرین قیمت طلای ۱۸ عیار:\n{price} تومان")
    else:
        print("❌ قیمت پیدا نشد")

if __name__ == "__main__":
    main()
