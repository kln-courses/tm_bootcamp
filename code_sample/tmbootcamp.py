#!/usr/bin/env python2
# -*- coding: utf-8 -*-w
"""
TODO

"""
import codecs, glob, re

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

def cleanstr(s):
    return re.sub(r'\d','',s.lower())

def tokenize(s, n = 1):
    """
    n-gram tokenization of string with maximum overlap
    """
    if type(s) == unicode:
        tokenizer = re.compile(r'\W*', re.UNICODE)
    else:
        tokenizer = re.compile(r'\W*')
    unigram = tokenizer.split(s)
    if n > 1:
        return [unigram[i:i+n] for i in range(len(unigram)-(n-1))]
    else:
        return [s for s in unigram if s]

def slicer(input, n = 100, cut_off = False):
    """
    slice tokenized text in slices of n chars/tokens
    - end cut off for full length normalization
    """
    slices = []
    for i in range(0,len(input),n):
        slices.append(input[i:(i+n)])
    if cut_off:
        del slices[-1]
    return slices

def smooth(l, n = 5):
    """moving average filter with window size n"""
    sigma = 0
    res = list( 0 for x in l)
    for i in range(0 , n):
        sigma = sigma + l[i]
        res[i] = sigma / (i + 1)
    for i in range( n, len(l) ):
        sigma = sigma - l[i - n] + l[i]
        res[i] = sigma / n
    return res
