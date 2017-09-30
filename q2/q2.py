with open("source.txt", "r") as f:
    txt = f.read()
    for c in txt:
        if c.isalpha():
            print(c)


