input_file_opened = False
while not input_file_opened:
    try:
        file_name=input('Enter filename: ')
        input_file= open(file_name, 'r')
        print(input_file.read())
        input_file_opened = True
        input_file.close()
    except:
        print("Input file not found: ")