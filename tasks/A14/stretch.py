import math
class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return round(math.pi*self.radius*self.radius,1)
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return (self.side*self.side)
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

c=circle(5)  
s=square(6)
r=rectangle(12,6)

print("circle area:",c.area())
print("square area:",s.area())
print("rectangle area:",r.area())
