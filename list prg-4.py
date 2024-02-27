n=int(input("enter the limit"))
l=[]
l1=[]
for i in range (n):
    j=int(input("enter the element"))
    l.insert(i,j)
for i in range (n):
    if l[i]%2 == 0:
     l1.insert(i,l[i])
l1.sort()
print(l1)
        

