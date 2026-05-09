import os
import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

PROGRESS_FILE = 'progress.txt'
CODES_FILE = 'codes.txt'

def read_codes():
    with open(CODES_FILE, 'r') as f:
        codes = [line.strip() for line in f if line.strip()]
    return codes

def read_progress():
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        return 0

def write_progress(index):
    with open(PROGRESS_FILE, 'w') as f:
        f.write(str(index))

def send_telegram_message(code):
    MESSAGE = f"""
🎉 Dear members, hello

🔑 Today's game VIP redemption code:{code}

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

    buttons = {
        "inline_keyboard": [
            [
                {"text": " play now", "url": "https://7wild.vip/install.html"},
                {"text": " Facebook ", "url": "https://www.facebook.com/profile.php?id=100094199282595"}
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
        return response.json()

def main():
    codes = read_codes()
    if len(codes) == 0:
        print("codes.txt 为空，退出")
        return

    current_index = read_progress()
    if current_index >= len(codes):
        print("所有兑换码已用完，停止发送。请更新 codes.txt 并将 progress.txt 重置为 0")
        return

    code = codes[current_index]
    print(f"准备发送第 {current_index+1} 个兑换码: {code}")
    result = send_telegram_message(code)
    print(result)

    # 发送成功后进度 +1
    write_progress(current_index + 1)

if __name__ == "__main__":
    main()
