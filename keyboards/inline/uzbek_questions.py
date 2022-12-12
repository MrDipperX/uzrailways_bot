from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import uzbek_questions_callback

questions_dict = {'pdf chipta olish':'pdf',
        'Chiptani qaytarish': 'cancel',
        'Chipta fakturasi':'schet',
        'Chiptani almashtirish':'change',
        'Chipta chegirmalari':'discount',
        "Platformada ro'yxatdan o'tish":'registration',
        "Chiptasiz chiqish" : "passport_no",
        "Yangi vagonlar va yo'nalishlar" : 'new_vagon',
        'Boshqa mavzu' : 'another'}

uzbek_questions = InlineKeyboardMarkup(row_width=1)
for key, value in questions_dict.items():
    uzbek_questions.insert(InlineKeyboardButton(text=key, callback_data = uzbek_questions_callback.new(item_name=value)))

return_questions_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ortga', callback_data='return_uzb')
        ]
    ]
)

return_questions_state_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ortga', callback_data='return_state_uzb')
        ]
    ]
)