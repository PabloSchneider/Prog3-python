#!/usr/bin/env python3
import sys
import collections
sonderzeichen="?,.:!-–"


def count_words(data):
    global sonderzeichen

    words = []
    worddict = {}
    for line in open(data):
        line = ''.join(x for x in line if x not in sonderzeichen)
        line = line.lower()
        line = line.split()
        for word in line:
            words.append(word)
    
    words.sort()
    word = ''
    for newword in words[1:]:
        if newword != word:
            word = newword
            countwords = words.count(word)
            worddict.update({word: countwords})
    
    sortedWords = sorted(worddict.items(), key=lambda x: x[1], reverse=True)
    counter = 0
    worddict.clear()
    for tupel in sortedWords:
        if counter < 25:
            worddict.update({tupel[0]:tupel[1]})
            counter = counter +1
    return worddict, len(words)
    

def count_chars(data):
    global sonderzeichen

    chars = []
    charsdict = {}
    for line in open(data):
        line = ''.join(x for x in line if x not in sonderzeichen)
        line = line.lower()
        line = line.split(' ')
        for word in line:
            for c in word:
                if c != '\n':
                    chars.append(c)
    print(chars)
    chars.sort()
    word = ''
    for newword in chars[1:]:
        if newword != word:
            word = newword
            countwords = chars.count(word)
            charsdict.update({word: countwords})
    
    sortedWords = sorted(charsdict.items(), key=lambda x: x[1], reverse=True)
    counter = 0
    charsdict.clear()
    for tupel in sortedWords:
        if counter < 25:
            charsdict.update({tupel[0]:tupel[1]})
            counter = counter +1
    return charsdict, len(chars)
        


mostWords, wordlength = count_words(sys.argv[1])

mostChars, charlength = count_chars(sys.argv[1])

print("_______words_______")
print(mostWords)
print("_______Chars_______")
print(mostChars)
print("___________________")
print("Wordlengt:", wordlength)
print("Charlengt:", charlength)