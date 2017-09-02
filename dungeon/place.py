#! /usr/bin/env python3

from random import randrange
from dungeon.character import Monster

class GameMap:
    
    number_of_rooms = randrange(6, 10)
    #1abdfrst number_of_rooms = 6
    place_name = [ "Cave", "Room", "Glen"]

    def __init__(self):
        self.rooms = []
    
    def build_rooms(self):
        """ Add room to map """
        for room in range(0, GameMap.number_of_rooms):
            name = GameMap.place_name[randrange(0, len(self.place_name))]
            if name is "Cave":
                room = Cave(name)
                self.rooms.append(room)
            elif name is "Glen":
                room = Glen(name)
                self.rooms.append(room)
            elif name is "Room":
                room = Room(name)
                self.rooms.append(room)


class Place:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def name(self):
        """ Return the room name """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Cave(Place):

    def __init__(self, name):
        super().__init__(name)
        self.monsters = 3
        self.bonus = "Damage"
        self.amount = 1

    def description(self):
        print("This cave has three monsters, and seems to give the monsters extra strength")

class Room(Place):

    def __init__(self, name):
        super().__init__(name)
        self.monsters = 1
        self.bonus = None
        self.amount = 0

    def description(self):
        print("This room doesn't seem to help the monsters")

class Glen(Place):

    def __init__(self, name):
        super().__init__(name)
        self.monsters = 2
        self.bonus = "Accuracy"
        self.amount = 1

    def description(self):
        print("This glen seems to give these two monsters better accuracy")
    
