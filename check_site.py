import os
import sys
import requests

URL = "https://etmgroup.store/login"
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message},
        timeout=10,
    )

try:
    resp = requests.get(URL, timeout=10)
    if resp.status_code >= 400:
        send_telegram(f"⚠️ {URL} ตอบ status {resp.status_code}")
        sys.exit(1)
except requests.RequestException as e:
    send_telegram(f"🔴 {URL} ล่ม/เข้าไม่ได้: {e}")
    sys.exit(1)
