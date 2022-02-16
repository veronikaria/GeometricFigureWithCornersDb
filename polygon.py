from point import Point
from figure import Figure
from math import sqrt

class Polygon(Figure):
    def __init__(self, angles):
        Figure.__init__(self, angles)
 
    def whoamI(self):
        if self.angles == 3:
            return "Трикутник"
        elif self.angles == 4:
            return "Чотирикутник"
        elif self.angles == 5:
            return "Пятикутник"
        else: return "Багатокутник"

    def area(self):
        pass
 
    def perimeter(self):
        pass

    def sideLen(self, first: Point, second: Point):
        return sqrt( (second.x-first.x)**2 + (second.y-first.y)**2 )

    def __str__(self):
        return "Багатокутник"
    