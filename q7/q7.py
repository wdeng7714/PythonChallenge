import re

from PIL import Image

img = Image.open('oxygen.png')
pix = img.load()  # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
print(img.size)  # (width, height)

print([pix[x, img.size[1] / 2] for x in range(
    30)])  # print the RGB of the central line to see the block size in pixel, which is 7 pixel per width block, except the first block whose width is 5 pixsels
output = "".join([chr(pix[4, 47][0])] + [chr(pix[5 + 7 * i, 47][0]) for i in range(86)])
print(output)
result = re.findall("\d+", output)
ret = ""
for i in result:
    ret += chr(int(i))

print(ret)
