import random
n = random.randint(1, 20)
life=4
for i in range(1, 6):
    guess = int(input("Guess any number: "))
    if guess > n and life>=1:
        print("TOO HIGH!!!!!!")
        print('you have', life, 'guesses left')
        life -= 1
    elif guess < n and life>=1:
        print("TOO LOW!!!")
        print('you have', life, 'guesses left')
        life -= 1
    elif n == guess:
        print("Congrats, you guessed right. YOU WIN!!")
    elif life==0:
        print('No guesses left. GAME OVER!!!!')

