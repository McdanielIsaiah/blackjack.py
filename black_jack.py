import random
pwins = 0
aiwins = 0
playerScore = 0
aiScore = 0
print("Welcome to BlackJack")
def gameStart():
    global playerScore
    global aiScore
    #Player game start
    prando1 = random.randint(1, 13)
    prando2 = random.randint(1, 13)
    print("Player1 got a ")
    print(faceCards(prando1), cardTypes())
    print(faceCards(prando2), cardTypes())
    if(prando1 == 11):
        prando1 = 10
    elif(prando1 == 12):
        prando1 = 10
    elif(prando1 == 13):
        prando1 = 10

    if(prando2 == 11):
        prando2 = 10
    elif(prando2 == 12):
        prando2 = 10
    elif(prando2 == 13):
        prando2 = 10
    playerScore = prando1 + prando2
    print(playerScore)
    print(" ")
    #AI game start
    airando1 = random.randint(1, 13)
    airando2 = random.randint(1, 13)
    print("AI got a ")
    print(faceCards(airando1), cardTypes())
    print(faceCards(airando2), cardTypes())
    if(airando1 == 11):
        airando1 = 10
    elif(airando1 == 12):
        airando1 = 10
    elif(airando1 == 13):
        airando1 = 10

    if(airando2 == 11):
        airando2 = 10
    elif(airando2 == 12):
        airando2 = 10
    elif(airando2 == 13):
        airando2 = 10
    aiScore = airando1 + airando2
    print(aiScore)

def playerhit():
    global playerScore
    pnewcard = random.randint(1, 13)
    print(faceCards(pnewcard), cardTypes())
    if(pnewcard == 11):
        pnewcard = 10
    elif(pnewcard == 12):
        pnewcard = 10
    elif(pnewcard == 13):
        pnewcard = 10
       
    
    playerScore += pnewcard
    print(playerScore)

def aihit():
    global aiScore
    ainewcard = random.randint(1, 13)
    print(faceCards(ainewcard), cardTypes())
    if(ainewcard == 11):
        ainewcard = 10
    elif(ainewcard == 12):
        ainewcard = 10
    elif(ainewcard == 13):
        ainewcard = 10
    aiScore += ainewcard
    print(aiScore)

def cardTypes():
    allCard = random.randint(1,4)
    if(allCard == 1):
        return "of hearts"
    elif(allCard == 2):
        return "of dimands"
    elif(allCard == 3):
        return "of spades"
    elif(allCard == 4):
        return "of clubs"

def faceCards(rando):
    if(rando == 11):
        return "Jack"
    elif(rando == 12):
        return "Queen"
    elif(rando == 13):
        return "King"
    elif(rando == 1):
        return "ace"
    else:
        return rando
    
def playergameLoop():
    while True:
        if(playerScore > 21):
            return
        elif(playerScore == 21):
            print("BlackJack")
            return
        decide = input("Hit or Pass: ")
        if(decide == "Hit" or decide == "hit"):
            playerhit()
        elif(decide == "Pass" or decide == "pass"):
            return
        elif(decide != "Hit" or decide != "hit"):
            print("Retry. Hit or Pass: ")

def aiGameloop():
    global playerScore
    global aiScore
    global pwins
    global aiwins
    while True:
        if(playerScore > 21):
            print("the player had: ", playerScore)
            print("the Ai had: ", aiScore)
            print("AI Wins")
            aiwins += 1
            return
        elif(aiScore > playerScore and aiScore <= 21):
            print("the player had: ", playerScore)
            print("the AI had: ", aiScore)
            print("AI Wins")
            aiwins += 1
            return
        elif(playerScore > aiScore and playerScore <= 21):
            print("the player had: ", playerScore)
            print("the AI had: ", aiScore)
            print("Player Wins")
            pwins += 1
            return
        elif(aiScore > 21):
            print("Player Wins!")
            pwins += 1
            return

while True:
    gameStart()
    playergameLoop()
    while True:
        if(playerScore > aiScore and playerScore <= 21):
            aihit()
        else:
            aiGameloop()
            break

    print("total player wins: ", pwins, " ", "total ai wins: ", aiwins)
    gameOn = input("Would you like to play again(Enter No to Quit)?")
    if(gameOn == "yes" or gameOn == "Yes"):
        print("Good Luck!")
    elif(gameOn == "No" or gameOn == "no"):
        print("Thanks for playering!")
        break
    else:
        print("Good Luck!")
