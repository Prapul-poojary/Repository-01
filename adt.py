class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("day=",self.d)
    def month(self):
        print("month=",self.m)
    def year(self):
        print("year=",self.y)
    def month_name(self):
        month=["unknown","january","february","march","april","may","june","july","august","september","october","november","december"]
        print("month name:",month[self.m])
    def is_leapyear(self):
        if(self.y%400==0) and (self.y%100==0):
            print("it is a leap year")
        elif(self.y%4==0) and (self.y%100!=0):
            print("it is a leap year")
        else:
            print("it's not leap year")

d1=date(3,1,1997)
d1.day()
d1.month()
d1.year()
d1.month_name()
d1.is_leapyear()