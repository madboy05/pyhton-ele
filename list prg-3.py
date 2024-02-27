n=int(input("enter the limit"))
l=[]
l1=[]
for i in range (n):
    j=int(input("enter the element"))
    l.insert(i,j)
k=int(input("enter the number"))
for i in range (n):
    if l[i]<k:
     l1.insert(i,l[i])
print(l1)
        

