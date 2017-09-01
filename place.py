#! /usr/bin/env python3

from random import randrange
from character import Monster

class GameMap:
    
    # number_of_rooms = randrange(6, 10)
    number_of_rooms = 6
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

    # def get_monster(self, num_monsters):
       # a = 0
       # print("HERE " + str(num_monsters))
       # print("HERE " + str(a))
       # while a < num_monsters:
            
       #     yield a

class Cave(Place):

    def __init__(self, name):
        super().__init__(name)
        self.monsters = 1
        self.bonus = "Damage"
        self.amount = 1


class Room(Place):

    def __init__(self, name):
        super().__init__(name)
        self.monsters = 1
        self.bonus = None
        self.amount = 0


class Glen(Place):

    def __init__(self, name):
        super().__init__(name)
        self.monsters = 1
        self.bonus = "Accuracy"
        self.amount = 1

    
