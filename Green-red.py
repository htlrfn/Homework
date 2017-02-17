from datetime import datetime
currmin = datetime.now().minute
n=0
green=[]
red=[]
for z in range (60):
	n+=1
	if n in range (4):
		green.append(z)
	else:
		red.append(z)
		if n >4:
			n=0
if currmin in green:
    print ('Тeкущее время:',datetime.now().hour,':',currmin, '\nЗеленый - можно ехать')
elif currmin in red:
    print ('Тeкущее время:',datetime.now().hour,':',currmin, '\nКрасный! Ждем зеленого')
else:
    print ('Вы вне времени - вам можно все:)')
input('\n\nНажмите Enter')
