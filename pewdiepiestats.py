import requests
import json
import time
import matplotlib.pyplot as plt
import time
url = "https://www.googleapis.com/youtube/v3/channels/?forUsername=pewdiepie%20&part=statistics%20&key=AIzaSyARAcSE2302K1NVDZbTrytTLXfz1EjzfDE"

xar = [] 
while True:    
    response = requests.get(url)
    if response.ok:
        cont = json.loads(response.content)
        s = int(cont['items'][0]['statistics']['subscriberCount'])
        xar.append(s)
    time.sleep(0.3)
    str = "PewDiePie Subscribers - Live :%d" %(s)
    plt.title(str)
    plt.plot(xar)
    plt.pause(0.05)

plt.show()
