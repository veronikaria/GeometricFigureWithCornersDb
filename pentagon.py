from polygon import Polygon
from point import Point
from triangle import Triangle

class Pentagon(Polygon):
    def __init__(self, a: Point, b: Point, c: Point, d: Point, e: Point):
        Polygon.__init__(self, 5)
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.E = e
        self.len_AB = self.sideLen(self.A, self.B)
        self.len_BC = self.sideLen(self.B, self.C)
        self.len_CD = self.sideLen(self.C, self.D)
        self.len_DE = self.sideLen(self.E, self.D)
        self.len_AE = self.sideLen(self.A, self.E)

    def area(self):
        t1 = Triangle(self.A, self.B, self.C)
        t2 = Triangle(self.A, self.C, self.D)
        t3 = Triangle(self.A, self.D, self.E)
        t4 = Triangle(self.A, self.B, self.E)
        area = t1.area() + t2.area() + t3.area() + t4.area()
        return area

    def perimeter(self):
        return self.len_AB + self.len_AE + self.len_BC + self.len_CD + self.len_DE

    def __mul__(self, other):
        a = self.A * other
        b = self.B * other
        c = self.C * other
        d = self.D * other
        e = self.E * other
        return Pentagon(a, b, c, d, e)

    def __eq__(self, other):
        return self.A==other.A and self.B==other.B and self.C==other.C and self.D==other.D and self.E == other.E

    def __str__(self):
        return "Пятикутник зі сторонами AB:{0}, BC:{1}, CD:{2}, DE:{3}, AE:{4}".format(self.len_AB, self.len_BC, self.len_CD, self.len_DE, self.len_AE)







