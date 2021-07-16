import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from cinderella import dispatcher
from cinderella.modules.disable import DisableAbleCommandHandler

ABUSE_STRINGS = (

    "Tere baap ne mujse madad li kyoki uska lauda chota tha", 
    "MADARCHOD",
    "Bhenchod ",
    " Apna jhaat kaat le burchode", 
    "Burchode", 
    "Gand me kir ke aulaad", 
    "Randi Ke Aulad",
    "Betichod", 
    "Tatte", 
    "Chutmarike", 
    "Adhi luli", 
    "Gand Ke Chopadike", 
    "laude", 
    "mother fucker"
  )

SONG_STRINGS = (
    "Mere Dost Hai Nakli La La La La", 
    "My friens are fake la la la la"
 )

@run_async
def abuse(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(ABUSE_STRINGS))
    else:
      message.reply_text(random.choice(ABUSE_STRINGS))

@run_async
def sing(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SONG_STRINGS))
    else:
      message.reply_text(random.choice(SONG_STRINGS))

__help__ = """
- /abuse : Abuse someone in Hindi/English
- /sing : First lines of some random Engish Songs.
"""

__mod_name__ = "😡ABUSE😡"

ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SING_HANDLER)
