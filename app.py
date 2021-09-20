from telegram.ext import Updater, CommandHandler
from telegram import bot, ParseMode
import os
import datetime
import pytz
from dotenv import load_dotenv
from flask import Flask
load_dotenv()

TOKEN = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
app = Flask(__name__)

def daily_job(update, context):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    context.bot.send_message(chat_id=CHAT_ID, text='Activating daily paramount notification!')
    sport = datetime.time(18, 23, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    trading = datetime.time(15, 00, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    forex = datetime.time(21, 00, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    print("Time its supposed to post", t)
    print("Time right now:", datetime.datetime.now())
    context.job_queue.run_daily(purchase_forex, test, days=tuple(range(5)), context=update)
    context.job_queue.run_daily(purchase_sports, test, days=tuple(range(5)), context=update)
    context.job_queue.run_daily(purchase_trading, trading, days=tuple(range(5)), context=update)

def purchase_forex(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://pstrading.online/forex'>here</a> to purchase a Paramount forex subscription!", parse_mode=ParseMode.HTML)

def purchase_sports(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://pstrading.online/sports'>here</a> to purchase a Paramount sports subscription!", parse_mode=ParseMode.HTML)

def purchase_trading(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Well thats the end of the trading day. Click <a href='https://pstrading.online/trading'>here</a> to purchase a Paramount trading subscription!", parse_mode=ParseMode.HTML)



@app.route("/")
def start():
    u = Updater(TOKEN, use_context=True)
    u.dispatcher.add_handler(CommandHandler('purchase', daily_job))
    u.start_polling()

if(__name__ == "__main__"): 
    app.run(debug=True)