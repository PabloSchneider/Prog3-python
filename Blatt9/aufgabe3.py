#!/usr/bin/env python3
import sys

chars = [x.lower() if x.isalpha() else x for x in open(sys.argv[1]).read()]
entschluesselungstabelle = ('e','n','i','a','s','t','r','u','h','d','l','c','m','o','g','k','w','b','z','f','v','p','j','x','y','q') 
elements = [charcounter for charcounter in chars if charcounter.isalpha()]
chardict = dict(sorted({newchar: elements.count(newchar) for newchar in chars if newchar.isalpha()}.items(),key=lambda x: x[1], reverse=True)) 
translation = {[x[0] for x in chardict][i]:entschluesselungstabelle[i] for i in range(0, len(entschluesselungstabelle))}
print("".join([translation.get(c) if c.isalpha() else c for c in chars]))

