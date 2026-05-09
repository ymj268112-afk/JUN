import os
import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

# 每天你要更换的内容，直接改这里的变量即可
CODE = "【7197L】"   # 每天只需改这个兑换码

MESSAGE = f"""
🎉 Dear members, hello

🔑 Today's game VIP redemption code: {CODE}

Validity period: Today only

➡️Detailed steps to claim:

⭐️Log in to your account.
⭐️Click on your avatar at the top.
⭐️Click on 'Gift'.
⭐️Enter the redemption code to claim.

➡️This code is limited in quantity and is on a first-come, first-served basis.
➡️Each user can only redeem once a day.

✅✅✅
Share this message and let your friends play with you!
"""

def send():
    # 定义两个按钮（左右并排）
    buttons = {
        "inline_keyboard": [
            [
                {"text": " play now", "url": "https://7wild.vip/install.html"},
                {"text": " Facebook Page", "url": "https://www.facebook.com/profile.php?id=100094199282595"}
            ]
        ]
    }

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open('image.png', 'rb') as photo:
        files = {'photo': photo}
        data = {
            'chat_id': CHAT_ID,
            'caption': MESSAGE,
            'parse_mode': 'Markdown',
            'reply_markup': str(buttons).replace("'", '"')
        }
        response = requests.post(url, files=files, data=data)
        print(response.json())

if __name__ == "__main__":
    send()
