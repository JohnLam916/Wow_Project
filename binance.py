from binance.websockets import BinanceSocketManager

client = Client('8BPotKLSrytB6XAQttvjqK8CXCBv2V0n5n1chP8tr37gikNvVpFYHRoeeh3Zx7gs', 'vxCDidOeUnZZi78ZvnKhOSPnUtm89mchSiqtQ8DBNDhfyQOCVCurZYhuh4fZtvKK')

bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
# then start the socket manager
bm.start()

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
