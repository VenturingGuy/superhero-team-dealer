import random
from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: string
          starting_health: Integer
          current_health: Integer
        '''
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
    
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) Check if at least on hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won.
        # 2) The hero (self) and their opponent must attack each other and each must take damage from the other's attack.
        # 3) After each attack, check if either the hero (self) or the opponent is alive.
        # 4) If one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop.
        if not self.abilities or not opponent.abilities:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                if opponent.is_alive() == False:
                    print(self.name + " has won!")
                self.take_damage(opponent.attack())
                if self.is_alive() == False:
                    print(opponent.name + " has won!")

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        ''' Calculate the total damage from all ability attacks.
             return: total_damage: Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        ''' Add armor to self.armors
             Armor: Armor Object
        '''

        # TODO: Add armor object that is passed into 'self.armors'
        self.armors.append(armor)

    def defend(self, damage_amt):
        ''' Calculate the total block amount from all armor blocks.
            return: total_block: Int
        '''
        total_block = 0
        # TODO: This method should run the block method on each armor in self.armors
        for armor in self.armors:
            total_block += armor.block()
        
        return total_block
             
    def take_damage(self, damage):
        ''' Updates self.current_health to reflect the damage minus the defense.
        '''

        # TODO: Create a method that updates self.current_health to the current
        # minus the amount returned from calling self.defend(damage)
        self.current_health -= (damage - self.defend(damage))

    def is_alive(self):
        ''' Return True or False depending on whether the hero is alive or not.
        '''

        # TODO: Check the current_health of the hero.
        # If it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True
            


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Amuro Ray", 200)
    hero2 = Hero("Char Aznable", 250)
    shield = Armor("Shield", 50)
    ability1 = Ability("Beam Rifle", 100)
    ability2 = Ability("Funnels", 200)
    ability3 = Ability("Fin Funnels", 250)
    hero1.add_ability(ability1)
    hero1.add_ability(ability3)
    hero2.add_ability(ability1)
    hero2.add_ability(ability2)
    hero1.add_armor(shield)
    hero1.fight(hero2)