#!/usr/bin/env python
# Project Euler, Problem 51
# -- Adam Michael

import itertools
import math
import random
import primes

def bar(primes):
  N = 6 ; I = range(1,N+1)
  primes = [p for p in primes if p >= 10**(N-1) and p < 10**N]

  combs = []
  for i in range(len(I)):
    combs += itertools.combinations(I,i+1)
  combs = [list(t) for t in combs]

  for comb in combs:
    sprimes = sorted(primes,key=baz(comb))
    for k, v in itertools.groupby(sprimes,key=baz(comb)):
      l = list(v)
      if len(l) >= 8:
        print k, len(l), l
  return

# 1-indexed
def baz(indices):
  def g(n):
    digits = [int(j) for j in str(n)]
    include = [digits[-i] for i in indices]
    exclude = [digits[-i] for i in range(1,len(digits)+1) if i not in indices]
    base = int(''.join(str(k) for k in include))
    if len(exclude) > 0 and not exclude.count(exclude[0]) == len(exclude):
      base = base + random.uniform(0.0,1.0)
    return base
  return g

if __name__ == '__main__':
  #MAX_PRIME = 1000
  #primes = primes.generate(MAX_PRIME)
  #print primes
  primes = primes.download()
  bar(primes)
  #print bar([1,2,4])(12345)
