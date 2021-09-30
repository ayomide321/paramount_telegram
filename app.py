from telegram.ext import Updater, CommandHandler
from telegram import bot, ParseMode
import os
import datetime
import pytz
import logging
from dotenv import load_dotenv
from flask import Flask
import feedparser
load_dotenv()

TOKEN = os.environ.get('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

sub_text = "\nInstagram: <a href='https://www.instagram.com/tradewithparamount'>TradeWithParamount</a>\nTwitter: <a href='https://www.twitter.com/tradewparamount'>TradeWParamount</a>"


def daily_job(update, context):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    sport = datetime.time(19, 00, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    trading = datetime.time(15, 30, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    forex = datetime.time(18, 00, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    print("Time its supposed to post sport", sport)
    print("Time its supposed to post trading", trading)
    print("Time its supposed to post forex", forex)
    context.bot.send_message(chat_id=CHAT_ID, text='Activating daily paramount notification!')
    context.job_queue.run_daily(purchase_forex, forex, days=tuple(range(7)), context=update)
    context.job_queue.run_daily(purchase_sports, sport, days=tuple(range(7)), context=update)
    context.job_queue.run_daily(purchase_trading, trading, days=tuple(range(7)), context=update)

def purchase_forex(context):
    print('running forex')
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://www.pstrading.online/forex'>here</a> to purchase a Paramount forex subscription!" + sub_text, parse_mode=ParseMode.HTML)

def purchase_sports(context):
    print('running sports')
    context.bot.send_message(chat_id=CHAT_ID, text="Enjoy our services? Click <a href='https://www.pstrading.online/sports'>here</a> to purchase a Paramount sports subscription!" + sub_text, parse_mode=ParseMode.HTML)

def purchase_trading(context):
    print('running trading')
    context.bot.send_message(chat_id=CHAT_ID, text="Well thats the end of the trading day. Click <a href='https://www.pstrading.online/trading'>here</a> to purchase a Paramount trading subscription!" + sub_text, parse_mode=ParseMode.HTML)

def purchase_trading_morning(context):
    print('running trading')
    context.bot.send_message(chat_id=CHAT_ID, text="Good Morning! We hope you have a good day. Click <a href='https://www.pstrading.online/trading'>here</a> to purchase a Paramount trading subscription!" + sub_text, parse_mode=ParseMode.HTML)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)





def main():

    u = Updater(TOKEN, use_context=True)
    u.dispatcher.add_handler(CommandHandler('start', daily_job, pass_job_queue=True))
    u.dispatcher.add_error_handler(error)

    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    sport = datetime.time(19, 00, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    trading = datetime.time(15, 30, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    forex = datetime.time(18, 00, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    morning_1 = datetime.time(9, 00, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    morning_2 = datetime.time(9, 30, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    morning_3 = datetime.time(10, 00, 00, 000000, tzinfo=pytz.timezone('America/Chicago'))
    print("Time its supposed to post sport", sport)
    print("Time its supposed to post trading", trading)
    print("Time its supposed to post forex", forex)
    #u.bot.send_message(chat_id=CHAT_ID, text='Activating daily paramount notification!')
    u.job_queue.run_daily(purchase_forex, forex, days=tuple(range(7)))
    u.job_queue.run_daily(purchase_sports, sport, days=tuple(range(7)))
    u.job_queue.run_daily(purchase_trading, trading, days=tuple(range(7)))
    u.job_queue.run_daily(purchase_forex, morning_3, days=tuple(range(7)))
    u.job_queue.run_daily(purchase_sports, morning_1, days=tuple(range(7)))
    u.job_queue.run_daily(purchase_trading_morning, morning_2, days=tuple(range(7)))


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