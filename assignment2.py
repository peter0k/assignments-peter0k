#!/usr/bin/env python2.7
# assigment2 bloom filter

#dependencies
import sys
from itertools import combinations
from bitarray import bitarray
import string
import numpy as np
import mmh3
from math import *

storage=list(combinations(string.ascii_lowercase, 5)) 
storage=["".join(i)for i in storage] # storage of strings of size 5

p=1.0e-7  # false positive rate
n=float(len(storage)/2)  # number of elements in storage

m = int(-n*log(p)/log(2)**2)  # number of bits
k = int(round(m/n)*log(2))    # number of hash functions

bfilter = bitarray(m) # allocate bloomfilter
bfilter.setall(False) 

# generate bloom filter for first half of storage
for j in range(1,k+1):
    for i in storage[:int(len(storage)/2)]:
        bfilter[mmh3.hash(i,j)%m]=1


def in_storage(query,k,m):
    """queries if query is NOT present"""
    bools = []
    for i in range(1,k+1):
        bools.append(bfilter[mmh3.hash(query,i)%m])
    return np.prod(bools)

print in_storage(storage[-1],k,m) #take string from second half of storage (not used for bloom filter)
print "size of storage",sys.getsizeof(storage)
print "size of bloom filter",sys.getsizeof(bfilter)
