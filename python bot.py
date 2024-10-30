import os
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Ganti dengan token bot Telegram Anda
TELEGRAM_TOKEN = '7630099641:AAEBSMcusTBa9FcOWhF_Q838NE6Rmpxl7qI'
# Ganti dengan kunci API OpenAI Anda
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo! Saya adalah bot ChatGPT. Kirimkan pesan untuk mulai!')

def respond(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    bot_reply = response['choices'][0]['message']['content']
    
    # Kirim balasan ke grup
    update.message.reply_text(bot_reply)

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
