list = []
num=input("Enter integers for list, with space in between: ")
numlist=num.split()
for i in numlist:
    if int(i)>100:
        list.append('over')
    elif int(i)>0 and int(i)<100:
        list.append((i))
    else:
        print('Invalid number.')
print(list)