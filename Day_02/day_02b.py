class Present:
    def __init__(self,dimensions) -> None:
        l,w,h = map(int,dimensions.split("x"))
        self.l = l
        self.w = w
        self.h = h
        self.a,self.b = sorted([self.l,self.w,self.h])[:2]
    
    def calcWrap(self):
        return 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l + self.a*self.b
    
    def calcRibbon(self):
        return self.a + self.a + self.b + self.b + self.h*self.w*self.l
    
filename = "Day_02/input.in"
with open(filename) as f:
    data = list(map(Present, f.read().split()))

print(sum([d.calcRibbon() for d in data]))