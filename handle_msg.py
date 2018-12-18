#coding:utf-8
import re
import template_json

def handle_message(message_text, sender_id):
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', message_text )

    if '不是我要的答案' in message_text :
        return '請您等待專人為您回答🙂  '

    if '嗨' in message_text :
        if len(message_text ) < 10:
            return '你好！🙂\n請問我能為您做些什麼？ '
    
    #love
    if '男友' in message_text or '女友' in message_text :
        if '交' in message_text or '配對' in message_text or '想' in message_text or '陪' in message_text:
            faq = template_json.Template_json(sender_id,template_type=2,
                   text="是否曾吃過屎", payload_yes = "START_STATE_YES", payload_no = "START_STATE_NO" )
            return faq

        return '請參考台灣10大交友APP https://ibuyranking.blogspot.com/2018/03/xd.html '
    
    #anything
    if len( message_text ) < 28 :
        if '天氣' in message_text :
            return '這裡有最新的天氣狀況哦🙂 https://tw.news.yahoo.com/weather/'

    return '抱歉>＿<\n我還無法處理這個問題，掰掰🙂 '
