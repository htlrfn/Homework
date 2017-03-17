from datetime import date

td=date.today()
ny=date(td.year + 1, 1 ,1)

print('До нового года осталось {} дней'.format((ny-td).days))
