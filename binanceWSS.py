import time
import logging

from binance import ThreadedWebsocketManager

api_key = None
api_secret = None

LastBinance = "      Waiting for Binance...      "

def run():
    
    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    twm.start()

    def handle_socket_message(msg):
        #print(msg['data'])
        global LastBinance
        LastBinance = ("Binance BUY = "+ str(round(float(msg['data']['b']),4)) + " SELL = " + str(round(float(msg['data']['a']),4)) )
        #time.sleep(1) ; disabled to keep LastBinance very updated

    streams = ['xrpusdt@bookTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()


