from triangle import Triangle
from point import Point
import math

class Equilateral(Triangle):
    def __init__(self,a: Point, b: Point, c: Point):
        Triangle.__init__(self, a, b, c)
 
    def area(self):
        return (math.pow(self.len_AB,2)*(math.sqrt(3)))/4
 
    def height(self):
        return (math.sqrt(3)*self.len_AB)/2

    def __str__(self):
        return ("Рівносторонній трикутник з трьома рівними сторонами сторонами: {0}".format(self.len_AB))


