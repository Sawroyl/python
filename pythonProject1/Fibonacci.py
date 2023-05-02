a=0
b=1
n=int(input('Enter a number: '))
if n<=0:
    print('Please enter a positive number.')
elif n==1:
    print('Fibonacci series: ',a)
else:
    print(a,b,end='\t')
    for i in range(2,n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
