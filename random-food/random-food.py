import random

def func():
    kind = input("what food do you want to eat [b , l , d]:")
    if kind == "b":
        breakfast()
    elif kind == "l":
        lunch()
    elif kind == "d":
        dinner()
    else:
        print("sorry , still not coded")

def breakfast():
    culture_1 = input("which culture do you want to eat from [egypt , USA ] :")
    if culture_1.lower() == "egpyt" or "egp" or "eg" or "egpt":
        # egbt = egyptian breakfast text
        egbt = open("egyptian-breakfast.txt")
        # egbr = egyptian breakfast read
        egbr = random.choice(egbt.read().splitlines())
        print(egbr)

def lunch():
    culture_2 = input("which culture do you want to eat from [egypt , USA ] :")

def dinner():
    culture_3 = input("which culture do you want to eat from [egypt , USA ] :")

func()
    