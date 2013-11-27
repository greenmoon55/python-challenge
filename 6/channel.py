import re
import zipfile
import sys

zip_file = zipfile.ZipFile('./channel.zip', mode='r')
def get_next(file):
    for line in f:
        #print line
        match = re.match(r'Next nothing is (\d+)', line)
        if match:
            return match.group(1)
        return ''

def file_name(id):
    return str(id) + '.txt'

def open_file(id):
    f = zip_file.open(file_name(id))
    info = zip_file.getinfo(file_name(id))
    sys.stdout.write(info.comment)
    return f

ids = []
f = open_file(90052)
ids.append(90052)
next_id = get_next(f)
while next_id:
    ids.append(next_id)
    f = open_file(next_id)
    next_id = get_next(f)

for line in f:
    print line

