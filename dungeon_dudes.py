#! /usr/bin/env python3

from dungeon.character import *
from dungeon.place import *
from dungeon.treasure import *
from dungeon.helper import *


def run_game(game_map, hero):
    try:
        while len(game_map.rooms) > 0:
            room = game_map.rooms.pop()
            room.description()
            # This portion generates a list of monsters in the room
            bad_guys = []
            for monster in range(room.monsters):
                monster = Monster()
                monster.update_stat(room.bonus, room.amount)
                bad_guys.append(monster)
            for single in bad_guys:
                print("{}'s health:{}".format(single.name, str(single.health)))
            winner = battle(hero, bad_guys[0])
            if winner is hero:
                print("You have been attacked by {}".format(bad_guys[0].name))
                answer = input("Would you like to jump out the window? [y] >")
                if answer is "y":
                    game_map.rooms = []
            else:
                while attack_menu(hero, bad_guys):
                    pass

    except DeadHeroException as ex:
        fmt = "You, {}, have been defeated by {}"
        print(fmt.format(hero.name, bad_guys[0].name))


def main():
    while (game_menu()):
        game_map = GameMap()
        hero = Hero(input("Enter your hero name: "))
        game_map.build_rooms()
        print("Entering the first ROOM! ")
        run_game(game_map, hero)
        print("Congrats you made it out alive")
        input("Press any key to continue...")
        clear_screen()


if __name__ == "__main__":
    try:
        print("\tWelcome to the Dungeon Dudes Adventure Quest")
        main()
    except KeyboardInterrupt as ex:
        pass
