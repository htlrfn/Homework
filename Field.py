y=input ('Введите площадь участка в сотках\nПо умолчанию:10\n')
if not y:
    y=10
x=float(y)*100
grx=input('Введите длину грядки в метрах\nПо умолчанию:15\n')
if not grx:
    grx=15
gry=input('Введите ширину грядки в метрах\nПо умолчанию:25\n')
if not gry:
    gry=25
gr=float(grx)*float(gry)
while x>gr:
    x=x-gr
x=float(x)
print ('При размере грядок',grx,'м.*',gry,'м.\n на вашем участке в ',y,'соток останется\n',round(x,2),'квадратных метров свободно')
