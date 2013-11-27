import pickle
import sys
obj = pickle.load(open('banner.p', 'r'))
for item in obj:
    for t in item:
        sys.stdout.write(t[0] * t[1])
    print
