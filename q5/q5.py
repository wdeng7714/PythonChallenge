import pickle

with open("banner.p", "rb") as f:
    banner = pickle.load(f)

for item in banner:
    line = ""
    for pair in item:
        line += pair[0] * int(pair[1])
    print(line)
