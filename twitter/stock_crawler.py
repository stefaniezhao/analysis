import os, urllib, urllib2, sys, time

def crawl_stock_realtime_data():
    nowTime = time.localtime()
    nowStr = time.strftime('%Y-%m-%d %H:%M:%S', nowTime)
        
    req=urllib2.Request(crawl_url)
    sock=urllib2.urlopen(req)
    data = sock.read()
    company_name, stock_name, current_price, open_price, last_close_price = data.split(",")
    f.write(nowStr + "\t" + current_price + "\t" + open_price + "\t" + last_close_price + "\n")

BASE_FOLDER = "/home/stefaniezhao/development/python/twitter/"
crawl_url = "http://download.finance.yahoo.com/d/quotes.csv?s=IBM&f=nsl1op&e=.csv"
filename = BASE_FOLDER + "stock_data.txt"
f=open(filename, 'w', 5)
f.write("time\t\t\tprice\topen\tclose\n");
crawl_stock_realtime_data()
f.close()


