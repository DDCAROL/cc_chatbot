# Facebook Messenger Bot
This is a simple python template that uses Flask to build a webhook for Facebook's Messenger Bot API.

[my reference](https://blog.hartleybrody.com/fb-messenger-bot/)

# FSM

[my fsm picture](https://raw.githubusercontent.com/DDCAROL/cc_chatbot/master/pic.png)


# How to Run & Interact with My Chatbot
Basic Chatbot Deploy: Heroku

mac終端機指令:

  1. heroku login
  2. git init
  3. heroku git:remote -a cryptic-ravine-2726
  4. git commit -am "chatbot haha"
  5. git push heroku master
  
聊天機器人:

  我做的是一個打屁機器人，只要和它說話都會回答。但主要要用這幾句話，才會開始回應有內容：「嗨」、「配對女友」、「天氣」，不然其他都是回應一樣的。
