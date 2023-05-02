def reduce_spaces():
    try:
        filename="example.txt"
        file1=open(filename,'r')
        fileread=file1.read()
        file2=fileread.replace(' ','')
        return file2
    except:
        print("File not found")
print (reduce_spaces())