import requests
import time


def timer():
    start=time.time()
    response=requests.get('https://8.8.8.8')
    if response.status_code==200:
        end=time.time()
        final=(end-start)*100
        print(f'{final:.2f}ms')
    else:
        print('404')


if __name__ == "__main__":
    timer()
