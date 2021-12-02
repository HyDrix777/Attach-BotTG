# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Attach-Bot/blob/main/LICENSE

import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Telegram Attach Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
𝗛𝗲𝗹𝗹𝗼 {}, 𝗜 𝗮𝗺 𝗮 𝗺𝗲𝗱𝗶𝗮 𝗼𝗿 𝗳𝗶𝗹𝗲 𝗶𝗻 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗮𝘁𝘁𝗮𝗰𝗵 𝗯𝗼𝘁. 𝗜 𝗰𝗮𝗻 𝗮𝘁𝘁𝗮𝗰𝗵 𝗽𝗵𝗼𝘁𝗼, 𝘃𝗶𝗱𝗲𝗼, 𝗮𝘂𝗱𝗶𝗼 𝗲𝘁𝗰. 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲𝗶𝗿 𝗽𝘂𝗯𝗹𝗶𝗰 𝗹𝗶𝗻𝗸𝘀 𝗶𝗻 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲.


"""
HELP_TEXT = """
<u><b>Steps :-</b></u>
- 𝗝𝘂𝘀𝘁 𝘀𝗲𝗻𝗱 𝗮 𝗵𝘁𝗺𝗹 𝗼𝗿 𝗺𝗮𝗿𝗸𝗱𝗼𝘄𝗻 𝗺𝗲𝘀𝘀𝗮𝗴𝗲
- 𝗥𝗲𝗽𝗹𝘆 𝗮 𝗹𝗶𝗻𝗸 𝗳𝗼𝗿 𝗮𝘁𝘁𝗮𝗰𝗵𝗶𝗻𝗴

<u><b>Tips :-</b></u>
• 𝗨𝘀𝗲 @Telegra_Xtgbot 𝗳𝗼𝗿 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 𝗹𝗶𝗻𝗸𝘀 𝗼𝗳 𝗽𝗵𝗼𝘁𝗼𝘀 𝗮𝗻𝗱 𝘃𝗶𝗱𝗲𝗼𝘀
• 𝗨𝘀𝗲 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗽𝘂𝗯𝗹𝗶𝗰 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗼𝗿 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗹𝗶𝗻𝗸𝘀
• 𝗬𝗼𝘂 𝗰𝗮𝗻 𝘀𝗲𝗻𝗱 𝗮𝗻𝘆 𝘁𝘆𝗽𝗲 𝗼𝗳 𝗹𝗶𝗻𝗸𝘀 𝗳𝗼𝗿 𝗮𝘁𝘁𝗮𝗰𝗵𝗶𝗻𝗴

𝗠𝗮𝗱𝗲 𝗯𝘆 🦸
"""
ABOUT_TEXT = """
- **Bot :** `Attach Bot`
- **Creator :** [Hydrix](https://t.me/HydraLivegrambot)
- **Andros :** [Hydra](https://t.me/Tg_Hydra_Galaxy)
- **Channel :** [Click here](https://t.me/Tg_Galaxy)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📣 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url='https://t.me/Tg_Galaxy'),
        InlineKeyboardButton('🗣️ 𝗢𝘄𝗻𝗲𝗿', url='https://t.me/HydraLivegrambot)
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

@FayasNoushad.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )

@FayasNoushad.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )

@FayasNoushad.on_message(filters.text & filters.private & filters.reply & filters.regex(pattern=".*http.*"))
async def attach(bot, update):
    await update.reply_text(
        text=f"[\u2063]({update.text}){update.reply_to_message.text}",
        reply_markup=update.reply_to_message.reply_markup
    )

FayasNoushad.run()
