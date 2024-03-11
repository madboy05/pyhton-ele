l={}
f=True
l1=[]
l2=[]
l3=[]
while (f==True):
    s=input("Enter team or stop :")
    if s=='stop':
        f==False
        break 
    n=int(input("enter no. of games won:"))
    n2=int(input("enter no. of games lost:"))
    l1.append(n)      
    l2.append(n2)
    l3.append(s)
    l[s]=[n,n2]    
for key in l:
    print(key)
print('team with greatest wins:',l3[l1.index(max(l1))])
print('team with greatest loss:',l3[l2.index(max(l2))])
s=input("Enter team to find win percentage")
l4=l[s]
print(l4)
print('win percentage:',float((l4[0])/(l4[0]+l4[1]))*100)
