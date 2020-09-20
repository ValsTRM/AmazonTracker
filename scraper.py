import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
from playsound import playsound
headers = {
    #"User-Agent": input("Search your user agent on Google. Paste it here: ")
   "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


URL = input("What item would you like to buy? Paste URL for Amazon item here: ")
#URL="https://www.amazon.com/EVGA-GeForce-Gaming-Graphics-11G-P4-2487-KR/dp/B07KVKRLG2/ref=sr_1_3?dchild=1&keywords=rtx+2080ti&qid=1600548714&sr=8-3%27"

response = requests.get(URL, headers=headers).content

soup = BeautifulSoup(response, 'html.parser')

def check_price():
    userinput= int(input("What is the target price you want?: "))
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    print("Product name & specs : ", title.strip())
    print("Product cost:",price)
    newprice = Decimal(sub(r'[^\d.]', '', price))
    if float(newprice) <= userinput:
        print("You can afford it!")
        playsound('ding-sound-effect_2.mp3')
    else:
        diff1 = float(newprice) - userinput
        diff_str = "You still need " + "$" + str(diff1) + " to buy it"
        print(diff_str)


check_price()
can_afford = True
while can_afford:
    can_afford = check_price()