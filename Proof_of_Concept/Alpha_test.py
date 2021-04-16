import binance
import Platform_Access 

#Validating my client key and allow me to access Binance data stream
from binance.client import Client

#Allows me to make trades
from binance.enums import *

#validating my API KEY 

client = Client(Platform_Access.API_Key, Platform_Access.API_Secret, tld = 'us')

#testing whether my key is correct
avg_price = client.get_avg_price(symbol='ETHUSDT')

print(avg_price)

#Making a test trade

# try:

order = client.create_test_order(

        symbol='ETHUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=1,
        price= '2023')

print(f"You have successfully completed a test order: {order}")
account_info = client.get_account()
print(account_info)
# except binance.exceptions.BinanceAPIException as e:
#     if e.message == "Filter failure: PERCENT_PRICE":
#         print("please enter a correct answer")
#     print(e.status_code)
#     print(e.message)

# #get account info

# # info = client.get_account()

# # print(info)

# # #get asset details

# # details = client.get_asset_details()

# # print(details)


# details = client.get_asset_details()

# print(details)


# print(order)

# #place an order 
# order = client.create_order(
#     symbol='BNBBTC',
#     side=SIDE_BUY,
#     type=ORDER_TYPE_LIMIT,
#     timeInForce=TIME_IN_FORCE_GTC,
#     quantity= 1,
#     price='0.00001')

# #Place a limit order

# order = client.order_limit_buy(
#     symbol='BNBBTC',
#     quantity=100,
#     price='0.00001')

# order = client.order_limit_sell(
#     symbol='BNBBTC',
#     quantity=100,
#     price='0.00001')

# #Place a market order

# order = client.order_market_buy(
#     symbol='BNBBTC',
#     quantity=100)

# order = client.order_market_sell(
#     symbol='BNBBTC',
#     quantity=100)