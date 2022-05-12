import random
from time import sleep, time
print("lets play rock paper scissors where R is for rock and p for paper and s for scissors")


def play():
    Robot = random.choice(['r', 'p', 's'])
    userinput = input("what did you choose [r , p , s]: ")
    if userinput == Robot:
        return 'it \'s a tie'
    if is_win(userinput, Robot):
        return 'you won!'
    return 'You lost!'


def is_win(userinput, Robot):
    if (userinput == 'r' and Robot == 's') or (userinput == 's' and Robot == 'p') or (userinput == 'p' and Robot == 'r'):
        return True


def main():
    print(play())
    sleep(2)
    main()


main()
