import logging
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

    # Utiliser un webhook au lieu de polling
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=trading-bot-production-a363.up.railway.app,
    )

if __name__ == "__main__":
    main()
