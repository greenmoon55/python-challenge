import urllib
import re
def wget(url):
    print url
    ufile = urllib.urlopen(url)
    text = ufile.read()
    return text

def valid(page):
    match = re.search(r'nothing is (\d+)', page)
    if match:
        dest = match.group(1)
        return dest
    return ''

#page = wget("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
page = wget("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")
result = valid(page)
while result != '':
    page = wget("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + result)
    result = valid(page)
print page
