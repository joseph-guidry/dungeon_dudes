#! /usr/bin/env python3

import unittest
from dungeon.character import *
from dungeon.place import *
from dungeon.game import *
from dungeon.treasure import *
from dungeon.utilities import *


class TestDungeons(unittest.TestCase):

    def test_make_character(self):
        good_guy = Character("Name")
        self.assertEqual(good_guy.name, "Name")

    def test_make_hero(self):
        good_guy = Hero("Name")
        self.assertEqual(good_guy.name, "Name")
        self.assertIsInstance(good_guy.health, int)
        self.assertEqual(good_guy.damage, 1)
        self.assertIsInstance(good_guy.bag, dict)

    def test_make_monster(self):
        bad_guy = Monster("Name")
        self.assertIsInstance(bad_guy.health, int)

    def test_make_place(self):
        new_place = Place()
        new_cave = Cave()
        new_room = Room()
        new_glen = Glen()

    def test_get_dice(self):
        dice_roll = Dice()
        self.assertEqual(dice_roll.sides, 6)

    def test_get_dice_roll(self):
        dice = Dice()
        self.assertIsInstance(dice.roll(), int)

    def test_make_map(self):
        room_map = GameMap()
        room_map.build_rooms()
        self.assertEqual(len(room_map.rooms), 6)

    def test_treasure_creation(self):
        item = Treasure()
        self.assertIsInstance(item.name, str)
        self.assertIsInstance(item.bonus, str)
        self.assertIsInstance(item.amount, int)

    def test_treasure_pick_up(self):
        hero = Hero("Jack")
        item = Treasure()
        hero.pickup(item)
        self.assertEqual(len(hero.bag), 1)
        
     def test_treasure_drop_pickup(self):
        hero = Hero("Jack")
        monster = Monster()
        while monster.drop_treasure() is not None:
            monst
        

    def test_stat_update(self):
        hero = Hero("Jack")
        item = Treasure()
        while item.name is "Potion":
            item = Treasure()
        hero.pickup(item)
        self.assertEqual(len(hero.bag), 1)
        if item.name is "Sword":
            self.assertNotEqual(hero.damage, 1)
        elif item.name is "Goggles":
            self.assertNotEqual(hero.accuracy, 0)

    def test_battle_monster(self):
        hero = Hero("Jack")
        bad_guy = Monster()
        battle(hero, bad_guy)
    
    def test_battle_monster_outcome(self):
        hero = Hero("Jack")
        bad_guy = Monster()
        m_health = bad_guy.health
        h_health = hero.health
        battle(hero, bad_guy)

        if h_health != hero.health:
            pass
            # print("hero:" + str(h_health) + ":" +  str(hero.health) )
        elif m_health != bad_guy.health:
            pass
            # print("hero:" + str(m_health) + ":" +  str(bad_guy.health) )
        else:
            raise Exception("No Change")

    def test_get_hero_health(self):
        hero = Hero("Mario")
        print("{} : {}".format(hero.name, hero.health))
        bad_guy = Monster()
        print("{} : {}".format(hero.name, hero.health))

   

if __name__ == "__main__":
    unittest.main()
