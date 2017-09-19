#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import io, os, re

root = os.path.expanduser('~/Documents/edu/bootcamps/tm_bootcamp')
datadir = 'brandes_data/'
os.chdir(root)

def dir2lignes(dirname):
    tokenizer = re.compile(r'\W*', re.UNICODE)
    data = []
    for fname in os.listdir(datadir):
        with io.open(datadir + fname) as f:
            lignes = [tokenizer.split(line.lower().rstrip()) for line in f.readlines() if line.rstrip()]

        data.append(lignes)
    data = [i for sublist in data for i in sublist]
    out = []
    for tokens in data:
        out.append([token for token in tokens if token])
    return out

data = dir2data(datadir)

# train model
from gensim import models
mdl = models.Word2Vec(data, size = 20, window = 5, seed = 1234, min_count = 3, workers = 2)

# representation of 'kvinde'
print mdl.wv['kvinde']
# ten most similar words to 'kvinde'
similar_words_list = mdl.wv.most_similar(positive=[u'kvinde'])
for i in similar_words_list:
    print i[0]

# complex associations
mdl.wv.most_similar_cosmul(positive=['stor', 'mand'], negative=['kvinde'])

# visualize representation of 'kvinde'
import matplotlib.pyplot as plt
plt.matshow(mdl['kvinde'].reshape((10,10)), fignum = 100, cmap=plt.cm.gray)
plt.show()

#
mdl.wv.doesnt_match("paris napoleon frankrig".split())
