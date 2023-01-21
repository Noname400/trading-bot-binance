live_trade = False

coin     = ["ETH"]
quantity = [0.002]
deposit_currency = ['BTC']
percent = [10]

leverage, pair = [], []

for i in range(len(coin)):
    pair.append(coin[i] + "USDT")
    if   coin[i] == "BTC": leverage.append(40)
    elif coin[i] == "ETH": leverage.append(30)
    else: leverage.append(20)

    print("Pair Name        :   " + pair[i])
    print("Trade Quantity   :   " + str(quantity[i]) + " " + coin[i])
    print("Leverage         :   " + str(leverage[i]))
    print("Deposit currency :   " + str(deposit_currency[i]))
    print("Percent          :   " + str(percent[i]))
    print()
