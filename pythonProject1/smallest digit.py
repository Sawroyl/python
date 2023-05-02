n=int(input("Enter a number: "))
smallest=n%10
while n>0:
    digit=n%10
    if digit<smallest:
        smallest=digit
    n=n//10
print("smallest digit is: ",smallest)