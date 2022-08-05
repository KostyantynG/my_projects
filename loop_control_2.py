chinese_years = {
    0: 'Monkey',
    1: 'Rooster',
    2: 'Dog',
    3: "Pig",
    4: "Rat",
    5: "Ox",
    6: "Tiger",
    7: "Rabbit",
    8: "Dragon",
    9: "Snake",
    10: "Horse",
    11: "Goat",
}
 
year = int(input("Enter the year: "))
while not 0 <= year < 2022:
    print('Enter the correct value')
    year = int(input("Enter the year: "))
 
k = year % 12
print("{} - The year of the {}.".format(year, chinese_years[k]))