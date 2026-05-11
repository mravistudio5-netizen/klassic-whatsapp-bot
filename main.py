import requests

TOKEN = "PASTE_ACCESS_TOKEN"
PHONE_NUMBER_ID = "PASTE_PHONE_NUMBER_ID"

messages = [
    ("919370100229", "Social Media Post"),
    ("918262942141", "Warehouse Open"),
    ("919561823015", "Kids Wear Section Open"),
    ("919699117010", "Third Floor Open")
]

url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

for number, text in messages:

    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    }

    requests.post(url, headers=headers, json=data)

print("Messages Sent")
