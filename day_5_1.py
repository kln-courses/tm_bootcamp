#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
binary classification with classes in separate directories in root directory
- logistic regresssion, feature engineering, vector space optimization, visualization
"""
from __future__ import division
import io, os, random, re
import numpy as np
from pandas import DataFrame
from unidecode import unidecode

def read_files(path, SPLITCHAR = '\n\n', normalization = False):
    paragraphs_ls, filenames_ls = [], []
    for (root, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root,filename)
            with io.open(filepath, 'r', encoding = 'utf-8') as f:
                text = f.read()
                paragraphs = text.split(SPLITCHAR)
                del paragraphs[0]
                i = 0
                for paragraph in paragraphs:
                    paragraph = paragraph.rstrip()
                    if paragraph:
                        if normalization:
                            paragraph = re.sub(r'\W+',' ', paragraph)
                            paragraph = re.sub(r'\d','',paragraph)
                            paragraph = re.sub(r'  +',' ',paragraph)
                            paragraph = unidecode(paragraph.lower())
                        paragraphs_ls.append(paragraph)
                        filenames_ls.append(filename+'_'+str(i))
                        i += 1
    return filenames_ls, paragraphs_ls

def make_df(path, classification):
    filenames, paragraphs = read_files(path, normalization = True)
    rows = []
    idx = []
    i = 0
    for paragraph in paragraphs:
        rows.append({'text': paragraph, 'class': classification})
        idx.append(filenames[i])
        i += 1
    df = DataFrame(rows, index = idx)
    return df
