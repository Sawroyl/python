mul=1
counter=0
num=1
while counter<20:
    if num%5==0:
        mul=num*mul
        counter+=1
    num+=1
print(mul)