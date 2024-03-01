d={}
l={}
f=True
while (f==True):
    s=input("Enter team or stop :")
    if s=='stop':
        f==False
        break   
    n=int(input("enter no. of games won"))
    n2=int(input("enter no. of games lost"))
    d[s]=n
    l[s]=n2
max=0
min=0
for key in d:
    print(key)
    if max<d[s]:
        max=d[s]
    if min>l[s]:
        min=l[s]
print(max)
print(min)