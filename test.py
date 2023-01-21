from binance.client import Client
api_key     = '1ai21UuBuezHm6KqlUVfsS0SnCQRBtTIURdE3rRikRslQWgFAQgApuI7FvkXAC8V'
api_secret  = '5zD2IiRHpZQ4b9SD6vwfxnYKDCu80Z478ae6uGa64vYBDTI8YLQpYQiibqrOSyf6'
client      = Client(api_key, api_secret)
# info = client.get_account()
# print(info)
# balance = client.get_asset_balance(asset='BTC')
# print(balance)
# # info = client.get_symbol_info('BNBBTC')
# # print(info)
# # status = client.get_account_status()
# # print(status)
# trades = client.get_my_trades(symbol='BNBBTC')
# print(trades)
info = client.get_margin_account()
print(info)