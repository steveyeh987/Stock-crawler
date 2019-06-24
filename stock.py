import sys
import twstock
import time
import requests

def get_max_stock_price(stock_id):
    counterline = 1
    countererror = 1
    current_maxprice = 0
    stock_id = str(stock_id)
    
    print("Executing...")
    while True:
        realdata = twstock.realtime.get(stock_id)
        if realdata['success']:
            realprice = float(realdata['realtime']['latest_trade_price'])
            
            if realprice > current_maxprice:
                print("Stock {}: price improve from {} to {}".format(stock_id, current_maxprice, realprice))
                url_ifttt = 'https://maker.ifttt.com/trigger/stock/with/key/c65-toVUcOtIsGa5AnZe_g?value1={}&value2={}&value3={}'.format(stock_id, current_maxprice, realprice)
                resl = requests.get(url_ifttt)
                print("The {}th line message: {}".format(counterline, resl.text))
                current_maxprice = realprice
                counterline = counterline + 1
                
            if counterline > 3:
                print("Ending...")
                break
                
        else:
            print("twstock executing error: ", realdata['rtmessage'])
            if counterror > 3:
                print("Ending...")
                break
            countererror = countererror +1
        for i in range(300):
            time.sleep(300)

if __name__ == '__main__':
    get_max_stock_price(sys.argv[1])
