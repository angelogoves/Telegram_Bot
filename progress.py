import math
import time
from pyrogram.emoji import *
from config import Config


# ------------------------------- Progress Bar 📊 -------------------------------

async def progress_bar(current, total, status_msg, start, msg):
    present = time.time()
    if round((present - start) % 3) == 0 or current == total:
        speed = current / (present - start)
        percentage = current * 100 / total
        time_to_complete = round(((total - current) / speed)) * 1000
        time_to_complete = TimeFormatter(time_to_complete)
        progressbar = "[{0}{1}]".format(
            ''.join([f"{BLACK_MEDIUM_SMALL_SQUARE}" for i in range(math.floor(percentage / 10))]),
            ''.join([f"{WHITE_MEDIUM_SMALL_SQUARE}" for i in range(10 - math.floor(percentage / 10))])
        )
        current_message = f"""**{status_msg}** {round(percentage, 2)}%
{progressbar}
{HOLLOW_RED_CIRCLE} **Speed**: {humanbytes(speed)}/s
{HOLLOW_RED_CIRCLE} **Done**: {humanbytes(current)}
{HOLLOW_RED_CIRCLE} **Size**: {humanbytes(total)}
{HOLLOW_RED_CIRCLE} **Time Left**: {time_to_complete}"""
        try:
            await msg.edit(text=current_message)
            Config.chat_id = msg.chat.id
            Config.message_id = msg.id
        except:
            pass


# -------------------------------Download Progress Bar 📊 -------------------------------

async def download_progress_bar(current, total, status_msg, start, msg):
    present = time.time()
    if round((present - start) % 3) == 0 or current == total:
        speed = current / (present - start)
        percentage = current * 100 / total
        time_to_complete = round(((total - current) / speed)) * 1000
        time_to_complete = TimeFormatter(time_to_complete)
        progressbar = "[{0}{1}]".format(
            ''.join([f"{BLACK_MEDIUM_SMALL_SQUARE}" for i in range(math.floor(percentage / 10))]),
            ''.join([f"{WHITE_MEDIUM_SMALL_SQUARE}" for i in range(10 - math.floor(percentage / 10))])
        )
        current_message = f"""**{status_msg}** {round(percentage, 2)}%
{progressbar}
{HOLLOW_RED_CIRCLE} **Speed**: {humanbytes(speed)}/s
{HOLLOW_RED_CIRCLE} **Done**: {humanbytes(current)}
{HOLLOW_RED_CIRCLE} **Size**: {humanbytes(total)}
{HOLLOW_RED_CIRCLE} **Time Left**: {time_to_complete}"""
        try:
            await msg.edit(text=current_message)
            Config.down_chat_id = msg.chat.id
            Config.down_message_id = msg.id
        except:
            pass


# ------------------------------- Size -------------------------------

def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + dic_powerN[n] + 'B'


# ------------------------- Time Formatting ⏰ ----------------------------

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " days, ") if days else "") + \
          ((str(hours) + " hours, ") if hours else "") + \
          ((str(minutes) + " min, ") if minutes else "") + \
          ((str(seconds) + " sec, ") if seconds else "") + \
          ((str(milliseconds) + " millisec, ") if milliseconds else "")
    return tmp[:-2]
