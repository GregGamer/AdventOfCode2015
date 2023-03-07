filename = "Day_01/input.in"
with open(filename) as f:
    data = f.read()

for i in range(len(data)):
    temp = sum([data[:i].count("("), -data[:i].count(")")]) 
    if temp == -1:
        print(i)
        break