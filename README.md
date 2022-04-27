# Telegram Bot 

[Read this in English](https://github.com/RDonii/DarsSavdo-Telegram-Bot#english)
## Uzbek
### Umumiy ma'lumot
Ta'lim beruvchi platformalarga ordamchi bo'luvchi o'quv kurslari savdosini telegram orqali ta'minlovchi botning eng sodda ko'rinishi. Botni yaratishdan maqsad bot bo'ylab kezish imkoniyatlarini ko'rsatish bo'lganligi uchun unga juda katta imkoniyatlar qo'shilmagan.

### Ishga tushirish
Botni ishga tushirish uchun sizga @BotFather va @userinfobot telegram botlaridan olingan quyidagi mahfiy qiymatlar kerak bo'ladi. .env faylini yaratib, jadvaldagi nomlar bilan saqlab qo'yish lozim.

| Nomi  | Qayerdan | .env nomi |
| ------------- | ------------- | ------------- |
| Bot token  | @BotFather  | BOT_TOKEN |
| Admin user id  | @userinfobot  | ADMINS |

Python tilining yangi versiyalaridan birini o'rnatib bo'lgach, `pip install -r requirements.txt` buyrug'i yordamida kerakli modullar o'rnatiladi.

So'ngra, `python app.py` orqali bot ishga tushiriladi.

## English
[O'zbek tilida o'qish](https://github.com/RDonii/DarsSavdo-Telegram-Bot#uzbek)
### General information
The simplest view of a bot that provides telegram sales of training courses that support educational platforms. Since the goal of creating the bot was to show the ability to navigate the bot, it didn’t add much potential.

### Dependencies
To run the bot, you will need special values from @BotFather and @userinfobot telegram bots. Create an .env file and save it with the names shown in the table.

| name  | Where | in .env |
| ------------- | ------------- | ------------- |
| Bot token  | @BotFather  | BOT_TOKEN |
| Admin user id  | @userinfobot  | ADMINS |

After installing one of the newer versions of Python, the required modules are installed using the command `pip install -r requirements.txt`.

Then the bot is launched with the commad `python app.py`.