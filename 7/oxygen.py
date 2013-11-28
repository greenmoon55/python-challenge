import png
import sys
f = open('oxygen.png', 'r')
reader = png.Reader(f)
iterator = reader.read()[2]
pixels = list(iterator)
#print len(pixels)
'''
for line in pixels:
    print line[:5]
print
'''

for line in pixels[43:52]:
    for code in line.tolist()[::4][::7]:
        sys.stdout.write(chr(code))
    print

codes = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for code in codes:
    sys.stdout.write(chr(code))

