list = []
while True:
    num = input("Enter an integer or 'press 0 to quit': ")
    inte = int(num)
    if inte > 100:
        list.append('over')
    elif inte > 0 and inte < 100:
         list.append(inte)
    elif inte == 0:
        break
    else:
        print("Please enter a valid number.")
print(list)
