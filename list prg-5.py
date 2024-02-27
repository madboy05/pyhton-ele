n=int(input("enter the limit for first list"))
l=[]
l1=[]
l2=[]
for i in range (n):
    j=int(input("enter the element"))
    l.insert(i,j)
n1=int(input("enter the limit for first list"))
for i in range (n1):
    j=int(input("enter the element"))
    l1.insert(i,j)
k=0
for i in range(n):
    for j in range(n1):
        if l[i]==l1[j]:
            l2.insert(k,l[i])
            k=k+1
            break
        

print(l2)
        

