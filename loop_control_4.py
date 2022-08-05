purchase = int(input("Enter the value of purchase in $: \n"))
discount = 0

while not purchase > 0:
    print("Enter positive value")
    purchase = int(input("Enter the value of purchase: \n"))

if purchase < 100:
    discount = purchase*0.05
    purchase -= discount
elif 100 <= purchase <= 200:
    discount = purchase*0.10
    purchase -= discount
else:
    discount = purchase*0.15
    purchase -= discount

print("Your discount is {} $ and your purchase cost is {} $".format(discount, purchase))
