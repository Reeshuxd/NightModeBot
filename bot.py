import logging
from os import environ
from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions

logging.basicConfig(level=logging.INFO)

try:
    CHAT_ID = int(environ["CHAT_ID"])
    TOKEN = environ["TOKEN"]
    TIMEZONE = environ["TIMEZONE"]
except Exception as e:
    print("Important Vars are missing\nBot is quitting.....")
    print(f"Error:\n{e}")
    exit(1)

nmbot = Client(
        "NightMode",
        bot_token=TOKEN,
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        )


async def group_close():
    try:
        await nmbot.send_message(
                CHAT_ID,
                "It's 12:00 AM\nGroup is Closing!"
                )
        await nmbot.set_chat_permissions(
                CHAT_ID,
                ChatPermissions()
                )
    except BaseException as e:
        await nmbot.send_message(
                CHAT_ID,
                f"**Error while closing group:** `{e}`"
                )
        logging.error(str(e))

async def group_open():
    try:
        await nmbot.send_message(
                CHAT_ID,
                "It's 6:00 AM\nGroup is opening"
                )
        await nmbot.set_chat_permissions(
                CHAT_ID,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_stickers=True,
                    can_send_animations=True
                    )
                )
    except BaseException as e:
        logging.error(str(e))
        await nmbot.send_message(
                CHAT_ID,
                f"**Error while opening group:**\n`{e}`"
                )


@nmbot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
            "Heya, I am a NightMode Bot\n**(c) [Reeshuxd](https://github.com/Reeshuxd)**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" My Source Code", url="github.com/Reeshuxd/NightModeBot")]
                ]
            )
        )

scheduler = AsyncIOScheduler(timezone=TIMEZONE)
scheduler.add_job(group_close, trigger="cron", hour=11, minute=59)
scheduler.start()

scheduler = AsyncIOScheduler(timezone=TIMEZONE)
scheduler.add_job(group_open, trigger="cron", hour=5, minute=59)
scheduler.start()

print("Successfully Started Bot!")
nmbot.run()
