with open('D:/Herald Week 1 Teaching Contents/Introductory programming Sujan Aryal/Week 7/input_file.TXT','r') as input_file:
    output_file=open('D:/Herald Week 1 Teaching Contents/Introductory programming Sujan Aryal/Week 7/output_file.TXT','w')
    line=input_file.readline()
    while line!="":
        output_file.write(line+'\n')
        line=input_file.readline()
        print(line)


