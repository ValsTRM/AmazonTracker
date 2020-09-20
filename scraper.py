import requests
#you use Beautiful soup to scrape through the amazon's html file and moving it over the python file
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
from playsound import playsound
headers = {
    
   "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

#User Inputs amazon's url
URL = input("What item would you like to buy? Paste URL for Amazon item here: ")
#Getting data from amazon bring the data and puts it into code
response = requests.get(URL, headers=headers).content
#is reading through the html of the amazon link
soup = BeautifulSoup(response, 'html.parser')
#User inputs price that he wants to have for the item
def check_price():
    userinput= int(input("What is the target price you want?: "))
     #get the title of the product
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    print("Product name & specs : ", title.strip())
    print("Product cost:",price)
    #compares target price with current price
    newprice = Decimal(sub(r'[^\d.]', '', price))
    if float(newprice) <= userinput:
        print("You can afford it!")
        playsound('ding-sound-effect_2.mp3')
        return False
    else:
        diff1 = float(newprice) - userinput
        diff_str = "You still need " + "$" + str(diff1) + " to buy it"
        print(diff_str)
        return True


check_price()
can_afford = True
while can_afford:
    can_afford = check_price()