import cPickle, nltk, sys
from optparse import OptionParser
from nltk.corpus import stopwords

def analysis_words(words, file):
    f = open(file)
    for line in f:
        words += [w for w in line.split()]

def processFile():
    parser = OptionParser(usage='usage: %prog [options] input_file')
    parser.add_option('-l', '--language_file', dest='language',
    help='Foreign language lexical file. This file should map\
                words to their lemmas', metavar='LANGUAGE_FILE')
    (options, args) = parser.parse_args()

    reader = open(args[0])
    all_files = reader.read().splitlines()
    words = []
    for f in all_files:
        analysis_words(words, f)
    
    print len(words)
    print len(set(words))
    print 1.0*len(set(words))/len(words)

    word_file = open("finance.word.pickle", "wb")
    cPickle.dump(words, word_file)
    word_file.close()
    analysis_using_FreqDist(words)

def loadFromPickle():
    words = cPickle.load(open("finance.word.pickle"))
    analysis_using_FreqDist(words)

def analysis_using_FreqDist(words):
    long_words = [w for w in words if len(w) > 5 and len(w)< 13]
    
    freq_dist = nltk.FreqDist(words)
    print "100 most frequent words"
    print freq_dist.keys()[:200]
    #print "50 least frequent tokens"
    #print freq_dist.keys()[-50:]

    freq_dist = nltk.FreqDist(long_words)
    print "100 most frequent long words"
    print freq_dist.keys()[:200]

    clean_words = [w for w in words if w.lower() not in stopwords.words('english')]
    freq_dist = nltk.FreqDist(clean_words)
    print "100 most frequent words without stopword"
    print freq_dist.keys()[:200]


loadFromPickle()
#processFile()
