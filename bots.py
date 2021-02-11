# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN

import math
import random

words=['word', 'word', 'word','word','word', 'word', 'word','word','word', 'word', 'word','word',
'word', 'word', 'word','word','word', 'word', 'word','word','word', 'word', 'word','word','word',
'word', 'word','word','word', 'word', 'word','word','word', 'word', 'word','word','word', 'word']

emoji=['stickerID',
       'stickerID',
       'stickerID',
       'stickerID',
       'stickerID']

def frase(update, context):
    phrase = random.choice(words)+" "+random.choice(words)+" "+random.choice(words)
    update.message.reply_text(phrase)

    val = int(open("count.txt", "r").read())
    add = val + 1
    file1 = open("count.txt", "w")
    file1.write(str(add))
    file1.close()

    update.message.reply_sticker(sticker=(random.choice(emoji)), disable_notification=True)

def dati(update, context):
    comb = len(words)
    fatt = math.pow(comb, 3)
    valstat = open("count.txt", "r").read()

    update.message.reply_text(str(comb) + " " + "parole\n" +
                              str("{0:,.0f}".format(fatt)).replace(",", ".") + " " + "combinazioni\n" +
                              valstat + " " + "frasi generate")

def main():
   upd= Updater(TOKEN, use_context=True)
   disp=upd.dispatcher

   disp.add_handler(CommandHandler("XXXXXXXX", frase))
   disp.add_handler(CommandHandler("YYYYYYYY", dati))

   upd.start_polling()

   upd.idle()

if __name__=='__main__':
   main()
