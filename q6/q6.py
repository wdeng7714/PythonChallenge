import re
from zipfile import ZipFile

next = str(90052)
ret = ""
while True:
    with ZipFile("zip/channel.zip") as z:
        ret += z.getinfo("{}.txt".format(next)).comment.decode()
        f = z.open("{}.txt".format(next))
    r = f.read().decode()
    n = re.findall(r'Next nothing is \d+', r)

    if len(n) < 1:
        if "Yes. Divide by two and keep going." in r:
            print("dividing by 2...")
            next = int(next) / 2
        else:
            break
    else:
        next = re.findall("\d+", n[0])[0]
    print(next)

print(ret)
