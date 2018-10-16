
from deck import Deck

class Players:
  def __init__(self):
    self.cards = []

  def get_cards(self,card):
    self.cards.append(card)

  def show_cards(self):
    print(self.cards)

  def count_points2(self):
    self.points = []
    self.score = 0
    self.aces = 0

    for i in range(len(self.cards)):
        self.points.append(str(self.cards[i]).split(" ")[0])
        if self.points[i].isdigit() == True:
            self.score += int(self.points[i])
        else:
            if self.points[i] == "A":
                self.aces += 1
            else:
                self.score += 10

    if (self.aces > 0):
        if (self.aces - 1 + 11)  + self.score > 21:
            self.score += self.aces
        else:
            self.score += (self.aces - 1 + 11)

    return (self.score)


  def isBlackJack(self):
    if len(self.cards) >=2:
      if (str(self.cards[0]).split(" ")[0] in ["J", "Q", "K"]  and str(self.cards[1]).split(" ")[0] == "A") or (str(self.cards[1]).split(" ")[0] in ["J", "Q", "K"]  and str(self.cards[0]).split(" ")[0] == "A"):
        print("True")
      else:
        print("False")
    else:
        print("False")



myDeck = Deck()
myDeck.shuffle()

player1 = Players()
dealer1 = Players()

for i in range(3):
  player1.get_cards(myDeck.pop())
  dealer1.get_cards(myDeck.pop())

print("Player1: " + str(player1.cards))
print("Dealer1: " + str(dealer1.cards))

print(player1.count_points2())

dealer1.isBlackJack()
