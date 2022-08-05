import math

number = int(input("Enter any positive real number: \n"))

H = math.floor((number - number%100)/100) 
#hundreds of a number
T = math.floor((number%100 - number%10)/10) 
#tens of a number
U = math.floor(number%10)
# = units of a number

print("The units are: ",H ,T, U)
print("Sum of all units = ", H+T+U)