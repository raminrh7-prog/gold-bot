import requests
from bs4 import BeautifulSoup
import re

PRICE_FILE = "price.txt"

def get_gold_price():
    try:
        url = "https://www.tala.ir/price/18k"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "fa-IR,fa;q=0.9"
        }
        r = requests.get(url, headers=headers, timeout=10, proxies={"http": None, "https": None})
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
        with open(PRICE_FILE, "w", encoding="utf-8") as f:
            f.write(price)
        print(f"Updated price: {price}")
    else:
        print("❌ قیمت پیدا نشد")

if __name__ == "__main__":
    main()
