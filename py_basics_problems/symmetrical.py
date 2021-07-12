def symmetrical(a):
    str_i=a
    n=len(str_i)
    if (n%2==0):
        mid=n//2
    else:
        mid=n//2+1
    start1=0
    start2=mid
    flag=0

    while(start1 < mid and start2 < n):
        if(str_i[start1]==str_i[start2]):
            start1+=1
            start2+=1
        else:
            flag=1
            break

    if(flag==0):
        print("Symmetrical String")
    elif(flag==1):
        print("Asymetircal String")

a=input("Enter a string :")
symmetrical(a)

