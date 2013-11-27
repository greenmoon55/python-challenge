import re
# regex = r'[A-Z]{3}[a-z][A-Z]{3}'
# EXACTLY!
regex = r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]'
f = open('equality.in', 'r')
str = ''
for line in f:
    str += line.strip();
results = re.findall(regex, str)
for result in results:
    print result

