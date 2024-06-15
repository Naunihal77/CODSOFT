a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter the operand: ")
if c == "+":
    print(a+b)
elif c == "*":
    print(a*b)
elif c == "-":
    print(a-b)
elif c == "/":
    if a == 0:
        print("0")
    elif b == 0:
        print("undefined")
    else:
        print(a/b)
