from polygon import Polygon
from point import Point
from math import sqrt

class Triangle(Polygon):
    def __init__(self, a: Point, b: Point, c: Point):
        Polygon.__init__(self, 3)
        self.A = a
        self.B = b
        self.C = c
        self.len_AB = self.sideLen(self.A, self.B)
        self.len_AC = self.sideLen(self.A, self.C)
        self.len_BC = self.sideLen(self.B, self.C)

    def area(self):
        p = self.perimeter()/2
        return round(sqrt(p*(p-self.len_AB)*(p-self.len_AC)*(p-self.len_BC)) ,2)

    def perimeter(self):
        return self.len_AB+self.len_AC+self.len_BC

    def __mul__(self, other):
        a = self.A * other
        b = self.B * other
        c = self.C * other
        return Triangle(a, b, c)

    def __eq__(self, other):
        return self.A==other.A and self.B==other.B and self.C==other.C

    def __str__(self):
        return "Трикутник АВС. Вершини трикутника: A{0}, B{1}, C{2}. Сторони трикутника: AB={3} BC={4} AC={5}".format(self.A, self.B, self.C, self.len_AB, self.len_BC, self.len_AC)

