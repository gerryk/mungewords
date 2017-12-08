#!/usr/bin/python

import sys

class WordList():
    seed_words = []
    def __init__(self,words):
       self.seed_words = words

    @staticmethod
    def upper_lower(word):
        w = list(word)
        for i in range(0,len(word)):
            yield word[:i] + word[i].upper() + word[i+1:]
            yield word[:i] + word[i:].upper()
            yield word[:i].upper() + word[i:]

    @staticmethod
    def l337speak(word):
        lookup = {
            'a' : '4',
            'b' : '8',
            'c' : '(',
            'e' : '3',
            'g' : '&',
            'h' : '#',
            'i' : '1',
            'l' : '1',
            'o' : '0',
            's' : '5',
            't' : '7',
            'x' : '%'
        }
        for k,v in lookup.iteritems():
            if k in word:
                new = word.replace(k,v)
                word = new
                yield word

if len(sys.argv) < 2:
    print "No words provided..."
    exit(1)
o = WordList(sys.argv[1:])
for w in o.seed_words:
    for p in o.upper_lower(w):
        print p
    for p in o.l337speak(w):
        print p


