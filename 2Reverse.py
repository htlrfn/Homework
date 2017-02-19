l=[1, 2, 3, 8, 14, 89, 45,]
print(l)
n = int(len(l)/2)
d=-1
c=0
while n > 0:
    l[c],l[d]= l[d],l[c]
    c+=1
    d-=1
    n-=1
print(l)
