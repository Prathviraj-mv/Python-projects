import random

print("Random rgb color code\n")
gen =True
while gen:

    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)

    rgb =[r,g,b]
    print(f"the rgb color code is {rgb} ")
    print("To continue press y else n\n")
    cont =input(":").lower()

    if cont == "y":
        gen =True
    else:
        gen = False
