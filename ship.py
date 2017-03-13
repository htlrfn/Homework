from string import ascii_letters



def coords(n):
    x1 = [x for x in range (1, 11)]
    y1 = [y for y in ascii_letters[0:10]]
    d=[]
    z=0
    c=0
    while z in range(0, len(x1)):
        while c in range(0, len(y1)):
            d.append((y1[z],x1[c]))
            c+=1
        c=0
        z+=1
    yield d[n]
#Генератор координат: пока не совсем решил где будет нужен, например в интерфейсе,
    #предлагая атаковать дальше по линии или столбцу или расставлять корабли на поле пользователя
    #еще у каждой координаты появляется свой номер (0-99)
    
class Player(object):
    def __init__(self, name):
        self.name=name
    def attack(pos):
        pass

class Ship(object): 
    def __init__(self, size):
        self.size=size
    def damaged(pos):
        pass

class Field(object):
    def __init__(self):
        pass
    def place_ships():
        pass
