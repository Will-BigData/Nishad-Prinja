import csv
import numpy as np
import pandas as pd
from random import sample
import random
from termcolor import colored

df = pd.read_csv('monsters.csv')
# n = 0
# while n < 5:
#     dfr.to_csv('output.csv', header=None, mode='a')
#     n += 1

# dfr = df.sample()
# print(dfr)
# dfr.to_csv('output.csv')

# class Character:
#     def __init__(self, name, location, weapons):
#         self.name = name
#         self.location = location
#         self.weapons = weapons

class Player:
    def __init__(self, name, location, weapons, playclass, race, maxhp, hp):
        # super().__init__(name=name, location=location, weapons=weapons)
        self.name = name
        self.location = location
        self.weapons = weapons
        # self._level= level
        # self._experience= experience
        self.playclass= playclass
        self.race= race
        # self._strength= strength
        # self._dexterity= dexterity
        # self._constitution= constitution
        # self._wisdom= wisdom
        # self._intelligence= intelligence
        # self._charisma= charisma
        self.maxhp= maxhp
        self.hp= hp
        # self._spells= spells
        # self._spellslots= spellslots
        # self._equipment= equipment     
        # self._speed= speed
        # self._skills= skills
        # self._proficiencies= proficiencies

        # def toJSON(self):
        #     return json.dumps(self)
            # {
            #     "name": self.name,
            #     "location": self.location,
            #     "weapons": self.weapons,
            #     "class": self.playclass,
            #     "race": self.race,
            #     "maxHP": self.maxhp,
            #     "HP": self.hp
            # }

player_name = input("\033[1m" + "What is the name of your character? " + "\033[0m")
print("\n")

class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

playclass = random.choice(class_list)
# print(playclass)

# weapons = ['Rapier', 'Longsword', 'Simple Weapon']
# print(weapons)

extended_weapons = ['Battleaxe', 'Flail', 'Glave', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'Warpick', 'Warhammer', 'Whip']
extended_weapons2 = ['Club', 'Dagger', 'Greatclub', 'Handaxe', 'Javelin', 'Light Hammer', 'Mace', 'Quarterstaff', 'Sickle', 'Spear', 'Light Crossbow', 'Dart', 'Shortbow', 'Sling']

weapon1 = random.choice(extended_weapons)
weapon2 = random.choice(extended_weapons2)
# print(weapon1)
# print(weapon2)

race = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']
race_choice = random.choice(race)
# print(race_choice)

location = ['Dark Sun', 'Dragonlance', 'Eberron', 'The Feywilds', 'Forgotten Realms', 'Greyhawk', 'The Planes of Existence', 'Planescape', 'Ravenloft', 'Spelljammer']
location_choice = random.choice(location)
# print(location_choice)

max_hp = random.randint(150, 300)

new_player = Player(player_name, location_choice, [weapon1, weapon2], playclass, race_choice, max_hp, max_hp)
# print(new_player.name)
# print(new_player.location)
# print(new_player.weapons)
# print(new_player.playclass)
# print(new_player.race)
# print(new_player.maxhp)
# print(new_player.hp)

print("\033[1m" + f"Welcome traveler! Let me introduce you to your character for this battle. Your name is {new_player.name} and you hail from {new_player.location}. Your weapons are the {new_player.weapons[0]} and the {new_player.weapons[1]}. You are a {new_player.playclass} of the race {new_player.race}. Your total hitpoints are {new_player.maxhp}. Welcome to the fight!" + "\033[0m")
print("\n")

dfr = df.sample()
new_dfr = df.sample()
first_monster = True

# print("These are the properties of my monster!")
# print(dfr['Name'])
# print(dfr['Size'])
# print(dfr['Type'])
# print(dfr['STR'])
# print(dfr['HP'])

class Monster:
    def __init__(self, name, size, type, strength, maxhp, hp):
        self.name = name
        self.size = size
        self.type = type
        self.strength = strength
        self.maxhp = maxhp
        self.hp = hp

monster = Monster(str(dfr['Name'].iloc[0]), str(dfr['Size'].iloc[0]), str(dfr['Type'].iloc[0]), int(dfr['STR'].iloc[0]), int(dfr['HP'].iloc[0]), 1)
# print("This is my monster!")
# print(monster.name)
# print(monster.size)
# print(monster.type)
# print(monster.strength)
# print(monster.maxhp)
# print(monster.hp)
# print("Properties read!")

def fight(player, monster):
    player_turn = True
    print("\033[4m" + f"Your adversary is the {monster.name} of type \"{monster.type}\" and size of {monster.size} with a total of {monster.maxhp} hitpoints." + "\033[0m")
    print("\n")
    while(player.hp > 0 and monster.hp > 0):
        if (player_turn == True):
            # print(player.name)
            choice = input("\033[1m" + "Would you like to attack (d20 roll), heal (gain 40 hp), or prepare (extra 2 d10 damage but on the next turn) and execute (type 'execute' after waiting a turn)? " + "\033[0m")
            print("\n")
            if (choice.strip().lower() == 'attack'):
                d20_roll = random.randint(0,20)
                print("\033[1m" + "Your damage roll was: " + "\033[0m" + str(d20_roll))
                monster_damage = monster.hp - d20_roll
                monster.hp = monster_damage
                weapon = player.weapons[random.randint(0, 1)]
                print(f"Ouch! {monster.name} was hit with your " + weapon + " and has " + str(monster_damage) + " hitpoints left!")
                if (d20_roll > 1):
                    print("\n")
                    print("Critical hit roll! Roll again for additional damage.")
                    critical_hit = random.randint(0, 20)
                    extra_damage = monster.hp - critical_hit
                    monster.hp = extra_damage
                    print("Your crit roll was " + str(critical_hit) + f". {monster.name} now has " + str(extra_damage) + " hitpoints left!")
                print("\n")
                player_turn = False
            if (choice.strip().lower() == 'heal'):
                healed_player = player.hp + 40
                player.hp = healed_player
                if (healed_player > player.maxhp):
                    healed_player = player.maxhp
                    player.hp = healed_player
                    print("You are now back at your max HP of " + str(healed_player) + "!")
                print("Your current HP after healing is " + str(healed_player) + ".")
                print("\n")
                player_turn = False
            if (choice.strip().lower() == 'prepare'):
                prepared = True
                # print(prepared)
                print("Getting ready to prepare more damage for next turn...")
                print("\n")
                player_turn = False
                continue
            if (choice.strip().lower() == 'execute'):
                try:
                    if (prepared == True):
                        roll_1 = random.randint(0, 20)
                        roll_2 = random.randint(0, 10)
                        roll_3 = random.randint(0, 10)
                        damage = roll_1 + roll_2 + roll_3
                        new_monster_hp = monster.hp - damage
                        monster.hp = new_monster_hp
                        weapon = player.weapons[random.randint(0, 1)]
                        print("Your first roll was " + str(roll_1) + ". Your second roll was " + str(roll_2) + ". Your third roll was " + str(roll_3) + ".")
                        print(f"{monster.name} was hit three times with your " + weapon + " and now has " + str(new_monster_hp) + " hitpoints!")
                        print("\n")
                        prepared = False
                        player_turn = False
                except:
                    print("\033[1m" + "You did not prepare before executing" + "\033[0m")
                    print("\n")
                    player_turn = True
                    continue
        elif (player_turn == False):
            print("\033[1m" + f"It is now the monster {monster.name}'s turn" + "\033[0m")
            hit_or_miss = random.randint(0, 1)
            if (hit_or_miss == 1):
                modifier = (monster.strength)//5
                d20_monster_roll = random.randint(0, 20)
                monster_hit = d20_monster_roll * modifier
                player_hit_hp = player.hp - monster_hit
                player.hp = player_hit_hp
                print("The monster hit you with its attack! You took " + str(monster_hit) + " damage. The monster's roll was " + str(d20_monster_roll) + " with a strength modifier of " + str(modifier) + f". Your health is now {player.hp}.")
                print("\n")
                player_turn = True
            elif (hit_or_miss == 0):
                print("The monster's attack missed! It is once again your turn!")
                print("\n")
                player_turn = True
    if (player.hp <= 0):
        print("\033[1m" + "Game over! You died! Time to play again." + "\033[0m")
        return
    if (monster.hp <= 0):
        print("The fight's not over! Time to fight a new monster!")
        # print("This is my monster!")
        # print(new_monster.name)
        # print(new_monster.size)
        # print(new_monster.type)
        # print(new_monster.strength)
        # print(new_monster.maxhp)
        # print(new_monster.hp)
        # print("Properties read!")
        global first_monster
        print(first_monster)
        print(new_dfr)
        if (first_monster == True):
            first_monster = False
            dfr.to_csv("monsters_defeated.csv")
        else:
            new_dfr.to_csv("monsters_defeated.csv", mode='a', header=False)
        new_monster = Monster(str(new_dfr['Name'].iloc[0]), str(new_dfr['Size'].iloc[0]), str(new_dfr['Type'].iloc[0]), int(new_dfr['STR'].iloc[0]), int(new_dfr['HP'].iloc[0]), 1)
        new_dfr = df.sample()
        fight(player, new_monster)
        




fight(new_player, monster)