ret = ""
import re

with open("q3/source.txt", "r") as f:
    txt = f.read()
    matches = re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", txt)
    for match in matches:
        ret += match[4]

    print(ret)
