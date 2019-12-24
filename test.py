import json
import time
import config
import requests

beginning_of_time = time.time()
BASE_URL = "https://paper-api.alpaca.markets"
HEADERS = {'APCA-API-KEY-ID': config.API_KEY, 'APCA-API-SECRET-KEY': config.SECRET_KEY}
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
POSITIONS_URL = "{}/v2/positions".format(BASE_URL)


def place_order(symbol, qty, side, type, time_in_force):
    stock_data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    response = requests.post(ORDERS_URL, json=stock_data, headers=HEADERS)
    return json.loads(response.content)


def limit_order(symbol, qty, side, type, time_in_force, limit_price):
    stock_data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force,
        "limit_price": limit_price
    }
    response = requests.post(ORDERS_URL, json=stock_data, headers=HEADERS)
    return json.loads(response.content)


def getAPosition(symbol):
    response = requests.get(POSITIONS_URL+"/"+symbol, headers=HEADERS)
    return json.loads(response.content)


def getAllPositions():
    response = requests.get(POSITIONS_URL, headers=HEADERS)
    return json.loads(response.content)


def getAllOrders():
    response = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(response.content)


def getAOrder(symbol):
    response = requests.get(ORDERS_URL+"/"+symbol, headers=HEADERS)
    return json.loads(response.content)


#for i in range (30):
#    limit_order("VKTX", i, "buy", "limit", "day", 7)

print(getAOrder("AAPL"))


time_elapsed = round(time.time() - beginning_of_time, 3)
print(time_elapsed)
