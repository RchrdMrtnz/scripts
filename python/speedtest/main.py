import requests
import time

start=time.time()

def timer():
    response=requests.get('https://google.com')
    if response.status_code==200:
        end=time.time()
        final=end-start
        print(f'{final:.2f}')
    else:
        print('404')


if __name__ == "__main__":
    timer()
