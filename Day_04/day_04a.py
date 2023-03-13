# Challenge Link: https://adventofcode.com/2015/day/4

from hashlib import md5
data = "yzbqklnj"

i = 0
while True:
    test = data + str(i)
    if md5(test.encode('utf-8')).hexdigest()[:5] == '00000':
        break
    i+=1

print(i)