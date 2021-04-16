import websocket

#channel that provides the data that we want, along with specifying the type of coin we're tracking and type of indicator we are using and at what time interval
streaming_data = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print("Opened Connection")

def on_closed(ws):
    print("Closed Connection")

def on_message(ws , message):
    print("recieved message")
    print(message)
#create a variable that will listen in on the stream, requires call back function which it provides.  
ws = websocket.WebSocketApp(streaming_data, on_open= on_open, on_close= on_closed, on_message= on_message)

ws.run_forever()