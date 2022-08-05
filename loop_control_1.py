berthYear = int(input("Enter the year of your birth: \n"))
while not 0 < berthYear <= 2022:
    print("Enter valid year \n")
    berthYear = int(input("Enter the year of your birth: \n"))

k = berthYear%12
if k == 0:
    chineseYear = "Monkey"
elif k%12 == 1:
    chineseYear = "Rooster"
elif k%12 == 2:
    chineseYear = "Dog"
elif k%12 == 3:
    chineseYear = "Pig"
elif k%12 == 4:
    chineseYear = "Rat"
elif k%12 == 5:
    chineseYear = "Ox"
elif k%12 == 6:
    chineseYear = "Tiger"
elif k%12 == 7:
    chineseYear = "Rabbit"
elif k%12 == 8:
    chineseYear = "Dragon"
elif k%12 == 9:
    chineseYear = "Snake"
elif k%12 == 10:
    chineseYear = "Horse"
elif k%12 == 11:
    chineseYear = "Goat"

print("{} - The year of the {}".format(berthYear, chineseYear))