x=None
y=None
n=0
c=0
try:
    print('''Введите двочное число для перевода в десятичную систему.
    \n(Или нажмите Enter)''')
    x=bin(int(input(),2))
except ValueError:
    print('Ничего не ввели, или это не двоичное число\n')
try:
    print('''Введите десятичное число для перевода в двоичную систему.''')
    y=int(input(),10)
except ValueError:
    print('Ничего не ввели, или это не десятичное число')


if not x:
    pass
else:
     while n<=(len(x)-3):
         v=int(x[n+2])
         c=(c*2+v)
         n+=1


if not x:
    pass
else:
    print('Число ',x[2:],' в десятичном виде - это: ',c)



if not y:
    pass
else:
    n=y
    c=0
    l=[]
    while n>=1:
        if n%2>0:
            n=n//2
            l.append('1')
        elif n%2==0:
            l.append('0')
            n=n//2



if not y:
    pass
else:
    l.reverse()
    s=''.join(l)
    print('Число ',y,' в двоичном виде - это ', s)
