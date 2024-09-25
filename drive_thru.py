def welcome():
    print("Hello, Welcome to McDonald's!")
    print("====")
    print("MENU")
    print("====")
    print("1) BigMac")
    print("2) Fries")
    print("3) Soda")
    print("4) McFlurry")
    print("5) Apple Pie")

def get_item(x):
    if x == 1:
        return "BigMac"

    elif x == 2:
        return "fries"

    elif x == 3:
        return "soda"
        
    elif x == 4:
        return "McFlurry"
        
    else:
        return "apple pie"

welcome()   

op = int(input('What would you like to order? '))

item = get_item(op)

print(f"Here is your {item}. Enjoy!")