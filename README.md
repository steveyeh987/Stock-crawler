# Stock crawler
Crawl the latest price of a stock and return the updated price using Python + IFTTT

# Requirements:  
- twstock
- [IFTTT settings](https://www.oxxostudio.tw/articles/201803/ifttt-line.html)

# Descriptions of scripts:  
By executing the script, it checks the price of your given stock_id every five minutes (you can decide the time range yourself by modifying time.sleep). If the lastest price is higher than the current highest price, then send a message to your line notify. The settings of line notify can refer to the above link (IFTTT).

- Execution:  
```
  python stock.py stock_id  
```
- Output:  
```
  Stock stock_id: price improve from current_highest_price to lastest_price  
```

An alternative is to schedulely executing the script by using linux command such as crontab.
