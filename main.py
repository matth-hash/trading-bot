import logging
from telegram.ext import Application, CommandHandler
from core.prime_handlers import start_handler, scan_handler
from core.config import TELEGRAM_TOKEN

# Configuration du logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("scan", scan_handler))

    application.run_polling()

if __name__ == "__main__":
    main()
