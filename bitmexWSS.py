from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep

LastBitmex = "     Waiting for BitMEX...             "

def run():
    logger = setup_logger()

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="wss://ws.bitmex.com/realtime", symbol="XRPUSD",
                         api_key=None, api_secret=None)

    #logger.info("Instrument data: %s" % ws.get_instrument())

    ws.get_instrument()['symbol']
    logging.info("The BitMEX Funding Rate is " + str(ws.get_instrument()['fundingRate']))
    logging.info("The BitMEX Indicative Funding Rate (for the Funding after next) is " + str(ws.get_instrument()['fundingRate']))

    # Run forever
    while(ws.ws.sock.connected):
        #logger.info("BitMEX Ticker: %s" % ws.get_ticker())
        #logger.info("BitMEX  BUY = " + str(ws.get_ticker()['buy']) + " SELL = " +  str(ws.get_ticker()['sell']))
        #print("BitMEX  BUY = " + str(ws.get_ticker()['buy']) + " SELL = " +  str(ws.get_ticker()['sell']) , end = "\r" )
        
        global LastBitmex
        LastBitmex = ("BitMEX BUY = " + str(ws.get_ticker()['buy']) + " SELL = " +  str(ws.get_ticker()['sell']))

        if ws.api_key:
            logger.info("BitMEX Funds: %s" % ws.funds())

        #sleep(1)

def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
