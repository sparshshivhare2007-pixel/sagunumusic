# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


import asyncio
import importlib
from pyrogram import idle
from pyrogram.types import BotCommand
from pytgcalls.exceptions import NoActiveGroupCall
import config
from ShrutiMusic import LOGGER, app, userbot
from ShrutiMusic.core.call import Nand
from ShrutiMusic.misc import sudo
from ShrutiMusic.plugins import ALL_MODULES
from ShrutiMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# Bot Commands List
# Bot Commands List with Custom Font Style
COMMANDS = [
    BotCommand("start", "🚀 𝐁𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"),
    BotCommand("help", "❓ 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮 𝐀𝐧𝐝 𝐌𝐚𝐧𝐲 𝐌𝐨𝐫𝐞 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬"),
    BotCommand("ping", "📡 𝐏𝐢𝐧𝐠 𝐀𝐧𝐝 𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐬"),
    BotCommand("play", "🎵 𝐒𝐭𝐚𝐫𝐭 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐓𝐡𝐞 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐓𝐫𝐚𝐜𝐤"),
    BotCommand("vplay", "📹 𝐒𝐭𝐚𝐫𝐭 𝐕𝐢𝐝𝐞𝐨 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠"),
    BotCommand("playrtmps", "📺 𝐏𝐥𝐚𝐲 𝐋𝐢𝐯𝐞 𝐕𝐢𝐝𝐞𝐨"),
    BotCommand("playforce", "⚠️ 𝐅𝐨𝐫𝐜𝐞 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨 𝐓𝐫𝐚𝐜𝐤"),
    BotCommand("vplayforce", "⚠️ 𝐅𝐨𝐫𝐜𝐞 𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 𝐓𝐫𝐚𝐜𝐤"),
    BotCommand("pause", "⏸ 𝐏𝐚𝐮𝐬𝐞 𝐓𝐡𝐞 𝐒𝐭𝐫𝐞𝐚𝐦"),
    BotCommand("resume", "▶️ 𝐑𝐞𝐬𝐮𝐦𝐞 𝐓𝐡𝐞 𝐒𝐭𝐫𝐞𝐚𝐦"),
    BotCommand("skip", "⏭ 𝐒𝐤𝐢𝐩 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐓𝐫𝐚𝐜𝐤"),
    BotCommand("end", "🛑 𝐄𝐧𝐝 𝐓𝐡𝐞 𝐒𝐭𝐫𝐞𝐚𝐦"),
    BotCommand("stop", "🛑 𝐒𝐭𝐨𝐩 𝐓𝐡𝐞 𝐒𝐭𝐫𝐞𝐚𝐦"),
    BotCommand("queue", "📄 𝐒𝐡𝐨𝐰 𝐓𝐫𝐚𝐜𝐤 𝐐𝐮𝐞𝐮𝐞"),
    BotCommand("auth", "➕ 𝐀𝐝𝐝 𝐀 𝐔𝐬𝐞𝐫 𝐓𝐨 𝐀𝐮𝐭𝐡 𝐋𝐢𝐬𝐭"),
    BotCommand("unauth", "➖ 𝐑𝐞𝐦𝐨𝐯𝐞 𝐀 𝐔𝐬𝐞𝐫 𝐅𝐫𝐨𝐦 𝐀𝐮𝐭𝐡 𝐋𝐢𝐬𝐭"),
    BotCommand("authusers", "👥 𝐒𝐡𝐨𝐰 𝐋𝐢𝐬𝐭 𝐎𝐟 𝐀𝐮𝐭𝐡 𝐔𝐬𝐞𝐫𝐬"),
    BotCommand("cplay", "📻 𝐂𝐡𝐚𝐧𝐧𝐞ｌ 𝐀𝐮𝐝𝐢𝐨 𝐏𝐥𝐚𝐲"),
    BotCommand("cvplay", "📺 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐕𝐢𝐝𝐞𝐨 𝐏𝐥𝐚𝐲"),
    BotCommand("cplayforce", "🚨 𝐂𝐡𝐚𝐧𝐧𝐞ｌ 𝐅𝐨𝐫𝐜𝐞 𝐀𝐮𝐝𝐢𝐨 𝐏𝐥𝐚𝐲"),
    BotCommand("cvplayforce", "🚨 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐅𝐨𝐫𝐜𝐞 𝐕𝐢𝐝𝐞𝐨 𝐏𝐥𝐚𝐲"),
    BotCommand("channelplay", "🔗 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐆𝐫𝐨𝐮𝐩 𝐓𝐨 𝐂𝐡𝐚𝐧𝐧𝐞𝐥"),
    BotCommand("loop", "🔁 𝐄𝐧𝐚𝐛𝐥𝐞/𝐃𝐢𝐬𝐚𝐛𝐥𝐞 𝐋𝐨𝐨𝐩"),
    BotCommand("stats", "📊 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬"),
    BotCommand("shuffle", "🔀 𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐓𝐡𝐞 𝐐𝐮𝐞𝐮𝐞"),
    BotCommand("seek", "⏩ 𝐒𝐞𝐞𝐤 𝐅𝐨𝐫𝐰𝐚𝐫𝐝"),
    BotCommand("seekback", "⏪ 𝐒𝐞𝐞𝐤 𝐁𝐚𝐜𝐤𝐰𝐚𝐫𝐝"),
    BotCommand("song", "🎶 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐨𝐧𝐠 (𝐌𝐩𝟑/𝐌𝐩𝟒)"),
    BotCommand("speed", "⏩ 𝐀𝐝𝐣𝐮𝐬𝐭 𝐀𝐮𝐝𝐢𝐨 𝐏𝐥𝐚𝐲𝐛𝐚𝐜𝐤 𝐒𝐩𝐞𝐞𝐝 (𝐆𝐫𝐨𝐮𝐩)"),
    BotCommand("cspeed", "⏩ 𝐀𝐝𝐣𝐮𝐬𝐭 𝐀𝐮𝐝𝐢𝐨 𝐒𝐩𝐞𝐞𝐝 (𝐂𝐡𝐚𝐧𝐧𝐞𝐥)"),
    BotCommand("tagall", "📢 𝐓𝐚𝐠 𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞"),
]

async def setup_bot_commands():
    """Setup bot commands during startup"""
    try:
        # Set bot commands
        await app.set_bot_commands(COMMANDS)
        LOGGER("ShrutiMusic").info("Bot commands set successfully!")
        
    except Exception as e:
        LOGGER("ShrutiMusic").error(f"Failed to set bot commands: {str(e)}")

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    
    # Setup bot commands during startup
    await setup_bot_commands()

    for all_module in ALL_MODULES:
        importlib.import_module("ShrutiMusic.plugins" + all_module)

    LOGGER("ShrutiMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Nand.start()

    try:
        await Nand.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ShrutiMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Nand.decorators()

    LOGGER("ShrutiMusic").info(
        "\x53\x68\x72\x75\x74\x69\x20\x4d\x75\x73\x69\x63\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x0a\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x73"
    )

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("ShrutiMusic").info("Stopping Shruti Music Bot...🥺")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
