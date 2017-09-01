#! /usr/bin/env python3

from random import randrange
from character import *
from place import *
from game import *


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

def game_menu():

    yes = [ "1", "yes", "y", "YES", "Yes", "Y"]
    no = [ "2", "q", "Q", "quit", "Quit", "QUIT"]
    while(True):
        print("\n\tPlease Enter a selection from the options below: \n")
        print("\t1 ) Start New Game")
        print("\t2 ) Quit")
        try:
            selection = input(" > ")
            if selection in yes:
                return True
            elif selection in no:
                return False
            else:
                print("Invalid selection. Try again!")
        except KeyboardInterrupt as ex:
            print("Attempting to exit with keyboard shortcut")

def menu_text():
    print("1 ) List items in the loot bag")
    print("2 ) Move to next location")
    print("3 ) Print Hero health")
    print("4 ) Print Monster Health")
    print("5 ) Attack")

def attack_menu(hero, monster):
    menu_text()
    option = input()
    
    if option is "1":
        print("Display loot bag")
        # print(str(hero.bag))
    elif option is "2":
        print("Advancing to the next room")
        # if monster.remaining is True:
            # print("Can not advance, consider attacking that monster")
        # else:
            # Return False
    elif option is "3":
        print("my hero's health: " + str(hero.health))
    elif option is "4":
        print("the monster's health: " + str(monster[0].health))
    elif option is "5":
        print("attack phase")
        # if monster.remaining is False:
            # attack(hero, monster)
            # if monster.health > 1:
                
        # else:
           # print("No monster to attack, consider going to the next room")
    else:
        print("Invalid Option")-abcdfgostz
    return True

def battle(hero, monster):
    """ Get dice roll to determine which character takes damage """
    dice = Dice()
    hero_results = roll_dice(dice)
    monster_results = roll_dice(dice)
    if hero_results >= monster_results:
        monster.take_damage(hero)
    else:
        hero.take_damage(monster)
    
   

def roll_dice(dice, roll=3):
    """ Return the highest dice roll """
    results = []
    for i in range(0,roll):
        results.append( dice.roll() )
    return max(results)

def main():
    try:
        print("\tWelcome to the Dungeon Dudes Adventure Quest")

        while (game_menu() ):
            game_map = GameMap()
            hero = Hero(input("Enter your hero name: "))
            game_map.build_rooms()
            print("Entering the first ROOM! ")

            while len(game_map.rooms) > 0:
                room = game_map.rooms.pop()
                print(room)
                print(room.bonus, room.amount)
                    
                # This portion generates a list of monsters in the room
                bad_guys = []
                for monster in range(room.monsters):
                    monster = Monster()
                    monster.update_stat(room.bonus, room.amount)
                    bad_guys.append(monster)

                print(str(bad_guys[0]))

                while attack_menu(hero, bad_guys):
                    print("Not Over Yet")

            print("Congrats you made it through the Gauntlet")
    except KeyboardInterrupt as ex:
        pass

if __name__ == "__main__": main()
"""
    try:
        main()
    except Exception as ex:
        print("Something failed to complete: exitting ... ")
"""
        
