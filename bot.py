import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

import settings

TOKEN = 'settings.TELEGRAM_API_KEY'

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
async def start_bot(update, context):
    print(update)
    mytext = """Привет {} Я простой бот имею только команду {}""".format(update.message.chat.first_name, '/start')
    logging.info(f'Пользователь {update.message.chat.username}')
    await update.message.reply_text(mytext)


async def chat(update, context):
    text = update.message.text
    logging.info(text)
    await update.message.reply_text(text)


def main():
    updtr = Application.builder().token(settings.TELEGRAM_API_KEY).build()

    updtr.add_handler(CommandHandler("start", start_bot))
    updtr.add_handler(MessageHandler(filters.TEXT, chat))

    updtr.run_polling()

if __name__ == '__main__':
    logging.info('Bot started')
    main()
