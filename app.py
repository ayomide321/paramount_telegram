from telegram.ext import Updater, CommandHandler
from telegram import bot, ParseMode
import os
import datetime
import pytz
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')



def daily_job(update, context):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    context.bot.send_message(chat_id=CHAT_ID, text='Activating daily paramount notification!')
    t = datetime.time(17, 2, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    print("Time its supposed to post", t)
    print("Time right now:", datetime.datetime.now())
    context.job_queue.run_daily(purchase, t, days=tuple(range(5)), context=update)

def purchase(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://pstrading.online/forex'>here</a> to purchase a Paramount forex subscription!", parse_mode=ParseMode.HTML)

u = Updater(TOKEN, use_context=True)
u.dispatcher.add_handler(CommandHandler('purchase', daily_job))
u.start_polling()