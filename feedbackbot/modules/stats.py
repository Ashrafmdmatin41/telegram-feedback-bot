""" Bot stats module"""
from pyrogram import Client, filters
from pyrogram.types import Message

from feedbackbot.db.curd import get_chats_count, get_stats
from feedbackbot.utils.filters import is_admin
from feedbackbot.utils.telegram_handlers import tg_exceptions_handler


@Client.on_message(filters.command("stats") & is_admin)
@tg_exceptions_handler
async def stats_for_users_handler(_: Client, message: Message) -> None:
    """
    Show Bot stats for admins.
    """
    total_users_count: int = get_chats_count()
    messages_stats = get_stats()
    if messages_stats:
        incoming_count = messages_stats.incoming
        outgoing_count = messages_stats.outgoing
    else:
        incoming_count = outgoing_count = 0
    text_message = f"""📈 <b>إحصائيات البوت</b>

👥 <b>المستخدمون</b>
• {total_users_count} مستخدم للبوت

✍️ <b>الرسائل</b>
• {incoming_count} رسالة واردة
  {outgoing_count} رد على الرسائل
"""
    await message.reply_text(text_message, reply_to_message_id=message.reply_to_message_id)
