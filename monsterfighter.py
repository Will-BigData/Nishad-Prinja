import pandas as pd
import random
import os

df = pd.read_csv('monsters.csv')

# Source: https://github.com/vannoywv/Dungeons-and-Dragons/blob/main/DDsetup.py
class Player:
    def __init__(self, name, location, weapons, playclass, race, maxhp, hp, prepared=False):
        self.name = name
        self.location = location
        self.weapons = weapons
        self.playclass= playclass
        self.race= race
        self.maxhp= maxhp
        self.hp= hp
        self.prepared= prepared
    def heal_hp(self, hp_healed=40):
        self.hp += hp_healed
        if (self.hp > self.maxhp):
            self.hp = self.maxhp
    def get_hp(self):
        return self.hp
    def get_max_hp(self):
        return self.maxhp
    def get_prepared(self):
        return self.prepared
    def set_prepared(self, boolean):
        self.prepared = boolean
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_weapons(self):
        return self.weapons
    def get_playclass(self):
        return self.playclass
    def get_race(self):
        return self.race
    def player_attack(self, d20_roll):
        player_damage = self.hp - d20_roll
        self.hp = player_damage


class Monster:
    def __init__(self, name, size, type, strength, maxhp, hp):
        self.name = name
        self.size = size
        self.type = type
        self.strength = strength
        self.maxhp = maxhp
        self.hp = hp
    def monster_attack(self, d20_roll):
        monster_damage = self.hp - d20_roll
        self.hp = monster_damage
    def get_hp(self):
        return self.hp
    def get_modifier(self, modifier_divisor):
        modifier = (self.strength)//modifier_divisor
        if (modifier == 0):
            modifier += 1
        return modifier

def fight():
    player_turn = True

    dfr = df.sample()
    monster = new_monster_blender(dfr)
    first_monster = True

    player = new_player()

    while (True):
        print("\033[4m" + f"Your adversary is the {monster.name} of type \"{monster.type}\" and size of {monster.size} with a total of {monster.maxhp} hitpoints." + "\033[0m")
        print("\n")
        while(player.get_hp() > 0 and monster.get_hp() > 0):
            if (player_turn == True):
                choice = input("\033[1m" + "Would you like to (a)ttack (d20 roll), (h)eal (gain 40 hp), or (p)repare (extra 2 d10 damage but on the next turn) and (e)xecute (type 'execute' after waiting a turn)? " + "\033[0m")
                print("\n")
                match (choice.strip().lower()[0]):
                    case ('a'):
                        player_attack_choice(player, monster)
                        player_turn = False
                    case ('h'):
                        player_heal_choice(player)
                        player_turn = False
                    case ('p'):
                        player_turn = player_prepare_choice(player)
                    case ('e'):
                        player_turn = player_execute_choice(player, monster)
            else:
                monster_turn(monster, player)
                player_turn = True
                
        if (player.get_hp() <= 0):
            print("\033[1m" + "Game over! You died! Time to play again." + "\033[0m")
            if (continue_or_not(whether_new_monster=False)):
                # dfr = choose_new_random_monster()
                # monster = new_monster_blender(dfr)
                player = new_player()
                first_monster = True
                player_turn = True
            else:
                return

        if (monster.get_hp() <= 0):
            write_monster_file(first_monster, dfr, player.get_name())
            dfr = choose_new_random_monster()
            first_monster = False

            if (continue_or_not(whether_new_monster=True)):
                monster = new_monster_blender(dfr)
                player_turn = True
            else:
                return

def write_monster_file (first_monster, dataframe, player_name):
    monsters_killed_path = "./monsters_killed"
    if not os.path.exists(monsters_killed_path):
        os.mkdir(monsters_killed_path)

    if (first_monster):
        dataframe.to_csv(f"monsters_killed/{player_name}_monsters_defeated.csv")
    else:
        dataframe.to_csv(f"monsters_killed/{player_name}_monsters_defeated.csv", mode='a', header=False)
    
def choose_new_random_monster():
    dataframe = df.sample()
    return dataframe

def new_monster_blender (dataframe):
    monster = Monster(str(dataframe['Name'].iloc[0]), str(dataframe['Size'].iloc[0]), str(dataframe['Type'].iloc[0]), int(dataframe['STR'].iloc[0]), int(dataframe['HP'].iloc[0]), int(dataframe['HP'].iloc[0]))          
    return monster

def new_player():
    player_name = input("\033[1m" + "What is the name of your character? " + "\033[0m")
    print("\n")

    # source: https://www.youtube.com/watch?v=iKB78i9tGsM&ab_channel=JadeyCatgirl99
    class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    playclass = random.choice(class_list)

    extended_weapons = ['Battleaxe', 'Flail', 'Glave', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'Warpick', 'Warhammer', 'Whip']
    extended_weapons2 = ['Club', 'Dagger', 'Greatclub', 'Handaxe', 'Javelin', 'Light Hammer', 'Mace', 'Quarterstaff', 'Sickle', 'Spear', 'Light Crossbow', 'Dart', 'Shortbow', 'Sling']
    weapon1 = random.choice(extended_weapons)
    weapon2 = random.choice(extended_weapons2)

    race = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']
    race_choice = random.choice(race)

    location = ['Dark Sun', 'Dragonlance', 'Eberron', 'The Feywilds', 'Forgotten Realms', 'Greyhawk', 'The Planes of Existence', 'Planescape', 'Ravenloft', 'Spelljammer']
    location_choice = random.choice(location)

    max_hp = random.randint(150, 300)

    player = Player(player_name, location_choice, [weapon1, weapon2], playclass, race_choice, max_hp, max_hp)

    print("\033[1m" + f"Welcome traveler! Let me introduce you to your character for this battle. Your name is {player.get_name()} and you hail from {player.get_location()}. Your weapons are the {player.get_weapons()[0]} and the {player.get_weapons()[1]}. You are a {player.get_playclass()} of the race {player.get_race()}. Your total hitpoints are {player.get_max_hp()}. Welcome to the fight!" + "\033[0m")
    print("\n")

    return player
            
def continue_or_not(whether_new_monster):
    do_continue = input("Would you like to continue? Yes or No? ")
    print("\n")
    if (do_continue.lower().startswith("y")):
        if(whether_new_monster):
            print("\033[1m" + "The fight's not over! Time to fight a new monster!" + "\033[0m")

        else:
            print("\033[1m" + "The fight's not over! Time to fight the adversary that killed you!" + "\033[0m")

        return True
    else:
        print("\033[1m" + "Thank you young traveler for your bravery! See you in the next fight!" + "\033[0m")
        print("\n")
        return False

def player_attack_choice(player, monster):
    d20_roll = random.randint(0,20)
    print("\033[1m" + "Your damage roll was: " + "\033[0m" + str(d20_roll))
    monster.monster_attack(d20_roll)
    weapon = player.weapons[random.randint(0, 1)]
    print(f"Ouch! {monster.name} was hit with your " + weapon + " and has " + str(monster.get_hp()) + " hitpoints left!")
    if (d20_roll == 20):
        print("\n")
        print("Critical hit roll! Roll again for additional damage.")
        critical_hit = random.randint(0, 20)
        monster.monster_attack(critical_hit)
        print("Your crit roll was " + str(critical_hit) + f". {monster.name} now has " + str(monster.get_hp()) + " hitpoints left!")
    print("\n")

def player_heal_choice(player):
    player.heal_hp()
    if (player.get_hp() == player.get_max_hp()):
        print("You are now back at your max HP of " + str(player.get_max_hp()) + "!")
    print("Your current HP after healing is " + str(player.get_hp()) + ".")
    print("\n")

def player_prepare_choice(player):
    if (player.get_prepared() == False):
        player.set_prepared(True)
        print("Getting ready to prepare more damage for next turn...")
        print("\n")
        return False
    else:
        print("\033[1m" + "You are already prepared..." + "\033[0m")
        print("\n")
        return True
    
def player_execute_choice(player, monster):
    if (player.get_prepared()):
        roll_1 = random.randint(0, 20)
        roll_2 = random.randint(0, 10)
        roll_3 = random.randint(0, 10)
        damage = roll_1 + roll_2 + roll_3
        monster.monster_attack(damage)
        weapon = player.weapons[random.randint(0, 1)]
        print("\033[1m" + "Your first roll was " + str(roll_1) + ". Your second roll was " + str(roll_2) + ". Your third roll was " + str(roll_3) + ". Your total damage is " + str(damage) + "." + "\033[0m")
        print(f"{monster.name} was hit three times with your " + weapon + " and now has " + str(monster.get_hp()) + " hitpoints!")
        print("\n")
        player.set_prepared(False)
        return False
    else:
        print("\033[1m" + "You did not prepare before executing" + "\033[0m")
        print("\n")
        return True
    
def monster_turn(monster, player):
    print("\033[1m" + f"It is now the monster {monster.name}'s turn" + "\033[0m")
    hit_or_miss = random.randint(0, 1)
    if (hit_or_miss == 1):
        modifier = monster.get_modifier(5)
        d20_monster_roll = random.randint(0, 20)
        monster_hit = d20_monster_roll * modifier
        player.player_attack(monster_hit)
        print("The monster hit you with its attack! You took " + str(monster_hit) + " damage. The monster's roll was " + str(d20_monster_roll) + " with a strength modifier of " + str(modifier) + f". Your health is now {player.get_hp()}.")
        print("\n")
    elif (hit_or_miss == 0):
        print("The monster's attack missed! It is once again your turn!")
        print("\n")

fight()