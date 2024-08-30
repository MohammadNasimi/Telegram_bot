from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests


async def fact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    fact = data.json()["text"]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=fact)
    
    
async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    print(job.chat_id)
    await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} seconds are over!")

async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_message.chat_id
    due = float(context.args[0])
    print(due)
    context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)


if __name__ == "__main__":
    token = "7291366744:AAFFY0L0FL-_HQHBN8QB2SelC24T6l8fD6k"
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler(["fact","start"], fact_handler))
    application.add_handler(CommandHandler("set", set_timer))
    application.run_polling()