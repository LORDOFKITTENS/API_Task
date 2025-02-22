import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Путь к файлу для сохранения данных
DATA_FILE = 'output.txt'

def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start."""
    user = update.effective_user
    message = (
        f"Привет, {user.first_name}!\n"
        "Я сохраню твои данные для дальнейшего использования."
    )
    update.message.reply_text(message)

    # Сохраняем данные пользователя в файл
    save_user_data(user)

def save_user_data(user):
    """Сохраняет данные пользователя в текстовый файл."""
    data = {
        'First Name': user.first_name,
        'Last Name': user.last_name or 'N/A',
        'Username': user.username or 'N/A',
        'User ID': user.id,
    }

    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("-" * 40 + "\n")  # Разделитель между записями

def main():
    """Основная функция для запуска бота."""
    # Загрузите токен из переменной окружения или config.json
    token = os.getenv(7805796024:AAHYV5UUhdLyzEKRk6UX5a01mu6sL2DrAtI)
    if not token:
        print("Токен не найден. Укажите его в переменной окружения TELEGRAM_BOT_TOKEN.")
        return

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Добавьте обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()