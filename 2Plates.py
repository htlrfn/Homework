plates=(int(input('Введите количество тарелок: ')))
fairy =(float(input('Введите количесво моющего средства: ')))
while fairy > 0 and plates > 0:
    plates = plates-1
    fairy = fairy - 0.5
    print('\nВымыта одна тарелка, еще осталось вымыть: ', plates,
          '\nМоющего средства осталось: ', fairy)
    if plates==0 and fairy ==0:
        print('\nГотово, все тарелки вымыты, моющее средство закончилось')
    elif plates == 0:
        print('\nТарелки закончились, осталось еще ',fairy,' моющего средства')
    elif fairy ==0:
        print('\nМоющее средство закончилось, не вымыто тарелок: ', plates)
