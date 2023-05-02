def multiplication_table(n):
    #print header row
    print(' ',end="\t")
    for i in range(1,11):
        print(i,end=('\t'))
    print()

    for j in range(1,11):
        print(j,'\t')
        for k in range(1,11):
            print(k*j,end='\t')
multiplication_table(1)