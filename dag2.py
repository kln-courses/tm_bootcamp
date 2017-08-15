#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
DAG 2:
    
    
"""
# preamble

import codecs, glob, io, os, re
root = '/home/kln/Documents/edu/bootcamps/tm_bootcamp'
os.chdir(root)

filenames = sorted(glob.glob('DATA/'+'*.txt'))
print filenames


with io.open(filenames[1],'r', encoding = 'utf-8') as fileobj:
    content = fileobj.read()

print content



text_list = []
fnames = []
for filename in filenames:
    with io.open(filename, 'r', encoding = 'utf-8') as fileobj:
        text_list.append(fileobj.read())
        fnames.append(filename)


def import_dir(dirpath):
    """
    Importer txt-filer (unicode) fra dirpath
    - retunerer text og filnavne i lister 
    """
    text_list = []
    fnames = sorted(glob.glob(dirpath+'*.txt'))
    for fname in fnames:
        with io.open(fname, 'r', encoding = 'utf-8') as f:
            text_list.append(f.read())
    newfname = []
    for fname in fnames:
        newfname.append(fname.split('/')[-1])
    return text_list, newfname

texts, fnames = import_dir('DATA/')

print len(texts)
print fnames

def read_vanilla(path):
    """
    read multiple vanilla files in folder on path with
    -  unicode or lat encoding
    """
    filenames = sorted(glob.glob(path+'*.txt'))
    text_ls = []
    for filename in filenames:
        try:
            with codecs.open(filename, encoding='UTF-8') as f:
                text = f.read()
        except:
            with codecs.open(filename, encoding='LATIN-1') as f:
                text = f.read()
        text_ls.append(text)
        titles = [re.sub(r'.txt','',f.split('/')[-1]) for f in filenames]
    return text_ls, titles


texts, fnames = read_vanilla('DATA/')


for text in texts:
    print text[2000:2100].split()
    print 
    print

## rensning af str elementer
import re
text = texts[1]
def tokenize(text, minlen = 0, numbers = False):
    """
    Clean and Tokenize string
    - remove tokens of minlen
    - remove number if True
    """
    text_ren = text.lower()
    text_ren = re.sub(r'\W+',' ',text_ren)
    if numbers:
        text_ren = re.sub(r'\d','', text_ren)
    text_ren = re.sub(r'\s+',' ',text_ren)# remove
    unigrams = text_ren.split()
    unigrams = [unigram for unigram in unigrams if len(unigram) > minlen]
    return unigrams

testtext = texts[1]
unigrams = tokenize(testtext, minlen = 1, numbers = True)

### NLTK til tokenisering
import nltk
nltk.download()

# sentence disambiguation
import nltk.data
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sent = sent_tokenizer.tokenize(text)
print sent[1010]
# word-level
from nltk.tokenize import word_tokenize
unigrams = word_tokenize(text)
print unigrams[:1000]


### optælling og rensning af hyppige ord
from operator import itemgetter

# the Frodo til Gandalf ratio
print tokens.count('frodo')/float(tokens.count('gandalf'))

def termfreq(unigrams):
    tf = dict([(unigram, unigrams.count(unigram)) for unigram in set(unigrams)])
    return tf

def term_nmax(unigrams, n = 100):
    tf = termfreq(unigrams)
    nmax = sorted(tf.iteritems(), key = itemgetter(1), reverse = True)[:n]
    return nmax
    
def gen_stoplist(unigrams, n = 100):
    nmax = term_nmax(unigrams, n)
    return [i[0] for i in nmax]


stoplist = gen_stoplist(unigrams, n = 100)

print stoplist

unigram_nostop = [unigram for unigram in unigrams if unigram not in unigrams]

# write stopwords to txt file
with io.open('stoplist_100.txt','w', encoding = 'utf-8') as f:
    for stopword in stoplist:
        f.write('%s\n' % stopword)
        

# stemmer til engelsk, men også danish option
from nltk.stem.snowball import SnowballStemmer
print unigrams[:1000]

stemmer = SnowballStemmer('english', ignore_stopwords = True)
unigrams_stem = [stemmer.stem(unigram) for unigram in unigrams]

print unigrams_stem[:1000]



### make tag-cloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def tag_cloud(unigrams, save = False, stop_set = None):
    """
    Make tag-cloud from list of tokens
    """
    wc = WordCloud(stopwords = stop_set).generate(' '.join(unigrams))
    plt.figure(figsize = (12,12), dpi = 200)
    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    if save:
        plt.savefig('wordcloud.png')
    else:
        plt.show()
    plt.close()
    
    
tag_cloud(unigrams_stem, True)
































