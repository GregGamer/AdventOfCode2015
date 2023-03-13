# Challenge Link: https://adventofcode.com/2015/day/5

filename = "Day_05/input.in"
with open(filename) as f:
    data = f.read().split()

nice_strings = 0
for d in data:
    # does not contain ab,cd,pq,xy
    if d.__contains__("ab") or d.__contains__("cd") or d.__contains__("pq") or d.__contains__("xy"):
        continue

    # contains three vowels
    nicely_count = sum([d.count(tmp) for tmp in 'aeiou'])
    if nicely_count < 3:
        continue

    # has two letters in a row
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            nice_strings += 1
            break
    

print(nice_strings)


    
