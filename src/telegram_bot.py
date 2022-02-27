import logging
from matplotlib.pyplot import text
from telegram.ext import *
# import responses
from telegram import Bot, update
import os
import dotenv
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("TELE_API")
bot = Bot(API_KEY)
gloabl = 0
# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello Embalmer! Welcome to Sarcophagus bot')
    bot.send_photo(update.message.chat_id, 'https://static.wixstatic.com/media/7688ef_f73547c3c232478f997883a8768deda9~mv2.gif')
    bot.sendMessage(update.message.chat_id,text = 'please message begin to start')
def help_command(update, context):
    update.message.reply_text('This is a bot to help you create you sarcophagus.For more info please visit https://sarcophagus.io/')


def custom_command(update, context):
    update.message.reply_text('Try using other commands')


def handle_message(update, context):

            text = str(update.message.text).lower()
            logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
            if text == 'begin':
                response='please send numbers from 1 to get instructions for corresponding steps'
            elif text=='1':
                response='Enter the name of your sarcophagi'
            elif text=='2':
                response='type the public key of recipient.(use : https://app.dev.sarcophagus.io/#/publicKey if required)'
            elif text=='3':
                response='choose the time until which you need the data to be wrapped(this can be altered through rewrapping)'
            elif text=='4':
                response='Pick an archaeologist with suitable metrics,bounty and digging fee for you!'
            elif text=='5':
                response='click on finish and wait some time till data is uploaded on arweave'
            elif text=='6':
                response='click sign button and approve the transaction from your wallet'
            
                

            # response = responses.get_response(text)
            update.message.reply_text(response)


    


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    # bot.sendMessage(1585090984,text='Hello')
  

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
