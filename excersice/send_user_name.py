import logging 
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN: Final = "7383894186:AAF3J5tMA0r1tvLerqwRQawEfgC5KYc_puo"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hi {update.effective_user.first_name}!"
    )

# async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.effective_chat.send_message(f"Hi {update.effective_user.first_name}!")
    
# async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f"Hi {update.effective_user.first_name}!")
    
if __name__=="__main__":
    # Create the Application and pass it your bot's token
    application= Application.builder().token(TOKEN).build()
    #Command Handler
    application.add_handler(CommandHandler("start", start_handler))
    # Run the Bot
    application.run_polling()