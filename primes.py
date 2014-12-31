#!/usr/bin/env python
# Prime library for Project Euler problems
# -- Adam Michael

from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen

def generate(max_prime):
  primes = [2]
  p = 3
  while (p < max_prime):
    if not any(map(lambda x: p % x == 0,primes)):
      primes += [p]
    p += 2
  return primes

def download(url="http://primes.utm.edu/lists/small/millions/primes1.zip",file="primes1.txt"):
  zipfile = ZipFile(StringIO(urlopen(url).read()))
  primes = []
  for line in zipfile.open(file).readlines()[2:]:
    primes += map(int,line.split())
  return primes