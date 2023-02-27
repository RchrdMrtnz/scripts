import requests 
import time

def weather():
    try:
        response=requests.get('https://wttr.in/Tachira?format=%l:+%t+\nPresipitation:+%p+\nHumidity:+%h\nWinds:+%w')
        if response.status_code==200:
            print(response.text)
        else:
           print('404')

    except:
        print('500')


if __name__ == "__main__":
    weather()
