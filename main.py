import os
import string
import random
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Telegram Bot Credentials (আপনার প্রদত্ত টোকেন ও চ্যাট আইডি)
TELEGRAM_BOT_TOKEN = "8577882986:AAG3AJM9dvDy89lwLk0zZj4pAHgmq84tQU4"
TELEGRAM_CHAT_ID = "7341717546"

def send_voucher_to_router(code, profile):
    """
    টেলিগ্রাম ব্যাকএন্ডের মাধ্যমে মাইক্রোটিকে কমান্ড পাঠানোর ফাংশন
    """
    message = f"/add_voucher {code} {profile}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        res = requests.post(url, json=payload, timeout=5)
        return res.status_code == 200
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        return False

def generate_code(length=5):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mahim UltraNet - Dashboard & Voucher Portal</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 15px; display: flex; justify-content: center; }
        .container { width: 100%; max-width: 480px; background: white; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); padding: 20px; box-sizing: border-box; }
        .header { text-align: center; border-bottom: 2px solid #007bff; padding-bottom: 10px; margin-bottom: 15px; }
        .header h2 { margin: 0; color: #007bff; font-size: 22px; }
        .user-info-card { background: #e9ecef; border-radius: 8px; padding: 12px 15px; margin-bottom: 15px; }
        .info-row { display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 13px; }
        .info-label { font-weight: bold; color: #495057; }
        .info-value { color: #212529; font-weight: 600; }
        .btn { background-color: #28a745; color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; font-size: 16px; cursor: pointer; font-weight: bold; }
        .btn:hover { background-color: #218838; }
        .voucher-box { background: #d4edda; border: 2px dashed #28a745; padding: 15px; margin-top: 15px; border-radius: 6px; text-align: center; }
        .voucher-code { font-size: 24px; font-weight: bold; color: #155724; letter-spacing: 2px; }
        .package-select { width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ced4da; margin-top: 5px; margin-bottom: 15px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>🌐 Mahim UltraNet</h2>
            <p style="margin: 5px 0 0; color: #6c757d; font-size: 12px;">কাস্টমার ড্যাশবোর্ড ও ভাউচার পোর্টাল</p>
        </div>

        <div class="user-info-card">
            <div class="info-row">
                <span class="info-label">💰 একাউন্ট ব্যালেন্স:</span>
                <span class="info-value">৳ ০০.০০</span>
            </div>
            <div class="info-row">
                <span class="info-label">📦 রানিং প্যাকেজ:</span>
                <span class="info-value">কোনো প্যাকেজ সক্রিয় নেই</span>
            </div>
            <div class="info-row">
                <span class="info-label">⏳ মেয়াদের সময় বাকি:</span>
                <span class="info-value">০ দিন ০০ ঘন্টা</span>
            </div>
        </div>

        <form method="POST">
            <label style="font-weight: bold; font-size: 13px; color: #495057;">প্যাকেজ নির্বাচন করুন (টাকায়):</label>
            <select name="package" class="package-select">
                <option value="2_tk">৳ ২ - ৩০ মিনিট</option>
                <option value="4_tk">৳ ৪ - ২ ঘণ্টা</option>
                <option value="6_tk">৳ ৬ - ৫ ঘণ্টা</option>
                <option value="8_tk">৳ ৮ - ৯ ঘণ্টা</option>
                <option value="10_tk">৳ ১০ - ১২ ঘণ্টা</option>
                <option value="12_tk">৳ ১২ - ১৪ ঘণ্টা</option>
                <option value="14_tk">৳ ১৪ - ১৬ ঘণ্টা</option>
                <option value="16_tk">৳ ১৬ - ১ দিন</option>
                <option value="18_tk">৳ ১৮ - ২ দিন</option>
                <option value="26_tk">৳ ২৬ - ৩ দিন</option>
                <option value="34_tk">৳ ৩৪ - ৪ দিন</option>
                <option value="44_tk">৳ ৪৪ - ৫ দিন</option>
                <option value="52_tk">৳ ৫২ - ৬ দিন</option>
                <option value="60_tk">৳ ৬০ - ৭ দিন</option>
                <option value="70_tk">৳ ৭০ - ৮ দিন</option>
                <option value="78_tk">৳ ৭৮ - ৯ দিন</option>
                <option value="86_tk">৳ ৮৬ - ১০ দিন</option>
                <option value="96_tk">৳ ৯৬ - ১১ দিন</option>
                <option value="114_tk">৳ ১illage - ১২ দিন</option>
                <option value="116_tk">৳ ১১৬ - ১৩ দিন</option>
                <option value="118_tk">৳ ১১৮ - ১৪ দিন</option>
                <option value="120_tk">৳ ১২০ - ১৫ দিন</option>
                <option value="122_tk">৳ ১২২ - ১৬ দিন</option>
                <option value="124_tk">৳ ১২৪ - ১৭ দিন</option>
                <option value="126_tk">৳ ১২৬ - ১৮ দিন</option>
                <option value="128_tk">৳ ১২৮ - ১৯ দিন</option>
                <option value="130_tk">৳ ১৩০ - ২০ দিন</option>
                <option value="132_tk">৳ ১৩২ - ২১ দিন</option>
                <option value="134_tk">৳ ১৩৪ - ২২ দিন</option>
                <option value="136_tk">৳ ১৩৬ - ২৩ দিন</option>
                <option value="138_tk">৳ ১৩৮ - ২৪ দিন</option>
                <option value="140_tk">৳ ১৪০ - ২৫ দিন</option>
                <option value="142_tk">৳ ১৪২ - ২৬ দিন</option>
                <option value="144_tk">৳ ১৪৪ - ২৭ দিন</option>
                <option value="146_tk">৳ ১৪৬ - ২৮ দিন</option>
                <option value="148_tk">৳ ১৪৮ - ২৯ দিন</option>
                <option value="150_tk">৳ ১৫০ - ১ মাস</option>
                <option value="280_tk">৳ ২৮০ - ২ মাস</option>
                <option value="360_tk">৳ ৩৬০ - ৩ মাস</option>
                <option value="400_tk">৳ ৪০০ - ৪ মাস</option>
            </select>
            <button type="submit" class="btn">🎟️ ভাউচার তৈরি করুন</button>
        </form>

        {% if voucher %}
        <div class="voucher-box">
            <p style="margin: 0; font-size: 13px;">আপনার জেনারেট হওয়া ভাউচার কোড:</p>
            <div class="voucher-code">{{ voucher }}</div>
            <p style="font-size: 11px; color: #155724; margin: 5px 0 0;">কোডটি সফলভাবে জেনারেট হয়েছে!</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    voucher = None
    if request.method == "POST":
        selected_package = request.form.get("package")
        code = generate_code()
        
        # ব্যাকগ্রাউন্ডে টেলিগ্রামের মাধ্যমে রাউটারে সিঙ্ক করার রিকোয়েস্ট পাঠানো
        send_voucher_to_router(code, selected_package)
        
        voucher = code
    return render_template_string(HTML_TEMPLATE, voucher=voucher)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  
