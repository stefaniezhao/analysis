import cPickle, nltk, sys
import json, math
import numpy as np
from optparse import OptionParser
from nltk.corpus import stopwords
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

def analysis_words(words, id_list, file):
    print file
    f = open(file)
    try:
        tweets = json.loads(f.read())
        for tweet in tweets[0]['results']:
            id = tweet['id']
            #print id
            if id in id_list: continue
            else:
                id_list.add(id)
                text = tweet['text']
                #print text
                words += [w for w in text.split()]
    except:
        print "Unexpected error:", sys.exc_info()[0]
        
def loadFile():
    parser = OptionParser(usage='usage: %prog [options] input_file')
    parser.add_option('-l', '--language_file', dest='language',
    help='Foreign language lexical file. This file should map\
                words to their lemmas', metavar='LANGUAGE_FILE')
    (options, args) = parser.parse_args()

    reader = open(args[0])
    all_files = reader.read().splitlines()
    words = []
    id_list=set([])
    for f in all_files:
        analysis_words(words, id_list, f)
    
    print len(words)
    print len(set(words))
    print 1.0*len(set(words))/len(words)

    word_file = open("twitter.stock.word.pickle", "wb")
    cPickle.dump(words, word_file)
    word_file.close()
    analysis_using_FreqDist(words)

def draw_tag_cloud(words, filename, size):
    tags = make_tags(words, maxsize=size)
    create_tag_image(tags, filename, size=(900, 600), background=(0, 0, 0))

def loadFromPickle(file, tag_file, size):
    words = cPickle.load(open(file))
    words = [w.lower() for w in words if w.isalpha()]
    #print "with stopword"
    #print "word num: " + str(len(set(words)))
    #analysis_using_FreqDist(words)

    print "without stopword"
    clean_words = remove_stopword(words)
    print "word num: " + str(len(set(clean_words)))
    top_words = analysis_using_FreqDist(clean_words)
    print top_words
    top_words_log = [(word, math.floor(np.log(freq*10))) for (word, freq) in top_words]
    #for item in top_words:
      #  print item[1]
    print top_words_log

    draw_tag_cloud(top_words_log, tag_file, size)
    
    #find_collocations(words)

def analysis_using_FreqDist(words):
    freq_dist = nltk.FreqDist(words)
    print "100 most frequent words"
    print freq_dist.keys()[:100]
    #print "50 least frequent tokens"
    #print freq_dist.keys()[-50:]
    #freq_dist.plot(50)
    
    #long_words = [w for w in words if len(w) > 5 and len(w)< 13]
    #freq_dist = nltk.FreqDist(long_words)
    #print "100 most frequent long words"
    #print freq_dist.keys()[:100]

    return freq_dist.items()[:100]
    

def remove_stopword(words):
    clean_words = [w for w in words if w not in stopwords.words('english') ]
    return clean_words

def find_collocations(words):
    english_words = [w.encode(encoding='UTF-8',errors='strict') for w in words]
    text = nltk.Text(english_words)
    print text.collocations()



def analysis():
    print "analysis IBM related twitter"
    file = "twitter.ibm.word.pickle"
    tag_file="twitter.ibm.word.tag.png"
    loadFromPickle(file, tag_file, 23)

    print "analysis IBM stock related twitter"
    file = "twitter.stock.word.pickle"
    tag_file="twitter.stock.word.tag.png"
    loadFromPickle(file, tag_file, 27)

analysis()
    

