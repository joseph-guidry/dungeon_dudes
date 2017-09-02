#! /usr/bin/env python3

from dungeon.character import *
from dungeon.place import *
from dungeon.treasure import *
from dungeon.helper import *


def run_game(game_map, hero):
    """ The game logic for dungeon dude Adventure Quest"""
    try:
        for room in game_map.rooms:
            room.description()
            # This portion generates a list of monsters in the room
            bad_guys = []
            for monster in range(room.monsters):
                monster = Monster()
                monster.update_stat(room.bonus, room.amount)
                bad_guys.append(monster)
            print("Attacked by {}".format(bad_guys[0].name))
            winner = battle(hero, bad_guys[0])
            if bad_guys[0].health < 1:
                bad_guys.pop(0)
            if room is game_map.rooms[0] and winner is hero:
                answer = input("Would you like to escape out the window[y]?>")
                if answer is "y":
                    game_map.rooms = []
            while attack_menu(hero, bad_guys):
                    pass

    except DeadHeroException as ex:
        fmt = "You, {}, have been defeated by {}"
        print(fmt.format(hero.name, bad_guys[0].name))


def main():
    """ Starts the Dungeon Dude Adventure Quest """
    while (start_menu()):
        game_map = GameMap()
        hero = Hero(input("Enter your hero name: "))
        game_map.build_rooms()
        print("Entering the first ROOM! ")
        run_game(game_map, hero)
        if hero.health > 0:
            print("Congrats you made it out alive")
        input("Press any key to continue...")
        clear_screen()


if __name__ == "__main__":
    try:
        print("\tWelcome to the Dungeon Dudes Adventure Quest")
        main()
    except KeyboardInterrupt:
        print("\nHope you enjoyed it")
