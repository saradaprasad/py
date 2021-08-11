def list_val_interchange():
    lst=["first",1,1.1,11,"lst"]
    size= len(lst)
    tmp=lst[0]
    lst[0]=lst[size-1]
    lst[size-1]=tmp
    print(size)
    for x in lst:
        print(x)

list_val_interchange()