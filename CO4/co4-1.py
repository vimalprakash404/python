class rectangle:
    def __init__(self,l1,b1):
        self.length=l1
        self.breadth=b1
    def area(self):
        return (self.length * self.breadth)

    def perimeter(self):
        return (2*(self.length+self.breadth))

l1 = int(input("enter length of the rectangle"))
b1 = int(input("enter breadth of the rectangle"))
r1=rectangle(l1,b1)
cr1= r1.area()
print("area of rectangle 1 =",cr1)
print("perimeter of rectangle 1 =",r1.perimeter())
l2 = int(input("enter length of the rectangle"))
b2 = int(input("enter breadth of the rectangle"))
r2=rectangle(l2,b2)
cr2=r2.area()
print("area of rectangle 2 =",cr2)
print("perimeter of rectangle 2 =",r2.perimeter())
if cr1 > cr2:
    print("first rectangle is large")
else:
    print("second rectangle is large")