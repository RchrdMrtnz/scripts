import requests
import time


def timer():
    try:
        start=time.time()
        response=requests.get('https://google.com')
        if response.status_code==200:
           end=time.time()
           final=(end-start)*100
           print(f'{final:.2f}ms')
        else:
           print('404')

    except:
        print('500')


if __name__ == "__main__":
    timer()
