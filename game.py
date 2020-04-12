from random import shuffle, randrange
import player
import util
import card
import math
import board


class Game:

    def __init__(self, nbPlayer, nbEpidemic):
        self.players = []
        for i in range(nbPlayer):
            self.players.append(player.Player(i))
        self.infectionDeck = self.createInfectionDeck()
        self.playerDeck = self.createPlayerDeck(nbEpidemic,nbPlayer)
        self.playerDiscardPile = []
        self.infectionDiscardPile = []
        self.board = board.Board()
        self.gameStatus = 0  # 0=in play, 1=game lost 2=game won

        self.disease_cubes = {"Blue": 24,
                            "Yellow": 24,
                            "Black": 24,
                            "Red": 24}

        #  Create initial diseases on board
        for i in range(3):
            for y in range(3):
                self.drawInfectionCard((3-i))


    def createInfectionDeck(self):
        deck = []
        for c in util.yellowCities:
            deck.append(card.Card(1, c, "Yellow"))
        for c in util.blackCities:
            deck.append(card.Card(1, c, "Black"))
        for c in util.redCities:
            deck.append(card.Card(1, c, "Red"))
        for c in util.blueCities:
            deck.append(card.Card(1, c, "Blue"))

        shuffle(deck)

        return deck


    def createPlayerDeck(self, numEpidemic, numPlayer):
        deck =[]
        for c in util.yellowCities:
            deck.append(card.Card(2, c, "Yellow"))
        for c in util.blackCities:
            deck.append(card.Card(2, c, "Black"))
        for c in util.redCities:
            deck.append(card.Card(2, c, "Red"))
        for c in util.blueCities:
            deck.append(card.Card(2, c, "Blue"))

        shuffle(deck)

        # We take out 2 cards for each players as starting cards
        for y in range(2):
            for i in range(numPlayer):
                self.players[i].hand.append(deck[-1])
                deck.pop()

        # Adding infection cards to the deck
        baseRange = math.floor(len(deck)/numEpidemic)
        nbLongerRanges = len(deck) % numEpidemic
        index = 0

        for i in range(numEpidemic):
            if nbLongerRanges > 0:
                usedRange = baseRange + 1
                nbLongerRanges -= 1
            else:
                usedRange = baseRange

            randomPosition  = randrange(0, usedRange)

            deck.insert(index + randomPosition, card.Card(3))

            index = index + usedRange + 1

        return deck


    def infectCity(self, city, color):
        """
        Method called to place a disease cube on a city
        :param city : City to be infected
        :param color : Color of the disease cube
        :return: None
        """
        index = self.board.getCityIndex(city)
        if self.board.cities[index].disease_cubes[color] == 3:
            # TODO Manage disease propagation
            pass
        else:
            self.board.cities[index].disease_cubes[color] += 1
            self.disease_cubes[color] -= 1
            # lose game if cube count for the color dropped below 0
            if self.disease_cubes[color] < 0:
                self.gameStatus = 1


    def drawInfectionCard(self, nbOfInfection = 1):

        """
        Method that manages the drawing of an infection card
        :param nbOfInfection: Number of cubes to be placed. Always 1 except when setting the game up
        :return: None
        """
        card = self.infectionDeck.pop(-1)
        self.infectionDiscardPile.append(card)
        for i in range(nbOfInfection):
            self.infectCity(card.city,card.color)




if __name__ == '__main__':
    test = Game(4,5)
    print('fin')