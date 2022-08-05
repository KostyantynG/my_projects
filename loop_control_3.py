S = int(input("Enter the distance that driver has covered: \n"))

while not S > 0:
    print("Enter positive distance")
    print()
    S = int(input("Enter the distance that driver has covered: \n"))

if  S/0.5 > 45:
    print("Driver violated the law")
else:
    print("Driver's speed is within limits")
