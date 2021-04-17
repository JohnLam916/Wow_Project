
#numpy is faster for computing, optimization for speed, memory
import numpy 

# for technical analysis utilizes numpy arrays for data types: http://mrjbq7.github.io/ta-lib/index.html
import talib

# utilizing genfromtxt to set up a numpy array from a CSV file: https://intellipaat.com/community/9398/how-do-i-read-csv-data-into-a-record-array-in-numpy
from numpy import genfromtxt

# we can build up a numpy array of closing prices for ETHUSDT as a numpy array sequence and use TA-lib to operate on that sequence and apply all the built in functions that TA-lib has and perform calculations for us

my_data = genfromtxt('2017-2021_Ethereum_Historical_candles.csv', delimiter=',')

# for the purpose of running an RSI we will be only interested in the closing price of Ethereum which is in the fourth index value in the array

closing_price = my_data[:,4]

print(closing_price)

# #generates a list of random numbers 
# close = numpy.random.random(100)

# print(close)

# #Calculate a simple moving average of the close prices, this function also takes an additional parameter that allows you to define what day of moving average you want, by default it is set to 30:

# #A moving average (MA) is a stock indicator that is commonly used in technical analysis. A simple moving average (SMA) is a calculation that takes the arithmetic mean of a given set of prices over the specific number of days in the past; for example, over the previous 15, 30, 100, or 200 days.

# moving_average = talib.SMA(close, timeperiod = 10)

# print(moving_average)

rsi = talib.RSI(closing_price)

print(rsi)