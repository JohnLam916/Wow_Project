import config, csv

from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)

#Once we have successfully built a bot, we will want to do some backtesting on our bot to see if the parameters we set it will be successful. In order to do some back testing on the bot, we will need to create a way to store data we stream from binance in order to do some backtesting on the bot. 

#streaming the historical data from 2017 - 2021 for etherum in daily candle stick intervals. Ticker symbols must end with T after specifying crypto currency and in what type of currency like American dollar, pound etc...

historical_candles = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "1 Mar, 2021")

# determine how many days of data is retrieved from binance
print(len(historical_candles))

#Opens a file for writing our data, we named our file "Historical_candles.csv" 
csvfile = open('Historical_candles.csv', 'w', newline='')

#gives us the ability to write a row and gives a reference to our file called "csvfile", giving it a delimiter with a comma. A delimiter is one or more characters that separate text strings
Candlestick_writer = csv.writer(csvfile, delimiter=',')

#separates the return data into individual rows
for candlestick in historical_candles:
    print(candlestick)

#We will pass the entire list to .writerow and it will convert it into a csv file
    Candlestick_writer.writerow(candlestick)

print(len(candlestick))