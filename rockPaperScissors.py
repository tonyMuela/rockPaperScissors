import random

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))

my_choice = random.randint(0,2)

if choice == 0:
    print("You Chose rock")
elif choice == 1:
    print("you chose paper")
elif choice == 2:
    print("you chose scissors")

if my_choice == 0:
    print("I Chose rock")
elif my_choice == 1:
    print("I chose paper")
elif my_choice == 2:
    print("I chose scissors")

if choice == 0 and my_choice == 2:
    print("You win")
elif choice < my_choice:
    print("You lose")
elif choice == my_choice:
    print("it's a tie")
