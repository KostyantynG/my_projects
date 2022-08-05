amount = int(input("How may dollars does Mary have?\n"))
cost = 2
count = 0
sum = 0
while amount - sum >= cost:
        count += 1
        sum += cost
if amount%2 == 0:
    print("She can buy", count, "candies")
else:
    print("She can buy", count, "candies and 1 dollar will remain")