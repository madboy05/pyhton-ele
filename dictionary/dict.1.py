s=input("enter a string ")
d={}
k=0
c=0
s1=""
for i in range(len(s)) :
    if s[i]!=" ":
        s1 =s1+s[i]
    else:
        d[k]=s1
        s1=""
        k=k+1
d[k]=s1
k=k+1   
for key in d:
    for i in range(k):
        if d[key] == d[i] and d[key] !=" ":
            c=c+1
            if c > 1:
                d[i]=" "
               
    if c>0:
        print(d[key],c)
        c=0

    