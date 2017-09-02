#! /usr/bin/env python3

"""import treasure"""
from random import randrange
from dungeon.treasure import *

class Character:

    bad_guy_names = ["Soundwave", "Megatron", "Starscream", "Buzzsaw",
                     "Ravage", "Barricade", "Blackout", "Fracture", "Skipjack"]

    """ The base class for any character used in the game """
    def __init__(self, char_name):
        if char_name is None:
            char_name = Character.bad_guy_names[randrange(0, len(Character.bad_guy_names))]
        self.name = char_name

    def __str__(self):
        return "{}".format(self.name)

    @property
    def name(self):
        """ Character Name """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def take_damage(self, character):
        self.health -= character.damage


class Hero(Character):
    """ Subclass of Character, adds attributes such as bag and health """
    def __init__(self, name, health=10):
        super().__init__(name)
        self.health = health
        self.accuracy = 0
        self.damage = 1
        self.bag = {}

    def __str__(self):
        output = []
        output.append("{}".format(super().__str__()))
        output.append(str(self.health))
        for item in self.bag:
            output.append(str(item))
            output.append(str(self.bag[item]))
        return " ".join(output)

    @property
    def health(self):
        """ The health for Hero Character"""
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def damage(self):
        """ The base damage for Hero Character"""
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def pickup(self, item):
        """ Method to pickup item dropped by monster """
        try:
            if item.name is self.bag[item.name]:
                print("Item is : " + item.name)
        except KeyError:
            self.bag.update({item.name: [item.bonus, item.amount]})
            self.update_stat()

    def update_stat(self):
        """ Modify stats after picking up item """
        if "Sword" in self.bag:
            self.damage += self.bag["Sword"][1]
        elif "Goggles" in self.bag:
            self.accuracy += self.bag["Goggles"][1]


class Monster(Character):
    """ Subclass of Character, add health attribute, and treasure drop """
    def __init__(self, name=None, health=None):
        super().__init__(name)
        if health is None:
            health = randrange(1, 4)
        self.health = health
        self.damage = 2
        self.accuracy = 0

    def __str__(self):
        output = []
        output.append("{}".format(super().__str__()))
        return " ".join(output)

    @property
    def health(self):
        """ The health for Monster Character"""
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def damage(self):
        """ The damage attribute for Monster Character """
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def drop_treasure(self):
        """ If true, after monster is defeated a random treasure drop """
        num = randrange(0,10)
        if num is randrange(0,10):
            print("dropping Treasure")
            return Treasure()
        else:
            return None
            

    def update_stat(self, bonus, amount):
        """ Modify stats for monster in the room """
        if bonus is None:
            return

        if bonus is "Damage":
            self.damage += amount
        elif bonus is "Accuracy":
            self.accuracy += amount
