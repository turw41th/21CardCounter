import sys

print("Welcome to the the card counter, a console based companion for your blackjack game")
print("Just run it next to your game of blackjack and enter the cards drawn into the software. Use the numbers or letters shown on the cards.")

"""
deck1 = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
deck2 = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
deck3 = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
deck4 = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
deck5 = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
deck6 = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
"""

runningcount = 0
decksremaining = 8

i = 1


while decksremaining > 0:
    while i < 52:
        card = input(">>>>Enter card > ").lower()

        """
        if card in deck1:
            deck1.remove(card)
        elif card in deck2:
            deck2.remove(card)
        elif card in deck3:
            deck3.remove(card)
        elif card in deck4:
            deck4.remove(card)
        elif card in deck5:
            deck5.remove(card)
        elif card in deck6:
            deck6.remove(card)
        """

        if card == "exit" or card == "quit":
            sys.exit()

        if card == "2" or card == "3" or card == "4" or card == "5" or card == "6":
            runningcount += 1
        elif card == "7" or card == "8" or card == "9":
            runningcount = runningcount
        elif card == "10" or card == "j" or card == "q" or card == "k" or card == "a":
            runningcount -= 1
        else:
            print("Please enter a valid card. You can use numbers from 2 - 10 and J, Q, K and A!")
            continue

        truecount = runningcount / decksremaining

        print("running count: " + str(runningcount))
        print(f"Your truecount: {str(round(truecount))}\n")
        print(f"Decks remaining: {str(decksremaining)}\n")

        i = i + 1

    decksremaining -= 1
    i = 1
