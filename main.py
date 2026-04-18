import logging
import os
from telegram.ext import Application, CommandHandler
from core.prime_handlers import start_handler, scan_handler
from core.config import TELEGRAM_TOKEN, WEBHOOK_URL

# Configuration du logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("scan", scan_handler))

    # Vérifie si WEBHOOK_URL est définie
    if WEBHOOK_URL:
        # Utiliser un webhook
        application.run_webhook(
            listen="0.0.0.0",
            port=8080,
            webhook_url=WEBHOOK_URL,
        )
    else:
        # Utiliser le polling si WEBHOOK_URL n'est pas définie
        application.run_polling()

if __name__ == "__main__":
    main()
