from telegram import Bot
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
import random
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
chat_id = os.getenv("CHAT_ID")

def predict_price():
    now = datetime.now(pytz.timezone('Asia/Dhaka')).strftime("%H:%M:%S")
    prediction = random.choice(["🔺 দাম বাড়বে", "🔻 দাম কমবে"])
    message = f"🕒 {now} — {prediction}"
    bot.send_message(chat_id=chat_id, text=message)

scheduler = BackgroundScheduler()
scheduler.add_job(predict_price, 'interval', seconds=10)
scheduler.start()

print("Bot is running...")
import time
while True:
    time.sleep(1)
