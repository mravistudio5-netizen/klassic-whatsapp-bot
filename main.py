import requests

url = "https://graph.facebook.com/v22.0/1122004077660916/messages"

headers = {
    "Authorization": "Bearer EAAUzgUnLfZA8BRZAGHdEWunM6TFc6I68mOnmx7hladleiWjJ7ZB0oeUsTujAm21Y5GTq8rxJluUZCMQObyqM8He7me8xhXaNGXlaV04s1sidDZCCB3LwW8KLuKu8GL3tlQZCkVAfqyYsSGl3ETxSCscZBF38ZAuzGDcKTUFiyfOIf7ZAob680ZASzxXNWQOPXOLnYiHK4dlZBio7yfFftCFalG09mM3xGotZAz94nn41wFaCcecfR2yODT7GlRZCbkgtilMsZC48DImVr9pG0eEGuYr4T2EAZDZD",
    "Content-Type": "application/json"
}

numbers = {
    "919561823015": "Warehouse Open",
    "918262942141": "Kids Wear Open"
}

for number, message_text in numbers.items():

    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
            "body": message_text
        }
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.text)
