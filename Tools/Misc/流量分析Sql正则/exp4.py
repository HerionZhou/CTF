import re

flag = ''
temp = {}

with open('4.csv', 'rb') as f:
    for s in f.readlines():
        data = re.search(b'select flag from answer\),(.*?),1\)\)=(.*?)--\+', s)
        temp[data[1].decode()] = data[2].decode()

for i in temp:
    flag += chr(int(temp[i]))

print(flag)
