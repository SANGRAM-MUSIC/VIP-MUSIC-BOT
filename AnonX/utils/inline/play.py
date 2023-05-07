import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 5:
        bar = "✯"
    elif 5 < anon < 10:
        bar = "☆"
    elif 10 <= anon < 15:
        bar = "✷"
    elif 15 <= anon < 20:
        bar = "✰"
    elif 20 <= anon < 25:
        bar = "✯"
    elif 25 <= anon < 30:
        bar = "☆"
    elif 30 <= anon < 35:
        bar = "✯"
    elif 35 <= anon < 40:
        bar = "✷"
    elif 40 <= anon < 45:
        bar = "✪"
    elif 45 < anon < 50:
        bar = "✯"
    elif 50 <= anon < 55:
        bar = "✷"
    elif 55 <= anon < 60:
        bar = "✰"
    elif 60 <= anon < 65:
        bar = "☆"
    elif 65 <= anon < 70:
        bar = "✯"
    elif 70 <= anon < 75:
        bar = "✷"
    elif 75 <= anon < 80:
        bar = "✰"
    elif 80 <= anon < 85:
        bar = "☆"
    elif 85 <= anon < 90:
        bar = "✯"
    elif 90 <= anon < 92:
        bar = "✷"
    elif 92 <= anon < 94:
        bar = "✰"
    elif 94 <= anon < 95:
        bar = "☆"
    elif 95 <= anon < 96:
        bar = "✯"
    elif 96 <= anon < 97:
        bar = "☆"
    else:
        bar = "✷"

    buttons = [
        [
            InlineKeyboardButton(
                text="𝘀ҡเp", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝘀τσρ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝗰ℓσѕε", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 5:
        bar = "✯"
    elif 5 < anon < 10:
        bar = "☆"
    elif 10 <= anon < 15:
        bar = "✷"
    elif 15 <= anon < 20:
        bar = "✰"
    elif 20 <= anon < 25:
        bar = "✯"
    elif 25 <= anon < 30:
        bar = "☆"
    elif 30 <= anon < 35:
        bar = "✯"
    elif 35 <= anon < 40:
        bar = "✷"
    elif 40 <= anon < 45:
        bar = "✪"
    elif 45 < anon < 50:
        bar = "✯"
    elif 50 <= anon < 55:
        bar = "✷"
    elif 55 <= anon < 60:
        bar = "✰"
    elif 60 <= anon < 65:
        bar = "☆"
    elif 65 <= anon < 70:
        bar = "✯"
    elif 70 <= anon < 75:
        bar = "✷"
    elif 75 <= anon < 80:
        bar = "✰"
    elif 80 <= anon < 85:
        bar = "☆"
    elif 85 <= anon < 90:
        bar = "✯"
    elif 90 <= anon < 92:
        bar = "✷"
    elif 92 <= anon < 94:
        bar = "✰"
    elif 94 <= anon < 95:
        bar = "☆"
    elif 95 <= anon < 96:
        bar = "✯"
    elif 96 <= anon < 97:
        bar = "☆"
    else:
        bar = "✷"
buttons = [
        [
            InlineKeyboardButton(
                text="𝘀ҡเp", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝘀τσρ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝗰ℓσѕε", callback_data=f"close"
            )
        ],
    ]
return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘀ҡเp", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝘀τσρ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝗰ℓσѕε", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘀ҡเp", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝘀τσρ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝗰ℓσѕε", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘀ҡเp", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝘀τσρ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝗰ℓσѕε", callback_data=f"close"
            )
        ],
    ]
    return buttons
