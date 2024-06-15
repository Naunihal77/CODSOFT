a = int(input())
b = int(input())
c = input()
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