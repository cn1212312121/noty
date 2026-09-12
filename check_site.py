import os
import sys
from datetime import datetime, timezone
import requests

URLS = [
    "https://etmgroup.store/login",
    "https://demox.store",
    "https://mobile.demox.store",
    "https://demoy.store",
    "https://mobile.demoy.store",
    "http://okcasino11.com"
]
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message},
        timeout=10,
    )

problems = []

for url in URLS:
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code >= 400:
            problems.append(f"⚠️ {url} ตอบ status {resp.status_code}")
    except requests.RequestException as e:
        problems.append(f"😱🔴 {url} ล่ม/เข้าไม่ได้: {e}")

if problems:
    send_telegram("\n".join(problems))
    sys.exit(1)
elif datetime.now(timezone.utc).minute == 0:
    send_telegram("✅ ทุกเว็บปกติ (" + ", ".join(URLS) + ")")
