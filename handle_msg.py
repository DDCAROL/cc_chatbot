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
    # Email
    if '信箱' in message_text or 'e-mail' in message_text or 'e mail' in message_text or 'email' in message_text or 'mail' in message_text :
        if '進入' in message_text or '登' in message_text or '使用' in message_text or '密碼錯誤' in message_text:
            return '若您是在校生:若無法登入信箱，可以請您嘗試在成功入口介面更改一次密碼，此動作將會同步您的成功入口密碼與個人信箱密碼。\n若您是畢業生:個人mail帳號，會於畢業6個月後停用，請在此6個月內將郵件中的信轉移到您個人使用的email中。'
        if '沒收到' in message_text or '沒有收到' or '收不到' in message_text or '垃圾信' in message_text :
            return '若有沒收到的信，有可能是因為被學校信件過濾系統誤判成是垃圾信件，若是使用個人信箱可以登入這個網頁找尋中途被攔截到的信件：http://antispam.ncku.edu.tw/symphony/login.html ，若是公務信箱則登入下面這個：http://eantispam.ncku.edu.tw/symphony/login.html'
        if '申請' in message_text :
            return '若要申請個人信箱，請先登入成功入口後，點選教職員工個人設定裡的個人用電子郵件帳號申請，填入相關資料後便可啟用'
        if 'outlook' in message_text :
            return '麻煩您參考計中說明文件 http://cc.ncku.edu.tw/files/11-1255-14653.php?Lang=zh-tw'

    #電腦教室開放時間
    if '電腦' in message_text or '教室' in message_text or '中心' in message_text :
        return '電腦教室相關訊息請參考 http://cc.ncku.edu.tw/files/11-1255-3303.php?Lang=zh-tw ，謝謝。'

    #dorm
    if '宿網' in message_text or '宿舍網路' in message_text :
        if 'p2p' in message_text :
            return '因使用P2P有侵權問題, 本校校園網路禁止使用P2P, 故本校宿網亦禁止使用P2P, 除非是特殊學術用途之使用, 可另行申請.🙂'
        if '故障' in message_text or '網路孔' in message_text:
            return '若確認網路有故障，麻煩至http://dorm.cc.ncku.edu.tw/ 進行使用者登入後進行故障申告，會由工程師為你處理，請耐心等候🙂'
        if 'authentication failed' in message_text :
            return '出現 "Authentication failed." 訊息, 有二種可能: \n1. 帳號或密碼輸入錯誤，請重新輸入再試一下。若不確定是否正確，可借室友電腦登入宿網管理系統看看。 \n2. 帳號被停用，登入宿網管理系統，查詢登錄資料，若被停用，在最後一項”特殊限制”中，會註明停用原因。'
        if '不通' in message_text or '不能' in message_text or '斷' in message_text or '認證' in message_text or '連' in message_text or '無法' in message_text or '問題' in message_text:
            faq = template_json.Template_json(sender_id,template_type=2,
                   text="是否曾申請過帳號呢? (請用是/否按扭回答以便記錄)", payload_yes = "START_STATE_YES", payload_no = "START_STATE_NO" )
            return faq

        return '請參考宿網管理系統FAQ http://dorm.cc.ncku.edu.tw/ '

    if '資安' in message_text :
        return '若您需要填寫資安通報，可以先從 https://goo.gl/YzegaO 這裡下載通報檔案，填寫完後直接回傳至security@mail.ncku.edu.tw 這個信箱，或是繳交紙本到計網中心一樓🙂'

    # if len(ip) > 0 :
        # data = {}
        # data['ip'] = unicode(ip[0])
        # data['mac'] = u'xx:xx:xx:xx:xx:xx nothing here'
        # url_values = urllib.urlencode(data)
        # print(url_values)
        # full_url = 'https://script.google.com/macros/s/AKfycbwdyCdon5MQYAz-U-WbP-EVgvymqnx5-k9AHDVBd2ZJ1CgShto/exec' + '?' + unicode(url_values)
        #
        # response = urllib.urlopen(full_url).read()
        # print(response)
        # if response == 'found!':
        #     return '您的網路位置IP被暫停使用 請聯絡計網中心 😨 聯絡方式：（06）2757575 ext.61010'
        # else : return '您的網路位置IP不在鎖網名單中，並非被暫停使用，請留下資料將有專人為您服務🙂'



    #授權軟體
    if '啟動' in message_text or '啟用' in message_text or '認證' in message_text :
        if '如何' in message_text or '怎麼' in message_text or '想' in message_text or '要' in message_text :
            return '您好🙂  windows或office需至校園授權軟體網頁下載啟用檔，若您在學校以外的網路,啟用授權軟體時必須先啟動vpn,才能進行產品認證 http://cc.ncku.edu.tw/files/11-1255-7637-1.php?Lang=zh-tw \n\n**若需要vpn連線教學請輸入「vpn教學」，謝謝:)'
        if '無法' in message_text or '失敗' in message_text or '不' in message_text :
            return '您好🙂  若無法啟用，請確認是否已連線校內網路：google 「IP 查詢」→進第一個連結。確認IP為成大IP(140.116.XXX.XXX)。\n若已連線校內網路，請問您的錯誤代碼error code為何?(小黑框裡倒數幾行，類似0xC...，若非一般常見錯誤代碼請等待專人協助或於中心二樓服務台服務時間內攜帶筆電前往詢問)。\n若未連線至校內網路，請使用vpn服務連線至校內網路再作啟用。http://cc.ncku.edu.tw/files/11-1255-7637.php?Lang=zh-tw\n\n**若需要vpn連線教學請輸入「vpn教學」，謝謝:)'
    if '0x80070005' in message_text :
        return '您好🙂  錯誤代碼:0x80070005，未使用系統管理員身份執行，請在啟用檔上按右鍵選擇"以系統管理員身份執行"。\n若按右鍵未出現"以系統管理員身份執行"選項，表示您尚未將下載的啟用壓縮檔解壓縮，請按右鍵解壓縮或是直接將內部檔案拉至桌面亦可，謝謝。'
    if '0xc004f074' in message_text :
        return '您好🙂  錯誤代碼:0xc004F074，1.請確認是否已連線校內網路。google 「IP 查詢」→進第一個連結。確認IP為成大IP(140.116.XXX.XXX)。\n2.請確認電腦右下角時間是否正確。(時區及時間上下午都要對，時區確定為台北+8:00，再使用網路同步時間。)\n3.若您ip已是成大140.116 上述兩項亦沒問題卻認證失敗，請嘗試使用vpn連線後再行認證。\n\n**若需要vpn連線教學請輸入「vpn教學」，謝謝:)'
    if 'script' in message_text :
        return '您好，找不到script可能是以下兩種情形\n1.啟用檔未解壓縮。若在檔案上按右鍵無"以系統管理員身份執行"選項，即可能未解壓縮，請按右鍵解壓縮或是直接將.bat檔拉至桌面亦可。\n2.啟用檔不符合軟體版本。若同一軟體有A.B兩種啟用檔，不知道用哪一個的話，可以兩個都下載下來解壓縮都啟用試試。\nhttp://www.cc.ncku.edu.tw/download/'
    if 'matlab' in message_text :
        if '下載' in message_text or '單機' in message_text :
            return '您好🙂  Matlab單機版不需使用校內網路認證，請前往Mathworks網站(www.mathworks.com)，使用"學校Email"及說明文件裡的cdkey申請一組帳號即可取得授權及下載。\n(以下網址需連線校內網路)\n詳細說明文件: ftp://140.116.249.78/Mathworks/MatlabR2016A/MATLAB_TAH_Single.pdf'
        if 'license' in message_text or 'network' in message_text :
            return '您好🙂  若需要license.dat或network.lic表示您目前選擇使用的matlab版本為校園網路版，可至http://www.cc.ncku.edu.tw/download/matlab.htm 下載校園網路版連線授權檔(注意事項第三及第四點擇一下載即可)。校園網路版使用時需連線至校內網路才能取得授權。\n若為個人使用建議您改用單機版，單機版使用時無在校內網路使用的限制。若想轉換至單機版請參考:\n(以下網址需連線校內網路)\nftp://140.116.249.78/Mathworks/MatlabR2016A/MATLAB_TAH_Single.pdf\n'
        if 'mac' in message_text or 'linux' in message_text :
            return '您好🙂  mac 或 linux版本可在申請單機版授權帳號後於matlab官網上登入下載。\n(以下網址需連線校內網路)\n詳細說明文件: ftp://140.116.249.78/Mathworks/MatlabR2016A/MATLAB_TAH_Single.pdf\nDetailed installation steps: ftp://140.116.249.78/Mathworks/MatlabR2016A/MATLAB_TAH_Single_En.pdf\nhttp://www.cc.ncku.edu.tw/download/matlab.htm'
    if 'visual studio' in message_text :
        return '您好🙂  1.visual studio 無限制校內網路，安裝完即可使用。\n2.2013版前無需輸入序號，但2015版需要輸入序號:7DHGB-NW9XQ-Q9GT6-BMGMC-GQ7XY。\nhttp://www.cc.ncku.edu.tw/download/key.htm\n3.2013版可在成大mybox下載(無需校內網路)。'
    if '網頁' in message_text :
        if 'forbidden' in message_text or 'access denied' in message_text or 'vpn' in message_text or '校外' in message_text or '拒絕顯示' in message_text or '不能下載' in message_text or '無法下載' in message_text or '壞' in message_text :
            return '您好🙂  1.請在網路和共用中心的網際網路中IP和DNA皆設定為自動取得，並從新開啟瀏覽器\n2.若無法進入校園授權軟體網頁，請使用vpn服務連線。\n3.若網頁打得開卻無法下載，可能只是打開網頁的暫存檔，同樣需使用vpn服務連線才能下載。\n\n**若需要vpn連線教學請輸入「vpn教學」，謝謝:)'
        if '開' in message_text or '進' in message_text :
            if '不' in message_text :
                return '您好🙂  1.若無法進入校園授權軟體網頁，請使用vpn服務連線。\n2.若網頁打得開卻無法下載，可能只是打開網頁的暫存檔，同樣需使用vpn服務連線才能下載。\n\n**若需要vpn連線教學請輸入「vpn教學」，謝謝~'
    if 'vpn' in message_text :
        if '安裝' in message_text or '下載' in message_text or '用' in message_text :
            return '您好🙂  請參考http://cc.ncku.edu.tw/files/11-1255-7637.php?Lang=zh-tw 的使用說明'
        if '連' in message_text or '卡' in message_text :
            return '您好🙂  如您是使用網頁版請到http://cc.ncku.edu.tw/files/11-1255-7637.php?Lang=zh-tw 下載連線軟體使用，並參考使用說明進行安裝及連線；若您是使用連線軟體，請先參考http://cc.ncku.edu.tw/files/11-1255-7637.php?Lang=zh-tw 的使用說明，並特別注意VPN使用完畢請登出以免影響下一次登入'
        if '教學' in message_text or '如何' in message_text or '怎麼' in message_text :
            return '您好🙂  1.開啟http://cc.ncku.edu.tw/files/11-1255-7637-1.php?Lang=zh-tw\n2.下載ssl vpn連線軟體，解壓縮後安裝。\n3.程式集→執行Juniper Network/Network Connect.exe。\n4.輸入登入網址：https://sslvpn9.twaren.net/ncku →執行。\n5.輸入成大信箱/入口帳密。登入後右下角圖示顯示已連線。\n6.確認ip檢查是否連線成功:google 「IP 查詢」→進第一個連結。確認IP為成大IP(140.116.XXX.XXX)。'

    if '軟體' in message_text or 'win' in message_text or 'office' in message_text :
        if '借' in message_text or '光碟' in message_text:
            return '您好🙂  若需要校園授權軟體可參考 http://cc.ncku.edu.tw/files/11-1255-6834-1.php?Lang=zh-tw 或是可以於計網中心服務時間帶一張證件至２樓借用光碟'
        if '下載' in message_text :
            return '您好🙂  校園授權軟體下載有兩種方式:\n1.校園授權網頁下載(需連線校內網路) http://cc.ncku.edu.tw/files/11-1255-6834-1.php?Lang=zh-tw\n2.成功大學mybox(校外網路可下載，但若需要進行啟用授權步驟仍得連進校內網路才能成功啟用，第一次使用mybox需開通。) https://mybox.ncku.edu.tw/ 登入後左邊"共用資料夾"可下載。'
        if '金鑰' in message_text or '過期' in message_text :
            return '您好🙂  windows及office皆為校內網路授權，授權一次為180天，若一直在校外網路待授權期限一到便會出現過期訊息，請連線至校內網路(可使用vpn連回)並重新執行啟用檔再次取得180天授權即可，謝謝。\n校園授權軟體網頁:http://cc.ncku.edu.tw/files/11-1255-6834-1.php?Lang=zh-tw\nssl vpn: http://cc.ncku.edu.tw/files/11-1255-7637.php?Lang=zh-tw\n\n**若需要vpn連線教學請輸入「vpn教學」，謝謝:)'
        return '您好🙂  請參考 http://cc.ncku.edu.tw/files/11-1255-6834-1.php?Lang=zh-tw ，謝謝。'

#=====================================================================


    #選課
    if '選課' in message_text :
        if '無法' in message_text or '忘' in message_text or '登' in message_text :
            return '您好🙂  選課系統與成功入口帳號密碼是一樣的，請先試登入成功入口到右上方設定做密碼變更，若成功入口也沒有辦法登入，則需要修改成功入口密碼,請攜帶雙證件(學生證以及身分證)於上班時間到計算機中心一樓服務台,做更改密碼之服務。'

    #moodle
    if 'moodle' in message_text :
        if '無法' in message_text or '忘' in message_text or '登' in message_text :
            return '您好🙂  moodle系統與成功入口帳號密碼是一樣的，請先試登入成功入口到右上方設定做密碼變更，若成功入口也沒有辦法登入，則需要修改成功入口密碼,請攜帶雙證件(學生證以及身分證)於上班時間到計算機中心一樓服務台,做更改密碼之服務。'


    #成功入口
    if '成功入口' in message_text :
        if '改' in message_text or '無法' in message_text or '忘' in message_text or '登' in message_text :
            return '您好🙂  若您是在校學生:若需要修改成功入口密碼,請攜帶雙證件(學生證以及身分證)於上班時間到計算機中心一樓服務台,做更改密碼之服務。\n若您已是畢業生:成功入口僅服務在校學生，故學生畢業後，成功入口帳號即停用。'

    #mybox
    if 'mybox' in message_text :
        return '您好🙂  若無法連結mybox，可能是mybox帳號尚未開通，請先到mybox系統 (http://mybox.ncku.edu.tw) 啟用你的mybox帳號'

    #畢業
    if '畢業' in message_text :
        return '您好🙂  成功入口僅服務在校學生，故學生畢業後，成功入口帳號即停用。個人mail帳號，則於畢業6個月後停用，而E-portfolio數位學習歷程檔可由該系統原網址登入使用。'

    #成績
    if '成績' in message_text :
        return '您好🙂  請由成功入口進去後，E-portfolio數位學習歷程檔裡就有成績查詢的選項 ， 或由註冊組網頁連到成績查詢網頁。( 註冊組 -> 線上服務 -> 學生 -> 成績查詢 )'


    #閒聊  字數不能太多

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
