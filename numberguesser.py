import random

top_of_range = input("Give me a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please print number larger that 0 next time")
        quit()
    else:
        print('Please print number number next time')

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make me a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time')
        continue

    if user_guess == random_number:
        print("Well done")
        break
    elif user_guess > random_number:
        print('you were above the number')
    else:
        print('you were below the number')

print('you got it in',guesses,"guesses")