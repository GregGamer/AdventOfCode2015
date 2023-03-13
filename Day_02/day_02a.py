# Challeng Link: https://adventofcode.com/2015/day/2

class Present:
    def __init__(self,dimensions) -> None:
        l,w,h = map(int,dimensions.split("x"))
        self.l = l
        self.w = w
        self.h = h
    
    def calcWrap(self):
        a,b = sorted([self.l,self.w,self.h])[:2]
        return 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l + a*b



filename = "Day_02/input.in"
with open(filename) as f:
    data = list(map(Present, f.read().split()))

print(sum([d.calcWrap() for d in data]))