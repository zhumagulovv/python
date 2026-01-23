from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

FAQ = {
    'наличие': '🚗 Актуальное наличие авто уточняйте у менеджера по телефону +996 774 814 583',
    'есть ли': '🚘 Подскажите модель и год — мы проверим наличие.',
    'цена': '💰 Цены зависят от модели и комплектации. Напишите модель.',
    'сколько стоит машина?': '💰 Стоимость зависит от модели и года выпуска.',
    'кредит': '🏦 Мы оформляем авто в кредит и рассрочку. Первоначальный взнос от 20%.',
    'рассрочка': '📄 Рассрочка до 36 месяцев.',
    'трейд': '🔄 Возможен Trade-In. Привозите авто на оценку.',
    'trade': '🔄 Trade-In доступен. Оценка бесплатная.',
    'тест': '🧪 Тест-драйв возможен по предварительной записи.',
    'адрес': '📍 г. Бишкек, ул. Табышалиева 29',
    '📍 Мы на карте': '📍 Мы находимся в г. Бишкек, ул. Табышалиева 29',
    'график': '⏰ Работаем ежедневно с 09:00 до 19:00',
    'время': '⏰ Салон открыт с 09:00 до 19:00',
    'контакты': '📞 +996 774 814 583\n📧 autosalon_okurmen@example.com'
}

MAP_URL = 'https://2gis.kg/bishkek/geo/15763234351062857/74.586745,42.871584'

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ['🚗 Наличие авто', '💰 Цены/Стоимость'],
        ['🏦 Кредит/Рассрочка','🔄 Trade-In/Трейд'],
        ['📞 Контакт', '🧪 Тест-драйв'],
        ['📍 Адрес/Карта', '⏰ График работы'],
    ],
    resize_keyboard=True
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🚗 Добро пожаловать в автосалон!\n\n'
        'Выберите интересующий пункт:',
        reply_markup=MAIN_KEYBOARD
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '✍️ Просто напишите вопрос.\n'
        'Например:\n'
        '— Есть ли Toyota Camry?\n'
        '— Сколько стоит авто?\n'
        '— Можно ли в кредит?'
    )

# Ответы на кнопки
# Ответы на кнопки
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '🚗 Наличие авто':
        await update.message.reply_text(
            '🚘 В наличии автомобили:\n'
            '•Toyota (Camry, Prius)\n'
            '•Honda (Fit, CR-V, Accord)\n'
            '•Daewoo (Matiz, Nexia)\n'
            '•Бюджетными китайскими электрокарами (Auchan A600 EV, Mini EV)\n'
            '•Mercedes-Benz E-класса, Hyundai.\n'
        )

    elif text == '💰 Цены/Стоимость':
        await update.message.reply_text(
            '💵 Цены зависят от модели и комплектации.\n'
        )

    elif text == '🏦 Кредит/Рассрочка':
        await update.message.reply_text(
            '🏦 Авто в кредит:\n'
            '• Первоначальный взнос от 20%\n'
            '• Срок до 36 месяцев\n\n'
            '📞 Для подробной информации свяжитесь с менеджером:\n'
            '+996774814583',
        )

    elif text == '🧪 Тест-драйв':
        await update.message.reply_text(
            '🧪 Тест-драйв по предварительной записи.\n'
        )

    elif text == '📍 Адрес/Карта':
        await update.message.reply_text(
            f'📍 Наш адрес:\n г. Бишкек, ул. Табышалиева 29\n\n'
            f'👉 Открыть на карте:\n{MAP_URL}'
        )

    elif text == '🔄 Trade-In/Трейд':
        await update.message.reply_text(
            "🔄 Trade-In доступен. Оценка бесплатная."
        )

    elif text == '⏰ График работы':
        await update.message.reply_text(
            "⏰ Работаем ежедневно с 09:00 до 19:00"
        )

    elif text == '📞 Контакт':
        await update.message.reply_text(
            "📞 +996 774 814 583\n📧 autosalon_okurmen@gmail.com"
        )

    else:
        await update.message.reply_text(
            'Пожалуйста, выберите пункт из меню 👇'
        )

# Обработка текста
async def faq_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    for key, answer in FAQ.items():
        if key in user_text:
            await update.message.reply_text(answer)
            return

    await update.message.reply_text(
        '❓ Уточните, пожалуйста, вопрос.\n'
        'Или напишите /help'
    )

if __name__ == '__main__':
    API_TOKEN = os.getenv('BOT_TOKEN')

    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Bot started")
    app.run_polling()
