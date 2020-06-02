from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import urllib.request
import json


REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"

ACCESSTOKEN = 'y0BDcp9f5IJrht0KFHhZsRP4Zq+h+Qh9E0ZKeD8oAEi4YVR1Jef58uIfA99nUf4/GydPX+3eNvrkcsLDL50N0CTMcCNhqd4uVu4av+7xssrbr84cGamvLeSXJhHwN0aQE//dgdrk60AQi6pYQPNnZwdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print('test')
        print(body)
        print('test')
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)
