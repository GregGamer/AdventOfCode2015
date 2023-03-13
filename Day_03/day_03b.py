# Challenge Link: https://adventofcode.com/2015/day/3

filename = "Day_03/input.in"
with open(filename) as f:
    data = f.read()
tmp = True

x_santa,y_santa = 0,0
x_robo,y_robo = 0,0
#     y+1
# x-1     x+1
#     y-1

route = set()
for dir_santa,dir_robo in zip(data[::2],data[1::2]):
        index_santa = 'x'+str(x_santa)+'y'+str(y_santa)
        route.add(index_santa)
        if dir_santa == "^":
            y_santa+=1
        if dir_santa == ">":
            x_santa+=1
        if dir_santa == "v":
            y_santa-=1
        if dir_santa == "<":
            x_santa-=1
        
        index_robo = 'x'+str(x_robo)+'y'+str(y_robo)
        route.add(index_robo)
        if dir_robo == "^":
            y_robo+=1
        if dir_robo == ">":
            x_robo+=1
        if dir_robo == "v":
            y_robo-=1
        if dir_robo == "<":
            x_robo-=1
    
index = 'x'+str(x_santa)+'y'+str(y_santa)
route.add(index)
index = 'x'+str(x_robo)+'y'+str(y_robo)
route.add(index)

# print(route)
print(len(route))
