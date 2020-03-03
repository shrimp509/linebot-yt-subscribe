#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,HttpResponseServerError
from django.http import HttpRequest, HttpResponse
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage, TemplateSendMessage, ConfirmTemplate
from linebot.models import PostbackAction, MessageAction
from django.conf import settings
import os, time

from crawler.views import crawl_subscribes_of_youtuber

line_bot_api = LineBotApi(settings.LINE_ACCESS_TOKEN)
handler = WebhookHandler(settings.CHANNEL_SECRET)


@csrf_exempt
def webhook_view(request):
    try:
        signature = request.headers["X-Line-Signature"]
        body_decode = request.body.decode('utf-8')
        handler.handle(body_decode, signature)
    except:
        return HttpResponse("OK")
    return HttpResponse("OK")


@handler.add(event=MessageEvent, message=TextMessage)
def handle_message(event: MessageEvent):
    try:
        result = crawl_subscribes_of_youtuber(event.message.text)
        line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=TextSendMessage(text=result)
        )
    except:
        line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=TextSendMessage(text="QQ")
        )

    # 應聲蟲
    # print("event source: ", event.source)
    # line_bot_api.reply_message(
    #     reply_token=event.reply_token,
    #     messages=TextSendMessage(text=event.message.text)
    # )



## How to push message?
# line_bot_api.push_message('U46acae51db9af9d9322a935b35e64f36', TextSendMessage(text='Hello World!'))


