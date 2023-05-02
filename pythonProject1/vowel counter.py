word=input('Enter a word: ')
counter=0
vowels='AEIOUaeiou'
for character in word:
    if character in vowels:
        counter+=1
print(counter)