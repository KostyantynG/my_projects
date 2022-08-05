import math

N = int(input("Enter the number: \n"))
sum = 0

while N >= 1:
    sum += math.floor(N%10)
    N = math.floor(N/10)

print("The sum is ", sum)

