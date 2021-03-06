import os
import random



The_Fool = 0
The_Fool_Reversed = 0
The_Magician = 1
The_Magician_Reversed = -1
The_High_Priestess = 2
The_High_Priestess_Reversed = -2
The_Empress = 3
The_Empress_Reversed = -3
The_Emperor = 4
The_Emperor_Reversed = -4
The_Heirophant = 5
The_Heirophant_Reversed = -5
The_Lovers = 6
The_Lovers_Reversed = -6
The_Chariot = 7
The_Chariot_Reversed = -7
Justice = 8
Justice_Reversed = -8
The_Hermit = 9
The_Hermit_Reversed = -9
Wheel_Of_Fortune = 10
Wheel_Of_Fortune_Reversed = -10
Strength = 11
Strength_Reversed = -11
The_Hanged_Man = 12
The_Hanged_Man_Reversed = -12
Temperance = 13
Temperance_Reversed = -13
The_Devil = 14
The_Devil_Reversed = -14
The_Tower = 15
The_Tower_Reversed = -15
The_Star = 16
The_star_Reversed = -16
The_Moon = 17
The_Moon_Reversed = -17
The_Sun = 18
The_Sun_Reversed = -18
Judgement = 19
Judgement_Reversed = -19
The_World = 20
The_World_Reversed = -20



class DeckList():

    DeckValues = [
        [0, 0],
        [1, -1],
        [2, -2],
        [3, -3],
        [4, -4],
        [5, -5],
        [5, -6],
        [5, -7],
        [5, -8],
        [5, -9],
        [5, -10],
        [5, -11],
        [5, -12],
        [5, -13],
        [5, -14],
        [5, -15],
        [5, -16],
        [5, -17],
        [5, -18],
        [5, -19],
        [5, -20]]

    DeckValues[0] = [The_Fool, The_Fool_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[2] = [The_High_Priestess, The_High_Priestess_Reversed]
    DeckValues[3] = [The_Empress, The_Empress_Reversed]
    DeckValues[4] = [The_Emperor, The_Emperor_Reversed]
    DeckValues[5] = [The_Heirophant, The_Heirophant_Reversed]
    DeckValues[6] = [The_Lovers, The_Lovers_Reversed]
    DeckValues[7] = [The_Chariot, The_Chariot_Reversed]
    DeckValues[8] = [Justice, Justice_Reversed]
    DeckValues[9] = [The_Hermit, The_Hermit_Reversed]
    DeckValues[10] = [Wheel_Of_Fortune, Wheel_Of_Fortune_Reversed]
    DeckValues[11] = [Strength, Strength_Reversed]
    DeckValues[12] = [The_Hanged_Man, The_Hanged_Man_Reversed]
    DeckValues[13] = [Temperance, Temperance_Reversed]
    DeckValues[14] = [The_Devil, The_Devil_Reversed]
    DeckValues[15] = [The_Tower, The_Tower_Reversed]
    DeckValues[16] = [The_Star, The_star_Reversed]
    DeckValues[17] = [The_Moon, The_Moon_Reversed]
    DeckValues[18] = [The_Sun, The_Sun_Reversed]
    DeckValues[19] = [Judgement, Judgement_Reversed]
    DeckValues[20] = [The_World, The_World_Reversed]




def shuffleDeck():
    for cards in range(0,len(DeckList.DeckValues)):
        random.shuffle(DeckList.DeckValues)

def deal():
    hand = DeckList.DeckValues
    for card in range(1):
        card = DeckList.DeckValues.pop()
        hand.append(card)
    return hand

def draw(dealerHand, playerHand):
    card = DeckList.DeckValues.pop()
    hand.append(card)
    return hand

def total(hand):
    total = 0
    total += hand
    return total

def playAgain():
    again = input("Do you wish to play again? (Yes/No) : ").lower()
    if (again == "yes"):
        dealerHand = []
        playerHand = []
        deck = DeckList.DeckValues
        game()

    else:
        print("Bye!")
        exit()

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def printResults(dealerHand, playerHand):
    clear()
    print("The dealer has a " + str(dealerHand) + "for a total of" + str(total(dealerHand)))
    print("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))

def fateTarot(dealerHand, playerHand):
    if total(playerHand) > dealerHand:
        printResults(dealerHand, playerHand)
        print("Congratualitions! You fought Fate and won!")
        playAgain()
    if total(playerHand) < dealerHand:
        printResults(dealerHand, playerHand)
        print("Sorry! You fought Fate and lost!")
        playAgain()

def results(dealerHand, playerHand):
    if(dealerHand == DeckList.DeckValues[0][0]):
        print("You win!!!!")
    elif(dealerHand == DeckList.DeckValues[0]):
        print(DeckList.DeckValues[:0])
        print("Dealer has lost! You have been spared by Fate!")

    elif(dealerHand == DeckList.DeckValues[0]):
        print(DeckList.DeckValues[0])
        print("Dealer has won! You fought Fate and lost!")

    elif(playerHand == DeckList.DeckValues[:0]):
        print(DeckList.DeckValues[:0])
        print("You have lost! The dealer has been favored by Fate!")

    elif(playerHand == DeckList.DeckValues[0]):
        print(DeckList.DeckValues[0])
        print("You have won! You have been favored by Fate!")


def game():
    choice = 0
    clear()
    dealerHandCount = 1
    playerHandCount = 1
    maxPlays = 5
    print ("WELCOME TO Fate Tarot\n")
    dealerHand = deal(DeckList.DeckValues)
    playerHand = deal(DeckList.DeckValues)
    while choice != "q":
        print ("The dealer has drawn " + str(dealerHand[0]))
        print ("You have drawn " + str(playerHand) + " for a total of " + str(total(playerHand)))
        fateTarot(dealerHand, playerHand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            draw(playerHand)
            while total(dealerHand) < total():
                playerHandCount+=1
                if playerHandCount > maxPlays:
                    print("out of plays")
                    break
                draw(dealerHand)
            results(dealerHand, playerHand)
            playAgain()
        elif choice == "s":
            while total(dealerHand) < :
                draw(dealerHand)
            draw(dealerHand, playerHand)
            playAgain()
        elif choice == "q":
            print("Bye!")
            exit()

