phrase="Ram is a student of Herald college. He is widely placed in college and is a good student ."
dict={}
word= phrase.split()
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)