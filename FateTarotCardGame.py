import random
from random import shuffle



The_Fool = 0
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
        [0],
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

    DeckValues[0] = [The_Fool]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]
    DeckValues[1] = [The_Magician, The_Magician_Reversed]




# aiHand = ?
# playerHand = ?

def deal():
    hand = DeckList.DeckValues
    print(hand)
    for c in range(1):
        card = deck.pop()


deal()

