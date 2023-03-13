# Challenge Link: https://adventofcode.com/2015/day/6

filename = "Day_06/input.in"
with open(filename) as f:
    rawdata = f.read().split("\n")

def index(x,y):
    return 'x'+str(x)+'y'+str(y)

# initialize big array
cells = {}
for i in range(1000):
    for j in range(1000):
        cells[index(i,j)] = 0


def on(start,end,cells):
    start_x,start_y = map(int,start.split(","))
    end_x,end_y = map(int,end.split(","))

    for x in range(start_x,end_x+1):
        for y in range(start_y,end_y+1):
            cells[index(x,y)] += 1


def off(start,end, cells):
    start_x,start_y = map(int,start.split(","))
    end_x,end_y = map(int,end.split(","))

    for x in range(start_x,end_x+1):
        for y in range(start_y,end_y+1):
            i = index(x,y)
            if cells[i] > 0:
                cells[i] -= 1

def toggle(start,end,cells):
    start_x,start_y = map(int,start.split(","))
    end_x,end_y = map(int,end.split(","))

    for x in range(start_x,end_x+1):
        for y in range(start_y,end_y+1):
            i = index(x,y)
            cells[i] += 2



for d in rawdata:
    if d[:5] == 'turn ':
        d = d[5:]
    tmp = d.split(" ")
    
    locals()[tmp[0]](tmp[1],tmp[3],cells)

print(sum(cells.values()))
    


