try:
    filename = "example.txt"
    file1 = open(filename, 'r')
    fileread = file1.read()
    print(fileread)
    file1.close()
except:
    print("Could not find file"+filename)
def extract_temp():
    final=fileread.split()
    for i in final:
        if i.isdigit():
            print(i)
extract_temp()