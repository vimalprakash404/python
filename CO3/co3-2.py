import graphics.trdGraphics.cuboid as cube
import graphics.trdGraphics.shpere as sp
import graphics.circle as ci
import graphics.rectangle as rect

print("Rectangle")
k = rect.area(10,20)
b= rect.perimeter(10,20)
print("area = ",k,"Perimeter = ",b)

print("circle")
t = ci.area(10)
k = ci.perimeter(10)
print("area = ",t,"Perimeter = ",k)
print("shpere")
a =sp.area(20)
print("area = ",a)
p = sp.perimeter(20)
print("perimeter = ",p)
print("cube")
a = cube.area(10,20,30)
p = cube.perimeter(10,20,30)
print("perimeter = ",p,"area = ",a)