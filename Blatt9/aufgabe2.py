#!/usr/bin/env python3
import sys
from_chars = ['w','g','s','n','q','c','d','v','m','e','y','l','u','z','o','a','b','h','r','j','f','k','x','i','p','t']
to_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("".join([(to_chars[from_chars.index(x)]) if x in from_chars else x for x in open(sys.argv[1]).read()]))