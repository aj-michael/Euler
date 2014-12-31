#!/usr/bin/env python
# Project Euler, Problem 54
# -- Adam Michael

face_cards = { 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
car = lambda x: x[0]
cadr = lambda x: x[1]
cdr = lambda x: x[1:]

def score(hand):
  score = rflush(hand)
  score = (score << 1) + sflush(hand)
  score = (score << 1) + four(hand)
  score = (score << 1) + fhouse(hand)
  score = (score << 1) + flush(hand)
  score = (score << 1) + straight(hand)
  score = (score << 1) + three(hand)
  score = (score << 1) + twopair(hand)
  score = (score << 1) + pair(hand)
  return score

def rflush(hand):
  return 0

def sflush(hand):
  return 0

def four(hand):
  values = map(car,hand)
  return 1 if any(values.count(x) == 4 for x in values) else 0

def fhouse(hand):
  return 1 if three(hand) + pair(hand) == 2 else 0

def flush(hand):
  suits = map(cadr,hand)
  return 1 if suits.count(suits[0]) == len(suits) else 0

def straight(hand):
  return 0

def three(hand):
  values = map(car,hand)
  return 1 if any(values.count(x) == 3 for x in values) else 0

def twopair(hand):
  return 0

def pair(hand):
  values = map(car,hand)
  return 1 if any(values.count(x) == 2 for x in values) else 0

def highCard(hand1,hand2):
  return 1 if max(map(car,hand1)) > max(map(car,hand2)) else 0

def compare(hand1, hand2):
  s1 = score(hand1)
  s2 = score(hand2)
  if s1 == s2:
    return highCard(hand1,hand2)
  else:
    return 1 if s1 > s2 else 0

def replaceFace(x):
  return face_cards[x] if x in face_cards else int(x)

if __name__ == '__main__':
  p1count = 0
  with open('p054_poker.txt','r') as f:
    for line in f.readlines():
      cards = line.split()
      hand1 = cards[0:5]
      hand2 = cards[5:10]
      hand1 = map(lambda x: [replaceFace(x[0]),x[1]], cards[0:5])
      hand2 = map(lambda x: [replaceFace(x[0]),x[1]], cards[5:10])
      p1count += compare(hand1,hand2)
  print p1count
