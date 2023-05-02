filename=open('example.txt', 'r')
fileread=filename.read()
print(fileread)
def count_letters(line):
    dict={}
    file=fileread.lower()
    for i in line:
        if file in dict:
            dict[file]+=1
        else:
            dict[file]=1
    return list(dict.items())
print(count_letters(fileread))

