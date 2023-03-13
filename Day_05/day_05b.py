# Challenge Link: https://adventofcode.com/2015/day/5

filename = "Day_05/input.in"
with open(filename) as f:
    data = f.read().split()

nice_strings = 0
for d in data:
    success_flag = 0
    # Contains 2 letters repeatidly (xyaxy)
    for i in range (len(d)-1):
        tmp = d[i]+d[i+1]
        if d.count(tmp) < 2:
            continue
        elif d.count(tmp) >= 2:
            success_flag += 1
            break

    # Contains the same Characters with a random Character between (xyx)
    for i in range(len(d)-2):
        if d[i] == d[i+2]:
            success_flag += 1

    if success_flag == 2:
        nice_strings += 1 

print(nice_strings)
