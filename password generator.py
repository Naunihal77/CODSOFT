import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%&*"
password_length = int(input("Enter the length of the password : "))
a = "".join(random.sample(password,password_length))
print(f"your password is {a}")