import collections
f = open('ocr.in', 'r')
dict = collections.defaultdict(int)
for line in f:
    for char in line:
        dict[char] = dict[char] + 1
        if char >= 'a' and char <= 'z': print char,
for key in sorted(dict.keys()):
    print key, dict[key]
