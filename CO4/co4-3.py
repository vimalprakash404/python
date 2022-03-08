class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()
l1 = int(input("Enter the length of first rectangle:"))
w1 = int(input("Enter the width of first rectangle:"))
r1 = Rectangle(l1, w1)
l2 = int(input("Enter the length of second rectangle:"))
w2 = int(input("Enter the width of second rectangle:"))
r2 = Rectangle(l2, w2)
if r1 < r2:
    print("rectangle 1 is smaller")
else:
    print("rectangle 2 is smaller")