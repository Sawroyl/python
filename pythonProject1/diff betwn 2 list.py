def listdif(list1,list2):
    dif1=list(set(list1)-set(list2))
    dif2=list(set(list2)-set(list1))
    return dif1,dif2
list1=["red", "orange", "green", "blue", "white"]
list2=["black", "yellow","green", "blue"]
dif1,dif2=listdif(list1,list2)
print("Color1-Color2",dif1)
print("Color2-Color1",dif2)