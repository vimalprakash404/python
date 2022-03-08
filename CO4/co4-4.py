class time:
    def __init__(self,h,m,s):
        self.__hh = h
        self.__mm = m
        self.__ss = s
    def __add__(self, other):
        hour = self.__hh + other.__hh
        minute = self.__mm + other.__mm
        second = self.__ss + other.__ss
        if second > 60:
            minute += int(second / 60)
            second = second % 60
        if minute > 60:
            hour += int(minute / 60)
            minute = minute % 60
        if hour > 24:
            hour = hour % 24
        t = time(hour,minute,second)
        return t
    def display(self):
        print(self.__hh,":",self.__mm,":",self.__ss)

h1 = int(input("enter hour ="))
m1 = int(input("enter minute ="))
s1 = int(input("enter second = "))
time1 = time(h1,m1,s1)
h2 = int(input("enter hour ="))
m2 = int(input("enter minute ="))
s2 = int(input("enter second = "))
time2 = time(h2,m2,s2)
t=time1+time2
t.display()
