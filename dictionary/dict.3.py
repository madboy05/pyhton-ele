x={'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
d={'k4': 'v4', 'k3': 'v5', 'k1': 'v1'}
c=0
for key in d:
    for i in x:
        if d[key] == x[i] and x[i] !=" ":
            c=c+1
            if c > 1:
                x[i]=" "     
    if c > 0:
         print(d[key])
         c=0