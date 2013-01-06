import twitter
import json
import cPickle
import nltk
import re
import networkx as nx
import sys

def encode(s):
    if isinstance(s, unicode): 
        return s.encode('gb2312') 
    else: 
        return s.decode('utf-8').encode('gb2312')

def get_rt_sources(tweet):
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
    return [source.strip()[1:]
            for tuple in rt_patterns.findall(tweet)
                for source in tuple
                    if source not in ("RT", "via")]
 

def analysis_network(search_results, word):
    g = nx.DiGraph()
    all_tweets = [tweet
        for page in search_results
            for tweet in page["results"]]
    
    for tweet in all_tweets:
        rt_sources = get_rt_sources(tweet["text"])
        if not rt_sources: continue
        for rt_source in rt_sources:
            g.add_edge(rt_source, tweet["from_user"],{"tweet_id":tweet["id"]})
    print g.number_of_nodes()
    print g.number_of_edges()

    try:
        nx.drawing.write_dot(g, "tweet_network_"+ word.strip()+".dot")
    except:
        print "Unexpected error:", sys.exc_info()[0]

def download_twitter_data(word):

    twitter_search = twitter.Twitter(domain="search.twitter.com")
    search_results = []
    try:
        for page in range(1,6):
            search_results.append(twitter_search.search(q=word, rpp=100, page=page, lang='en',result_type="recent"))
        #print json.dumps(search_results, sort_keys=True, indent=1)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        
    f=open("twitter_r_"+ word.strip()+".json.txt", 'w', 5)
    f.write(json.dumps(search_results, sort_keys=True, indent=1))
    f.close()
    
    tweets = [r['text']\
          for result in search_results \
              for r in result['results']]
    print tweets
    f=open("twitter_r_"+ word.strip()+".tweets.txt", 'w', 5)
    for tweet in tweets:
        try:
            f.write(tweet + "\n")
        except:
            print "Unexpected error:", sys.exc_info()[0]
    f.close()

    analysis_network(search_results, word)
    

    words = []
    for t in tweets:
        words += [w for w in t.split()]

    print len(words)
    print len(set(words))
    print 1.0*len(set(words))/len(words)
    print 1.0*sum([len(t.split()) for t in tweets])/len(tweets)

    f = open("twitter_r.word_"+ word.strip()+".pickle", "wb")
    cPickle.dump(words, f)
    f.close()

def analysis_words(filename):
    words = cPickle.load(open(filename))
    freq_dist = nltk.FreqDist(words)
    print "50 most frequent tokens"
    print freq_dist.keys()[:50]
    print "50 least frequent tokens"
    print freq_dist.keys()[-50:]

def analysis_network_sample():
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
    example_tweets = ["RT @BookOfComedy: iPhone + iPad + iMac + iPod = iBroke",
                      "RT @JimCarrey: I'm sick of new Apple icrap! Gee, ihope the new ipad isn't so thin that my finger breaks through when iwipe my APPLE OWNED ASS WITH IT!  8^Q",
                      "Apple debuts iPad mini, moving to dominate mobile-optimised advertising http://t.co/WMt6ZL0N via @Tnooz/@sean_oneill"]
    for t in example_tweets:
        print rt_patterns.findall(t)



#download_twitter_data("Big Bang")
analysis_words("twitter_r.word_Big Bang.pickle")
