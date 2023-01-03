print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

num = 10
i = 0
guess_limit = 3
guess = 0

while i < guess_limit:
    guess = int(input("Enter your guess: "))
    i += 1
    if guess == num:
        print("Congratulations! You've guessed it right!")
        break
    elif guess < num:
        print("Too low!")
        continue
    elif guess > num:
        print("Too high!")
        continue

if (i == guess_limit & guess != num):
    print("Sorry, you lose!")