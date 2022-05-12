import random
userinput = input("do you want to play a game? [Y/N] :")
if (userinput == "y" or userinput == "Y"):
    print("okay cool \n we are going to play Rock paper scissor")
    print("ready")
    print("Rock")
    print("Paper")
    print("Scissor")
    print("Shoot")
    userinput = input("what did you choose: ")
    Robot = random.choice(['Rock', 'paper', 'Scissor'])
