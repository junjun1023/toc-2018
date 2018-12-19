import requests
from urllib.request import urlopen

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAADZBPAz8j68BAOpAqQaAnytMkv6PhxQJ6FjHEMFY2OIqzEKah3Sdb0XVvmZCHZB4oeLOlxVsVRrBI67PslLf7ctrEOVhn35UE6RcBQxx4zvOp7qZCXW0orgZCFiZCXt3AOSi2rdlZAWqsXxlPIBDj4VWNIcWlzxUZC4L53ebgKcOgZDZD"

DIST_BUTTON = [
    {
        "type": "postback",
        "title": "北區",
        "payload": "north"
    },
    {
        "type": "postback",
        "title": "東區",
        "payload": "east"
    },
    {
        "type": "postback",
        "title": "中西區",
        "payload": "west_central"
    }
]

TYPE_BUTTON = [
    {
        "type": "postback",
        "title": "飯",
        "payload": "rice"
    },
    {
        "type": "postback",
        "title": "麵",
        "payload": "noodles"
    },
    {
        "type": "postback",
        "title": "點心",
        "payload": "snack"
    }
]

SAT_BUTTON = [
    {
        "type": "postback",
        "title": "滿意",
        "payload": "satisfied"
    },
    {
        "type": "postback",
        "title": "重選",
        "payload": "reselect"
    }
]

BYE_BUTTON = [
    {
        "type": "postback",
        "title": "拜拜",
        "payload": "bye"
    }
]

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    send_action(id)
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    data = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": img_url,
                    "is_reusable": True
                }
            }
        }
    }
    send_action(id)
    response = requests.post(url, json=data)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    data = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": buttons
                }
            }
        }
    }
    response = requests.post(url, json=data)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_action(id):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    data = {
        "recipient": {
            "id": id
        },
        "sender_action": "typing_on"
    }

    response = requests.post(url, json=data)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
