import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip().lower()

    if texto == "hola":
        await update.message.reply_text(
            "Hola ya recupere mi cuenta Josito el rey 👑"
        )


def main():
    if not TOKEN:
        raise RuntimeError("Falta configurar TELEGRAM_BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            responder
        )
    )

    print("Bot encendido...")
    app.run_polling()


if __name__ == "__main__":
    main()