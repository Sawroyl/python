
list=['andrew','cyndy','emery','nicole','jason','brynn','bob','arthur','lyn']
lst=set()
vowels=['a','e','i','o','u']
for str in list:
    if str[0].lower() in vowels:
        lst.add(str)
print(lst)



