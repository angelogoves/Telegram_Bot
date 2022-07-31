from config import Config
from pyrogram.types import MessageEntity


def rename(new_name):
    new_name = new_name.replace(" ", ".")
    new_name = new_name.replace("_", ".")
    new_name = new_name.replace("@T4TVSeries", "HEVC-ACG")
    new_name = new_name.replace("GalaxyTV", "ACG")
    new_name = new_name.replace("PSA", "ACG")
    new_name = new_name.replace(".x264-[YTS.LT]", ".x264-ACG")
    new_name = new_name.replace(".x264.YIFY", ".x264-ACG")
    new_name = new_name.replace(".x264.YIFY.[YTS.AG]", ".x264-ACG")
    new_name = new_name.replace(".x264-[YTS.AG]", ".x264-ACG")
    new_name = new_name.replace("YIFY", "ACG")
    new_name = new_name.replace(".mp4", "")
    return new_name


def modify_caption_to_filename(msg_caption, file_ext):
    find = "\n\n"
    if find in msg_caption:
        new_name, rest = msg_caption.split(find)
    else:
        new_name = msg_caption
    new_name = new_name.replace(" ", ".")
    new_name = new_name.replace("_", ".")
    new_name = new_name.replace("\n", "")
    new_name = new_name.replace(".mkv", "")
    return new_name + file_ext


def file_caption(caption):
    caption = caption + "\n\n" + Config.acg_caption
    return caption


def file_captions(caption):
    caption = caption + "\n\n"
    return caption


def file_caption_entities(caption, caption_entities):
    entity1 = MessageEntity(type="bold", offset=len(caption) + 2, length=9)
    entity2 = MessageEntity(type="text_link", offset=len(caption) + 2, length=3, url="https://t.me/+PyuSAyLunZ45NGM1")
    Config.acg_caption_entities = [entity1, entity2]
    caption_entities = caption_entities + Config.acg_caption_entities
    return caption_entities


def send_caption_entities(caption):
    entity1 = MessageEntity(type="bold", offset=len(caption) + 2, length=9)
    entity2 = MessageEntity(type="text_link", offset=len(caption) + 2, length=3, url="https://t.me/+PyuSAyLunZ45NGM1")
    Config.acg_caption_entities = [entity1, entity2]
    caption_entities = Config.acg_caption_entities
    return caption_entities
