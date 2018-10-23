print("Welcome to the game of Nim!\nThe rules are simple, there are 15 matches in a pile.\nThe goal is to make your opponent take the last match.\nYou are alllowed to take the amount between 1 and 3")

run = True
mleft = 15
playerlastturn = 0



def ComputerTurn():
    global mleft
    global playerlastturn
    global run
    if not run:
        return 0
    print("Its Computers Turn!")
    if checkLost("pc"):
        return 0
    took = 5 - playerlastturn
    if took > 3:
        took=3
    if took < 1:
        took = 1
    if (mleft - took) == 0:
        took = 1
    if (mleft- took)<1:
        took = 3 - playerlastturn
    mleft -= took
    print("Computer took " + str(took) + " matches!")

def PlayerTurn():
    global mleft
    global playerlastturn
    global run
    if not run:
        return 0
    print("Its your turn!")
    if checkLost("player"):
        return 0;
    took = int(input("How many matches do you take? (1-3): "))
    if took > 3 or took < 1:
        print("Did you read the rules? Take between 1 and 3 matches!")
        return 0;
    print("You took " + str(took) + " matches!")
    mleft -= took
    playerlastturn = took
    return 1

def checkLost(player):
    global run
    #player is a string of the player who we are checking
    if mleft > 1:
        return False
    if player == "player":
        print("You Lost!!!!")
        run = False
        return True
    elif player == "pc":
        print("You Won!!")
        run = False
        return True
    else:
        print("ERORR WTF DID YOU MESS WITH MY CODE?")
        return False


while run:
    print("There are " + str(mleft) + " matches left!")
    PlayerTurn()
    ComputerTurn()
