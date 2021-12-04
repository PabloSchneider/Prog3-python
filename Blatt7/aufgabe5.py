#!/usr/bin/env python3

def devocalize(s: str):
    "doese devocalize a string"
    vocals = "aeiou"
    s = ''.join(x for x in s if x not in vocals)
    return s

print(devocalize("Das ist ein Baerenspass"))

help(devocalize)