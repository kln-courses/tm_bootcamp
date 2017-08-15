#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Introduktion til Python programmering
 - import af data
 - loops
 -
"""
### preamble - gør miljø klar
import os
root = "/home/kln/Desktop/tm_bootcamp"
os.chdir(root)# skifte til arbejdsfolder

# variable
v_kg = 55
print v_kg
s = 'denne variabel skal slættes'
del s# slet variable

print 'vægt i pund er', v_kg * 2.2

# importere data
import numpy as np
data = np.loadtxt('DATA/inflammation-01.csv', delimiter = ',') 
print data
print type(data)
print data.dtype
print data.shape

# index for dele af data matrix
print 'den første værdi i første bog', data[0,0]
print 'den miderste værdi', data[30,20]
print 'den første bog', data[0,:]

# beregning af centrale tendenser fra matrix
print np.median(data[0,:])

# funktioner der ikke tager input
import time
print time.ctime()

# plot matrix som heatmap
import matplotlib.pyplot as plt
% matplotlib inline
image = plt.imshow(data)
plt.show()

print type(data)

## opbyg plot
fig = plt.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

axes1.plot(np.mean(data, axis = 0))
axes1.set_ylabel('gennemsnit')

axes2.plot(np.max(data, axis = 0))
axes2.set_ylabel('maximum')

axes3.plot(np.min(data, axis = 0))
axes3.set_ylabel('minimum')


### 
word = 'Brandes'
print word[0]
print word[1].upper()
print word[2].upper()
print word[3].upper()

# out of index
print word[10]
for john in word:
    print john.upper()

# lister as str
text_liste = ['Brandes', 'Grundtvig', 'Andersen']
print text_liste
print text_liste[1]
print type(text_liste)
print type(text_liste[0])

for s in text_liste:
    print s.upper()

length = 0
vokaler = 'aeiou'
for vokal in text_liste:
    #print vokal
    length = length + 1

print length

s1 = 'Neumann'
s2 = ''
print s2
for char in s1:
    print char
    s2 = char.lower() + s2

print s2

bogstav = 'k'
for bogstav in 'abc':
    print bogstav

print bogstav






