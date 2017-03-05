import sys
from diary_parts import taskdt, storage
conn=storage.connect()
storage.initialize(conn)

l=('''Ежедневник. Выберите действие:
      1. Вывести список задач
      2. Добавить задачу
      3. Отредактировать задачу
      4. Завершить задачу
      5. начать задачу сначала
      6. Выход''')
x=None
tdate=None
while not x or x not in range (1,7):
    print(l)
    try:
        x = int(input('>',))
    except ValueError:
        print('Введите число от 1 до 6, сооветствующее пункту меню')

if x==6:
    print('Работа завершена, выходим.')
    sys.exit

if x==1:
    while tdate is None:
        tdate = (taskdt.tdate())        
    rows=storage.find_all_by_date(conn, tdate)
    print('''[ID]-[Задача]-[Дата]-[Статус]''')
    for row in rows:            
        print('\n[{row[id]}]-[{row[task]}]-[{row[taskdate]}]-[{row[status]}]'.format(row=row) )
if x==2:
    while tdate is None:
        print('''Введите дату, на которую нужно добавить задачу
Или нажмите Enter, если задачу нужно добавить на завтра''')
        tdate = (taskdt.tdate())
    status = '-'   
    task = (str(input('Текст задачи:',)))
    storage.add_entry(conn, task, tdate, status)
    
if x==3:
    print('''Редактирование задачи:
Введите Id задачи:''')
    pk=int(input('ID:',))
    data=str(input('Текст задачи:',))
    storage.change_task(conn,data,pk)
if x==4:
    print('''Завершение задачи:
Введите Id задачи:''')
    pk=int(input('ID:',))
    status = 'Выполнено'
    storage.change_status(conn, status, pk)

if x==5:
    print('''Начать задачу сначала:
Введите Id Задачи:''')
    pk=int(input('ID:',))
    status = '-'
    storage.change_status(conn, status, pk)

conn.close()
