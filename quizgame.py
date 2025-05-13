print('welcome to my game')

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("great, lets go")
score = 0

answer = input("Question 1: Capital of wales? ")
if answer.lower() == "cardiff":
     print("correct")
     score += 1
else:
    print("wroooong")

answer = input("Question 2: What animal is on the Welsh flag? ")
if answer.lower() == "dragon":
     print("yes correct")
     score += 1
else:
    print("wroooong")

answer = input("Question 3: what animal has cubed poo? ")
if answer.lower() == "wombat":
     print("correct")
     score += 1
else:
    print("wroooong")

answer = input("what country has most islands in the world? ")
if answer.lower() == "sweden":
     print("yes correct, you have won the game")
     score += 1
else:
    print("wroooong byeeeee")

print("you got " + str((score/4)*100) + "%")