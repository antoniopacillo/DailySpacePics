import telepot, requests, datetime, time
from credenziali import *

telegrambot = telepot.Bot(token)
chat_id = canale
daily_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
request = requests.get(daily_url)
req_json = request.json()

while True:
    ora = datetime.datetime.now().time()
    invio = ora.replace(hour = 9, minute = 30, second = 0)
    if ora == invio:
        daily_pic = req_json['url']
        if len(req_json['date']+" ~ "+req_json['title']+" ~ Copyright: "+req_json['copyright']+"\n"+req_json['explanation']) > 1024:
            daily_caption = req_json['date']+" ~ "+req_json['title']+" ~ Copyright: "+req_json['copyright']
            description = req_json['explanation']
            telegrambot.sendPhoto(chat_id, daily_pic, daily_caption)
            telegrambot.sendMessage(chat_id, description)
        else:
            daily_caption = req_json['date']+" ~ "+req_json['title']+" ~ Copyright: "+req_json['copyright']+"\n"+req_json['explanation']
            telegrambot.sendPhoto(chat_id, daily_pic, daily_caption)
    time.sleep(1)
