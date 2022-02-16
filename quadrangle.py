from polygon import Polygon
from point import Point
from math import sqrt

class Quadrangle(Polygon):
    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        Polygon.__init__(self, 4)
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.len_AB = self.sideLen(self.A, self.B)
        self.len_BC = self.sideLen(self.B, self.C)
        self.len_CD = self.sideLen(self.C, self.D)
        self.len_AD = self.sideLen(self.A, self.D)

    def area(self):
        p = self.perimeter()/2
        area = sqrt((p-self.len_AB)*(p-self.len_CD)*(p-self.len_AD)*(p-self.len_BC))
        return area

    def perimeter(self):
        return self.len_AB + self.len_AD + self.len_BC + self.len_CD

    def __mul__(self, other):
        a = self.A * other
        b = self.B * other
        c = self.C * other
        d = self.D * other
        return Quadrangle(a, b, c, d)

    def __eq__(self, other):
        return self.A==other.A and self.B==other.B and self.C==other.C and self.D==other.D

    def __str__(self):
        return "Чотирикутник з координатами А{0} B{1} C{2} D{3} та зі сторонами AB:{4}, BC:{5}, AD:{6}, CD:{7}".format(self.A, self.B, self.C, self.D, self.len_AB, self.len_BC, self.len_AD, self.len_CD)







