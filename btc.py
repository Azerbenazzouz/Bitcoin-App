import requests
import json
import time
import datetime
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *


app=QApplication([])
fen=loadUi("btc.ui")
fen.show()
#while True :

def price():
    responseu = requests.get(f"https://api.coinbase.com/v2/prices/BTC-USD/spot")
    datau = responseu.json()
    priceu = datau["data"]["amount"]
    #TND
    responset = requests.get(f"https://api.coinbase.com/v2/prices/BTC-TND/spot")
    datat = responset.json()
    pricet = datat["data"]["amount"]
    #euro
    responsee = requests.get(f"https://api.coinbase.com/v2/prices/BTC-EUR/spot")
    datae = responsee.json()
    pricee = datae["data"]["amount"]
    fen.usd.setText(str(priceu))
    fen.tnd.setText(str(pricet))
    fen.euro.setText(str(pricee))
    fen.time.setText(str(datetime.datetime.now()))
#time.sleep(5)
#fen.coin.setCurrentIndex(0)
fen.time.setText(str(datetime.datetime.now()))
price()
fen.ref.clicked.connect(price)
app.exec_()
