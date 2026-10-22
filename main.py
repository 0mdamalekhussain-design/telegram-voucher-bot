import os
import string
import random
from flask import Flask, render_template_string, request

app = Flask(__name__)

# ৫ ডিজিটের র‍্যান্ডম ভাউচার কোড জেনারেট করার ফাংশন
def generate_voucher():
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for i in range(5))

# ওয়েব পোর্টালের ডিজাইন (HTML & CSS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mahim UltraNet - Voucher Portal</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        h2 { color: #007bff; margin-bottom: 10px; }
        p { color: #666; font-size: 14px; }
        .btn { background-color: #28a745; color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; font-size: 16px; cursor: pointer; margin-top: 15px; }
        .btn:hover { background-color: #218838; }
        .voucher-box { background: #e8f5e9; border: 2px dashed #4caf50; padding: 15px; margin-top: 20px; border-radius: 6px; }
        .voucher-code { font-size: 22px; font-weight: bold; color: #2e7d32; letter-spacing: 2px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🌐 Mahim UltraNet</h2>
        <p>হটস্পট ভাউচার পেতে নিচের বাটনে ক্লিক করুন</p>
        
        <form method="POST">
            <button type="submit" class="btn">🎟️ ভাউচার নিন (Get Voucher)</button>
        </form>

        {% if voucher %}
        <div class="voucher-box">
            <p>আপনার ভাউচার কোড:</p>
            <div class="voucher-code">{{ voucher }}</div>
            <p style="font-size: 12px; margin-top: 5px;">এই কোড দিয়ে ইন্টারনেটে লগইন করুন</p>
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
        # মাইক্রোটিক ভাউচার জেনারেট হচ্ছে
        voucher = generate_voucher()
        # এখানে চাইলে জেনারেট হওয়া কোডটি মাইক্রোটিকের API-তে পাঠানোর কোড যুক্ত করা যাবে
    return render_template_string(HTML_TEMPLATE, voucher=voucher)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  
