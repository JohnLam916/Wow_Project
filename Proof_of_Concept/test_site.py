from binance.client import Client
import Platform_Access 

#test key and secret
api_key = "kp1BEut4wlcicOggZeunzYArlqG7iNdpHnQv2c47l4fDWUJcYh9dCkPnZVRTy4Yx"
api_secret = "Q8TGBPO2IamjlwnhtUKVXCsWZyQXuwOkyLHWyrfhFFQG39WBemHywpozupWu125r"

client = Client(api_key, api_secret)

client.API_URL = 'https://testnet.binance.vision/api'

print(client.get_account())