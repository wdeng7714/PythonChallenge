import re

import requests

url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
while True:
    n = re.findall(r'the next nothing is \d+', r.text)
    if len(n) < 1:
        if "Yes. Divide by two and keep going." in r.text:
            print("dividing by 2...")
            next = int(next) / 2
        else:
            break
    else:
        next = re.findall("\d+", n[0])[0]
    print(next)
    r = requests.get("{}{}".format(url_base, next))
