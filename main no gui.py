import bitmexWSS, binanceWSS
import threading
import sys
import logging
import time
import tkinter as tk
from tkinter import messagebox, ttk


#TODO: make bitmex and binance websocket py files and start both OKDONE

#T1 is the Bitmex thread
T1 = threading.Thread(target=bitmexWSS.run)
T1.start()

#T2 is the Binance thread
T2 = threading.Thread(target=binanceWSS.run)
T2.start()

logging.info("Both BitMEX and Binance Threads started...")

def start_everything():
    try:
        while True:
            print("XRPUSD: " + str(bitmexWSS.LastBitmex) + " | " + str(binanceWSS.LastBinance) , end = "\r" )
            time.sleep(0.2)
    except Exception as e:
        print(e)

T3 = threading.Thread(target=start_everything)
T3.start()

#Join BitMEX and Binance Listeners
T1.join()
T2.join()

#TODO: if time is <2 minutes until BitMEX funding, should start both bitmex and binance wss

#TODO: store the last price in a value, will need this price to open positions on both bitmex and binance

#TODO: calculate the stop loss and take profit prices for the bitmex position, and then also store this in a value

#TODO: the binance position will have the Bitmex values swapped, ie the Binance stop is the bitmex take profit and vice versa

#TODO: wait until after funding finished. Take the average of the bitmex price and binance price, and exit both positions at this price

#TODO: wait 30 seconds and check if both positions out. If everything done, then print success and quit
