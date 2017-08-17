#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
sentiment analysis for literature

"""
# preamble
import os
root = '/home/kln/Documents/edu/bootcamps/tm_bootcamp'
os.chdir(root)
# egne moduler
import tmbootcamp as tm
import quickndirty as qd

## import data
texts, filenames = tm.read_vanilla('DATA/')
# check files
print filenames

# tokenize one document at word level
i = 3#file index
print 'modeling sentiment in:', filenames[i]
unigrams = tm.tokenize(texts[i].lower())
print unigrams[:100]
# slice unigrams in slices of 500 tokens
slices = tm.slicer(unigrams, n = 500, cut_off = True)

# import sentiment dictionary
import pandas as pd
labmt = pd.read_csv('resource/labmt_dict.csv', sep='\t',
                    encoding = 'utf-8', index_col = 0)
# show properties of labmt dictionary
print labmt.head()
print labmt.shape
print labmt.tail()

## zero-center score and build dictionary
avg = labmt.happiness_average.mean()
sent_dict = (labmt.happiness_average - avg).to_dict()

# build sentiment vector of sum sentiment score for each slice
sent_vec = []
for slice in slices:
    sent_vec.append(sum([sent_dict.get(unigram, 0.0) for unigram in slice]))

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(tm.smooth(sent_vec,50), color = 'k')
ax.axhline(y = np.mean(sent_vec), c='r', linewidth = 1) 
ax.set_xlabel('Slice')
ax.set_ylabel('Sentiment')
plt.show()
plt.savefig()
plt.close()


### BRANDES SENTILIZER
texts, filenames = tm.read_vanilla('brandes_data/')


unigrams_ls = []
for text in texts:
    unigrams_ls.append(tm.tokenize(text.lower()))

afinn = pd.read_csv('resource/AFINN-da-32.txt', sep='\t',
                    encoding = 'utf-8', index_col = 0)
#print afinn.head()
#print afinn.tail()

afinn_dict = afinn.sentiment.to_dict()

brandes_feel = []
for i, unigrams in enumerate(unigrams_ls):
    v = [afinn_dict.get(unigram, 0.0) for unigram in unigrams]
    brandes_feel.append([np.sum(v),np.var(v)])
    print filenames[i]+':', brandes_feel[i][0]
    print

def sentilizer(dirpath):
    texts, filenames = tm.read_vanilla(dirpath)
    unigrams_ls = []
    for text in texts:
        unigrams_ls.append(tm.tokenize(text.lower()))
    afinn = pd.read_csv('resource/AFINN-da-32.txt', sep='\t',
                    encoding = 'utf-8', index_col = 0)
    afinn_dict = afinn.sentiment.to_dict()
    brandes_feel = []
    for i, unigrams in enumerate(unigrams_ls):
        v = [afinn_dict.get(unigram, 0.0) for unigram in unigrams]
        brandes_feel.append([np.sum(v),np.var(v)])
        print filenames[i]+':', brandes_feel[i][0]
        print
        print 'Number of words used:', sum([i > 0.0 for i in v])/len(unigrams)
        print


sentilizer('brandes_data/')


len(v)

from __future__ import division
def sentilizer(dirpath, sentpath = 'resource/AFINN-da-32.txt'):
    texts, filenames = tm.read_vanilla(dirpath)
    unigrams_ls = []
    for text in texts:
        unigrams_ls.append(tm.tokenize(text.lower()))
    afinn = pd.read_csv(sentpath, sep='\t', encoding = 'utf-8', index_col = 0)
    afinn_dict = afinn.sentiment.to_dict()
    brandes_feel = []
    for i, unigrams in enumerate(unigrams_ls):
        v = [afinn_dict.get(unigram, 0.0) for unigram in unigrams]
        brandes_feel.append([np.sum(v),np.var(v)])
        print filenames[i]+':', brandes_feel[i][0]
        print
        print 'Number of words used:', sum([i > 0.0 for i in v])/len(unigrams)
        print
sentilizer('brandes_data/')


x = plotdist(v)
plt.show()
#import tmbootcamp as tm
#texts, filesnames = tm.read_vanilla('brandes_data/')

