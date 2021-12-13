import time
import logging
from time import sleep

from binance import ThreadedWebsocketManager

api_key = None
api_secret = None

LastBinance = "      Waiting for Binance...      "

def run():
    symbol = 'XRPUSD'

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    twm.start()


    def handle_socket_message(msg):
        #print(f"message type: {msg['e']}")
        #print(msg['data'])
        #logging.info("Binance BUY = "+ str(round(float(msg['data']['b']),4)) + " SELL = " + str(round(float(msg['data']['a']),4)) )

        #print("Binance BUY = "+ str(round(float(msg['data']['b']),4)) + " SELL = " + str(round(float(msg['data']['a']),4)) , end = "\r" )
        global LastBinance
        LastBinance = ("Binance BUY = "+ str(round(float(msg['data']['b']),4)) + " SELL = " + str(round(float(msg['data']['a']),4)) )

        #time.sleep(1)


    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['xrpusdt@bookTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()


