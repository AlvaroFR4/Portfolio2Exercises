#Write a program that asks for a password, compares it with one stored in a constant and prints "Access
#granted" or "Wrong password". The comparison must ignore upper and lower case.
PASSWORD = "pipopi1234"

user_password = input("Enter password: ")

if user_password.lower() == PASSWORD.lower():
    print("Access granted")
else:
    print("Wrong password")