from telegram.ext import Updater, CommandHandler
from telegram import bot
import os
import datetime
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')



def daily_job(update, context):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    context.bot.send_message(chat_id=CHAT_ID, text='Setting daily paramount notification!')
    t = datetime.time(3, 16, 00, 000000)
    context.job_queue.run_daily(purchase, t, days=tuple(range(5)), context=update)

def purchase(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Emjoy our services? Click <a href="">here</a> to purchase a Paramoutn forex subscription!", parse_mode=ParseMode.HTML)

u = Updater(TOKEN, use_context=True)
u.dispatcher.add_handler(CommandHandler('purchase', daily_job))
u.start_polling()