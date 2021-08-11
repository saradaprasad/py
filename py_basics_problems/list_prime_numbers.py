def print_prime(xn,yn):
    ctr=2
    lst=[]
    while(xn <= yn ):
        i=2
        zn=xn
        ctr=2
        while(i < zn):
            if(zn % i == 0):
                ctr+=1
            i+=1
        if(ctr == 2):
            lst.append(xn)
        xn+=1

    for x in lst:
        print(x)

x,y=input("Print prime numbers between : ").split()
xn=int(x)
yn=int(y)
print_prime(xn,yn)