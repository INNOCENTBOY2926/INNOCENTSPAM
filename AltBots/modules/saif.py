from random import choice

from telethon import events

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import DEAD, ALTRON


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sgali(?: |$)(.*)" % hl))
async def gali(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in ALTRON:
                await e.reply("𝙽𝙾, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝙳𝙴𝚅𝙻𝙾𝙿𝙴𝚁 𝙾𝙵 𝙳𝙴𝙰𝙳 𝙱𝙾𝚃 .")
            elif uid == OWNER_ID:
                await e.reply("𝙽𝙾, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝙾𝚆𝙽𝙴𝚁 𝙾𝙵 𝙳𝙴𝙰𝙳 𝙱𝙾𝚃 ")
            elif uid in SUDO_USERS:
                await e.reply("𝙽𝙾, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙾𝙵 𝙳𝙴𝙰𝙳 𝙱𝙾𝚃 .")
            else:                
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(DEAD)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl} ɢᴀʟɪ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
