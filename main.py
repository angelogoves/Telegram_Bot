import os
import logging
import time
from datetime import datetime

from pyrogram import Client, filters, idle
from config import Config
from func import modify_caption_to_filename, rename, file_caption, file_captions, file_caption_entities, send_caption_entities
from progress import progress_bar, download_progress_bar

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

bot = Client("bot",
             bot_token=Config.BOT_TOKEN,
             api_id=Config.API_ID,
             api_hash=Config.API_HASH)
bot.start()
me = bot.get_me()
print(f"Successfully deployed @{me.username}")
start_time = time.time()


@bot.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(c, m):
    chat_id = m.from_user.id
    if chat_id == Config.OWNER_ID or chat_id == Config.ACG_ID or chat_id == Config.C_ID:
        print(f"User_id : {chat_id} ; User_name : {m.from_user.first_name} {m.from_user.last_name}")
        await m.reply_text(f"HI {m.from_user.first_name}😌\nWhat would you like to do "
                           f"today?\n**/sendseries\nOR\n/sendmovies**")
    else:
        print(f"User_id : {chat_id} ; User_name : {m.from_user.first_name} {m.from_user.last_name}")
        await m.reply(f"HI {m.from_user.first_name}\nI don't know you 🙁\nOops.. I know your name now😅")


@bot.on_message(filters.command("help") & filters.private & filters.incoming)
async def get_help(c, m):
    await m.reply(f'<a href="https://www.google.com">**GO ASK GOOGLE**</a>')


@bot.on_message(filters.command("sendseries") & filters.private & filters.incoming)
async def send_series(c, m):
    chat_id = m.from_user.id
    if chat_id == Config.ACG_ID:
        path = Config.PATH_ACGSERIES
        os.chdir(path)
        for folder in os.listdir():
            new_path = os.path.join(path + '\\' + folder)
            os.chdir(new_path)
            await bot.send_sticker(chat_id=m.from_user.id, sticker=f"{Config.STICKER}{folder}.webp")
            # await bot.send_sticker(chat_id=m.from_user.id, sticker=f"{Config.STICKER}1.webp")
            for file in os.listdir():
                file_name, file_ext = os.path.splitext(file)
                newname = rename(file_name) + file_ext
                os.rename(file, newname)
            for f in os.listdir():
                file_name, file_ext = os.path.splitext(f)
                print(f"Sending file... {f}   {current_time}")
                send_message = await m.reply_text(f"**Sending File**\n{f}")
                await m.reply_document(
                    document=f,
                    caption=file_caption(file_name),
                    # caption_entities=send_caption_entities(file_name),
                    thumb=Config.THUMB_ACGSERIES,
                    progress=progress_bar,
                    progress_args=("Sending:", start_time, send_message))
                await bot.delete_messages(Config.chat_id, Config.message_id)
                # print(f"Message Deleted   Chat id : {Config.chat_id}  Message id : {Config.message_id}")
                os.chdir(new_path)
                os.remove(f)
            os.chdir(path)
            os.rmdir(folder)
            await bot.send_sticker(chat_id=m.from_user.id, sticker=Config.STICKER + "end.webp")
        await bot.send_sticker(chat_id=m.from_user.id, sticker=Config.STICKER + "the_end.webp")
        await m.reply("**Folder Empty**")
    else:
        await m.reply("**Folder Empty**")


@bot.on_message(filters.command("sendmovies") & filters.private & filters.incoming)
async def send_movies(c, m):
    chat_id = m.from_user.id
    if chat_id == Config.ACG_ID:
        os.chdir(Config.PATH_ACGMOVIES)
        for file in os.listdir():
            file_name, file_ext = os.path.splitext(file)
            newname = rename(file_name) + file_ext
            os.rename(file, newname)
        for f in os.listdir():
            file_name, file_ext = os.path.splitext(f)
            print(f"Sending file... {f}   {current_time}")
            send_message = await m.reply_text(f"**Sending File**\n{f}")
            await m.reply_document(
                document=f,
                caption=file_caption(file_name),
                # caption_entities=send_caption_entities(file_name),
                thumb=Config.THUMB_ACGMOVIES,
                progress=progress_bar,
                progress_args=("Sending:", start_time, send_message)
                )
            await bot.delete_messages(Config.chat_id, Config.message_id)
            # print(f"Message Deleted   Chat id : {Config.chat_id}  Message id : {Config.message_id}")
            os.remove(f)
        await bot.send_sticker(chat_id=m.from_user.id, sticker=Config.STICKER + "the_end.webp")
    await m.reply("**Folder Empty**")


@bot.on_message(filters.command("nptel") & filters.private & filters.incoming)
async def send_nptel(c, m):
    chat_id = m.from_user.id
    if chat_id == Config.OWNER_ID:
        path = Config.PATH_NPTEL
        os.chdir(path)
        for folder in os.listdir():
            new_path = os.path.join(path + '\\' + folder)
            os.chdir(new_path)
            await bot.send_photo(
                chat_id=m.chat.id,
                photo=Config.THUMB_NPTEL,
                caption=file_caption(folder)
            )
            for f in os.listdir():
                file_name, file_ext = os.path.splitext(f)
                print(f"Sending file... {f}")
                send_message = await m.reply_text(f"**Sending File**\n{f}")
                await m.reply_document(
                    document=f,
                    caption=file_caption(file_name),
                    caption_entities=send_caption_entities(file_name),
                    thumb=Config.THUMB_NPTEL,
                    progress=progress_bar,
                    progress_args=("Sending:", start_time, send_message))
                await bot.delete_messages(int(Config.chat_id), int(Config.message_id))
                os.remove(f)
            await bot.send_sticker(chat_id=m.from_user.id, sticker=Config.STICKER + "the_end.webp")
    await m.reply("**Folder Empty**")


@bot.on_message((filters.command("download") | filters.document | filters.video) & filters.private & filters.incoming)
async def download(c, m):
    if m.text == "/download":
        await m.reply_text("Send Files to Download")
    elif not m.caption:
        print(f"{m.document.file_name}\t already Exist")
    else:
        os.chdir(Config.DOWNLOAD_PATH)
        filename = m.document.file_name
        file_name, file_ext = os.path.splitext(filename)
        newname = modify_caption_to_filename(m.caption, file_ext)
        if newname in os.listdir():
            print(f"{newname} already Exist")
        elif filename in os.listdir():
            os.rename(filename, newname)
            print(f"{filename}\nRenamed to \n{newname}")
        else:
            await m.reply(f"{newname}\n**Doesn't Exist**")
            """
            print(f"Downloading file... {filename}")
            send_message = await m.reply_text(f"**Downloading File**\n{filename}")
            path = f"{Config.DOWNLOAD_PATH}\\{filename}"
            await m.download(
                file_name=path,
                progress=download_progress_bar,
                progress_args=("Downloading:", start_time, send_message))
            await bot.delete_messages(int(Config.down_chat_id), int(Config.down_message_id))
            # print(f"Message Deleted   Chat id : {Config.down_chat_id}  Message id : {Config.down_message_id}")
            os.rename(filename, newname)
            await m.reply(f"{newname}\n**Downloaded**")
            """


@bot.on_message(filters.photo & filters.private & filters.incoming)
async def photo(c, m):
    chat_id = m.from_user.id
    if chat_id == Config.OWNER_ID or chat_id == Config.ACG_ID or chat_id == Config.C_ID:
        if m.caption:
            await bot.send_photo(
                chat_id=m.chat.id,
                photo=m.photo.file_id,
                caption=file_captions(m.caption),
                caption_entities= m.caption_entities,
                # caption_entities=file_caption_entities(m.caption, m.caption_entities),
                reply_markup=m.reply_markup
            )
            await m.reply(Config.acg_caption)


if idle():
    bot.stop()
    print("Ok bye 😢.")
