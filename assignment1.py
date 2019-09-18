#!/usr/bin/env python2.7
# assigment1 count min sketch, reference: Approximating Data with the Count-Min Data Structure

import random as rnd
import numpy as np
import mmh3
import time

def cms(chars,w,d,stream_length):
    
    # init array C of wxd counters to 0
    C=np.zeros((d, w)).astype(int)

    # feed stream and updating counters
    while stream_length:
        i = chars[rnd.randrange(0, len(chars),1)]

        for j in range(d):
            #C[j,mmh3.hash(i,j)%w]+=1        
            C[j,mmh3.hash(i,j)&(w-1)]+=1
        stream_length -= 1
    return C

def eval_counters(C,w,d):

    # evaluate counters
    e = np.inf
    for i in chars:
        for j in range(d):
            e = min(e,C[j,mmh3.hash(i,j)%w])
        print i,int(e)
        e = np.inf


chars = ['A','B','C'] # set to be streamed
# w width is integer power of 2
# d depth
w=4;d=5

for i in range(8):
    stream_length= 10**i
    t0=time.time()
    C = cms(chars,w,d,stream_length)
    print time.time()-t0

eval_counters(C,w,d)
