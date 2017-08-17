#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:11:10 2017

@author: kln
"""
from __future__ import division
# preamble
import os
import numpy as np
root = '/home/kln/Documents/edu/bootcamps/tm_bootcamp'
os.chdir(root)
# egne moduler
import tmbootcamp as tm

## import data
texts, filenames = tm.read_vanilla('DATA/')

# remove numbers, casefold and tokenize
unigrams = []
for text in texts:
    s = tm.cleanstr(text)
    unigrams.append(tm.tokenize(s))

# slice
slices = []
for text in unigrams:
    slices.append(tm.slicer(text, n = 500, cut_off = True))
    
def TTR(tokens):
    """
    Type-token ratio for list of tokens
    """
    n_type = len(set(tokens))
    n_tokens = len(tokens)
    return n_type/n_tokens*100

# TTR for each slice in each book by Tolkien
dynam_ttr = []
for slcs in slices:
    tmp = []
    for slc in slcs:
        tmp.append(TTR(slc))
    dynam_ttr.append(tmp)
    
## AFINN applied to texts
import pandas as pd
sentpath = 'resource/AFINN-en-165.txt'# change for other dictionary
afinn = pd.read_csv(sentpath, sep='\t', encoding = 'utf-8', index_col = 0)
afinn_dict = afinn.sentiment.to_dict()
dynam_afinn = []
for slcs in slices:
    tmp = []
    for slc in slcs:
        scr = sum([afinn_dict.get(unigram, 0.0) for unigram in slc])
        tmp.append(scr)
    dynam_afinn.append(tmp)


# plotting
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.plot(tm.smooth(dynam_ttr[0]), color = 'k')
# add mean line
ax1.axhline(y = np.mean(tm.smooth(dynam_ttr[0])), c = 'r')
# add 2 standard deviations lines
ax1.axhline(y = np.mean(tm.smooth(dynam_ttr[0])) + 2*np.std(tm.smooth(dynam_ttr[0])), c = 'g')
ax1.axhline(y = np.mean(tm.smooth(dynam_ttr[0])) - 2*np.std(tm.smooth(dynam_ttr[0])), c = 'g')
# remaining three books
ax2 = fig.add_subplot(2,2,2)
ax2.plot(tm.smooth(dynam_ttr[1], 10), color = 'k')
ax3 = fig.add_subplot(2,2,3)
ax3.plot(tm.smooth(dynam_ttr[2], 10), color = 'k' )
ax4 = fig.add_subplot(2,2,4)
ax4.plot(tm.smooth(dynam_ttr[3], 10), color = 'k') 
plt.close()

def plotdist(x, sv = 0, filename = "dist.png"):
    """ histogram with normal fit """
    mu = np.mean(x)
    sigma =  np.std(x)
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='k', alpha=0.75)
    y = mlab.normpdf(bins, mu, sigma)
    ax = plt.plot(bins, y, 'r--', linewidth=1)
    plt.ylabel('Probability')
    plt.grid(True)
    if sv == 1:
        plt.savefig(filename, dpi = 300)
    else:
        plt.show()
        plt.close()

plotdist(dynam_afinn[3])

### identify extreme slices
text = dynam_afinn[3]
# top 10 sentiment slices
top10 = sorted(dynam_afinn[3], reverse = True)[:10]# ten most positive
# top10 = sorted(dynam_afinn[3], reverse = True)[-10:]# ten most negative
idx = []
for scr in top10[:3]:
    i = text.index(scr)
    idx.append(i)
    print ' '.join(slices[3][i])
    print '-----'
    print 


