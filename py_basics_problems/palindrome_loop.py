def palindrome(in_var):
    var=in_var
    start=0
    print(len(var))
    last=len(var)-1
    mid=(len(var)-1)//2
    flag=0
    print('start : ',start,' last :',last,' mid :',mid,' flag :',flag)
    while(start < mid):
        if(var[start]==var[last]):
            start+=1
            last-=1
        else:
            flag=1
            break

    if (flag==1):
        print("Not a palindrome numer!")
    else:
        print("A Palindrome Number")

var=input("Enter a string :")
var=var.lower()
palindrome(var)