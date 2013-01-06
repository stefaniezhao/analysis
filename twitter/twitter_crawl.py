import os, urllib, urllib2, sys
import twitter
import json
import time, datetime
import threading

#os.environ["http_proxy"] = "http://hkce01.hk.ibm.com:80"
#proxy_handler=urllib2.ProxyHandler({'http':'http://hkce01.hk.ibm.com:80'})
#opener = urllib2.build_opener(proxy_handler)
#opener.addheaders = [('User-agent','Mozilla/5.0')]
#urllib2.install_opener(opener)
#req=urllib2.Request("http://search.twitter.com")
#sock=urllib2.urlopen(req)
#data=sock.read()
#print data
BASE_FOLDER = "/home/stefaniezhao/development/python/twitter/"
twitter_search = twitter.Twitter(domain="search.twitter.com")
crawl_url = "http://download.finance.yahoo.com/d/quotes.csv?s=IBM&f=nsl1op&e=.csv"
filename = BASE_FOLDER + "stock_data.txt"
f=open(filename, 'w', 5)
f.write("time\t\t\tprice\topen\tclose\n");

def crawl_twitter(word):
    try: 
        nowTime = time.localtime()
        nowStr = time.strftime('%Y-%m-%d %H:%M:%S', nowTime)

        filename = word + "/twitter-" + nowStr + ".txt"
        result_filepath = BASE_FOLDER + filename
        f=open(result_filepath, 'w', 5)
        search_results = []
        for page in range(1,2):
            search_results.append(twitter_search.search(q=word, rpp=100, page=page, lang="en", result_type="recent"))
        f.write(json.dumps(search_results, sort_keys=True, indent=1))
        print filename + " is created."
        f.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]

def crawl_stock_realtime_data():
    nowTime = time.localtime()
    nowStr = time.strftime('%Y-%m-%d %H:%M:%S', nowTime)
    try:
        req=urllib2.Request(crawl_url)
        sock=urllib2.urlopen(req)
        data = sock.read()
        company_name, stock_name, current_price, open_price, last_close_price = data.split(",")
        f.write(nowStr + "\t" + current_price + "\t" + open_price + "\t" + last_close_price + "\n")
        print nowStr + " stock data is saved"
    except:
        print "Unexpected error:", sys.exc_info()[0]

def crawl_thread():
    words = ["IBM", "$IBM"]  
    for word in words:
        crawl_twitter(word);
        #print word
    crawl_stock_realtime_data()


def run():
    crawl_thread()
    threading.Timer(300.0, run).start()

threading.Timer(1.0, run).start()

