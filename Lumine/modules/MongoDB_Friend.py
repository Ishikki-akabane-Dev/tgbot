import json
import html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler, Filters, CallbackQueryHandler, run_async
from telegram.utils.helpers import escape_markdown, mention_html

from Lumine import dispatcher
from Lumine.modules.helper_funcs.extraction import extract_user


def friendx(update: Update, context: CallbackContext):
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    bot = context.bot
    args = context.args
    if message.reply_to_message:
        repl_message = message.reply_to_message
        user_id = repl_message.from_user.id
        useridd = int(user_id)
        message.reply_text(
            "Choose",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="✅", callback_data=f"friend={useridd}"
                        ),
                        InlineKeyboardButton(text="❌", callback_data=f"friend_del={useridd}"),
                    ]
                ]
            )
        )

def friendx_btn(update: Update, context: CallbackContext):
    bot = context.bot
    query = update.callback_query
    user = update.effective_user
    senderid = update.effective_user.id
    sender_name = update.effective_user.first_name
    sender_id = int(senderid)
    query_id = query.id
    splitter = query.data.split("=")
    query_match = splitter[0]
    if query_match != "friend_del":
        user_id = splitter[1]
        user_id = int(user_id)
        if user_id == senderid:
            query.message.edit_text(f"Congratulations🎊!!!\n{sender_name} accepted your friend request")
        else:
            bot.answer_callback_query(query_id, text="Not your Query!!!")
    else:
        user_id = splitter[1]
        user_id = int(user_id)
        if user_id == senderid:
            query.message.delete()
        else:
            bot.answer_callback_query(query.id, text="Not your Query!!!")

FRIENDX_HANDLER = CommandHandler("friend", friendx, run_async=True)
FRIENDX_BTN_HANDLER = CallbackQueryHandler(friendx_btn)

dispatcher.add_handler(FRIENDX_HANDLER)
dispatcher.add_handler(FRIENDX_BTN_HANDLER)