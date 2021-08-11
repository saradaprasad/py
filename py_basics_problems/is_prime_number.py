def is_prime(in_x):
    ctr=2
    i=2

    while(i < in_x):
        if(in_x%2==0):
            ctr+=1
        i+=1

        if(ctr==3):
            break;

    if(ctr==2):
        print("Prime Number!")
    else:
        print("Not a Prime Number")

x=input("Enter a number : ")
xn=int(x)
is_prime(xn)
