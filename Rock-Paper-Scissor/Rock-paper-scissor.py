import random
from time import sleep
userinput = input("do you want to play a game? [Y/N] :")


def main():
    if (userinput == "y" or userinput == "Y"):
        print("okay cool \n we are going to play Rock paper scissor")
        sleep(1)
        print("ready")
        sleep(1)
        print("Rock")
        sleep(1)
        print("Paper")
        sleep(1)
        print("Scissor")
        sleep(1)
        print("Shoot")
        sleep(1)
        Rock_Paper_Scissor()


def Rock_Paper_Scissor():
    userinput = input("what did you choose: ")
    Robot = random.sample(['Rock', 'paper', 'Scissor'], k=1)
    if(userinput == Robot):
        print('Oh it is a draw lets plat again')
        sleep(1)
        Rock_Paper_Scissor()


main()
