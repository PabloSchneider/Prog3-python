#!/usr/bin/env python3
import sys

print("".join([(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'][['w','g','s','n','q','c','d','v','m','e','y','l','u','z','o','a','b','h','r','j','f','k','x','i','p','t'].index(x)]) if x in ['w','g','s','n','q','c','d','v','m','e','y','l','u','z','o','a','b','h','r','j','f','k','x','i','p','t'] else x for x in open(sys.argv[1]).read()]))
