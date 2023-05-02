num = int(input("Enter any number: "))
if num<0:
    print("Please enter a positive number: ")
elif num==0:
    print('Factorial of',num,'=',num)
else:
    facto=1
    for i in range(1,num+1):
        facto=facto*i
    print('The factorial of',num,'is',facto)
