if __name__=='__main__':
    print('Модуль получения даты для diary')



import sys
from datetime import datetime


def tdate (cyear=None, cmonth=None, cdate=None):
    cdt = datetime.now()
    print('''Введите год (например 2017),
или нажмите Enter если год - {} '''.format(cdt.year))
    try:
        cyear=int (input('>',))
    except ValueError:
        print('год - {}\n'.format(cdt.year))
        cyear = cdt.year
    print('''Введите месяц (например 03),
или нажмите Enter если месяц - {} '''.format(cdt.month))
    try:
        cmonth = int (input('>'),)
    except ValueError:
        print('месяц - {}\n'.format(cdt.month))   
        cmonth = cdt.month
    print('''ведите дату (например 05),
или нажмите Enter если дата - {}'''.format(cdt.day))
    try:
        cdate= int (input('>'),)
    except ValueError:
        print('дата - {}\n'.format(cdt.day))    
        cdate = cdt.day
    comb=str('{} {} {}'.format(cdate, cmonth, cyear))
    try:
        tdate=(datetime.strptime(comb,'%d %m %Y')).date()
        print (tdate)        
    except (ValueError, UnboundLocalError):    
        print('''
***Некорректно введена дата***
''')
        tdate=None
    return tdate
