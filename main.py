import requests

ACCESS_TOKEN = "EAAUzgUnLfZA8BRZAGHdEWunM6TFc6I68mOnmx7hladleiWjJ7ZB0oeUsTujAm21Y5GTq8rxJluUZCMQObyqM8He7me8xhXaNGXlaV04s1sidDZCCB3LwW8KLuKu8GL3tlQZCkVAfqyYsSGl3ETxSCscZBF38ZAuzGDcKTUFiyfOIf7ZAob680ZASzxXNWQOPXOLnYiHK4dlZBio7yfFftCFalG09mM3xGotZAz94nn41wFaCcecfR2yODT7GlRZCbkgtilMsZC48DImVr9pG0eEGuYr4T2EAZDZD"
PHONE_NUMBER_ID = "1122004077660916"

messages = [
    ("919370100229", "Social Media Post"),
    ("918262942141", "Warehouse Open"),
    ("919561823015", "Kids Wear Section Open"),
    ("919699117010", "Third Floor Open")
]

for number, text in messages:

    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.text)
