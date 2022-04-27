from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

productInline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🛍Sotib olish', callback_data='buy_now'),
            InlineKeyboardButton(text="📦Bo'lib to'lash", callback_data='buy_later')
        ],
        [
            InlineKeyboardButton(text='🔗Bizning sahifa', url='www.ccslife.uz')
        ],
        [
            InlineKeyboardButton(text='📧Yaqiningizga ulashish', switch_inline_query='Oppa gungamstar')
        ],
        [
            InlineKeyboardButton(text='🔎Qidirish', switch_inline_query_current_chat='')
        ]
    ]
)