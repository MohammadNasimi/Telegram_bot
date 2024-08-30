from typing import Final

from telegram import (
    Update,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler,
)

BOT_TOKEN: Final = "7383894186:AAF3J5tMA0r1tvLerqwRQawEfgC5KYc_puo"

GENDER, PHOTO, BIO = range(3)

data_user = {}

async def start_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    # write your code here
    text = ("Hi, I'm here to find out more information about you."
        "You can /cancel me at any time you want.\n\n"
        "Are you a Boy or a Girl?")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )
    return GENDER



async def gender_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    text = ("Okay, Now can you please send me a photo of your self."
        "If you don't want to do that, you can /skip this state.")
    # write your code here
    data_user[update.effective_chat.id] = update.message.text
    await context.bot.send_message(text=text,
                                   chat_id=update.effective_chat.id)
    return PHOTO

async def photo_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    # write your code here
    text =("Okay, Now can you please send me a bio about yourself.")
    image = await update.message.photo[-1].get_file()
    url_image = await image.download_to_drive(f"photos/user_{update.effective_user.id}.jpg")
    data_user[update.effective_chat.id] = url_image
    await context.bot.send_message(text=text,
                                   chat_id=update.effective_chat.id)
    return BIO

async def skip_photo_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    # write your code here
    text =("Okay, Now can you please send me a bio about yourself.")

    await context.bot.send_message(text=text,
                                   chat_id=update.effective_chat.id)
    return BIO


async def bio_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    # write your code here
    data_user[update.effective_chat.id] = update.message.text
    await context.bot.send_message(text="Thank you! I hope we can talk again some day.",
                                   chat_id=update.effective_chat.id)
    
    return ConversationHandler.END



async def cancel_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    # write your code here
    data_user[update.effective_chat.id] = update.message.text
    await context.bot.send_message(text="Bye! I hope we can talk again some day.",
                                   chat_id=update.effective_chat.id)
    return ConversationHandler.END

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("error:",context.error,"on Update",update)
    
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("start", start_command_handler)],
            states={
                GENDER: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND, gender_message_handler
                    )
                ],
                PHOTO: [
                    MessageHandler(filters.PHOTO, photo_message_handler),
                    CommandHandler("skip", skip_photo_command_handler),
                ],
                BIO: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, bio_message_handler)
                ],
            },
            fallbacks=[
                CommandHandler("cancel", cancel_command_handler),
            ],
            allow_reentry=True,
        )
    )
    app.add_error_handler(error_handler)
    app.run_polling()
