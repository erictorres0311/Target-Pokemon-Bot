import requests

def send_telegram_message(message):
    token = "7685195148:AAGH7K3ZRmeXFAdGd6QI20musFA-iqx_d_A"
    chat_id = "7598605884"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")