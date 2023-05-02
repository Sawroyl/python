try:
    n1 = int(input('Enter a number: '))
    n2 = int(input('Enter another number: '))
    div=n1/n2
    print(div)
except Exception as e:
    print("Error:Cannot divide by zero",e)

except ValueError:
    print("Error:Invalid integer entered.")