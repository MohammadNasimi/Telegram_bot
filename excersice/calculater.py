from typing import Final

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

BOT_TOKEN: Final = "7383894186:AAF3J5tMA0r1tvLerqwRQawEfgC5KYc_puo"


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, I'm a bot! Thanks for using me!",
        reply_to_message_id=update.effective_message.id,
    )


async def add_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # write your code here
    try:
        a = context.args
        n= int(a[0])
        m=int(a[1])
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{n} + {m} = {n + m}",
            reply_to_message_id=update.effective_message.id,
        )
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"error {e}",
            reply_to_message_id=update.effective_message.id,
        )


async def multiplication_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    # write your code here
    try:
        a = context.args
        n= int(a[0])
        m=int(a[1])
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{n} * {m} = {n * m}",
            reply_to_message_id=update.effective_message.id,
        )
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"error {e}",
            reply_to_message_id=update.effective_message.id,
        )


async def calculate_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # write your code here
    try:
        
        resp = eval(' '.join(context.args))
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"{' '.join(context.args)} = {resp}",
                reply_to_message_id=update.effective_message.id,
            )
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"error {e}",
            reply_to_message_id=update.effective_message.id,
        )


if __name__ == "__main__":
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # adding handlers
    bot.add_handler(CommandHandler("start", start_command_handler))
    # add all your handlers here
    bot.add_handler(CommandHandler("add",add_command_handler))
    bot.add_handler(CommandHandler("mult",multiplication_command_handler))
    bot.add_handler(CommandHandler("calc",calculate_command_handler))
    # start bot
    bot.run_polling()
