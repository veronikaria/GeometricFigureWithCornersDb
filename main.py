import shelve

from triangle import Triangle
from isosceles import Isosceles
from equilateral import Equilateral
from quadrangle import Quadrangle
from point import Point
from pentagon import Pentagon

polygons=[]
exit = False
while exit==False:
    print("1. Довільний Трикутник")
    print("2. Рівнобедерний Трикутник")
    print("3. Рівносторонній Трикутник")
    print("4. Чотирикутник")
    print("5. П'ятикутник")
    choose= int(input("Оберіть номер фігури від 1 до 5 : "))
    if choose==1:
        x1, y1 = [int(x) for x in input("Координати вершини А трикутника АВС: ").split()]
        x2, y2 = [int(x) for x in input("Координати вершини В трикутника АВС: ").split()]
        x3, y3 = [int(x) for x in input("Координати вершини С трикутника АВС: ").split()]
        triangle = Triangle(Point(x1,y1), Point(x2, y2), Point(x3, y3))
        polygons.append(triangle)
        print("Ви ввели такий довільний трикутник: ")
        print(triangle)
        print("Периметер: ",triangle.perimeter())
        print("Площа: ", triangle.area())
        print("Помножимо на 3 всі координати:")
        print(triangle * 3)
        print()
    elif choose==2:
        x1, y1 = [int(x) for x in input("Координати вершини А трикутника АВС: ").split()]
        x2, y2 = [int(x) for x in input("Координати вершини В трикутника АВС: ").split()]
        x3, y3 = [int(x) for x in input("Координати вершини С трикутника АВС: ").split()]
        isosceles = Isosceles(Point(x1,y1), Point(x2, y2), Point(x3, y3))
        polygons.append(isosceles)
        print("Ви ввели такий рівнобедерний трикутник: ")
        print(isosceles)
        print("Периметер: ",isosceles.perimeter())
        print("Площа: ", isosceles.area())
        print("Помножимо на 8 всі координати:")
        print(isosceles * 8)
        print()
    elif choose==3:
        x1, y1 = [int(x) for x in input("Координати вершини А трикутника АВС: ").split()]
        x2, y2 = [int(x) for x in input("Координати вершини В трикутника АВС: ").split()]
        x3, y3 = [int(x) for x in input("Координати вершини С трикутника АВС: ").split()]
        equilateral = Equilateral(Point(x1,y1), Point(x2, y2), Point(x3, y3))
        polygons.append(equilateral)
        print("Ви ввели такий рівносторонній трикутник: ")
        print(equilateral)
        print("Периметер: ",equilateral.perimeter())
        print("Площа: ", equilateral.area())
        print("Помножимо на 5 всі координати:")
        print(equilateral * 5)
        print()
    elif choose==4:
        x1, y1 = [int(x) for x in input("Координати вершини А чотирикутника АВС: ").split()]
        x2, y2 = [int(x) for x in input("Координати вершини В чотирикутника АВС: ").split()]
        x3, y3 = [int(x) for x in input("Координати вершини С чотирикутника АВС: ").split()]
        x4, y4 = [int(x) for x in input("Координати вершини D чотирикутника АВС: ").split()]
        quadrangle = Quadrangle(Point(x1,y1), Point(x2, y2), Point(x3, y3),Point(x4, y4))
        polygons.append(quadrangle)
        print("Ви ввели такий довільний чотирикутник: ")
        print(quadrangle)
        print("Периметер: ",quadrangle.perimeter())
        print("Площа: ", quadrangle.area())
        print("Помножимо на 2 всі координати:")
        print(quadrangle * 2)
        print()  
    elif choose==5:
        x1, y1 = [int(x) for x in input("Координати вершини А пятикутника АВС: ").split()]
        x2, y2 = [int(x) for x in input("Координати вершини В пятикутника АВС: ").split()]
        x3, y3 = [int(x) for x in input("Координати вершини С пятикутника АВС: ").split()]
        x4, y4 = [int(x) for x in input("Координати вершини D пятикутника АВС: ").split()]
        x5, y5 = [int(x) for x in input("Координати вершини E пятикутника АВС: ").split()]
        pentagon = Pentagon(Point(x1,y1), Point(x2, y2), Point(x3, y3),Point(x4, y4), Point(x5, y5))
        polygons.append(pentagon)
        print("Ви ввели такий довільний п'ятикутник: ")
        print(pentagon)
        print("Периметер: ",pentagon.perimeter())
        print("Площа: ", pentagon.area())
        print("Помножимо на 10 всі координати:")
        print(pentagon * 10)
        print()      
    answer = input("Бажаєте продовжити? yes\\no: ")
    if answer.lower()=='n' or answer.lower()=='no':
        exit=True


triangle1 = Triangle(Point(1,2), Point(5, 2), Point(3, 11))
triangle2 = Triangle(Point(1,4), Point(4, 4), Point(2, 9))
isoscele1 = Isosceles(Point(2,2), Point(4, 2), Point(3, 4))
quadrangle1 = Quadrangle(Point(-1,-10), Point(2, 4), Point(3,7),Point(5, 6))
pentagon1 = Pentagon(Point(-8,-5), Point(5, 4), Point(2,37),Point(4, 8), Point(12,34))
polygons.append(triangle1)
polygons.append(triangle2)
polygons.append(isoscele1)
polygons.append(quadrangle1)
polygons.append(pentagon1)

with shelve.open('test.db') as db:
    triangles=[]
    pentagons=[]
    quadrangles=[]
    id_triangle = 1
    id_quadrangle = 1
    id_pentagon = 1
    for ob in polygons:
        if type(ob)==Triangle or type(ob)==Isosceles or type(ob)==Equilateral:
            js = { 
            'id': id_triangle,
            'angles':ob.angles,
            'type' : str(type(ob).__name__),
            'points': {'A': str(ob.A), 'B': str(ob.B), 'C': str(ob.C)},
            'sides': {'AB':ob.len_AB, 'AC':ob.len_AC, 'BC':ob.len_BC},
            'perimeter':ob.perimeter(), 
            'area':ob.area(), 
            'details': str(ob) 
            }
            if (type(ob)==Isosceles):
                js['height']=ob.heigth()
            triangles.append(js)
            id_triangle+=1
        elif type(ob)==Quadrangle:
            quadrangles.append( { 
            'id': id_quadrangle,
            'angles':ob.angles,
            'points': {'A': str(ob.A), 'B': str(ob.B), 'C': str(ob.C), 'D':str(ob.D)},
            'sides': {'AB':ob.len_AB, 'BC':ob.len_BC, 'CD':ob.len_CD, 'AD': ob.len_AD},
            'perimeter':ob.perimeter(), 
            'area':ob.area(), 
            'details': str(ob) })
            id_quadrangle+=1
        elif type(ob)==Pentagon:
            pentagons.append( { 
            'id': id_pentagon,
            'angles':ob.angles,
            'points': {'A': str(ob.A), 'B': str(ob.B), 'C': str(ob.C), 'D':str(ob.D), 'E':str(ob.E)},
            'sides': {'AB':ob.len_AB, 'BC':ob.len_BC, 'CD':ob.len_CD, 'DE': ob.len_DE, 'AE': ob.len_AE},
            'perimeter':ob.perimeter(), 
            'area':ob.area(), 
            'details': str(ob) })
            id_pentagon+=1
    db['Triangles'] = triangles
    db['Quadrangles'] = quadrangles
    db['Pentagons'] = pentagons

with shelve.open('test.db') as db:
    print("\tТрикутники")
    print(db['Triangles'])
    print("\tЧотирикутники")
    print(db['Quadrangles'])
    print("\tП'ятикутники")
    print(db['Pentagons'])


