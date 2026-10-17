import logging
import random
import string
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8577882986:AAErWeGS1nwF_v8_0z1i78q1ylR4VGO1C_c"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def generate_voucher():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(6))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    voucher_code = generate_voucher()
    
    response_text = (
        f"ধন্যবাদ, {user_name}! আপনার পেমেন্ট সফলভাবে যাচাই করা হয়েছে।\n\n"
        f"আপনার ওয়াইফাই হটস্পট ভাউচার কোড:\n"
        f"🔑 **{voucher_code}**\n\n"
        f"পোর্টালে এই কোডটি ব্যবহার করে ইন্টারনেট উপভোগ করুন!"
    )
    
    await update.message.reply_text(response_text, parse_mode="Markdown")

if __name__ == '__main__':
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .connect_timeout(30.0)
        .read_timeout(30.0)
        .build()
    )
    
    message_handler = MessageHandler(filters.TEXT, handle_message)
    application.add_handler(message_handler)
    
    print("ভাউচার অটোমেশন বোট চালু হয়েছে...")
    application.run_polling()
