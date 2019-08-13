REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = "DLqiA9OWC+jxteK7NemNm0RTK9zuESdGC2TaFBadF17v89eToc/8YAPvw+fMVOf3rgqYXbyb/nOSnyk2wMwK6GgTqC/Aha0wMndNxHdwa9mOegEdOosLT6KEbK5d9PXiFgY4W0QgzaJXmzTkGfCa9wdB04t89/1O/w1cDnyilFU="

def post_text(reply_token, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(ACCESS_TOKEN)
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
    }
    requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

    #res = requests.get('https://api.line.me/v2/bot/message/reply')
