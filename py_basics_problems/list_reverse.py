def lst_reverse(lst):
    print(lst, " Prior to reversing list")
    rlst=[]
    for ele in reversed(lst):
        rlst.append(ele)

    print(rlst," Post reversing list")

    print(rlst[::-1]," Reversing again")

lst=[10,20,30,40,50,60]
lst_reverse(lst)
