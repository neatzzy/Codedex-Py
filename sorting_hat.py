gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
flag = True

while flag:
    print("Q1) Do you like Dawn or Dusk?")
    print("1) Dawn")
    print("2) Dusk")
    answer1 = int(input("Enter the number of your choice: "))

    if answer1 == 1:
        gryffindor += 1
        ravenclaw += 1
        flag = False
    elif answer1 == 2:
        hufflepuff += 1
        slytherin += 1
        flag = False
    else:
        print("Wrong input")
        print(" ")

print(" ")
flag = True

while flag:
    print("Q2) When I'm dead, I want people to remember me as:")
    print("1) The Good")
    print("2) The Great")
    print("3) The Wise")
    print("4) The Bold")
    answer2 = int(input("Enter the number of your choice: "))

    if answer2 == 1:
        hufflepuff += 2
        flag = False
    elif answer2 == 2:
        slytherin += 2
        flag = False
    elif answer2 == 3:
        ravenclaw += 2
        flag = False
    elif answer2 == 4:
        gryffindor += 2
        flag = False
    else:
        print("Wrong input")
        print(" ")

print(" ")
flag = True

while flag:
    print("Q3) Which kind of instrument most pleases your ear?")
    print("1) The violin")
    print("2) The trumpet")
    print("3) The piano")
    print("4) The drum")
    answer3 = int(input("Enter the number of your choice: "))

    if answer3 == 1:
        slytherin += 4
        flag = False
    elif answer3 == 2:
        hufflepuff += 4
        flag = False
    elif answer3 == 3:
        ravenclaw += 4
        flag = False
    elif answer3 == 4:
        gryffindor += 4
        flag = False
    else:
        print("Wrong input")
        print(" ")

print(" ")

if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
    print("You belong to Gryffindor!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("You belong to Hufflepuff!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("You belong to Ravenclaw!")
elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    print("You belong to Slytherin!")
