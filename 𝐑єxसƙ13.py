#!/usr/bin/env python3
# ────────────────────────────────────────────
#   #𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰★𝐑єxस𓆪
# ────────────────────────────────────────────
import hashlib, sys, unicodedata
from telegram import Bot, ChatMemberAdministrator, ChatPermissions, Update

def __boot_lock():
    _EXPECTED = "43046988a1ab381d2522ec8d709324b915174138cd826c24d58801b373d4a918"
    _MARKER   = "\U0001d5d0\u029f\U0001d5e8x\U0001d362"
    try:
        src = __file__
        if src.endswith((".pyc", ".pyo")):
            src = src[:-1]
        with open(src, "r", encoding="utf-8", errors="replace") as _f:
            for _line in _f:
                _s = _line.rstrip("\n")
                if _s.startswith("#") and _MARKER in _s:
                    _got = hashlib.sha256(unicodedata.normalize("NFC", _s).encode()).hexdigest()
                    if _got != _EXPECTED:
                        pass
                    return
        return
    except Exception:
        return

__boot_lock()

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import asyncio, functools, gc, json, logging, os, platform as _plt, random, requests, time, socket, whois
from typing import Dict, List, Optional, Set, Tuple

# Stable GC Tweaks for performance
gc.set_threshold(700, 10, 10)

if _plt.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
else:
    try:
        import uvloop as _uvloop; _uvloop.install()
    except ImportError:
        pass

from telegram.constants import ParseMode
from telegram.error import RetryAfter, TelegramError
from telegram.ext import (
    Application, ChatMemberHandler,
    CommandHandler, ContextTypes, MessageHandler, PrefixHandler, filters,
)

# ══════════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════════
TOKENS: List[str] = [
"9049986490:AAFhjq9ZBWp4UGKEssysGNz4BvVG7TSUHPE",
    "9103055664:AAGc1J1dTqIfPKrsaH1BPUyU9e-LAGDHXyk",
     "9054752815:AAF7TfJVAsRDI9eNf_RLIcjZs-Y0k2x2Tek",
    "9105692666:AAG__kj0uAhGHR8qYFyJoEGqlE6ZzpWOwzQ",
    "9018238064:AAHO5cHNZS9x-F4kfu6e5dGhTk8soH7EmYM",
    "8691008881:AAHe6cLViAvojVUWz1LJWH0aL6_6STE8SUw",
    "9093216253:AAHlGJmK0IqDGvGBtgczEbeUCpRhKvGdbIA",
    "9285374348:AAFFNXmqZBEBc6ugo_wdAEAy4rIfIM7QrZU",
    "9290806869:AAH90BdzK2aZue-z2Qb5LTCqVPAYHX6vaWM",
    "9174400159:AAG7kFUC6JGwdOEAK61k893H3mIFHdbsNus",]

OWNERS:     frozenset = frozenset({7851807910})
SUDO_PATH:  str       = "v13_sudo.json"
NEXUS_PATH: str       = "v13_nc_bots.json"

FLEET_USERNAMES: List[str] = [f"uD_Error{i}_Bot" for i in range(100, 110)]

# Compressed Speed Settings
_Λ_PULSE: float = 0.01 
_Θ_HOUND: float = 60.0

_ξ_GLYPH = "nc"
_ν_GLYPH = "spam"
_μ_GLYPH = "swipe"

_Δ_delay: List[float] = [0.0]
_Φ_mpfp: List[Optional[str]] = [None]

# ══════════════════════════════════════════════════════════
#  EMOJI / TEXT POOLS
# ══════════════════════════════════════════════════════════
_P_NC: List[str] = [
"😀᭄","😃᭄","😄᭄","😁᭄","😆᭄","😅᭄","😂᭄","🤣᭄","😊᭄",
"😇᭄","🙂᭄","🙃᭄","😉᭄","😌᭄","😍᭄","🥰᭄","😘᭄","😗᭄",
"😙᭄","😚᭄","😋᭄","😛᭄","😝᭄","😜᭄","🤪᭄","🤨᭄","🧐᭄",
"🤓᭄","😎᭄","🥸᭄","🤩᭄","🥳᭄","😏᭄","😒᭄","😞᭄","😔᭄",
"😟᭄","😕᭄","🙁᭄","☹️᭄","😣᭄","😖᭄","😫᭄","😩᭄","🥺᭄",
"😢᭄","😭᭄","😤᭄","😠᭄","😡᭄","🤬᭄","🤯᭄","😳᭄","🥵᭄",
"🥶᭄","😱᭄","😨᭄","😰᭄","😥᭄","😓᭄","🤗᭄","🤔᭄","🫢᭄",
"🤭᭄","🤫᭄","🤥᭄","😶᭄","😐᭄","😑᭄","😬᭄","🫠᭄","🙄᭄",
"😯᭄","😦᭄","😧᭄","😮᭄","😲᭄","🥱᭄","😴᭄","🤤᭄","😪᭄"
]

_P_NCCHUD: List[str] = [
"━━━𝙏𝙀𝙍𝘼 𝘽𝘼𝙋 ★𝐑єxस₊˚.⋆🐶࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙍𝘼𝙉𝘿𝙄₊˚.⋆🐱࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼₊˚.⋆🦁࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙍𝘼𝙉𝘿𝙄 𝘽𝘼𝘾𝙃𝙄₊˚.⋆🐯࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝙄 𝙆𝘼𝙇𝙄 𝘾𝙃𝙐𝙏 𝙈𝙀 𝙇𝙐𝙉𝘿₊˚.⋆🐵࿐𓂃𓈒",
"━━━★𝐑єxस 𝘽𝙃𝘼𝙂𝙒𝘼𝘼𝙉 𝘼𝙔𝘼 𝙃𝘼𝙄 𝙏𝙀𝙍𝙄 𝙈𝘼 𝘾𝙃𝙊𝘿𝙉𝙀₊˚.⋆🐸࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝙊 𝙅𝙊𝙃𝙃𝙉𝙔 𝘽𝙃𝙄 𝘾𝙃𝙊𝘿 𝘿𝙀𝙂𝘼₊˚.⋆🐼࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙇𝘼𝙉𝙂𝘿𝙄₊˚.⋆🐨࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙀 𝙈𝙊𝙈 𝙆𝙀 𝘽𝙃𝙊𝙎𝘿𝙀 𝙋𝙀 𝙇𝘼𝘼𝙏 𝙈𝘼𝙍𝙐₊˚.⋆🐮࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙀 𝘽𝙐𝘼 𝙆𝙄 𝙂𝘼ɴ𝘿 𝙈𝙀 𝙇𝘼𝘼𝙏 𝙈𝘼𝙍𝙐₊˚.⋆🐷࿐𓂃𓈒",
"━━━𝙄𝘿𝙃𝙀𝙍 𝘼𝘼 𝙋𝙄𝙇𝙇𝙀 𝙏𝙀𝙍𝙄 𝘽𝙀𝙃𝙉 𝘾𝙃𝙊𝘿𝙐₊˚.⋆🐔࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝘼 𝙈𝙄𝘼 𝙆𝙃𝘼𝙇𝙄𝙁𝘼 𝙆𝙄 𝘼𝙐𝙇𝘼𝘿𝘿₊˚.⋆🦊࿐𓂃𓈒",
"━━━𝘽𝙀𝙃𝙉 𝘾𝙃𝙊𝘿 𝙏𝙀𝙍𝘼 𝘽𝘼𝙋₊˚.⋆🐺࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙀 𝘽BA𝙋 𝙆𝙀 𝙇𝙐𝙉𝘿 𝙋𝙀𝙍 𝙏𝙀𝙍𝙄 𝙈𝘼₊˚.⋆🐗࿐𓂃𓈒",
"━━━𝙏𝙐 𝘽𝘼𝙎 𝙁𝘼𝙏𝙏𝙀 𝘾𝙊𝙉𝘿𝙊𝙈 𝙆𝘼 𝙉𝘼𝙏𝙄𝙅𝘼 𝙃𝘼𝙄 𝙋𝙄𝙇𝙇𝙀₊˚.⋆🐴࿐𓂃𓈒",
"━━━𝙅𝘼𝙔𝘼𝘿𝘼 𝘽𝘼𝘼𝙆 𝘽𝘼𝘼𝙆 𝙈𝘼𝙏 𝙆𝙍 𝙒𝙍𝙉𝘼 𝙄𝘿𝙃𝙀𝙍 𝙃𝙄 𝘾𝙃𝙊𝘿 𝘿𝙐𝙉𝙂𝘼₊˚.⋆🦄࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝙄 𝙈𝙊𝙈 𝙆𝙄 𝘾ＨＵＴ 𝙈𝙀 𝙐𝙉𝙂𝙇𝙄 𝙂ＨＵＳＡ𝙐₊˚.⋆🐝࿐𓂃𓈒",
"━━━𝙏𝙀𝙍𝘼 𝘽BA𝙋 𝙍ＮＤＹ 𝘽𝘼ＣＨＡ₊˚.⋆🦋࿐𓂃𓈒",
"━━━𝙏𝙀𝙍Ｉ 𝙈Ａ 𝙆Ｉ ＣＨＵＴ 𝙈Ｅ 𝘼𝙐𝙏𝙊𝙈𝘼 𝙒ＯＲ𝙆𝙁𝙇Ｏ𝙒₊˚.⋆🐢࿐𓂃𓈒",
"━━━𝙏𝙀𝙍Ｉ 𝙈Ａ 𝙆Ｏ 𝙕𝙐Ｃ𝙆 𝘾ＨＯＤＥＧＡ₊˚.⋆🦎࿐𓂃𓈒",
"━━━𝙏𝙀𝙍Ｉ 𝙈𝙐𝙈𝙈Ｙ 𝙆Ｉ ＣＨＵＴ 𝙈Ｅ 𝙆ＥＬＬＡ 𝙈𝘼Ｒ𝙐₊˚.⋆🦀࿐𓂃𓈒"
]

_P_NC_UD_ERROR: List[str] = [
    "🩷","❤️","🧡","💛","💚","🩵","💙","💜","🖤","🩶","🤎","🤍",
]

_P_SEXUAL: List[str] = [
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕐",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕑",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕒",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕓",
     "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕔",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕕",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕖",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕗",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕘",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕙",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕚",
    "━━━━(𝐓ꫀʀꫝ 𝐁ꪖᴘ ★𝐑єxस)━━━━ 🕛",
]

_P_SWIPE_ULTRA: List[str] = [
    "𝟏. 𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 {name} 𝐀𝐘𝐀 𝐇𝐀𝐈 𝐒𝐔𝐍 𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄! 🔥",
    "𝟐. 𝐀𝐁𝐄 {name} 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐁𝐇𝐀𝐆 𝐌𝐀𝐓 𝐆𝐀𝐍𝐃 𝐅𝐀𝐀𝐃 𝐃𝐔𝐍𝐆𝐀! 💀",
    "𝟑. {name} 𝐓𝐄𝐑𝐄 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐋𝐀𝐀𝐓 𝐌𝐀𝐑𝐔 𝐑𝐀𝐍𝐃𝐈 𝐊𝐄? 🤡",
    "𝟒. 𝐒𝐔𝐍 {name} 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐍 𝐊𝐀 𝐑𝐄𝐘𝐏 𝐊𝐀𝐑 𝐃𝐔𝐍𝐆𝐀 𝐁𝐇𝐀𝐆 𝐌𝐀𝐓! 👺",
    "𝟓. 𝐎𝐘𝐄 {name} 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐁𝐄𝐂𝐇 𝐃𝐈𝐘𝐀 𝐊𝐘𝐀? 💸",
    "𝟔. {name} 𝐓𝐄𝐑𝐄 𝐊𝐇𝐀𝐀𝐍𝐃𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐏𝐈𝐋𝐋𝐄! 🐒",
    "𝟕. 𝐒𝐔𝐍 {name} 𝐓𝐄𝐑𝐄 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐈𝐍𝐊 𝐂𝐇𝐔𝐓 𝐌𝐀𝐑𝐔 𝐒𝐀𝐀𝐋𝐄! 👅",
    "𝟖. {name} 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐎𝐘𝐎 𝐌𝐀𝐈 𝐋𝐄 𝐉𝐀 𝐊𝐀𝐑 𝐏𝐄𝐋𝐔 𝐊𝐘𝐀? 🏨",
    "𝟗. 𝐁𝐄𝐇𝐍 𝐂𝐇𝐎𝐃 {name} 𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 ★𝐔ᴅ_𝐄ʀʀᴏ𝐑 𝐇𝐔 𝐌𝐀𝐈! 👑",
    "𝟏𝟎. {name} 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐏𝐇𝐀𝐀𝐑 𝐃𝐔𝐍𝐆𝐀 𝐀𝐀𝐉! 🧨"
]

SLIDE1_MESSAGES = [
    "𝐓ᴍᴋʙ 𝐑ɴᴅʏ ᴋᴇ 𝐋ᴀᴅᴋᴇ 😈🖕🏻😈🖕🏻😈",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴍᴀʀ ɢʏɪ ¿😆😆😆",
    "𝐀ᴀʀ ꜱᴀᴍᴀɴᴅᴀʀ ᴘᴀᴀʀ ꜱᴀᴍᴀɴᴅᴀʀ ʙᴇᴇᴄʜ ᴍɪᴇ ʜᴀɪ ɴᴀɪʏᴀ ᴘʜʟᴇ ᴛᴇʀɪ ʙʜᴇɴ चोदू ʙᴀᴀᴅ ᴍɪᴇ चोदू ᴍᴀɪʏᴀ ¡! 🥰🖕🏻🥰🖕🏻🥰🖕🏻",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ʜᴜᴍᴇꜱʜᴀ ᴍᴜᴊʜꜱᴇ ʜɪ ᴋʏᴜ चुडती है ¡! 😡🤬😡🤬😡",
    "𝐃ᴇᴋʜ ᴀᴀᴊ ᴛᴇʀɪ 𝐌ᴀᴀ ᴋᴀ ɴᴀɴɢᴀ ᴅᴀɴᴄᴇ ᴅɪᴋʜᴀᴜ ! 🩰🧑🏻‍🩰",
]

SLIDE2_MESSAGES = [
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐆ᴜʟᴀʙɪ 𝐂ʜᴜᴛ ᴍɪᴇ 𝐌ᴜᴛ ᴋʀ ʙʜᴀɢ ᴊᴀᴜɢᴀ 𝐁ꜱᴅᴋ ! 😆",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴄʜᴏᴅɴᴇ ᴀʀʜᴀ ʜᴜ ʀᴜᴋ ᴡʜɪ ɢᴜﻠᴀᴍ ! 😾",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋᴇ ʙᴏᴏʙɪᴇꜱ ᴋᴇ ʙᴇᴇᴄʜ ᴍɪᴇ ʟɴᴅ ꜰᴀꜱᴀ ᴋʀ ᴍᴜᴛʜ ᴍᴀᴀʀ ᴅᴜɢᴀ ʙꜱᴅᴋ 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍɪᴇ ᴍᴀɢɢɪᴇ ʙɴᴀ ᴋʀ ᴍᴜᴛʜ ʙʜᴀʀ ᴅᴜɢᴀ ! 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ʙʜᴛ ʀᴏᴛɪ ᴇʏ ʙɪʟᴋᴜʟ 𝐓ᴇʀɪ ᴛʀʜ ᴅᴏɴᴏ ʀɴᴅ¥ ʀᴏɴᴀ ᴋʀᴛᴇ ʜᴏ ᴇᴡᴡ ! 😆",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋɪ ɢᴜʟᴀʙɪ ᴄʜᴛ ᴋᴀᴀᴛ ᴅᴜɢᴀ ɢᴜʟᴀᴍ ! 😆",
    "𝐂ʜʟ ɢᴜʟᴀᴍ ɢᴜʟᴀᴍɪ ᴋʀ ! 😾",
]

SLIDE3_PATTERN = "{text} જ⁀➴🍃જ⁀➴😆જ⁀➴❤️"

# ══════════════════════════════════════════════════════════
#  TITLE CACHE
# ══════════════════════════════════════════════════════════
_ρ_hive: Dict[str, str] = {}
_ρ_CAP  = 512

def _τ_forge(raw: str, cap: int = 255) -> str:
    hit = _ρ_hive.get(raw)
    if hit is not None:
        return hit
    s = raw
    while len(s.encode("utf-16-le")) // 2 > cap:
        s = s[:-1]
    s = s.rstrip()
    if len(_ρ_hive) >= _ρ_CAP:
        for k in list(_ρ_hive)[:64]:
            del _ρ_hive[k]
    _ρ_hive[raw] = s
    return s

# ══════════════════════════════════════════════════════════
#  VAULT
# ══════════════════════════════════════════════════════════
class _Vault:
    __slots__ = (
        "sentinels", "_nc_live", "_spam_live",
        "_mark_ids", "_mark_names",
        "_flood_chats", "_fronts", "_ops", "_auto_slide_data"
    )

    def __init__(self):
        self.sentinels:    Set[int]                        = set(OWNERS)
        self._nc_live:     Dict[int, bool]                 = {}
        self._spam_live:   Dict[int, bool]                 = {}
        self._mark_ids:    Set[int]                        = set()
        self._mark_names:  Dict[int, str]                  = {}
        self._flood_chats: Set[int]                        = set()
        self._fronts:      Set[int]                        = set()
        self._ops:         Dict[tuple, List[asyncio.Task]] = {}
        self._auto_slide_data: Dict[int, dict]             = {}
        self._load_sudo()

    def _load_sudo(self):
        try:
            if os.path.exists(SUDO_PATH):
                with open(SUDO_PATH) as f:
                    self.sentinels = set(json.load(f))
            self.sentinels.update(OWNERS)
        except Exception:
            self.sentinels = set(OWNERS)

    def _persist(self):
        try:
            with open(SUDO_PATH, "w") as f:
                json.dump(list(self.sentinels), f)
        except Exception:
            pass

    def _is_sentinel(self, uid: int) -> bool:
        return uid in self.sentinels

    def _enqueue(self, cid: int, slot: str, task: asyncio.Task):
        key = (cid, slot)
        lst = self._ops.get(key)
        if lst is None: self._ops[key] = [task]
        else:           lst.append(task)

    def _sweep(self):
        for key in list(self._ops):
            alive = [t for t in self._ops[key] if not t.done()]
            if alive: self._ops[key] = alive
            else:     del self._ops[key]

    def _abort(self, cid: int, slot: str):
        for t in self._ops.pop((cid, slot), []):
            t.cancel()

    def _abort_all(self):
        for key in list(self._ops):
            for t in self._ops.pop(key, []):
                t.cancel()

    def _tally(self) -> int:
        return sum(1 for v in self._ops.values() for t in v if not t.done())

    def _kill_nc(self, cid: int):    self._nc_live[cid]   = False
    def _kill_spam(self, cid: int):  self._spam_live[cid] = False
    def _kill_swipe(self, cid: int): self._flood_chats.discard(cid)

    def _kill_all(self, cid: int):
        self._kill_nc(cid); self._kill_spam(cid); self._kill_swipe(cid)

_χ = _Vault()

# ══════════════════════════════════════════════════════════
#  HELPER UTILS
# ══════════════════════════════════════════════════════════
def safe_task(coro):
    async def _wrapped():
        try:
            await coro
        except Exception as e:
            logging.error(f"Background task failure: {e}")
    return asyncio.create_task(_wrapped())

# ══════════════════════════════════════════════════════════
#  BOT POOLS & PRESENCE
# ══════════════════════════════════════════════════════════
_ω_apps:        List[Application]      = []
_ω_fleet:       List[Bot]              = []
_ω_annexe:      List[Bot]              = []
_ω_ann_tk:      List[str]              = []
_ω_nc_ledger:   Dict[int, tuple]       = {}
_ω_ghost_ids:   Set[int]               = set()
_chup_silenced: Set[Tuple[int, int]]   = set()
_ω_ud_enhanced: Set[int]               = set()

# PRESENCE TRACKER FOR DYNAMIC LEADER ELECTION
_ω_chat_presence: Dict[int, Set[int]]  = {}

# ══════════════════════════════════════════════════════════
#  LEADER SYSTEM (DYNAMIC ELECTIVE SYSTEM)
# ══════════════════════════════════════════════════════════
_ω_leader_id: Optional[int] = None   

def _σ_set_leader(bot_id: int):
    global _ω_leader_id
    _ω_leader_id = bot_id

def _σ_is_leader(bot_id: int) -> bool:
    global _ω_leader_id
    active_fleet_ids = [b.id for b in _ω_fleet if b.id]
    if not active_fleet_ids:
        return False
    if _ω_leader_id not in active_fleet_ids:
        _ω_leader_id = active_fleet_ids[0]
    return bot_id == _ω_leader_id

def _σ_mark_presence(chat_id: int, bot_id: int):
    if chat_id not in _ω_chat_presence:
        _ω_chat_presence[chat_id] = set()
    _ω_chat_presence[chat_id].add(bot_id)

def _σ_is_chat_leader(bot_id: int, chat_id: int) -> bool:
    if not chat_id:
        return _σ_is_leader(bot_id)
        
    _σ_mark_presence(chat_id, bot_id)
    
    if _σ_is_leader(bot_id):
        return True
        
    active_bots = _ω_chat_presence.get(chat_id, set())
    global_leader = _ω_leader_id
    
    if global_leader and global_leader in active_bots:
        return False
        
    if active_bots:
        local_leader = sorted(list(active_bots))[0]
        return bot_id == local_leader
        
    return False

def _σ_sync_ids():
    global _ω_ghost_ids
    _ω_ghost_ids = {b.id for b in _ω_fleet + _ω_annexe if b.id}

def _σ_ghost() -> Set[int]: return _ω_ghost_ids

def _σ_battalion() -> List[Bot]:
    combined = _ω_annexe + _ω_fleet
    return combined if combined else []

def _σ_fronts(primary: int) -> List[int]:
    out, seen = [primary], {primary}
    for cid in _χ._fronts:
        if cid not in seen:
            seen.add(cid); out.append(cid)
    return out

# ══════════════════════════════════════════════════════════
#  LIVE HACKING TYPE ANIMATION HELPER
# ══════════════════════════════════════════════════════════
async def _live_hacking_animation(msg):
    stages = [
        "🤖 ELECTING SECURE FLEET LEADER...",
        "⚡ BYPASSING GATEWAY HANDSHAKES...",
        "🔥 ACCELERATING CORES ENGINE MATRIX...",
        "🎛️ SYSTEM POWER THREADS STABILIZED [100%]"
    ]
    for stage in stages:
        try:
            await msg.edit_text(f"<code>[RUNNING] {stage}</code>", parse_mode=ParseMode.HTML)
            await asyncio.sleep(0.15)
        except Exception:
            break

# ══════════════════════════════════════════════════════════
#  PERSISTENCE
# ══════════════════════════════════════════════════════════
def _π_pull() -> List[str]:
    try:
        if os.path.exists(NEXUS_PATH):
            with open(NEXUS_PATH) as f:
                return json.load(f)
    except Exception:
        pass
    return []

def _π_push():
    try:
        with open(NEXUS_PATH, "w") as f:
            json.dump(_ω_ann_tk, f)
    except Exception:
        pass

async def _π_boot_annexe(tok: str) -> Optional[Bot]:
    try:
        from telegram.request import HTTPXRequest as _R
        b = Bot(token=tok, request=_R(
            connection_pool_size=1024, read_timeout=40.0,
            write_timeout=40.0, connect_timeout=15.0, pool_timeout=20.0,
        ))
        me = await b.get_me()
        print(f"  annexe: @{me.username}")
        return b
    except Exception as e:
        print(f"  annexe fail: {e}")
        return None

# ══════════════════════════════════════════════════════════
#  DECORATORS (ABSOLUTE MAXIMUM FLOOD SUPPRESSION)
# ══════════════════════════════════════════════════════════
_DENIED = "𝘼𝙪𝙠𝙖𝙩 𝙗𝙖𝙣𝙖 𝙧𝙖𝙣𝙙𝙞 𝙠𝙚 𝙗𝙖𝙘𝙘𝙝𝙚 𝐑єxस 𝙨𝙖𝙮 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙡𝙚 𝙩𝙪 𝙣𝙚🎀🎀"

def _gate(fn):
    @functools.wraps(fn)
    async def _w(u: Update, c: ContextTypes.DEFAULT_TYPE):
        chat_id = u.effective_chat.id if u.effective_chat else 0
        if not chat_id or not _σ_is_chat_leader(c.bot.id, chat_id):
            return
            
        if not u.effective_user or not _χ._is_sentinel(u.effective_user.id):
            try: await u.message.reply_text(_DENIED)
            except Exception: pass
            return
        try:
            return await fn(u, c)
        except RetryAfter as e:
            logging.warning(f"Flood limit suppression active. Halting execution for {e.retry_after}s")
            await asyncio.sleep(e.retry_after + random.uniform(0.2, 0.7))
            try:
                return await fn(u, c)
            except Exception: pass
        except Exception as e:
            logging.error(f"Suppressed unhandled exception: {e}")
            pass
    return _w

def _crown(fn):
    @functools.wraps(fn)
    async def _w(u: Update, c: ContextTypes.DEFAULT_TYPE):
        chat_id = u.effective_chat.id if u.effective_chat else 0
        if not chat_id or not _σ_is_chat_leader(c.bot.id, chat_id):
            return
            
        if not u.effective_user or u.effective_user.id not in OWNERS:
            try: await u.message.reply_text(_DENIED)
            except Exception: pass
            return
        try:
            return await fn(u, c)
        except RetryAfter as e:
            await asyncio.sleep(e.retry_after + random.uniform(0.2, 0.7))
            try: return await fn(u, c)
            except Exception: pass
        except Exception: pass
    return _w

# ══════════════════════════════════════════════════════════
#  UTILS
# ══════════════════════════════════════════════════════════
def _υ_strip(msg) -> str:
    txt = msg.text or msg.caption or ""
    raw = ""
    if msg.entities:
        for e in msg.entities:
            if e.type == "bot_command" and e.offset == 0:
                after = txt[e.offset + e.length:]
                raw   = after[1:] if after.startswith(" ") else after
                break
    if not raw:
        p = txt.split(None, 1)
        raw = p[1] if len(p) > 1 else ""
    return " ".join(raw.splitlines())

# ══════════════════════════════════════════════════════════
#  NC ENGINE — QUEUE-RELAY
# ══════════════════════════════════════════════════════════
_ι_lockout: Dict[int, float] = {}

def _ι_jambed(bid: int) -> bool:
    exp = _ι_lockout.get(bid, 0.0)
    return exp > 0.0 and time.monotonic() < exp

def _ι_jam(bid: int, secs: float):
    _ι_lockout[bid] = time.monotonic() + secs

def _ι_unjam(bid: int):
    _ι_lockout.pop(bid, None)

async def _ι_worker(bot: Bot, cid: int, flag: dict, q: "asyncio.Queue[str]"):
    while flag.get(cid):
        try:
            title = await asyncio.wait_for(q.get(), timeout=0.5)
        except (asyncio.TimeoutError, asyncio.CancelledError):
            return

        try:
            await bot.set_chat_title(cid, title)
            q.task_done()
            if _Δ_delay[0] > 0:
                await asyncio.sleep(_Δ_delay[0])
        except RetryAfter as e:
            _ι_jam(bot.id, float(e.retry_after) + 1.0)
            await asyncio.sleep(e.retry_after + random.uniform(0.1, 0.5))
            q.task_done()
        except TelegramError as e:
            err = str(e).lower()
            if any(x in err for x in ("bad request", "chat not found", "not enough rights")):
                _ι_jam(bot.id, 60.0) 
            q.task_done()
        except Exception:
            q.task_done()

async def _ι_feeder(cid: int, flag: dict, titles: list, q: "asyncio.Queue[str]"):
    n          = len(titles)
    idx        = 0
    pool_depth = max(len(_σ_battalion()), 1) + 2
    while flag.get(cid):
        try:
            if q.qsize() < pool_depth:
                await q.put(_τ_forge(titles[idx % n]))
                idx += 1
            else:
                await asyncio.sleep(0.001)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(0.001)

async def _ι_mode_relay(cid: int, flag: dict, titles: list):
    pool = _σ_battalion()
    if not pool: return
    q    = asyncio.Queue(maxsize=max(len(pool) * 2, 8))
    subs = [safe_task(_ι_feeder(cid, flag, titles, q))]
    for bot in pool:
        t = safe_task(_ι_worker(bot, cid, flag, q))
        _χ._enqueue(cid, _ξ_GLYPH, t)
        subs.append(t)
    try:
        while flag.get(cid):
            await asyncio.sleep(_Λ_PULSE)
    except asyncio.CancelledError:
        pass
    for t in subs:
        if not t.done(): t.cancel()
    while not q.empty():
        try: q.get_nowait(); q.task_done()
        except Exception: break

async def _ι_overseer(primary: int, titles: list, flag: dict):
    targets  = _σ_fronts(primary)
    runners: Dict[int, asyncio.Task] = {}
    for cid in targets:
        t = safe_task(_ι_mode_relay(cid, flag, titles))
        _χ._enqueue(cid, _ξ_GLYPH, t)
        runners[cid] = t
    try:
        while flag.get(primary):
            await asyncio.sleep(_Λ_PULSE)
            for cid in list(runners):
                if not flag.get(cid):
                    if not runners[cid].done(): runners[cid].cancel()
                    del runners[cid]; continue
                if runners[cid].done():
                    nt = safe_task(_ι_mode_relay(cid, flag, titles))
                    _χ._enqueue(cid, _ξ_GLYPH, nt)
                    runners[cid] = nt
    except asyncio.CancelledError:
        pass

def _ι_ignite(primary: int, titles: list, flag: dict):
    _ω_nc_ledger[primary] = (titles, flag)
    sup = safe_task(_ι_overseer(primary, titles, flag))
    _χ._enqueue(primary, _ξ_GLYPH, sup)

# ══════════════════════════════════════════════════════════
#  MENUS (CLEAN MENU VS ISOLATED HACK CONSOLE)
# ══════════════════════════════════════════════════════════
MENU_TEXT = """\
<b>[ 🔘 ★𝐑єxस </b>

<b> [ ⚔️ ATTACK ] </b>
┣ <code>.n1</code> | <code>.n2</code> | <code>.n3</code> | <code>.n4</code>
┣ <code>.rr1</code> | <code>.rr2</code> | <code>.rr3</code> | <code>.uswipe</code>
┗ <code>.spam</code> | <code>.raidadd</code> | <code>.raidlist</code>

<b> [ 🛡️ STOP ] </b>
┣ <code>.stopnc</code> | <code>.stoprr</code> | <code>.swipestop</code>
┗ <code>.spamstop</code> | <code>.stopall</code> | <code>.raidclear</code>

<b> [ ⚙️ SYSTEM & AUTH ] </b>
┣ <code>.auth</code> | <code>.unauth</code> | <code>.authlist</code> | <code>.id</code>
┣ <code>.addbot</code> | <code>.listbot</code> | <code>.delbot</code> | <code>.leader</code>
┗ <code>.start</code> | <code>.panel</code> | <code>.ping</code> | <code>.status</code> | <code>.speed</code>

<b> [ 👤 UTILS & PROFILE ] </b>
┣ <code>.mute</code> | <code>.unmute</code> | <code>.muteall</code> | <code>.unmuteall</code>
┣ <code>.addpfp</code> | <code>.pfp</code> | <code>.spfp</code> | <code>.menupfp</code> | <code>.delmenupfp</code>
┗ <code>.clone</code> | <code>.leavegc</code> | <code>.weather</code> | <code>.time</code>

<b> [ 💻 CONSOLE MODULES ] </b>
┣ <code>.hack</code> | <code>.bypass</code> | <code>.squeeze</code> | <code>.uD_Error</code>
┗ <code>.wipe</code> | <code>.wakeup</code> | <code>.over</code>
"""

PANEL_TEXT = """\
<b>[ 🔘 ★★𝐑єxस </b>

<b> [ 💻 EXPLOIT CORE MODULES ] </b>
┣ <code>.hack</code>    - Live DNS & OSINT Mainframe Parse
┣ <code>.inject</code>  - Memory Allocation Payload
┗ <code>.bypass</code>  - HaveIBeenPwned Core Auditor

<b> [ 📡 ADVANCED CYBER VECTORS ] </b>
┣ <code>.dox</code>     - Triangulate Geolocation Trace
┣ <code>.flood</code>   - Network Buffer Overflow
┗ <code>.root</code>    - Elevate Interactive UID=0

<b> [ ⚡ EXTRAS & RECON ] </b>
┣ <code>.scan</code>    - Vulnerability Port Audit
┣ <code>.breach</code>  - Decrypt SQL Database Tables
┣ <code>.wipe</code>    - Clear Logs & Purge Recent Messages
┣ <code>.wakeup</code>  - Fleet Bot Status Diagnostic
┣ <code>.squeeze</code> - Lock Chat & Restrict Name Changes
┗ <code>.ransom</code>  - Simulated Key Crypto-Lock

<b> [ ⚠️ NOTICE ] </b>
<i>Console interface running under sandbox emulation mode.</i>
"""

async def _send_menu_split(bot: Bot, chat_id: int, is_panel: bool = False):
    fid = _Φ_mpfp[0]
    text = PANEL_TEXT if is_panel else MENU_TEXT
    try:
        if fid:
            await bot.send_photo(chat_id, photo=fid, caption=text, parse_mode=ParseMode.HTML)
        else:
            await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)
    except RetryAfter as e:
        await asyncio.sleep(e.retry_after + random.uniform(0.1, 0.5))
        try: await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)
        except Exception: pass
    except Exception:
        try: await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)
        except Exception: pass

@_gate
async def _cmd_start(u: Update, c: ContextTypes.DEFAULT_TYPE):
    await u.message.reply_text("— 🇺🇩_🇪ref𝙧of 𝐓🇪ref🇮 V3 ❤️‍🔥 —\n\n★🇺🇩_🇪ref𝙧ofwrapper ENTERS THE CHAT 💲")
    await _send_menu_split(c.bot, u.effective_chat.id, is_panel=False)

@_gate
async def _cmd_menu(u: Update, c: ContextTypes.DEFAULT_TYPE):
    await _send_menu_split(c.bot, u.effective_chat.id, is_panel=False)

@_gate
async def _cmd_panel(u: Update, c: ContextTypes.DEFAULT_TYPE):
    await _send_menu_split(c.bot, u.effective_chat.id, is_panel=True)

@_gate
async def _cmd_menupfp(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = u.message
    if not msg.reply_to_message or not msg.reply_to_message.photo:
        _Φ_mpfp[0] = None
        return await msg.reply_text("🗑 Menu photo cleared.")
    _Φ_mpfp[0] = msg.reply_to_message.photo[-1].file_id
    await msg.reply_text("✅ Menu photo saved! <code>.panel</code> will now send it as thumbnail.", parse_mode=ParseMode.HTML)

@_gate
async def _cmd_delmenupfp(u: Update, c: ContextTypes.DEFAULT_TYPE):
    _Φ_mpfp[0] = None
    await u.message.reply_text("🗑️ <b>Menu Photo Removed Successfully!</b>\nAll interactive menus will now operate in ultra-speed text mode.", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  NC HANDLERS
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_nc(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    name = _υ_strip(u.message).strip()
    if not name: return await u.message.reply_text("❗ Usage: <code>.n1 &lt;name&gt;</code>", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)
    
    tgts = _σ_fronts(cid); pool = _σ_battalion()
    titles = [f"{name}{s}" for s in _P_NC]
    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)
    for t in tgts: _χ._nc_live[t] = True
    await msg.edit_text(
        f"✅ <b>NC SMOOTH ACTIVATED</b> | <code>{len(pool)}</code> bots × <code>{len(tgts)}</code> GC",
        parse_mode=ParseMode.HTML)
    _ι_ignite(cid, titles, _χ._nc_live)

@_gate
async def _cmd_ncchud(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    name = _υ_strip(u.message).strip()
    if not name: return await u.message.reply_text("❗ Usage: <code>.n2 &lt;name&gt;</code>", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)
    
    tgts = _σ_fronts(cid); pool = _σ_battalion()
    titles = [f"{name}{s}" for s in _P_NCCHUD]
    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)
    for t in tgts: _χ._nc_live[t] = True
    await msg.edit_text(
        f"⚡ <b>NC FAST ACTIVATED</b> | <code>{len(pool)}</code> bots × <code>{len(tgts)}</code> GC",
        parse_mode=ParseMode.HTML)
    _ι_ignite(cid, titles, _χ._nc_live)

@_gate
async def _cmd_ncLEVI(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    name = _υ_strip(u.message).strip()
    if not name: return await u.message.reply_text("❗ Usage: <code>.n3 &lt;name&gt;</code>", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)
    
    tgts = _σ_fronts(cid); pool = _σ_battalion()
    titles = [f"{name}{s}" for s in _P_NC_UD_ERROR]
    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)
    for t in tgts: _χ._nc_live[t] = True
    await msg.edit_text(
        f"💖 <b>NC BOT SYNC ACTIVATED</b> | <code>{len(pool)}</code> bots × <code>{len(tgts)}</code> GC",
        parse_mode=ParseMode.HTML)
    _ι_ignite(cid, titles, _χ._nc_live)

@_gate
async def _cmd_sexual(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    name = _υ_strip(u.message).strip()
    if not name: return await u.message.reply_text("❗ Usage: <code>.n4 &lt;name&gt;</code>", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)
    
    tgts = _σ_fronts(cid); pool = _σ_battalion()
    titles = [f"{name} {s}" for s in _P_SEXUAL]
    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)
    for t in tgts: _χ._nc_live[t] = True
    await msg.edit_text(
        f"🔥 <b>NC ULTRA FAST ACTIVATED</b> | <code>{len(pool)}</code> bots × <code>{len(tgts)}</code> GC",
        parse_mode=ParseMode.HTML)
    _ι_ignite(cid, titles, _χ._nc_live)

@_gate
async def _cmd_ruk(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    tgts = _σ_fronts(cid)
    live = sum(1 for t in tgts if _χ._nc_live.get(t))
    for t in tgts:
        _χ._kill_nc(t); _ω_nc_ledger.pop(t, None)
        _χ._abort(t, _ξ_GLYPH); _χ._abort(t, _μ_GLYPH)
        _χ._flood_chats.discard(t)
    await u.message.reply_text(
        f"🛑 <b>STOPPED</b> — <code>{live}</code>/<code>{len(tgts)}</code> GC(s)",
        parse_mode=ParseMode.HTML)

@_gate
async def _cmd_delay(u: Update, c: ContextTypes.DEFAULT_TYPE):
    raw = _υ_strip(u.message).strip().lower()
    if not raw:
        ms = round(_Δ_delay[0] * 1000, 2)
        return await u.message.reply_text(
            f"⏱ Current delay: <code>{ms} ms</code>\n"
            f"Usage: <code>.speed 0</code> · <code>.speed 200ms</code> · <code>.speed 0.5</code> · <code>.speed 1s</code>",
            parse_mode=ParseMode.HTML)
    try:
        if raw.endswith("ms"):
            val = float(raw[:-2]) / 1000.0
        elif raw.endswith("s"):
            val = float(raw[:-1])
        else:
            val = float(raw)
        if val < 0: raise ValueError
        _Δ_delay[0] = val
        ms   = round(val * 1000, 2)
        info = "🚀 MAX SPEED" if val == 0 else f"<code>{ms} ms</code>"
        await u.message.reply_text(
            f"⚡ <b>Relay delay</b> → {info}", parse_mode=ParseMode.HTML)
    except (ValueError, IndexError):
        await u.message.reply_text(
            "❗ Bad format. Try: <code>.speed 0</code> <code>.speed 200ms</code> <code>.speed 0.5</code>",
            parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  P Swipe
# ══════════════════════════════════════════════════════════
async def _ultra_swipe_task(bot: Bot, cid: int, target_name: str, bot_index: int):
    idx = bot_index 
    while cid in _χ._flood_chats:
        try:
            raw_text = _P_SWIPE_ULTRA[idx % len(_P_SWIPE_ULTRA)]
            formatted_text = raw_text.format(name=target_name)
            await bot.send_message(cid, formatted_text)
            idx += 1 
            await asyncio.sleep(0.001)
        except asyncio.CancelledError:
            return
        except RetryAfter as e:
            await asyncio.sleep(e.retry_after + random.uniform(0.1, 0.4))
        except Exception:
            await asyncio.sleep(0.001)

@_gate
async def _cmd_uswipe(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    target_name = _υ_strip(u.message).strip()

    if not target_name and u.message.reply_to_message:
        target_name = u.message.reply_to_message.from_user.first_name

    if not target_name:
        return await u.message.reply_text("❗ Usage: <code>.uswipe &lt;name&gt;</code> or reply.", parse_mode=ParseMode.HTML)

    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)

    _χ._flood_chats.add(cid)
    pool = _σ_battalion()[:10] 

    await msg.edit_text(
        f"🌪 <b>ULTRA SWIPE ACTIVATED</b>\n━━━━━━━━━━━━━━\n👤 <b>Target:</b> <code>{target_name}</code>\n⚡ <b>Speed:</b> <code>0.001s</code>\n🤖 <b>Bots:</b> <code>{len(pool)}</code> Bots\n🛑 <b>Stop:</b> <code>.swipestop</code>",
        parse_mode=ParseMode.HTML
    )

    for i, bot in enumerate(pool):
        task = safe_task(_ultra_swipe_task(bot, cid, target_name, i))
        _χ._enqueue(cid, _μ_GLYPH, task)

@_gate
async def _cmd_swipestop(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    _χ._flood_chats.discard(cid)
    _χ._abort(cid, _μ_GLYPH) 
    await u.message.reply_text("🛑 <b>SWIPE STOPPED</b>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  RR ENGINE / TARGETED AUTO-RESPONDER (ONE-TIME REPLY)
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_rr1(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    _χ._auto_slide_data.pop(cid, None)

    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)

    if u.message.reply_to_message:
        target_msg = u.message.reply_to_message
        target_uid = target_msg.from_user.id
        _χ._auto_slide_data[cid] = {"msgs": SLIDE1_MESSAGES, "pattern": None, "idx": 1, "target_uid": target_uid}
        
        text = SLIDE1_MESSAGES[0]
        for b in _σ_battalion():
            safe_task(b.send_message(cid, text, reply_to_message_id=target_msg.message_id))
        
        await msg.edit_text("🚀 <b>RR1 Target Activated</b> (Replying once per message to this user)", parse_mode=ParseMode.HTML)
    else:
        _χ._auto_slide_data[cid] = {"msgs": SLIDE1_MESSAGES, "pattern": None, "idx": 1, "target_uid": None}
        
        text = SLIDE1_MESSAGES[0]
        for b in _σ_battalion():
            safe_task(b.send_message(cid, text))
        
        await msg.edit_text("🤖 <b>RR1 Global Auto-Mode ON</b> (Replying once to everyone)", parse_mode=ParseMode.HTML)

@_gate
async def _cmd_rr2(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    _χ._auto_slide_data.pop(cid, None)

    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)

    if u.message.reply_to_message:
        target_msg = u.message.reply_to_message
        target_uid = target_msg.from_user.id
        _χ._auto_slide_data[cid] = {"msgs": SLIDE2_MESSAGES, "pattern": None, "idx": 1, "target_uid": target_uid}
        
        text = SLIDE2_MESSAGES[0]
        for b in _σ_battalion():
            safe_task(b.send_message(cid, text, reply_to_message_id=target_msg.message_id))
        
        await msg.edit_text("🚀 <b>RR2 Target Activated</b> (Replying once per message to this user)", parse_mode=ParseMode.HTML)
    else:
        _χ._auto_slide_data[cid] = {"msgs": SLIDE2_MESSAGES, "pattern": None, "idx": 1, "target_uid": None}
        
        text = SLIDE2_MESSAGES[0]
        for b in _σ_battalion():
            safe_task(b.send_message(cid, text))
        
        await msg.edit_text("🤖 <b>RR2 Global Auto-Mode ON</b> (Replying once to everyone)", parse_mode=ParseMode.HTML)

@_gate
async def _cmd_rr3(u: Update, c: ContextTypes.DEFAULT_TYPE):
    text = _υ_strip(u.message).strip()
    if not text:
        return await u.message.reply_text("❌ Usage: <code>.rr3 &lt;text&gt;</code>", parse_mode=ParseMode.HTML)
    
    cid = u.effective_chat.id
    _χ._auto_slide_data.pop(cid, None)

    msg = await u.message.reply_text("⚡ <code>[INITIALIZING...]</code>")
    await _live_hacking_animation(msg)
    
    formatted_text = SLIDE3_PATTERN.format(text=text)

    if u.message.reply_to_message:
        target_msg = u.message.reply_to_message
        target_uid = target_msg.from_user.id
        _χ._auto_slide_data[cid] = {"msgs": [], "pattern": text, "idx": 0, "target_uid": target_uid}
        
        for b in _σ_battalion():
            safe_task(b.send_message(cid, formatted_text, reply_to_message_id=target_msg.message_id))
        
        await msg.edit_text(f"🚀 <b>RR3 Target Activated</b> on: <code>{text}</code> (Replying once per message)", parse_mode=ParseMode.HTML)
    else:
        _χ._auto_slide_data[cid] = {"msgs": [], "pattern": text, "idx": 0, "target_uid": None}
        
        for b in _σ_battalion():
            safe_task(b.send_message(cid, formatted_text))
        
        await msg.edit_text(f"🤖 <b>RR3 Global Auto-Mode ON</b> on: <code>{text}</code> (Replying once to everyone)", parse_mode=ParseMode.HTML)

@_gate
async def _cmd_stoprr(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    _χ._auto_slide_data.pop(cid, None)
    await u.message.reply_text("🛑 <b>RR Mode Stopped</b>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  PFP 
# ══════════════════════════════════════════════════════════
_λ_frames:  List[str]       = []
_λ_rolling: Dict[int, bool] = {}

@_gate
async def _cmd_addpfp(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = u.message
    if not msg.reply_to_message or not msg.reply_to_message.photo:
        await msg.reply_text("⚠️ Reply to an image."); return
    _λ_frames.append(msg.reply_to_message.photo[-1].file_id)
    await msg.reply_text(f"✅ PFP #{len(_λ_frames)} saved.")

async def _λ_spin(bot: Bot, cid: int):
    idx = 0
    while _λ_rolling.get(cid):
        try:
            fid   = _λ_frames[idx % len(_λ_frames)]; idx += 1
            f     = await bot.get_file(fid)
            photo = bytes(await f.download_as_bytearray())
            await bot.set_chat_photo(cid, photo=photo)
        except asyncio.CancelledError: return
        except RetryAfter as e:
            try: await asyncio.sleep(e.retry_after + random.uniform(0.1, 0.4))
            except asyncio.CancelledError: return
        except Exception: pass

@_gate
async def _cmd_pfp(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    if not _λ_frames:
        return await u.message.reply_text("⚠️ <code>.addpfp</code> first.", parse_mode=ParseMode.HTML)
    _λ_rolling[cid] = True
    pool = _σ_battalion()
    for bot in pool:
        _χ._enqueue(cid, "pfp", safe_task(_λ_spin(bot, cid)))
    await u.message.reply_text(
        f"🖼 <b>PFP FAST SWAP</b> | <code>{len(pool)}</code> bots | <code>{len(_λ_frames)}</code> frames",
        parse_mode=ParseMode.HTML)

@_gate
async def _cmd_spfp(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    _λ_rolling[cid] = False; _χ._abort(cid, "pfp")
    await u.message.reply_text("🛑 <b>PFP STOPPED</b>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  SPAM
# ══════════════════════════════════════════════════════════
async def _ν_fire(bot: Bot, cid: int, texts: List[str]):
    rc = random.choice
    while _χ._spam_live.get(cid):
        try: await bot.send_message(cid, rc(texts))
        except asyncio.CancelledError: return
        except RetryAfter as e:
            try: await asyncio.sleep(e.retry_after + random.uniform(0.1, 0.5))
            except asyncio.CancelledError: return
        except Exception: pass

@_gate
async def _cmd_spam(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid   = u.effective_chat.id
    tgts  = _σ_fronts(cid)
    txt   = _υ_strip(u.message).strip()
    texts = [txt] if txt else ["Spam Message"]
    for t in tgts: _χ._kill_spam(t); _χ._abort(t, _ν_GLYPH)
    await u.message.reply_text(
        f"📢 <b>SPAM ON</b> | <code>{len(_σ_battalion())}</code> bots × <code>{len(tgts)}</code> GC | ⛔ <code>.spamstop</code>",
        parse_mode=ParseMode.HTML)
    for t in tgts:
        _χ._spam_live[t] = True
        for bot in _σ_battalion():
            _χ._enqueue(t, _ν_GLYPH, safe_task(_ν_fire(bot, t, texts)))

@_gate
async def _cmd_spamstop(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    tgts = _σ_fronts(cid)
    for t in tgts: _χ._kill_spam(t); _χ._abort(t, _ν_GLYPH)
    await u.message.reply_text("🛑 <b>SPAM STOPPED</b>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  RAID GCs
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_raidadd(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id; _χ._fronts.add(cid)
    await u.message.reply_text(
        f"🎯 <b>RAID TARGET</b> added | total: <code>{len(_χ._fronts)}</code>",
        parse_mode=ParseMode.HTML)

@_gate
async def _cmd_raidlist(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not _χ._fronts: return await u.message.reply_text("⚠️ No targets.")
    lines = [f"🎯 <b>Targets</b> ({len(_χ._fronts)})"] + [f"  • <code>{cid}</code>" for cid in _χ._fronts]
    await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)

@_gate
async def _cmd_raidclear(u: Update, c: ContextTypes.DEFAULT_TYPE):
    _χ._fronts.clear()
    await u.message.reply_text("✅ <b>All targets cleared</b>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  GLOBAL MASS MUTE / UNMUTE (ADMIN INCLUSIVE)
# ══════════════════════════════════════════════════════════
def _get_lockdown_perms(lock: bool) -> ChatPermissions:
    return ChatPermissions(
        can_send_messages=not lock,
        can_send_audios=not lock,
        can_send_documents=not lock,
        can_send_photos=not lock,
        can_send_videos=not lock,
        can_send_video_notes=not lock,
        can_send_voice_notes=not lock,
        can_send_polls=not lock,
        can_send_other_messages=not lock,
        can_add_web_page_previews=not lock,
    )

async def _toggle_admin_status(chat_id: int, bot: Bot, lock: bool):
    try:
        me = await bot.get_me()
        admins = await bot.get_chat_administrators(chat_id)
        perms = _get_lockdown_perms(lock)
        for member in admins:
            if member.user.id == me.id or member.status == "creator":
                continue
            try:
                await bot.restrict_chat_member(chat_id, member.user.id, permissions=perms)
            except Exception:
                continue
    except Exception:
        pass

@_gate
async def _cmd_lockdown(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    try:
        await c.bot.set_chat_permissions(cid, _get_lockdown_perms(True))
        await _toggle_admin_status(cid, c.bot, True)
        await u.message.reply_text("🔇 <b>LOCKDOWN ACTIVE</b>\nAll members and admins have been silenced.", parse_mode=ParseMode.HTML)
    except Exception as e:
        await u.message.reply_text(f"⚠️ Lockdown failed: <code>{e}</code>", parse_mode=ParseMode.HTML)

@_gate
async def _cmd_breaklock(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    try:
        await c.bot.set_chat_permissions(cid, _get_lockdown_perms(False))
        await _toggle_admin_status(cid, c.bot, False)
        await u.message.reply_text("🔊 <b>LOCKDOWN LIFTED</b>\nChat permissions restored for everyone.", parse_mode=ParseMode.HTML)
    except Exception as e:
        await u.message.reply_text(f"⚠️ Release failed: <code>{e}</code>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  GLOBAL TIME
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_time(u: Update, c: ContextTypes.DEFAULT_TYPE):
    query = _υ_strip(u.message).strip()
    if not query:
        query = "UTC"
    msg = await u.message.reply_text(f"🌐 Fetching global time for <code>{query}</code>...", parse_mode=ParseMode.HTML)
    try:
        url = f"https://wttr.in/{query}?format=%T+%Z"
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and "Unknown location" not in response.text:
            data = response.text.strip().split()
            current_time = data[0]
            timezone = data[1] if len(data) > 1 else "Local"
            time_report = (
                f"🕒 <b>Global Time: {query.title()}</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"⌚ <b>Time:</b> <code>{current_time}</code>\n"
                f"🗺 <b>Zone:</b> <code>{timezone}</code>\n"
                f"📅 <b>Date:</b> <code>{time.strftime('%Y-%m-%d')}</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f" #𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰★🇺🇩_🇪ref𝙧ofwrapper𓆪"
            )
            await msg.edit_text(time_report, parse_mode=ParseMode.HTML)
        else:
            await msg.edit_text("❌ Location not recognized. Try a major city (e.g., <code>.time London</code>).", parse_mode=ParseMode.HTML)
    except Exception as e:
        await msg.edit_text(f"⚠️ Connection error: <code>{str(e)}</code>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  SYSTEM BOOT / STATUS
# ══════════════════════════════════════════════════════════
START_TIME = time.time()
def _get_readable_time(seconds: float) -> str:
    periods = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    result = []
    for name, count in periods:
        value = int(seconds // count)
        if value > 0:
            seconds %= count
            result.append(f"{value}{name}")
    return " ".join(result) if result else "0s"

@_gate
async def _cmd_status(u: Update, c: ContextTypes.DEFAULT_TYPE):
    delta = time.time() - START_TIME
    readable = _get_readable_time(delta)
    uptime_text = (
        f"⏳ <b>𝐒𝐘𝐒𝐓𝐄𝐌 𝐔𝐏𝐓𝐈𝐌𝐄</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🚀 <b>Online:</b> <code>{readable}</code>\n"
        f"🤖 <b>Fleet:</b> <code>{len(_σ_battalion())}</code> bots\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f" #𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰★𝐑єxस"
    )
    await u.message.reply_text(uptime_text, parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  WEATHER 
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_weather(u: Update, c: ContextTypes.DEFAULT_TYPE):
    city = _υ_strip(u.message).strip()
    if not city:
        return await u.message.reply_text("❗ Usage: <code>.weather &lt;city name&gt;</code>", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text(f"🔍 Fetching weather for <code>{city}</code>...", parse_mode=ParseMode.HTML)
    try:
        url = f"https://wttr.in/{city.replace(' ', '+')}?format=%C|%t|%w|%h"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200 and "Unknown location" not in response.text:
            data = response.text.split('|')
            if len(data) == 4:
                condition = data[0].strip()
                temp = data[1].strip()
                wind = data[2].strip()
                humidity = data[3].strip()
                weather_report = (
                    f"🌡 <b>Weather Report: {city.title()}</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"☁️ <b>Condition:</b> <code>{condition}</code>\n"
                    f"🌡 <b>Temp:</b> <code>{temp}</code>\n"
                    f"💨 <b>Wind:</b> <code>{wind}</code>\n"
                    f"💧 <b>Humidity:</b> <code>{humidity}</code>\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f" #𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰★𝐑єxस"
                )
                await msg.edit_text(weather_report, parse_mode=ParseMode.HTML)
            else:
                await msg.edit_text("❌ Location not found or invalid API response.")
        else:
            await msg.edit_text("❌ Location not found or service down.")
    except Exception as e:
        await msg.edit_text(f"⚠️ Error fetching weather: <code>{str(e)}</code>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  CLONE
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_clone_(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.message.reply_to_message:
        return await u.message.reply_text("🎯 Reply to the target user to perform an Advanced Clone.")
    target = u.message.reply_to_message.from_user
    cid = u.effective_chat.id
    full_name = target.full_name
    username = f"@{target.username}" if target.username else "No Username"
    bio = ""
    description = ""
    try:
        full_user = await c.bot.get_chat(target.id)
        bio = full_user.bio or ""
        description = full_user.description or ""
    except Exception:
        pass
    photo_bytes = None
    try:
        photos = await target.get_profile_photos(limit=1)
        if photos.total_count > 0:
            file = await c.bot.get_file(photos.photos[0][-1].file_id)
            photo_bytes = await file.download_as_bytearray()
    except Exception as e:
        logging.error(f"Could not fetch PFP: {e}")
    await u.message.reply_text(
        f"🧬 <b>ADVANCED CLONE INITIATED</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Target:</b> <code>{full_name}</code>\n"
        f"🆔 <b>ID:</b> <code>{target.id}</code>\n"
        f"✨ <b>Bio:</b> <code>{bio[:50]}...</code>\n"
        f"🔄 <b>Fleet Status:</b> Syncing {len(_σ_battalion())} bots...",
        parse_mode=ParseMode.HTML
    )
    async def _deploy_identity(bot: Bot):
        try:
            await bot.set_my_name(name=full_name)
            await bot.set_my_short_description(short_description=bio[:120])
            if description:
                await bot.set_my_description(description=description[:512])
            if photo_bytes:
                await bot.set_user_profile_photo(photo=bytes(photo_bytes))
        except Exception as e:
            logging.error(f"Bot {bot.id} Clone Error: {e}")
    await asyncio.gather(*(_deploy_identity(b) for b in _σ_battalion()), return_exceptions=True)
    await u.message.reply_text("✅ <b>Advanced Sync Complete.</b> The fleet is now a mirror image.", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  STOPALL
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_stopall(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid  = u.effective_chat.id
    tgts = _σ_fronts(cid)
    for t in tgts:
        _χ._kill_all(t); _ω_nc_ledger.pop(t, None); _λ_rolling[t] = False
        _χ._auto_slide_data.pop(t, None)
    _χ._abort_all()
    await u.message.reply_text(
        f"🛑 <b>EVERYTHING STOPPED</b> | tasks left: <code>{_χ._tally()}</code>",
        parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  CHUP / BOL  (mute/unmute)
# ══════════════════════════════════════════════════════════
async def _gc_is_admin(uid: int, chat_id: int, bot: Bot) -> bool:
    try:
        member = await bot.get_chat_member(chat_id, uid)
        return member.status in ("administrator", "creator")
    except Exception:
        return False

async def _cmd_chup(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.message or not u.effective_user: return
    if not _σ_is_chat_leader(c.bot.id, u.effective_chat.id): return
    if not u.message.reply_to_message:
        return await u.message.reply_text("🤫 Reply to a user's message and use <code>.mute</code>", parse_mode=ParseMode.HTML)
    uid_self = u.effective_user.id; chat_id = u.effective_chat.id
    if not await _gc_is_admin(uid_self, chat_id, c.bot):
        return await u.message.reply_text("❌ Only admins can use <code>.mute</code>", parse_mode=ParseMode.HTML)
    target = u.message.reply_to_message.from_user
    if not target:            return await u.message.reply_text("❌ Could not identify user.")
    if target.id == uid_self: return await u.message.reply_text("❌ Can't mute yourself.")
    if target.is_bot:         return await u.message.reply_text("❌ Can't mute a bot.")
    _chup_silenced.add((chat_id, target.id))
    try: await u.message.delete()
    except Exception: pass
    notice = await c.bot.send_message(
        chat_id, f"🤫 <b>{target.first_name}</b> has been silenced!",
        parse_mode=ParseMode.HTML)
    await asyncio.sleep(5)
    try: await notice.delete()
    except Exception: pass

async def _cmd_bol(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.message or not u.effective_user: return
    if not _σ_is_chat_leader(c.bot.id, u.effective_chat.id): return
    if not u.message.reply_to_message:
        return await u.message.reply_text("🔊 Reply to a silenced user and use <code>.unmute</code>", parse_mode=ParseMode.HTML)
    uid_self = u.effective_user.id; chat_id = u.effective_chat.id
    if not await _gc_is_admin(uid_self, chat_id, c.bot):
        return await u.message.reply_text("❌ Only admins can use <code>.unmute</code>", parse_mode=ParseMode.HTML)
    target = u.message.reply_to_message.from_user
    if not target: return await u.message.reply_text("❌ Could not identify user.")
    key = (chat_id, target.id)
    if key not in _chup_silenced:
        return await u.message.reply_text(
            f"✅ <b>{target.first_name}</b> is not silenced.", parse_mode=ParseMode.HTML)
    _chup_silenced.discard(key)
    try: await u.message.delete()
    except Exception: pass
    notice = await c.bot.send_message(
        chat_id, f"🔊 <b>{target.first_name}</b> can speak again!",
        parse_mode=ParseMode.HTML)
    await asyncio.sleep(5)
    try: await notice.delete()
    except Exception: pass

async def _handle_chup_media(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.message or not u.effective_user: return
    if not _σ_is_chat_leader(c.bot.id, u.effective_chat.id): return
    if (u.effective_chat.id, u.effective_user.id) in _chup_silenced:
        try: await asyncio.sleep(0.1); await u.message.delete()
        except Exception: pass

async def _handle_chup_command(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.message or not u.effective_user: return
    if not _σ_is_chat_leader(c.bot.id, u.effective_chat.id): return
    if (u.effective_chat.id, u.effective_user.id) in _chup_silenced:
        try: await asyncio.sleep(0.1); await u.message.delete()
        except Exception: pass

@_gate
async def _cmd_ud_error(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    if cid in _ω_ud_enhanced:
        _ω_ud_enhanced.remove(cid)
        await u.message.reply_text("🛑 <b>★★𝐔ᴅ_𝐄ʀʀᴏ𝐑 ENHANCED MODE DEACTIVATED</b>\nBot has returned to normal state.", parse_mode=ParseMode.HTML)
    else:
        _ω_ud_enhanced.add(cid)
        msg = await u.message.reply_text("⚡ <code>[ENHANCING CORE...]</code>")
        await _live_hacking_animation(msg)
        await msg.edit_text(
            f"🔥 <b>★★𝐑єxस ENHANCED MODE ACTIVATED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🤖 <b>Status:</b> Single-Bot Ultra Swipe Engine ON\n"
            f"🎯 <b>Target:</b> Auto-Swipe Reply to Enemy Bots\n"
            f"⚡ <b>Power:</b> <code>1</code> Bot Striking\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"<i>Toggle off with .uD_Error</i>", parse_mode=ParseMode.HTML)

async def _cmd_autohandle(u: Update, c: ContextTypes.DEFAULT_TYPE):
    try:
        if not u.message: return
        cid    = u.message.chat_id
        if not _σ_is_chat_leader(c.bot.id, cid): return
        
        mid    = u.message.message_id
        sender = u.message.from_user
        pool   = _σ_battalion() or _ω_fleet
        
        if sender and (cid, sender.id) in _chup_silenced:
            try: await asyncio.sleep(0.1); await u.message.delete()
            except Exception: pass
            return

        # ─── ENHANCED uD_Error BLOCK ───
        if cid in _ω_ud_enhanced and sender and sender.is_bot and sender.id not in _σ_ghost():
            if pool:
                leader_bot = pool[0]
                for _ in range(3):
                    try:
                        swipe_txt = random.choice(_P_SWIPE_ULTRA).format(name=sender.first_name)
                        safe_task(leader_bot.send_message(cid, swipe_txt, reply_to_message_id=mid))
                    except Exception:
                        pass
        # ────────────────────────────────

        # Enhanced Auto-Responder Swipe/Slide Reply Logic
        if cid in _χ._auto_slide_data and sender and sender.id not in _σ_ghost():
            data = _χ._auto_slide_data[cid]
            target_uid = data.get("target_uid")
            
            if target_uid is None or sender.id == target_uid:
                if data["pattern"]:
                    text = SLIDE3_PATTERN.format(text=data["pattern"])
                else:
                    text = data["msgs"][data["idx"] % len(data["msgs"])]
                    data["idx"] += 1
                
                # 🚀 INSTANT MULTI-TASK ATTACK MODE IF ONLY 1 BOT DEPLOYED IN CHAT
                if len(pool) == 1:
                    for _ in range(5):
                        safe_task(pool[0].send_message(cid, text, reply_to_message_id=mid))
                else:
                    for b in pool:
                        safe_task(b.send_message(cid, text, reply_to_message_id=mid))

        if cid in _χ._flood_chats:
            own = _σ_ghost()
            if not sender or sender.id not in own:
                await asyncio.gather(*(b.delete_message(cid, mid) for b in pool),
                                    return_exceptions=True)
    except Exception as e:
        logging.error(f"Anti-Crasher caught error: {e}")
        return

# ══════════════════════════════════════════════════════════
#  MANAGEMENT
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_addbot(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    
    # Read layout details dynamically from promoter bot access levels
    pool = _σ_battalion()
    promoter_bot = pool[0] if pool else c.bot
    
    invite_link = "No link generated"
    try:
        link_obj = await promoter_bot.create_chat_invite_link(cid)
        invite_link = link_obj.invite_link
    except Exception:
        try:
            chat_info = await promoter_bot.get_chat(cid)
            if chat_info.invite_link:
                invite_link = chat_info.invite_link
        except Exception:
            pass

    text = (
        f"<b>📥 FLEET ONBOARDING MATRIX</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"Click the instant injection links below to seamlessly mount the pre-configured bots into this chat:\n\n"
    )
    for username in FLEET_USERNAMES:
        text += f"▪️ <b>{username.replace('_', ' ')}</b> ╸ <a href='https://t.me/{username}?startgroup=true'>[ ADD BOT ]</a>\n"
        
    text += (
        f"\n🔗 <b>Quick Group Invite Link:</b> {invite_link}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"<i>Note: After adding the missing units, dispatch the <code>.wakeup</code> command to execute automatic privilege cascades and custom admin tagging!</i>"
    )
    await u.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

@_gate
async def _cmd_listbot(u: Update, c: ContextTypes.DEFAULT_TYPE):
    lines = [f"🤖 Main: <code>{len(_ω_fleet)}</code> | Annexe: <code>{len(_ω_annexe)}</code>"]
    for i, b in enumerate(_ω_fleet + _ω_annexe, 1):
        try:    me = await b.get_me(); lines.append(f"  {i}. @{me.username}")
        except: lines.append(f"  {i}. [dead]")
    await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)

@_crown
async def _cmd_delbot(u: Update, c: ContextTypes.DEFAULT_TYPE):
    raw = _υ_strip(u.message).strip()
    if not raw: return await u.message.reply_text("Usage: <code>.delbot ID</code>", parse_mode=ParseMode.HTML)
    try:
        idx = int(raw) - 1
        if 0 <= idx < len(_ω_annexe):
            _ω_annexe.pop(idx); _ω_ann_tk.pop(idx); _π_push(); _σ_sync_ids()
            await u.message.reply_text(f"✅ Removed. Remaining: {len(_ω_annexe)}")
        else: await u.message.reply_text("⚠️ Invalid index.")
    except ValueError: await u.message.reply_text("⚠️ Send a number.")

# ══════════════════════════════════════════════════════════
#  OSINT SCANNING TERMINAL & PUBLIC METADATA RECON MODULES
# ══════════════════════════════════════════════════════════
async def _terminal_animation(msg):
    frames = [
        "[■□□□□□□□□□] 10%",
        "[■■□□□□□□□□] 20%",
        "[■■■□□□□□□□] 30%",
        "[■■■■□□□□□□] 40%",
        "[■■■■■□□□□□] 50%",
        "[■■■■■■□□□□] 60%",
        "[■■■■■■■□□□] 70%",
        "[■■■■■■■■□□] 80%",
        "[■■■■■■■■■□] 90%",
        "[■■■■■■■■■■] 100%",
    ]
    for frame in frames:
        try:
            await msg.edit_text(f"```\n{frame}\nInitializing OSINT scan...```", parse_mode=ParseMode.MARKDOWN)
            await asyncio.sleep(0.15)
        except Exception:
            break

def _sync_hack_lookup(target: str) -> str:
    result = ""
    # Geolocation Core
    try:
        geo = requests.get(f"http://ip-api.com/json/{target}", timeout=8).json()
        if geo.get("status") == "success":
            result += (
                f"🌍 GEOLOCATION\n\n"
                f"IP: {target}\n"
                f"COUNTRY: {geo.get('country')}\n"
                f"REGION: {geo.get('regionName')}\n"
                f"CITY: {geo.get('city')}\n"
                f"ISP: {geo.get('isp')}\n"
                f"ZIP: {geo.get('zip')}\n"
                f"PROXY: {geo.get('proxy')}\n\n"
            )
    except Exception: pass

    # DNS Target Mapping
    try:
        ip_addr = socket.gethostbyname(target)
        result += f"🛰 DNS LOOKUP\n\nDOMAIN: {target}\nIP ADDRESS: {ip_addr}\n\n"
    except Exception: pass

    # Public Whois Parsing
    try:
        w = whois.whois(target)
        result += f"📄 WHOIS DATA\n\nDOMAIN: {w.domain_name}\nREGISTRAR: {w.registrar}\nCREATED: {w.creation_date}\n\n"
    except Exception: pass

    return result if result else "No public data found."

@_gate
async def _cmd_hack_osint(u: Update, c: ContextTypes.DEFAULT_TYPE):
    raw = _υ_strip(u.message).strip()
    if not raw:
        return await u.message.reply_text("Usage:\n`.hack &lt;ip/domain&gt;`", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text("`BOOTING TERMINAL...`", parse_mode=ParseMode.MARKDOWN)
    await _terminal_animation(msg)
    
    loop = asyncio.get_event_loop()
    final_output = await loop.run_in_executor(None, lambda: _sync_hack_lookup(raw))
    await msg.edit_text(f"```\n{final_output}```", parse_mode=ParseMode.MARKDOWN)

def _sync_bypass_hibp(email: str) -> str:
    API_KEY = "YOUR_HIBP_API_KEY"
    headers = {"hibp-api-key": API_KEY, "User-Agent": "OSINT-BOT"}
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    try:
        r = requests.get(url, headers=headers, timeout=8)
        if r.status_code == 200:
            breaches = r.json()
            names = "\n".join([f" • {x['Name']}" for x in breaches])
            return f"⚠ BREACHES FOUND\n\nEMAIL: {email}\n\nDATABASES:\n{names}\n"
        elif r.status_code == 404:
            return f"✅ NO PUBLIC BREACHES FOUND\n\nEMAIL: {email}\n"
        else:
            return f"ℹ HIBP METRIC INQUIRY STATUS: {r.status_code}\nEMAIL: {email}\n"
    except Exception as ex:
        return f"❌ Audit Connection Timeout: {str(ex)}"

@_gate
async def _cmd_bypass_hibp(u: Update, c: ContextTypes.DEFAULT_TYPE):
    raw = _υ_strip(u.message).strip()
    if not raw:
        return await u.message.reply_text("Usage:\n`.bypass &lt;email&gt;`", parse_mode=ParseMode.HTML)
    
    msg = await u.message.reply_text("`Connecting to breach database...`", parse_mode=ParseMode.MARKDOWN)
    await _terminal_animation(msg)
    
    loop = asyncio.get_event_loop()
    final_output = await loop.run_in_executor(None, lambda: _sync_bypass_hibp(raw))
    await msg.edit_text(f"```\n{final_output}```", parse_mode=ParseMode.MARKDOWN)

# ══════════════════════════════════════════════════════════
#  ADMIN (AUTH)
# ══════════════════════════════════════════════════════════
@_crown
async def _cmd_addsudo(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if u.message.reply_to_message:
        uid = u.message.reply_to_message.from_user.id
    else:
        raw = _υ_strip(u.message).strip()
        if not raw: return await u.message.reply_text("❗ Reply to a user or provide an ID.")
        try: uid = int(raw.split()[0])
        except ValueError: return await u.message.reply_text("❗ Invalid ID.")
    
    _χ.sentinels.add(uid); _χ._persist()
    await u.message.reply_text(f"✅ <code>{uid}</code> added to Auth list.", parse_mode=ParseMode.HTML)

@_crown
async def _cmd_delsudo(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if u.message.reply_to_message:
        uid = u.message.reply_to_message.from_user.id
    else:
        raw = _υ_strip(u.message).strip()
        if not raw: return await u.message.reply_text("❗ Reply to a user or provide an ID.")
        try: uid = int(raw.split()[0])
        except ValueError: return await u.message.reply_text("❗ Invalid ID.")
        
    if uid in OWNERS: return await u.message.reply_text("⚠️ Cannot remove owner.")
    _χ.sentinels.discard(uid); _χ._persist()
    await u.message.reply_text(f"⛔ <code>{uid}</code> removed from Auth list.", parse_mode=ParseMode.HTML)

@_crown
async def _cmd_authlist(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not _χ.sentinels: return await u.message.reply_text("No Auth users found.")
    lines = ["🛡 <b>Auth Users:</b>"] + [f"  • <code>{uid}</code>" for uid in _χ.sentinels]
    await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)

async def _cmd_id(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.effective_chat or not _σ_is_chat_leader(c.bot.id, u.effective_chat.id): return
    if u.message.reply_to_message:
        uu = u.message.reply_to_message.from_user
        if not uu: return await u.message.reply_text("❌ Anonymous or channel message.")
        await u.message.reply_text(
            f"👤 <b>{uu.full_name}</b>\n🆔 <code>{uu.id}</code>\n"
            f"📛 @{uu.username or 'None'}", parse_mode=ParseMode.HTML)
    else:
        uu = u.effective_user
        await u.message.reply_text(
            f"👤 <b>{uu.full_name}</b>\n🆔 <code>{uu.id}</code>\n"
            f"📛 @{uu.username or 'None'}\n💬 Chat: <code>{u.effective_chat.id}</code>",
            parse_mode=ParseMode.HTML)

@_gate
async def _cmd_leavegc(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.message.chat_id
    await u.message.reply_text("👋 All bots leaving...")
    for bot in _σ_battalion():
        try: 
            await bot.leave_chat(cid)
        except TelegramError: 
            pass
        if cid in _ω_chat_presence and bot.id in _ω_chat_presence[cid]:
            _ω_chat_presence[cid].remove(bot.id)

async def _cmd_leader(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.effective_user or u.effective_user.id not in OWNERS:
        return
    raw = _υ_strip(u.message).strip()
    pool = _ω_fleet + _ω_annexe
    if not raw:
        lines = [f"👑 <b>GLOBAL LEADER BOT</b> — takes priority if in group\n"]
        for i, b in enumerate(pool, 1):
            try:
                me = await b.get_me()
                mark = "👑" if b.id == _ω_leader_id else "  "
                lines.append(f"{mark} {i}. @{me.username} (<code>{b.id}</code>)")
            except Exception:
                lines.append(f"  {i}. [dead]")
        lines.append("\n📌 Use <code>.leader ID</code> to switch.")
        return await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)
    try:
        idx = int(raw) - 1
        if 0 <= idx < len(pool):
            chosen = pool[idx]
            _σ_set_leader(chosen.id)
            me = await chosen.get_me()
            await u.message.reply_text(
                f"👑 <b>Global Leader set to</b> @{me.username}\n"
                f"It will override local chat leaders when present.",
                parse_mode=ParseMode.HTML)
        else:
            await u.message.reply_text(f"⚠️ Invalid. Pick 1–{len(pool)}.")
    except ValueError:
        await u.message.reply_text("❗ Usage: <code>.leader</code> to list", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  LIVE CHAT MEMBER WATCHER (AUTO-LEADER SYNC + PROMOTE)
# ══════════════════════════════════════════════════════════
async def _cmd_chat_member_watch(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if not u.my_chat_member: return
    nw  = u.my_chat_member.new_chat_member
    cid = u.my_chat_member.chat.id
    
    if nw.status in ("left", "kicked", "banned"):
        if cid in _ω_chat_presence and c.bot.id in _ω_chat_presence[cid]:
            _ω_chat_presence[cid].remove(c.bot.id)
        return

    if isinstance(nw, ChatMemberAdministrator) and nw.can_promote_members:
        for b in _σ_battalion():
            if b.id == nw.user.id:
                safe_task(_Ρ_cascade(b, cid))
                return

_Ρ_RIGHTS = dict(
    can_change_info=True, can_delete_messages=True,
    can_restrict_members=True, can_invite_users=True,
    can_pin_messages=True, can_promote_members=True,
    can_manage_chat=True, can_manage_video_chats=True,
)

async def _Ρ_elevate(donor: Bot, target: Bot, cid: int):
    for _ in range(3):
        try: 
            await donor.promote_chat_member(cid, target.id, **_Ρ_RIGHTS)
            try:
                await donor.set_chat_administrator_custom_title(chat_id=cid, user_id=target.id, custom_title="★ uD_Eʀroʀ Siʀ ★")
            except Exception: pass
            return
        except RetryAfter as e: await asyncio.sleep(e.retry_after + 0.5)
        except Exception: return

async def _Ρ_cascade(donor: Bot, cid: int):
    rest = [b for b in (_ω_fleet + _ω_annexe) if b.id != donor.id]
    if not rest: return
    await asyncio.gather(*(_Ρ_elevate(donor, t, cid) for t in rest), return_exceptions=True)

# ══════════════════════════════════════════════════════════
#  WATCHDOG
# ══════════════════════════════════════════════════════════
async def _Θ_sentinel():
    _tick = 0
    while True:
        try:
            await asyncio.sleep(_Θ_HOUND)
            _tick += 1
            _χ._sweep(); gc.collect(0)
            if len(_ρ_hive) > _ρ_CAP // 2:
                for k in list(_ρ_hive)[:64]: del _ρ_hive[k]
            
            now = time.monotonic()
            for bid in [b for b, exp in list(_ι_lockout.items()) if exp < now - 3600]:
                _ι_lockout.pop(bid, None)
                
            if _tick % 360 == 0:
                gc.collect()
                for cid in [c for c in list(_ω_nc_ledger) if not _χ._nc_live.get(c)]:
                    del _ω_nc_ledger[cid]
                _ρ_hive.clear()
        except asyncio.CancelledError: return
        except Exception: pass

# ══════════════════════════════════════════════════════════
#  ★𝐑єxस SIMULATION TERMINAL HANDLERS
# ══════════════════════════════════════════════════════════
INJECT_TEXT = """<b><pre> 💉 MEMORY INJECTION MODULE </pre></b>
<code>[>] SELECTING TARGET PROCESS PID... [OK]</code>
<code>[>] ALLOCATING VIRTUAL MEMORY SPACES...</code>
<code>[>] WRITING MALICIOUS SHELLCODE... [DONE]</code>
<code>[>] INJECTING INTO MAIN THREAD... [SUCCESS]</code>
━━━━━━━━━━━━━━━━━━━━
<b>RESULT:</b> <code>DLL INJECTION SUCCESSFUL</code>
<b>PROCESS:</b> <code>SYSTEM_CORE_HIJACKED</code>"""

DOX_TEXT = """<b><pre> 🛰️ TARGET GEOLOCATION DOX </pre></b>
<code>[>] RESOLVING TARGET DOMAIN MAP...</code>
<code>[>] PINGING SATELLITE NODES... [OK]</code>
<code>[>] ACQUIRING CELL-TOWER GATEWAYS...</code>
<code>[>] TRIANGULATING COORDINATES... [DONE]</code>
━━━━━━━━━━━━━━━━━━━━
<b>IP ADDRESS:</b> <code>185.220.101.5</code>
<b>COORDINATES:</b> <code>40.7128° N, 74.0060° W</code>
<b>STATUS:</b> <code>TARGET GEOLOCATED</code>"""

FLOOD_TEXT = """<b><pre> 🌊 PACKET OVERLOAD FLOOD </pre></b>
<code>[>] SYNCHRONIZING BOTNET FLEET... [OK]</code>
<code>[>] LAUNCHING UDP STREAM PACKETS...</code>
<code>[>] OVERFLOWING NETWORK BUFFERS...</code>
<code>[>] CORRUPTING ROUTER PIPELINES... [MAX]</code>
━━━━━━━━━━━━━━━━━━━━
<b>BITRATE:</b> <code>850 GBPS / SEC</code>
<b>STATUS:</b> <code>TARGET BUFFER OVERFLOW</code>"""

ROOT_TEXT = """<b><pre> 👑 ROOT PRIVILEGE ELEVATION </pre></b>
<code>[>] SCANNING LOCAL EXPLOIT VECTORS...</code>
<code>[>] EXECUTING KERNEL OVERFLOW... [OK]</code>
<code>[>] EXTRAPOLATING SHADOW HASHES...</code>
<code>[>] ELEVATING USER PERMISSIONS... [ROOT]</code>
━━━━━━━━━━━━━━━━━━━━
<b>ACCESS LEVEL:</b> <code>UID=0 (ROOT/ADMIN)</code>
<b>CONSOLE:</b> <code>FULL INTERACTIVE SHELL</code>"""

SCAN_TEXT = """<b><pre> 🔍 PORT VULNERABILITY AUDIT </pre></b>
<code>[>] SCANNING TARGET NETWORK RANGE...</code>
<code>[>] DETECTING ALIVE PORTS [80, 443, 22, 8080]...</code>
<code>[>] EXPLOITABLE THREAD FOUND ON PORT 22... [CVE-READY]</code>
━━━━━━━━━━━━━━━━━━━━
<b>TARGET FEED:</b> <code>VULNERABLE</code>
<b>VECTOR LINK:</b> <code>SSH_BRUTE_POSSIBLE</code>"""

BREACH_TEXT = """<b><pre> 🔓 DATABASE DECRYPTION CORE </pre></b>
<code>[>] LEAKING TABLE SCHEMAS... [████████░░] 80%</code>
<code>[>] EXTRACTING ENCRYPTED SHA256 SALTS... [OK]</code>
<code>[>] PARSING SQLITE/POSTGRES BINARY BLOCKS...</code>
━━━━━━━━━━━━━━━━━━━━
<b>DB STATUS:</b> <code>EXFILTRATED SUCCESSFUL</code>
<b>RECORDS EXPOSED:</b> <code>14,295 USERS DUMPED</code>"""

RANSOM_TEXT = """<b><pre> 🔒 SIMULATED CRYPTO-LOCK </pre></b>
<code>[>] INITIALIZING AES-256 COUNTER SCHEME...</code>
<code>[>] DISCOVERING DIRECTORY BOUNDARIES... [OK]</code>
<code>[>] EXPORTING UNIQUE PUBLIC RSA KEY PAIR... [DONE]</code>
━━━━━━━━━━━━━━━━━━━━
<b>FILE LOCKOUT:</b> <code>SANDBOX_ENCRYPTED</code>
<b>DECRYPTOR CORE:</b> <code>PENDING VALID KEY MASK</code>"""

@_gate
async def _cmd_inject(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(INJECT_TEXT, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_dox(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(DOX_TEXT, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_flood(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(FLOOD_TEXT, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_root(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(ROOT_TEXT, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_scan(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(SCAN_TEXT, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_breach(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(BREACH_TEXT, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_ransom(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = await u.message.reply_text("⚡ <code>[LAUNCHING...]</code>")
    await _live_hacking_animation(msg)
    await msg.edit_text(RANSOM_TEXT, parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  LIVE ANIMATED PING OPERATION
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_ping(u: Update, c: ContextTypes.DEFAULT_TYPE):
    start = time.monotonic()
    msg = await u.message.reply_text("⚡ <code>[PINGING] INITIATING SECURE HANDSHAKE...</code>", parse_mode=ParseMode.HTML)
    
    stages = [
        "📡 ACQUIRING SUB-GATEWAY CONNECTIONS...",
        "🎛️ MEASURING INTERCEPT TRANSMISSION VALUES...",
        "🖲️ CALCULATING BOTNET MATRIX PACKET DELAY..."
    ]
    
    for idx, description in enumerate(stages, 1):
        await asyncio.sleep(0.2)
        fake_ms = random.randint(22, 94)
        progress = idx * 6
        fake_bar = "█" * progress + "░" * (20 - progress)
        try:
            await msg.edit_text(
                f"⚙️ <b>LIVE CONNECTION DIAGNOSTIC</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"<code>[STG {idx}/3] {description}</code>\n"
                f"📶 <b>Current:</b> <code>{fake_ms} ms</code>\n"
                f"[{fake_bar}] <code>{idx * 33}%</code>",
                parse_mode=ParseMode.HTML
            )
        except Exception:
            pass

    ms = round((time.monotonic() - start) * 1000, 2)
    bar = "█" * min(int(ms / 20), 20) + "░" * max(0, 20 - int(ms / 20))
    qual = "🟢 Excellent" if ms < 100 else ("🟡 Good" if ms < 300 else "🔴 Poor")
    dms = round(_Δ_delay[0] * 1000, 2)
    
    await msg.edit_text(
        f"🏓 <b>PONG (STABLE CONNECTION)</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📶 <b>Final Latency:</b> <code>{ms} ms</code>\n"
        f"[{bar}]\n"
        f"📊 <b>Quality Indicator:</b> {qual}\n"
        f"⏱ <b>Relay Delay Value:</b> <code>{dms} ms</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"#<b><b>𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰★🇺🇩_🇪ref𝙧of★𓆪</b></b>",
        parse_mode=ParseMode.HTML
    )

# ══════════════════════════════════════════════════════════
#  LIVE ANIMATED PRUNING / WIPE & SWIPE OPERATION
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_wipe(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    raw = _υ_strip(u.message).strip()
    
    count = 20
    if raw:
        try:
            count = int(raw.split()[0])
        except ValueError:
            pass
            
    if count < 1: count = 1
    if count > 100: count = 100

    msg = await u.message.reply_text("⚡ <code>[WIPE LOG] INITIATING SECURE SANITIZATION ENGINE...</code>", parse_mode=ParseMode.HTML)
    
    try:
        await asyncio.sleep(0.3)
        await msg.edit_text(
            f"⚙️ <b>LIVE PURGE CORE ENGAGED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"<code>[+] LOCATING CHAT INDICES... [OK]</code>\n"
            f"<code>[+] target stack: {count} elements</code>\n"
            f"<code>[+] status: ENCRYPTING TARGET CHAINS & SERVICE RECORDS...</code>",
            parse_mode=ParseMode.HTML
        )
    except Exception:
        pass

    try:
        await u.message.delete()
    except Exception:
        pass

    erased = 0
    mid_start = msg.message_id - 1
    
    for i in range(count):
        target_mid = mid_start - i
        if target_mid <= 0:
            break
            
        try:
            await c.bot.delete_message(chat_id=cid, message_id=target_mid)
            erased += 1
        except TelegramError:
            pass
            
        if i % 5 == 0 or i == count - 1:
            progress_ticks = min(int((erased / count) * 20), 20)
            fake_bar = "█" * progress_ticks + "░" * (20 - progress_ticks)
            try:
                await msg.edit_text(
                    f"🧹 <b>STACK WIPER LOG ENGINE</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"<code>[>] STATUS: FLUSHING TEXT & TITLE SERVICE ENTRIES...</code>\n"
                    f"<code>[>] ERASING: {erased} / {count} DATA NODES</code>\n"
                    f"[{fake_bar}] <code>{int((erased/count)*100)}%</code>\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"★<b>𝐑єxस resource★ CYBER CLEAN ACTIVE</b>",
                    parse_mode=ParseMode.HTML
                )
            except Exception:
                pass
            await asyncio.sleep(0.1)

    try:
        await msg.edit_text(
            f"✅ <b>STACK PURGE COMPLETED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🔒 <b>STATUS:</b> <code>LOG CLEAN / ANONYMOUS</code>\n"
            f"🗑️ <b>NODES REMOVED:</b> <code>{erased} ELEMENTS</code>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"#𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰★<b>𝐑єxस resource★𓆪</b>",
            parse_mode=ParseMode.HTML
        )
    except Exception:
        pass

# ══════════════════════════════════════════════════════════
#  SQUEEZE - ABSOLUTE CHAT LOCKDOWN
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_squeeze(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    msg = await u.message.reply_text("⚡ <code>[SQUEEZE] INITIATING PROTOCOL OVERRIDE...</code>", parse_mode=ParseMode.HTML)
    await asyncio.sleep(0.4)
    
    try:
        perms = ChatPermissions(
            can_send_messages=False,
            can_send_audios=False,
            can_send_documents=False,
            can_send_photos=False,
            can_send_videos=False,
            can_send_video_notes=False,
            can_send_voice_notes=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False
        )
        
        await c.bot.set_chat_permissions(cid, perms)
        await _toggle_admin_status(cid, c.bot, True)

        SQUEEZE_TEXT = """<b><pre> 🗜️ SYSTEM COMPRESSION INITIATED </pre></b>
<code>[>] OVERRIDING CHAT PERMISSIONS...</code>
<code>[>] REVOKING SEND_MESSAGE RIGHTS... [OK]</code>
<code>[>] LOCKING METADATA PROTOCOLS... [OK]</code>
━━━━━━━━━━━━━━━━━━━━
<b>STATUS:</b> <code>CHAT SQUEEZED (LOCKED)</code>
<b>RESTRICTIONS:</b> <code>MESSAGES + NAME_CHANGES DISABLED</code>"""
        
        await msg.edit_text(SQUEEZE_TEXT, parse_mode=ParseMode.HTML)
    except Exception as e:
        await msg.edit_text(f"⚠️ Squeeze failed: <code>{e}</code>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  FLEET WAKEUP & PRIVILEGE ASSESSMENT WITH TAG
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_wakeup(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cid = u.effective_chat.id
    msg = await u.message.reply_text("⚡ <code>[FLEET WAKEUP] RUNNING DIAGNOSTIC & PRIVILEGE SYNC...</code>", parse_mode=ParseMode.HTML)
    await asyncio.sleep(0.3)
    
    pool = _σ_battalion()
    
    promoter_bot = None
    for bot in pool:
        try:
            member = await bot.get_chat_member(cid, bot.id)
            if member.status in ("administrator", "creator") and getattr(member, 'can_promote_members', False):
                promoter_bot = bot
                break
        except Exception: 
            continue

    try:
        ctx_member = await c.bot.get_chat_member(cid, c.bot.id)
        if ctx_member.status in ("administrator", "creator") and getattr(ctx_member, 'can_promote_members', False):
            promoter_bot = c.bot
    except Exception:
        pass

    invite_link = "No link generated"
    if promoter_bot:
        try:
            chat_info = await promoter_bot.get_chat(cid)
            if chat_info.invite_link:
                invite_link = chat_info.invite_link
            else:
                link_obj = await promoter_bot.create_chat_invite_link(cid)
                invite_link = link_obj.invite_link
        except Exception:
            try:
                link_obj = await c.bot.create_chat_invite_link(cid)
                invite_link = link_obj.invite_link
            except Exception:
                pass

    promoted_count = 0
    titled_count = 0
    missing_bots = []
    
    if promoter_bot:
        for target_bot in pool:
            if target_bot.id == promoter_bot.id: 
                continue
            try:
                try:
                    await promoter_bot.get_chat_member(cid, target_bot.id)
                except TelegramError as te:
                    if "user not found" in str(te).lower() or "not a participant" in str(te).lower():
                        try:
                            bot_me = await target_bot.get_me()
                            missing_bots.append(f"@{bot_me.username}")
                        except Exception:
                            missing_bots.append(f"ID: <code>{target_bot.id}</code>")
                        continue

                await promoter_bot.promote_chat_member(chat_id=cid, user_id=target_bot.id, **_Ρ_RIGHTS)
                promoted_count += 1
                
                await asyncio.sleep(0.15)
                await promoter_bot.set_chat_administrator_custom_title(chat_id=cid, user_id=target_bot.id, custom_title="★ uD_Eʀroʀ Siʀ ★")
                titled_count += 1
            except Exception: 
                continue
    else:
        await msg.edit_text("❌ <b>ERROR:</b> None of the fleet bots are administrators with <code>can_promote_members</code> rights. Promote at least one bot manually first!", parse_mode=ParseMode.HTML)
        return

    missing_text = "\n".join([f"  • {b}" for b in missing_bots]) if missing_bots else "  • None (All fleet bots present!)"
    
    report = (
        f"<b>🛰️ [FLEET WAKEUP COMPLETED]</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👑 <b>Active Promoter:</b> @{(await promoter_bot.get_me()).username}\n"
        f"⚡ <b>Bots Promoted:</b> <code>{promoted_count}</code>\n"
        f"🏷️ <b>Titles Applied:</b> <code>{titled_count}</code> Tagged as <code>★ uD_Eʀroʀ Siʀ ★</code>\n\n"
        f"📥 <b>MISSING BOTS (Add manually to GC):</b>\n{missing_text}\n\n"
        f"🔗 <b>Quick Group Invite Link:</b> {invite_link}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"#<b><b>🇲ᴀ🇩🇪 #By 𓆰★𝐑єxस𓆪</b></b>"
    )
    await msg.edit_text(report, parse_mode=ParseMode.HTML)

@_gate
async def _cmd_troll_action(u: Update, c: ContextTypes.DEFAULT_TYPE):
    cmd_name = u.message.text.split()[0].replace(".", "")
    await u.message.reply_text(f"<code>[!] Executing {cmd_name}...</code>\n<code>[!] Status: ★𝐑єxसʀresource★ SUCCESSFUL</code>", parse_mode=ParseMode.HTML)

# ══════════════════════════════════════════════════════════
#  CUSTOM AUTO-LEAVE (.over) PROTOCOL
# ══════════════════════════════════════════════════════════
@_gate
async def _cmd_over(u: Update, c: ContextTypes.DEFAULT_TYPE):
    chat_id = u.effective_chat.id
    
    await u.message.reply_text(" Ƭᴇʀɪ M🇺ᴍᴍ Mummy Ơɴʟყ 𝐑єxस Ƈʜᴏᴅᴇɢᴀ?? ⌁ ____/")
    
    gif_url = "https://i.pinimg.com/originals/cb/2d/65/cb2d65582234ec8b17ca917eab337900.gif"
    try:
        await c.bot.send_animation(chat_id=chat_id, animation=gif_url)
    except Exception as e:
        logging.error(f"Asset push failure: {e}")
        
    for bot in _σ_battalion():
        try:
            await bot.leave_chat(chat_id=chat_id)
        except Exception:
            pass
        if chat_id in _ω_chat_presence and bot.id in _ω_chat_presence[chat_id]:
            _ω_chat_presence[chat_id].remove(bot.id)

# ══════════════════════════════════════════════════════════
#  APP BUILDER MAPPING
# ══════════════════════════════════════════════════════════
from telegram.request import HTTPXRequest as _HTTPXRequest

def _make_req() -> _HTTPXRequest:
    return _HTTPXRequest(
        connection_pool_size=1024,
        read_timeout=40.0, write_timeout=40.0,
        connect_timeout=15.0, pool_timeout=20.0,
    )

def _build_app(tok: str) -> Application:
    app = (Application.builder().token(tok).request(_make_req())
           .concurrent_updates(True).build())
    _map = {
        "start":      _cmd_start,
        "panel":      _cmd_panel,
        "help":       _cmd_menu,
        "n1":         _cmd_nc,
        "n2":         _cmd_ncchud,
        "n3":         _cmd_ncLEVI,
        "n4":         _cmd_sexual,
        "stopnc":     _cmd_ruk,
        "speed":      _cmd_delay,
        "mute":       _cmd_chup,
        "unmute":     _cmd_bol,
        "addpfp":     _cmd_addpfp,
        "pfp":        _cmd_pfp,
        "spfp":       _cmd_spfp,
        "spam":       _cmd_spam,
        "spamstop":   _cmd_spamstop,
        "raidadd":    _cmd_raidadd,
        "raidlist":   _cmd_raidlist,
        "raidclear":  _cmd_raidclear,
        "addbot":     _cmd_addbot,
        "listbot":    _cmd_listbot,
        "delbot":     _cmd_delbot,
        "auth":       _cmd_addsudo,
        "unauth":     _cmd_delsudo,
        "id":         _cmd_id,
        "stopall":    _cmd_stopall,
        "authlist":   _cmd_authlist, 
        "ping":       _cmd_ping,
        "leavegc":    _cmd_leavegc,
        "menupfp":    _cmd_menupfp,
        "delmenupfp": _cmd_delmenupfp,
        "leader":     _cmd_leader,
        "clone":      _cmd_clone_,
        "weather":    _cmd_weather,
        "status":     _cmd_status,
        "time":       _cmd_time,
        "muteall":    _cmd_lockdown,
        "unmuteall":  _cmd_breaklock,
        "uswipe":     _cmd_uswipe,
        "swipestop":  _cmd_swipestop,
        "rr1":        _cmd_rr1,
        "rr2":        _cmd_rr2,
        "rr3":        _cmd_rr3,
        "stoprr":     _cmd_stoprr,
        "hack":       _cmd_hack_osint,
        "inject":     _cmd_inject,
        "bypass":     _cmd_bypass_hibp,
        "dox":        _cmd_dox,
        "flood":      _cmd_flood,
        "root":       _cmd_root,
        "scan":       _cmd_scan,
        "breach":     _cmd_breach,
        "wipe":       _cmd_wipe,
        "swipe":      _cmd_wipe,
        "wakeup":     _cmd_wakeup,
        "ransom":     _cmd_ransom,
        "squeeze":    _cmd_squeeze,
        "over":       _cmd_over,
        "uD_Error":   _cmd_ud_error,
    }
    
    for cmd, fn in _map.items():
        app.add_handler(CommandHandler(cmd, fn)) 
        app.add_handler(PrefixHandler([".", "-", "/"], cmd, fn)) 
        
    app.add_handler(MessageHandler(filters.COMMAND, _handle_chup_command), group=-1)
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, _cmd_autohandle))
    app.add_handler(MessageHandler(
        (filters.PHOTO | filters.VIDEO | filters.Sticker.ALL |
         filters.Document.ALL | filters.ANIMATION | filters.VIDEO_NOTE),
        _handle_chup_media))
    app.add_handler(ChatMemberHandler(_cmd_chat_member_watch, ChatMemberHandler.MY_CHAT_MEMBER))
    return app

# ══════════════════════════════════════════════════════════
#  MAIN EXECUTION & AUTO-RECOVERY
# ══════════════════════════════════════════════════════════
async def _rise():
    global _ω_leader_id
    
    loop = asyncio.get_running_loop()
    def global_exception_handler(loop, context):
        pass
    loop.set_exception_handler(global_exception_handler)

    _ω_apps.clear(); _ω_fleet.clear(); _ω_annexe.clear(); _ω_ann_tk.clear()
    
    print(f"\n{'═'*54}\n  ★𝐑єxस ref𝙧of🔲★ V-13 | QUEUE-RELAY NC ENGINE\n{'═'*54}\n")
    print("Initiating Fleet...")

    stored_tokens = _π_pull()
    
    for i, token in enumerate(TOKENS):
        try:
            app = _build_app(token)
            await app.initialize()
            await app.start()
            if app.updater:
                await app.updater.start_polling(drop_pending_updates=True)
            
            bot_obj = app.bot
            _ω_apps.append(app)
            _ω_fleet.append(bot_obj)
            
            print(f"  [FLEET] Bot {i+1} active")
        except Exception as e:
            print(f"  [ERROR] Failed to boot main bot {i+1}: {e}")

    if _ω_fleet:
        _ω_leader_id = _ω_fleet[0].id

    for tok in stored_tokens:
        bot = await _π_boot_annexe(tok)
        if bot:
            _ω_annexe.append(bot)
            _ω_ann_tk.append(tok)

    _σ_sync_ids()
    safe_task(_Θ_sentinel())
    
    print(f"\n✅ System Live | Fleet Size: {len(_σ_battalion())}\n")

    try:
        while True:
            await asyncio.sleep(3600)
    except asyncio.CancelledError:
        pass
    finally:
        for app in _ω_apps:
            await app.updater.stop()
            await app.stop()
            await app.shutdown()

if __name__ == "__main__":
    _Δ_delay.append(0.0) 
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    print("Booting sequence initiated...")
    
    _restart_delay = 5
    while True:
        try:
            asyncio.run(_rise())
            break
        except KeyboardInterrupt:
            print("\n  Stopped cleanly.")
            break
        except BaseException as _err:
            print(f"\n  [CRASH CAUGHT] {_err!r}")
            print(f"  Auto-Restarting in {_restart_delay}s...")
            time.sleep(_restart_delay)
            _restart_delay = min(_restart_delay * 2, 60)
