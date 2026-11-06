# Calculator
mark = float(input("Enter mark (0-10): "))

if mark < 0 or mark > 10:
    print("Invalid mark: must be between 0 and 10.")
elif mark < 5:
    print("Fail / Insuficiente")
elif mark < 6:
    print("Pass / Suficiente")
elif mark < 7:
    print("Pass / Bien")
elif mark < 9:
    print("Very good / Notable")
else:
    print("Excellent / Sobresaliente")

# Leap year checker
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year / es un año bisiesto")
else:
    print(f"{year} is not a leap year / no es un año bisiesto")
    