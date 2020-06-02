from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from linebot_app.utils import message_creater
from linebot_app.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        # print('test')
        # print(request)
        # print('test')
        # request = json.loads(request.body.decode('utf-8'))
        # events = request['events']
        # events = request_json['events']
        request_json = json.loads(request.body.decode('utf-8'))
        events = request_json['events']
        reply_token = events[0]['replyToken']
        if events[0]["type"]=="message":
            if events[0]["message"]["type"]=="text":
                print('テキスト')
                message = events[0]['message']
                print(reply_token)
                line_message = LineMessage(message_creater.create_single_text_message(message['text']))
                line_message.reply(reply_token)
            elif events[0]["message"]["type"]=="image":
                print('画像')
                line_message = LineMessage(message_creater.create_single_text_message("画像データ"))
                line_message.reply(reply_token)
        return HttpResponse("ok")
