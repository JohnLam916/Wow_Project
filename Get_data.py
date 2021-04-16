import config, csv 
import json

from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

print(len(candles))

csvfile = open('15minute.csv', 'w', newline='')

candles_stick_writer = csv.writer(csvfile, delimiter=',')

for candlestick in candles:
    print(candlestick)

    candles_stick_writer.writerow(candlestick)
'''
prices = client.get_all_tickers()

print(prices)

for price in prices:
    print(price)

'''    