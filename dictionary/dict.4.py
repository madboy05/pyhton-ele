stock={'pencil':4,'book':5,'rubber':3,'pen':7}
price={'pencil':7,'book':35,'rubber':5,'pen':15}
bill=0
print("enter purchase items and quantity and if you want to stop enter stop:")
f=True
while (f==True):
    s=input("Enter purchase item or stop purchase:")
    if s == 'stop':
         f==False
         break
     
    if(stock[s]==0 or stock[s]==""):
        print("stock not available")
        continue
    q=int(input("Enter quantity"))
    p=int(stock[s])

    if (p< q):
        print("stock not available")
        continue
    else:
        bill=bill+price[s]*int(q)
        stock[s]=stock[s]-int(q)

print("total bill is",bill)
