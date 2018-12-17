#coding:utf-8
import template_json

def set_temp(payload, recipient_id):  # simple wrapper for logging to stdout on heroku

    if payload == 'START_STATE_NO' :
        faq = template_json.Template_json(recipient_id,template_type=2, #yes/no button
              text = "💩", payload_yes = "OWNER_YES", payload_no = "OWNER_NO" )

    elif payload == 'START_STATE_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問大便是好吃的嗎?", payload_yes = "ACC_OWN_SEAT_YES", payload_no = "ACC_OWN_SEAT_NO" )

    elif payload == 'ACC_OWN_SEAT_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3, #another button
              text = "那你還沒吃過好吃的大便", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'ACC_OWN_SEAT_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "💩💩💩💩💩多吃一點💩💩💩💩💩", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'OWNER_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "好吃？", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'OWNER_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "下次見吧！", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    else :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "掰掰", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    return faq
