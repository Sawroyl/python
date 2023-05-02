def check_quotes(quote):
    count=0
    for char in quote:
        if char=="'":
            count+=1
        elif char=='"':
            count+=1
        return count%2==0

filename=open('example.txt','r')
quote=filename.read()
print(quote)
print(check_quotes(quote))