from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")],
        [KeyboardButton(text="Отсосать")],
        [KeyboardButton(text="Экстренная помощь")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт",
)

def get_sizer_digs_keyboard() -> InlineKeyboardMarkup:
    main_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Получи размер своего члена", callback_data="my_dick_size")],
    ])
    
    return main_inline_kb
