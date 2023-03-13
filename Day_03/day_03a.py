# Challenge Link: https://adventofcode.com/2015/day/3

filename = "Day_03/Jinput.in"
with open(filename) as f:
    data = f.read()

x,y = 0,0
#     y+1
# x-1     x+1
#     y-1
route = set()
for d in data:
    index = 'x'+str(x)+'y'+str(y)
    route.add(index)

    if d == "^":
        y+=1
    if d == ">":
        x+=1
    if d == "v":
        y-=1
    if d == "<":
        x-=1

index = 'x'+str(x)+'y'+str(y)
route.add(index)

# print(route)
print(len(route))
