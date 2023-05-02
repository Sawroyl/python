#at first, counter is set 0
posi=0
zero=0
nega=0
while True:
    num=int(input('Enter any number.We will start count. When done, press 0 to stop:'))
    if num==0:
        break
    elif num>=1:
        posi+=1
    elif num<0:
        nega+=1
    else:zero+=1
print("Positive count is:",posi)
print("Negative count is:",nega)
print("Zero count is:",zero)

