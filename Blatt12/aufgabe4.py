import sys 
import re



pattern = re.compile(r'[a-zA-Z]+')

for line in sys.stdin: 
    line = line.split()
    newLine = ""
    for word in line:
        match = pattern.match(word)
        print(match)
        if match:
            match = match.group()
            match = match[::-1]
            newLine += match
        else:
            newLine += word;
        newLine += " ";
    print(newLine)