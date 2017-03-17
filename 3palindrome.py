def pal(x):
    y=int(len(x)/2)
    if x[:y] == x[::-1][:y]:
        print('Палиндром')
    else:
        print('Не палиндром')

pal(input(':>',))
