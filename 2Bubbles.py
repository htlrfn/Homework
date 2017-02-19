l=[1, 2, 3, 8, 14, 89, 45]
print(l)
c=0
n=1
while n<len(l)-1:
    while c < len(l)-n:
        if l[c]>l[c+1]:
            l[c],l[c+1]=l[c+1],l[c]
            c+=1
        elif l[c]<=l[c+1]:
            c+=1
    n+=1
    c=0
print(l)
