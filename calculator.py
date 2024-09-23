def add(x,y):
    return int(x) + int(y)

def sub(x,y):
    return int(x) - int(y)

def mul(x,y):
    return int(x) * int(y)

def div(x,y):
    return float(x) / float(y)

def exp(x,y):
    return int(x) ** int(y)

print("==========")
print("CALCULATOR")
print("==========")
print(" ")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Exponential")
print(" ")
op = int(input("Enter the desired operation: "))
ab = input("Enter two numbers: ").split()
a,b = ab


if op == 1:
    res = add(a,b)
    print(f"The result is {res}")

elif op == 2:
    res = sub(a,b)
    print(f"The result is {res}")

elif op == 3:
    res = mul(a,b)
    print(f"The result is {res}")

elif op == 4:
    res = div(a,b)
    print(f"The result is {res:.2f}")

elif op == 5:
    res = exp(a,b)
    print(f"The result is {res}")