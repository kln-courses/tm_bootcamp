#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


"""

import tmbootcamp as tm
texts, filesnames = tm.read_vanilla('brandes_data/')

unigrams_ls = []
for text in texts:
    unigrams_ls.append(tm.tokenize(tm.cleanstr(text)))
    
unigrams = unigrams_ls[0]
