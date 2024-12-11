from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")],
        [KeyboardButton(text="Отсосать")],
        [KeyboardButton(text="Экстренная помощь")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт",
)
