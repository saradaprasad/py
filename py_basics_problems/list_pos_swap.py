def swap(list,pos1,pos2):
    print(list, " <-- Pre  Swapping")
    list[pos1],list[pos2] = list[pos2],list[pos1]
    print(list,"  <-- Post Swapping")

list= [1.0,2.0,3.0,4.0,5.0]
pos1,pos2= 2, 5
swap(list,pos1-1,pos2-2)

