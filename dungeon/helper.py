#! /usr/bin/env python3

import os
from random import *


class DeadHeroException(Exception):
    """ When Hero runs out of life points """
    pass


class Dice:
    """ A dice obj used return a int between 1 and number of sides """
    def __init__(self):
        self._sides = 6

    @property
    def sides(self):
        """ The dice used in the game """
        return self._sides

    def roll(self):
        """ Return a dice roll int value """
        return randrange(1, self.sides + 1)


def clear_screen():
    if os.name is "posix":
        os.system("clear")
    elif os.name is "nt":
        os.system("cls")


def game_menu():

    yes = ["1", "yes", "y", "YES", "Yes", "Y"]
    no = ["2", "q", "Q", "quit", "Quit", "QUIT"]
    while(True):
        print("\n\tPlease Enter a selection from the options below: \n")
        print("\t1 ) Start New Game")
        print("\t2 ) Quit")
        try:
            selection = input(" > ")
            print(selection)
            if selection in yes:
                return True
            elif selection in no:
                return False
            else:
                print("Invalid selection. Try again!")
        except KeyboardInterrupt as ex:
            print("\nPlease select one of the two options")


def menu_text():

    clear_screen()

    print("1 ) List items in the loot bag")
    print("2 ) Move to next location")
    print("3 ) Print Hero health")
    print("4 ) Print Monster Health")
    print("5 ) Attack")


def attack_menu(hero, monster):
    input("Press any key to continue...")
    menu_text()
    option = input()

    if option is "1":
        print("Display loot bag")
        for item in hero.bag:
            print(str(item))
    elif option is "2":
        print("Advancing to the next room")
        if len(monster) is 0:
            return False
        else:
            print("Can not advance, consider attacking that monster")
    elif option is "3":
        print("{}'s health: {}".format(hero.name, str(hero.health)))
    elif option is "4":
        for single in monster:
            print("{}'s health: {}".format(single.name, str(single.health)))
    elif option is "5":
        if len(monster) is not 0:
            print("Preparing to battle {}".format(monster[0]))
            battle(hero, monster[0])
            if monster[0].health < 1:
                print(str(monster[0].name) + " has been defeated")
                item = monster[0].drop_treasure()
                if item is not None:
                    print("{} found {}".format(hero.name, item.name))
                    hero.pickup(item)
                monster.pop(0)
            if hero.health < 1:
                raise DeadHeroException
        else:
            print("No monster to attack, consider going to the next room")
    else:
        print("Invalid Option")

    return True


def battle(hero, monster):
    """ Get dice roll to determine which character takes damage """
    dice = Dice()
    hero_results = roll_dice(dice)
    monster_results = roll_dice(dice)
    if hero_results >= monster_results:
        monster.take_damage(hero)
        return monster
    else:
        hero.take_damage(monster)
        return hero


def roll_dice(dice, roll=3):
    """ Return the highest dice roll """
    results = []
    for i in range(0, roll):
        results.append(dice.roll())
    return max(results)
