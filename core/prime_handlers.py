import logging
from telegram import Update
from telegram.ext import ContextTypes
from core.prime_algo import run_scan

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot de trading démarré ! Utilise /scan pour analyser le marché.")

async def scan_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Lancement du scan...")
    try:
        results = run_scan()
        for result in results:
            await update.message.reply_text(f"Signal: {result['symbol']} - {result['signal']} (Score: {result['score']})")
    except Exception as e:
        logging.error(f"Erreur lors du scan: {e}")
        await update.message.reply_text(f"Une erreur est survenue: {e}")
