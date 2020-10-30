def check(x,n,p):
    #Right Diagonal
    if x[p] == 1:
        if not(p%n)== 0:
            if x[p-1]==2:
                return False
        if int(p/n)>0:
            if x[p-n]==2:
                return False
            if not((p+1)%n)== 0:
                if x[p-n+1]==1:
                    return False
    #Left Diagonal
    elif x[p] == 2:
        if not(p%n)== 0:
            if x[p-1]==1:
                return False
        if int(p/n)>0:
            if x[p-n]==1:
                return False
            if not((p)%n)== 0:
                if x[p-n-1]==2:
                    return False
    return True
def extend(x,p,n,c,q):
    global s
    if q == c:
        print(x)
        s = s + 1
        return
    elif len(x) == n * n or (n * n - len (x)) < (c-q):
        return
    else:
        for i in [1,2,0]:
            x.append(i)
            l = len(x)-1
            if check(x,n,l) == True:
                if x[l] == 1 or x[l] == 2:
                    q = q + 1
                extend(x,p,n,c,q)
                if x[l] == 1 or x[l] == 2:
                    q = q - 1
            x.pop()
x = []
extend(x,p=0,n=5,c=16,q=0)
print("There are ", s, " solutions.")
