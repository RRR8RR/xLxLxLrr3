import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["اصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/4edb726cd168c2f4e1654.jpg",
        caption=f"""**⩹━★⊷⌯⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
★᚜ اسم سورس:-رنثون
★᚜ نوعه:-ميوزك
★᚜ للغه برمجه:- بايثون
★᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
★᚜ مجال تشغيل :- تشغيل بوتات الميوزك
★᚜ نظام تشغيل:-cr بوت ميوزك
★᚜ الاصدار 4.0.1 pyrogram 
★᚜ تاريخ تاسيس:-21-3-2023
★᚜ مأسس رنثون:- [𓆩˹ 【﻿𝗔َِ𝗹َِ𝘀َِ𝗵| 🇮🇶】•༄►](https://t.me/BxxBxxL)

**⩹━★⊷⌯𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝⌯⊶★━⩺ ⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝⌯⊶★━⩺ ⌝", url=f"https://t.me/xLxLxLrr3"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


