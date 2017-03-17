from datetime import datetime


x=(datetime.now().minute%5)


if x<3:
    print('Green')
else:
    print('Red')
