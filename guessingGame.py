import random

chances = 5
user_input = None

rand_num = random.randint(1, 9)
# print(rand_num)
try: 
    while chances != 0:
        user_input = int(input("Enter your guess(1-9): "))
        if int(user_input) == int(rand_num):
            print("You win!")
            exit()
        else:
            print("You missed!")
            chances -= 1

        print("You had " + str(chances) + " chances left")

except ValueError:
    print("Please enter a number, not a string")
    exit()
    