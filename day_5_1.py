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

# change to workgin directory
os.chdir(os.path.expanduser('~/Documents/edu/bootcamps/tm_bootcamp'))

### generate data
OT = 'old_testament'
NT = 'new_testament'

SRCS = [('DATA/kjv_books/ot',OT),('DATA/kjv_books/nt',NT)]

data = DataFrame({'text': [], 'class': []})

for path, classification in SRCS:
    data = data.append(make_df(path, classification))

print data.head()
print data.tail()
print data.shape

# unbias
def printdist(df):
    """
    Data-specific function for printing distributions of binary classification data
    """
    print 'class distribution: ', OT, sum(df['class'] == OT), NT, sum(df['class'] == NT)

printdist(data)

def unbias_data(df, n):
    random.seed(1234)
    res = DataFrame({'text': [], 'class': []})
    C = list(set(df['class']))
    for c in C:
        idx = df[df['class'] == c].index.tolist()
        df_c = df.loc[random.sample(idx, n)]
        res = res.append(df_c)
    return res.reindex(np.random.permutation(res.index))


data_800 = unbias_data(data, 800)

printdist(data_800)

# split data
ratio = 0.8
mask = np.random.rand(len(data_800)) <= ratio
data_train = data_800[mask]
data_test  = data_800[~mask]

data_train.shape
data_test.shape

## features (text) og repsponse (class)
# training
train_X = data_train['text'].values
train_y = data_train['class'].values
# test
test_X = data_test['text'].values
test_y = data_test['class'].values

### model training
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.linear_model import LogisticRegressionCV

# vectorizer
vec = CountVectorizer()
train_feat = vec.fit_transform(train_X)

feat_names = vec.get_feature_names()

# classifier
clf = LogisticRegressionCV()
clf.fit(train_feat, train_y)

### model validation
test_feat = vec.transform(test_X)
pred = clf.predict(test_feat)

# performance metrics
confmat = metrics.confusion_matrix(test_y, pred)
print confmat
perf_acc = metrics.accuracy_score(test_y, pred)
print perf_acc

# model summary
print metrics.classification_report(test_y,pred)

# most infomrative features
coef_feat_names = sorted(zip(clf.coef_[0], feat_names))

print coef_feat_names[:10]





####
import eli5

eli5.show_weights(clf, vec = vec, top = 25)

i = 5
text = data_800['text'][i]
print data_800['class'][i]

eli5.show_prediction(clf, text, vec = vec)
