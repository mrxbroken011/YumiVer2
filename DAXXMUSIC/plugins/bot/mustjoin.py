from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app

MUST_JOIN = "KGF_ROCY"

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    
    try:
        await app.get_chat_member(MUST_JOIN, msg.from_user.id)
    except UserNotParticipant:
        link = f"https://t.me/{MUST_JOIN}" if MUST_JOIN.isalpha() else (await app.get_chat(MUST_JOIN)).invite_link
        try:
            await msg.reply_photo(
                photo="https://telegra.ph/file/dfde87c32f8951c6b7628.jpg", 
                caption=(
                    "๏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ "
                    "[๏sᴜᴘᴘᴏʀᴛ๏](https://t.me/Dasi_girl_boys_video_chat_group) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ "
                    "ᴛʜᴇɴ ᴊᴏɪɴ [๏sᴜᴘᴘᴏʀᴛ๏](https://t.me/Dasi_girl_boys_video_chat_group) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !\n\n"
                    "𝐏ᴏᴡᴇʀᴇᴅ  𝐁ʏ : `[—͟͞™ɪɴɴᴏᴄ͢͢͢ᴇɴᴛ आत्मा </𝟑 ｡˚](t.me/KGF_ROKY)💥"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("๏Jᴏɪɴ๏", url=link)]
                    ]
                )
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !`💥")
