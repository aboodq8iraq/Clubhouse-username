import requests
import random
from time import sleep
count = int(input("Enter Number Username (2,3,4) - > > "))
while True:
    username=''.join(random.choice("abcdefghijklmnopqrstwxyz1234567890") for i in range(count))
    r = requests.get(f"https://clubhouse.com/@{username}",headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    if r.status_code==200:
        print(f"This is Username isn't Avaliable - > {username}")
    elif r.status_code==404:
        print(f"Nice! it's Avaliable  - > {username}")
    else:
        print("There was an error!!")
    sleep(1)
     
