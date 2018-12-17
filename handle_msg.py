#coding:utf-8
import re
import template_json

def handle_message(message_text, sender_id):
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', message_text )

    if '不是我要的答案' in message_text :
        return '請您等待專人為您回答🙂  '

    if '你好' in message_text or '請問' in message_text or '嗨' in message_text or '哈囉' in message_text or 'hi' in message_text or 'hello' in message_text:
        if len(message_text ) < 10:
            return '你好！🙂\n請問我能為您做些什麼？ '
    
    #dorm
    if '宿網' in message_text or '宿舍網路' in message_text :
        if '不通' in message_text or '不能' in message_text or '斷' in message_text or '認證' in message_text or '連' in message_text or '無法' in message_text or '問題' in message_text:
            faq = template_json.Template_json(sender_id,template_type=2,
                   text="是否曾申請過帳號呢? (請用是/否按扭回答以便記錄)", payload_yes = "START_STATE_YES", payload_no = "START_STATE_NO" )
            return faq

        return '請參考宿網管理系統FAQ http://dorm.cc.ncku.edu.tw/ '

    if '資安' in message_text :
        return '若您需要填寫資安通報，可以先從 https://goo.gl/YzegaO 這裡下載通報檔案，填寫完後直接回傳至security@mail.ncku.edu.tw 這個信箱，或是繳交紙本到計網中心一樓🙂'
    
    #閒聊
    if len( message_text ) < 28 :
        if '謝謝' in message_text or '感謝' in message_text :
            return '很高興能為您幫上忙～ 😀'

        if '笨蛋' in message_text or '弱' in message_text or '爛' in message_text or '白痴' in message_text or '白癡' in message_text or '智障' in message_text :
            return '因為我還在學習當中嘛，不要這樣～～'

        if '沒' in message_text :
            if '女朋友' in message_text or '女友' in message_text or '男朋友' in message_text or '男友' in message_text :
                return '我們可以一起繼續魯下去👻'

        if '天氣' in message_text :
            return '這裡有最新的天氣狀況哦🙂 https://tw.news.yahoo.com/weather/'

        if '睡覺' in message_text or '睡著' in message_text :
            return '🐷'

        if '大便' in message_text or '尿' in message_text :
            return '您先請'

        if '喜歡你' in message_text or '愛你' in message_text :
            return '對不起 我心有所屬了😳'

        if '單身' in message_text :
            return '對，我就是在等你 💗'

        if '再見' in message_text or '掰掰' in message_text :
            return '有緣再相會～🙂'

        if '唱歌' in message_text :
            return '我不會唱歌，但我可以給你youtube哦！！🙂  https://www.youtube.com/'

        if '難過' in message_text :
            return '我難過的是放棄你放棄愛～https://www.youtube.com/watch?v=T0LfHEwEXXw'

        if '失戀' in message_text :
            return '天涯何處無芳草，何必單戀一枝花'

        if '你是誰' in message_text :
            return '我是可愛的機器人'

        if '講笑話' in message_text or '聽笑話' in message_text :
            return '老師:大雄.老師給你90元，你再去跟胖虎借10元，這樣你總共有多少錢？\n大雄:0元。...\n老師:你根本不懂數學了!!!!!!\n大雄:你根本不懂胖虎......'

        if '星期幾' in message_text or '幾點' in message_text :
            return '麻煩請往螢幕角落看'

        if '我帥' in message_text or '我很帥' in message_text :
            return '帥到分手'

        if '討厭你' in message_text :
            return '嗚嗚嗚嗚嗚嗚嗚嗚嗚😭'

        if '運勢' in message_text :
            return '大吉大利，從來沒有這麼好過'

        if '新年快樂' in message_text or '恭喜發財' in message_text :
            return '🏮恭喜發財，紅包拿來🏮'

    return '抱歉> < 我還無法處理這個問題，請您等待專人為您回答🙂 '
