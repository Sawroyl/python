lst=[]
listofdicts=[{'name':'Emma','age':18,},{'name':'Jack','age':17,},{'name':'Andrew','age':21,},]
for ppl in listofdicts:
    if ppl['age']>18:
         lst.append(ppl)
print('list of dictionary with only 18+ people is: ',lst)
