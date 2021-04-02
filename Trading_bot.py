import websocket

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    print("recieved message")
    print(message)

ws = websocket.WebSocketApp(SOCKET, on_open = on_open, on_close = on_close, on_message = on_message ) 
ws.run_forever()


'''
from binance.enums import *
from binance.client import Client

RSI_PERIOD = 14
OVERSOLD_THRESHOLD = 30
OVERBOUGHT_THRESHOLD = 70
TRADE_QUANTITY = 0.005
TRADE_SYMBOL = 'ETHUSD'
SOCKET = 

closes = []
in_position = False
client = Client(config.API_KEY, config.API_SECRET, tld='us')
'''