month = int(input("Enter the number of month: \n"))


while not 1 <= month <= 12:
    print()
    print("Enter the number from 1 to 12")
    print()
    month = int(input("Enter the number of month: \n"))

if 3 <= month <= 5:
    print()
    print("Spring")
elif 6 <= month <= 8:
    print()
    print("Summer")
elif 9 <= month <= 11:
    print()
    print("Autumn")
elif 0 < month <= 2 or month == 12:
    print()
    print("Winter")