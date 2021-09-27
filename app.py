from telegram.ext import Updater, CommandHandler
from telegram import bot, ParseMode
import os
import datetime
import pytz
import logging
from dotenv import load_dotenv
from flask import Flask
load_dotenv()

TOKEN = os.environ.get('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def daily_job(update, context):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    context.bot.send_message(chat_id=CHAT_ID, text='Activating daily paramount notification!')
    sport = datetime.time(11, 25, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    trading = datetime.time(15, 00, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    forex = datetime.time(18, 00, 10, 000000, tzinfo=pytz.timezone('America/Chicago'))
    print("Time its supposed to post", sport)
    print("Time right now:", datetime.datetime.now())
    context.job_queue.run_daily(purchase_forex(update, context), forex, days=tuple(range(5)), context=update)
    context.job_queue.run_daily(purchase_sports(update, context), sport, days=tuple(range(5)), context=update)
    context.job_queue.run_daily(purchase_trading(update, context), trading, days=tuple(range(5)), context=update)

def purchase_forex(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://pstrading.online/forex'>here</a> to purchase a Paramount forex subscription!", parse_mode=ParseMode.HTML)

def purchase_sports(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://pstrading.online/sports'>here</a> to purchase a Paramount sports subscription!", parse_mode=ParseMode.HTML)

def purchase_trading(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="Well thats the end of the trading day. Click <a href='https://pstrading.online/trading'>here</a> to purchase a Paramount trading subscription!", parse_mode=ParseMode.HTML)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)





def main():

    u = Updater(TOKEN, use_context=True)
    u.dispatcher.add_handler(CommandHandler('start', daily_job))
    u.dispatcher.add_error_handler(error)

    # Start the Bot
    u.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url="https://paramount-telegram.herokuapp.com/" + TOKEN)


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    u.idle()

if __name__ == '__main__':
    main()