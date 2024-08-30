from typing import Final

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

BOT_TOKEN: Final = "7383894186:AAF3J5tMA0r1tvLerqwRQawEfgC5KYc_puo"



async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, I'm a bot! Thanks for using me!",
        reply_to_message_id=update.effective_message.id,
    )


async def upper_case_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    # write your code here
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=update.message.text.upper(), 
                                   reply_to_message_id=update.effective_message.id)


async def echo_sticker_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    # write your code here
    await context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker=update.effective_message.sticker.file_id,
        reply_to_message_id=update.effective_message.id,
    )


if __name__ == "__main__":
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # adding handlers
    bot.add_handler(CommandHandler("start", start_command_handler))
    # add all your handlers here
    bot.add_handler(MessageHandler(filters.TEXT, upper_case_message_handler))
    bot.add_handler(MessageHandler(filters.Sticker, upper_case_message_handler))

    # start bot
    bot.run_polling()
