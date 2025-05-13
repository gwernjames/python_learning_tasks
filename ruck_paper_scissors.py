import random

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissors']

while True:
    user_input = input('type rock/paper/scissors or Q to quit: ').lower()
    if user_input == str('q'):
        break

    if user_input not in options:
        print("not a valid option")
        continue

    random_number = random.randint(0,2)
    # 0 = rock, 1 = paper, 2 = scissors
    computer_guess = options[random_number]
    print("computer picked: ",computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("you won!")

print('cheers')