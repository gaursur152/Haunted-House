from Room import Inventory
from Room import Monster
from Room import Room
import random
class Player:
    def __init__(self):
        self.health = 100
        self.inventory = Inventory()
        self.current_room = None

    def __take_dammage__(self):
        self.health = self.health - self.current_room.monster.attack_power
        
        #I assume pass is like a place holder

    def __update_room__(self,new_room ):
        self.current_room = new_room
        

        #pass
    
    def __pick_up__(self, item):

        if item in self.current_room.inventory.items:
            self.inventory.add(item)
            self.current_room.inventory.remove_item(item)


    def __random_error__(self):
        self.phrase = ["You Missed!", "Lousy Shot", "Nope! Try Again", "Monsted doged it! Try again.", "Bad aim", "You failed", "not close enough"] 
        num = random.randint(0, 6)
        print(self.phrase[num])
    

    def use_weapon(self, weapon, monster):
        if(weapon in self.inventory.items):
            """checks if weapon is a key in the dictionary"""

            if(weapon == "Bat"):
                random_num = random.randint(1, 100000000)
                if random_num % 3 == 0:
                    monster.life_points = monster.life_points - 29
                    print("Damage done - 29!")
                else:
                    self.__take_dammage__()
                    self.__random_error__()
                    

            elif (weapon == monster.weakness):
                    monster.life_points = 0
                    self.inventory.remove_item(weapon)
                    print("Critical hit! Bonus points on weapon choice")

            elif (weapon == "Garlic" ):
                    self.__take_dammage__()
                    print("No damage can be done on this monster with Garlic")
            
            elif (weapon == "Gun" ):
                random_num = random.randint(1,1000000000)
                if random_num % 2 == 0:
                    monster.life_points = monster.life_points - 55
                    print("Damage done! -55")
                else:
                    self.__take_dammage__()
                    self.__random_error__()

            elif (weapon == "Silver Sword" ):
                random_num = random.randint(1, 100000000)
                if random_num % 5 == 0:
                    monster.life_points = monster.life_points - 50
                    print("Damage done! - 50")
                else:
                    self.__take_dammage__()
                    self.__random_error__()
            
            elif (weapon == "Fire" ):
                random_num = random.randint(1, 100000000)
                if random_num % 20 <= 12:
                    monster.life_points = monster.life_points - 67
                    print("Damage done! -67")
                else:
                    self.__take_dammage__()
                    self.__random_error__()

        else:
            print("Not stored in Inventory")
        
        if(monster.life_points <= 0):
            self.current_room.monster = None
            print(monster.name + " has been defeated! You can move on to the next room")
        #pass
