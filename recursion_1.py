def calculate_GCD(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return calculate_GCD(num2, (num1 % num2))
 
num1 = int(input('Enter the first positive integer value: '))
num2 = int(input('Enter the second positive integer value: '))
 
print('The greatest common divisor of %d and %d is %d.' %(num1, num2, calculate_GCD(num1, num2)))