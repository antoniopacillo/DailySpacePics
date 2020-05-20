import telepot, requests, datetime, time
from credenziali import *

telegrambot = telepot.Bot(token)
chat_id = canale

while True:
    daily_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    request = requests.get(daily_url)
    req_json = request.json()
    daily_pic = req_json['url']
    daily_caption = req_json['date']+" ~ "+req_json['title']+" ~ Copyright: "+req_json['copyright']+"\n"+req_json['explanation']
    ora = datetime.datetime.now().time()
    invio = ora.replace(hour = 7, minute = 0, microsecond = 0)
    if ora == invio:
        telegrambot.sendPhoto(chat_id, daily_pic, daily_caption)
    time.sleep(2)