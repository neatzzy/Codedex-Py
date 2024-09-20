import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))

cpu = random.randint(1, 3)

if player == 1:
    print("You picked ✊")
    if cpu == 1:
        print("CPU picked ✊")
        print("It's a tie!")
    elif cpu == 2:
        print("CPU picked ✋")
        print("You lose!")
    else:
        print("CPU picked ✌️")
        print("You win!")
elif player == 2:
    print("You picked ✋")
    if cpu == 1:
        print("CPU picked ✊")
        print("You win!")
    elif cpu == 2:
        print("CPU picked ✋")
        print("It's a tie!")
    else:
        print("CPU picked ✌️")
        print("You lose!")
else:
    print("You picked ✌️")
    if cpu == 1:
        print("CPU picked ✊")
        print("You lose!")
    elif cpu == 2:
        print("CPU picked ✋")
        print("You win!")
    else:
        print("CPU picked ✌️")
        print("It's a tie!")