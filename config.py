import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    OWNER_ID = int(os.getenv("OWNER_ID"))
    ACG_ID = int(os.getenv("ACG_ID"))
    C_ID = int(os.getenv("C_ID"))

    THUMB_ACGSERIES = os.getenv("THUMB_ACGSERIES")
    THUMB_ACGMOVIES = os.getenv("THUMB_ACGMOVIES")
    STICKER = os.getenv("STICKER")

    acg_caption = os.getenv("acg_caption")
    acg_caption_entities = []

    PATH_ACGSERIES = os.getenv("PATH_ACGSERIES")
    PATH_ACGMOVIES = os.getenv("PATH_ACGMOVIES")

    DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH")

    chat_id = ""
    message_id = ""
    down_chat_id = ""
    down_message_id = ""
