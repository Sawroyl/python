num = int(input("Enter a positive integer: "))
if num >= 1:
    print("Multiplication table of", num, 'is: ')
    for i in range(1, 11):
        print(num, '*', i, '=', num * i)
while num < 1:
    print('Wrong input')
    int(input('Please enter a positive integer:'))
    if num >= 1:
        print("Multiplication table of", num, 'is: ')
        for i in range(1, 11):
            print(num, '*', i, '=', num * i)
