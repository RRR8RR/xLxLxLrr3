import asyncio

import os
import time
import requests
from config import OWNER_ID, USER_OWNER
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين 𝗥𝗨𝗡𝗧𝗛𝗢𝗡","المطورين","مطورين","مطورين رنثون"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/4edb726cd168c2f4e1654.jpg",
        caption=f"""**⩹━★⊷━⌞ 𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين رنثون ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗔َِ𝗹َِ𝘀َِ𝗵 | 🇮🇶 ˹َّّ ", url=f"https://t.me/BxxBxxL"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "★⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝⚡", url=f"https://t.me/xLxLxLrr3"),
                
        ],

            ]

        ),

    )








@app.on_message(
    command(["حمد","مبرمج السورس","احمد","احمد"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("BxxBxxL")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["قناة السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("xLxLxLrr3")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["مطورك","حمد","حمادي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("BxxBxxL")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}مطوري\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**معلومات المطور الاساسي \n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور البوت", url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/xLxLxLrr3"),                        
                 ],
            ]
        ),
    )
    


@app.on_message(
    command(["ذكاء حياه"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/4edb726cd168c2f4e1654.jpg",
        caption=f"""**⩹⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس رنثون\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗔َِ𝗹َِ𝘀َِ𝗵 | 🇮🇶 ˹َّّ", url=f"https://t.me/BxxBxxL"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝⚡", url=f"https://t.me/xLxLxLrr3"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/4edb726cd168c2f4e1654.jpg",
        caption=f"""**⩹⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس رنثون\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗔َِ𝗹َِ𝘀َِ𝗵 | 🇮🇶 ˹َّّ", url=f"https://t.me/BxxBxxL"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞𝗦𝗢𝗨𝗥𝗖𝗘 • 𝗥𝗨𝗡𝗧𝗛𝗢𝗡⌝⚡", url=f"https://t.me/xLxLxLrr3"),
                ],

            ]

        ),

    )



    
