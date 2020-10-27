import random

# Two useful variables for creating Cards.
suite = 'H D S C'.split()
ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.allcards = [(s, r) for s in suite for r in ranks]  # same as 2 nested for loops

    def splitdeck(self):
        random.shuffle(self.allcards)
        self.splits = [self.allcards[:26], self.allcards[26:]]


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, handcards):
        self.handcards = handcards

    def __str__(self):
        return str(self.handcards)

    def __len__(self):
        return len(self.handcards)

    def losecard(self):
        v = self.handcards.pop()
        return v

    def addcard(self, add):
        self.handcards.insert(0, add)

    def __getitem__(self, handcards):
        return self.handcards[-1]


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def nextplay(self):
        return self.hand[-1]

    def checkcards(self):
        if len(self.hand) != 0:
            return True
        else:
            return False


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")


def score(pts):
    points_table = {"A": 1,
                    "2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9,
                    "10": 10,
                    "J": 11,
                    "Q": 12,
                    "K": 13}

    return points_table.get(pts)


mydeck = Deck()
mydeck.splitdeck()
myhand = Hand(mydeck.splits[0])
print("P1: {}".format(myhand))
otherhand = Hand(mydeck.splits[1])
print("P2: {}".format(otherhand))
playerone = Player("P1", myhand)
playertwo = Player("P2", otherhand)


def game_logic(onenext, twonext, tmp=[]):
    pointsone = score(onenext[1])
    pointstwo = score(twonext[1])

    if pointsone > pointstwo:
        x = playertwo.hand.losecard()
        playerone.hand.addcard(playerone.hand.losecard())
        playerone.hand.addcard(x)
        if (len(tmp) != 0):
            for i in tmp:
                playerone.hand.addcard(i)
            del tmp[:]
        print("{0} lost {1}".format(playertwo.name, x))
    elif pointsone < pointstwo:
        y = playerone.hand.losecard()
        playertwo.hand.addcard(playertwo.hand.losecard())
        playertwo.hand.addcard(y)
        if (len(tmp) != 0):
            for i in tmp:
                playertwo.hand.addcard(i)
            del tmp[:]
        print("{0} lost {1}".format(playerone.name, y))
    else:
        print("It is war!")
        war_logic(onenext, twonext, tmp)


def war_logic(one, two, temp=[]):
    temp.append(one)
    temp.append(two)
    print(temp)
    playerone.hand.losecard()
    playertwo.hand.losecard()
    game_logic(playerone.nextplay(), playertwo.nextplay(), temp)
    # whoever wins, add cards in temp to their deck


while playerone.checkcards() == True and playertwo.checkcards() == True:
    onp = playerone.nextplay()
    tnp = playertwo.nextplay()

    game_logic(onp, tnp)

if len(playerone.hand) == 0:
    print("{} Won!".format(playertwo.name))
else :
    print("{} Won!".format(playerone.name))

# Use the 3 classes along with some logic to play a game of war!
