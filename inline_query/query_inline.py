from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler ,InlineQueryHandler

token = "7291366744:AAFFY0L0FL-_HQHBN8QB2SelC24T6l8fD6k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def inlineHandle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_request = update.inline_query
    if not inline_request:
        return

    query = inline_request.query
    if not query:
        return

    responses = [
            InlineQueryResultArticle(id='1', title="UpperCase", input_message_content=InputTextMessageContent(query.upper())),
            InlineQueryResultArticle(id='2', title="LowerCase", input_message_content=InputTextMessageContent(query.lower())),
            ]

    await inline_request.answer(responses)
    
if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(InlineQueryHandler(inlineHandle))
    application.run_polling()