import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from telegram.ext import Updater, MessageHandler, Filters
from django.conf import settings
from api.models import CustomUser


def handle_text(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    try:
        user = CustomUser.objects.get(telegram_token=text)
        user.telegram_chat_id = str(chat_id)
        user.save()
        update.message.reply_text("Токен успешно привязан!")
    except CustomUser.DoesNotExist:
        update.message.reply_text("Токен не найден. Пожалуйста, проверьте и попробуйте снова.")


def start_bot():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text & ~Filters.command, handle_text)
    dp.add_handler(text_handler)
    print("Bot has started! Listening for messages...")
    updater.start_polling()

if __name__ == "__main__":
    start_bot()
