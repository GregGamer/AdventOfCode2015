# Challeng Link: https://adventofcode.com/2015/day/1

filename = "Day_01/input.in"
with open(filename) as f:
    data = f.read()
    
print(sum([data.count("("), -data.count(")")]))