import sys
import math
print('Обозначьте координаты вершин треугольника. (Принимаются только целые числа)')
try:
    x1=int(input('Введите координату x, точки a '))
    y1=int(input('Введите координату y, точки a '))
    x2=int(input('Введите координату x, точки b '))
    y2=int(input('Введите координату y, точки b '))
    x3=int(input('Введите координату x, точки c '))
    y3=int(input('Введите координату y, точки c '))
except ValueError:
    print('Запустите программу еще раз, вы ввели некорректное значение (не целое число)')
    sys.exit()
l=[]
l1=math.fabs(math.sqrt((x2-x1)**2+(y2-y1)**2))
l.append(l1)
l2=math.fabs(math.sqrt((x3-x2)**2+(y3-y2)**2))
l.append(l2)
l3=math.fabs(math.sqrt((x3-x1)**2+(y3-y1)**2))
l.append(l3)
l4=sorted(l)
s1=round((l4[0])**2+(l4[1])**2)
s2=round((l4[2])**2)
if s1==s2:
    print('Треугольник - прямоугольный')
else:
    print('Треугольник - не прямоугольный')
