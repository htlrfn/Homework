x=int(input('x :> ',))
y=int(input('y :> ',))

def quart(x,y):
    if x==0 and y==0:
        z=0
    elif x==0 or y==0:
        z=5
    elif x > 0 and y >0:
        z=1
    elif x<0 and y<0:
        z=3
    elif x>0 and y<0:
        z=4
    elif x<0 and y>0:
        z=2
    return z

q=quart(x,y)

if q==0:
    print('Начало координат')
elif q==5:
    print('На оси')
else:
    print('Точка находится в {} чеверти'.format(q))
