import util


class Board:
    def __init__(self):
        self.cities = []

        # Creation of the nodes representing the cities
        for c in util.yellowCities:
            self.cities.append(Board.City(c, "Yellow"))
        for c in util.blackCities:
            self.cities.append(Board.City(c, "Black"))
        for c in util.redCities:
            self.cities.append(Board.City(c, "Red"))
        for c in util.blueCities:
            self.cities.append(Board.City(c, "Blue"))
            if c == "Atlanta":
                self.cities[-1].research_station = True  # Initial research station on Atlanta

        # Adding the possible destinations to each nodes
        for c in self.cities:
            for d in util.adjList:
                if c.name == d[0]:
                    c.destinations = d[1:]
                    break


    def getCityIndex(self, city):
        """
        Method to find the index of a given city in the cities list of the board
        :param city (String):
        :return (int): index of the city being looked for
        """
        for i in range(len(self.cities)):
            if city == self.cities[i].name:
                return i

        return -1  # return -1 if index is not found.


    class City:
        def __init__(self, name, color):
            self.name = name
            self.color = color
            self.destinations = []
            self.research_station = False
            self.disease_cubes = {"Blue": 0,
                                  "Yellow": 0,
                                  "Black": 0,
                                  "Red": 0}
