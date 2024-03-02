from  requests import
import random
from aiogram import Bot, Update
from aiogram.ext import Updater, CommandHandler, CallbackContext


UNSPLASH_API_KEY = 'YOUR_API_KEY'

def get_nature_image():
    
    url = f"https://api.unsplash.com/photos/random?query=nature&client_id={UNSPLASH_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if 'urls' in data:
        return data['urls']['regular']
    else:
        return None

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот, который отправляет случайные изображения природы. Введите /nature, чтобы получить изображение.")

def nature(update: Update, context: CallbackContext):
    nature_image_url = get_nature_image()
    if nature_image_url:
        update.message.reply_photo(nature_image_url)
    else:
        update.message.reply_text("Извините, не удалось получить изображение природы. Попробуйте еще раз позже.")

def main():
    
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("nature", nature))

    
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()