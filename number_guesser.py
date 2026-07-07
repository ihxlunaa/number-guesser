import random
ans = random.randint(1,100)
print('Guess a number from 1 to 100: ')
guess = 0
count = 0
while guess != ans:
    guess = int(input())
    count += 1
    if guess < ans:
        print('Guess a bigger number')
    elif guess > ans:
        print('Guess a smaller number')
print('Bingo! Number of guesses:', count)
