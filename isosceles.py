from triangle import Triangle
from point import Point
from math import sqrt

class Isosceles(Triangle):
    def __init__(self, a: Point, b: Point, c: Point):
        Triangle.__init__(self, a, b, c)
 

    def heigth(self):
        return self.area()/self.len_AC

    def __str__(self):
        if self.len_BC==self.len_AB:
            return ("Рівнобедерний трикутник з бічними сторонами: {0} та {1} та основою: {2}".format(self.len_AB, self.len_BC, self.len_AC))
        elif self.len_BC==self.len_AC:
            return ("Рівнобедерний трикутник з бічними сторонами: {0} та {1} та основою: {2}".format(self.len_AC, self.len_BC, self.len_AB))
        else:
            return ("Рівнобедерний трикутник з бічними сторонами: {0} та {1} та основою: {2}".format(self.len_AB, self.len_AC, self.len_BC))


