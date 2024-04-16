import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**ℍɪɪ** ┈━═𝗠𝗬 𝗧𝗫𝗧 𝗟𝗢𝗩𝗘𝗥═━┈🙈❤️\n\n𝗜 𝗔𝗠 𝗔 𝗕𝗢𝗧 𝗙𝗢𝗥 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗟𝗜𝗡𝗞𝗦 𝗙𝗥𝗢𝗠 𝗬𝗢𝗨𝗥 **.𝗧𝗫𝗧** 𝗙𝗜𝗟𝗘 𝗔𝗡𝗗 𝗧𝗛𝗘𝗡 𝗨𝗣𝗟𝗢𝗔𝗗 𝗧𝗛𝗔𝗧 𝗙𝗜𝗟𝗘 𝗢𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗦𝗢 𝗕𝗔𝗦𝗜𝗖𝗔𝗟𝗟𝗬 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 𝗙𝗜𝗥𝗦𝗧 𝗦𝗘𝗡𝗗 𝗠𝗘 /upload  𝗕𝗢𝗧 𝗠𝗔𝗗 𝗕𝗬 👀💙 @hemendra148 𝗛𝗘𝗠𝗨 𝗔𝗥𝗠𝗬 ..")


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**𝗦𝗧𝗢𝗢𝗣𝗘𝗗**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["upload"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('𝗜𝗧𝗦 𝗛𝗘𝗠𝗨 𝗕𝗢𝗧 𝗛𝗘𝗥𝗘 𝗦𝗘𝗡𝗗 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 🗂 ⚡️ ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝗧𝗢𝗧𝗔𝗟 𝗟𝗜𝗡𝗞𝗦 𝗙𝗢𝗨𝗡𝗗 𝗜𝗡 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 𝗔𝗥𝗘 🔗🔗** **{len(links)}**\n\n**✍️ 𝗡𝗢𝗪 𝗦𝗘𝗡𝗗 𝗠𝗘 𝗙𝗥𝗢𝗠 𝗪𝗛𝗘𝗥𝗘 𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗜𝗡𝗜𝗧𝗜𝗔𝗟 𝗜𝗦** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝗘𝗡𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗦𝗢𝗟𝗨𝗧𝗜𝗢𝗡 𝗙𝗢𝗥 𝗨𝗥 𝗟𝗘𝗖𝗧𝗨𝗥𝗘𝗦 🎬📸**\n144,240,360,480,720,1080 𝗣𝗟𝗘𝗔𝗦𝗘 𝗖𝗛𝗢𝗢𝗦𝗘 𝗤𝗨𝗔𝗟𝗜𝗧𝗬")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("𝗘𝗡𝗧𝗘𝗥 𝗨𝗥 𝗡𝗔𝗠𝗘 ✍️ 𝗔𝗦 𝗔 𝗛𝗜𝗚𝗛𝗟𝗜𝗚𝗛𝗧𝗘𝗥 💋 𝗧𝗢 𝗟𝗘𝗖𝗧𝗨𝗥𝗘𝗦 🥹❤️")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("𝗡𝗢𝗪 𝗦𝗘𝗡𝗗 𝗠𝗘 𝗧𝗛𝗘 🖼️ 𝗧𝗛𝗨𝗠𝗕𝗡𝗔𝗜𝗟 𝗨𝗥𝗟/nEg » https://graph.org/file/05be568f195e32e75f32f.jpg \n 𝗢𝗥 𝗜𝗙 𝗗𝗢𝗡'𝗧 𝗪𝗔𝗡𝗧 𝗧𝗛𝗨𝗠𝗕𝗡𝗔𝗜𝗟 𝗦𝗘𝗡𝗗 = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[📽️] Vid_ID:** {str(count).zfill(3)}.** {𝗻𝗮𝗺𝗲𝟭}{MR}.mkv\n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                cc1 = f'**[📁] Pdf_ID:** {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭}{MR}.pdf \n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


bot.run()
