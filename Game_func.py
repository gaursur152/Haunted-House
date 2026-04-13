
from Room import Room
from Room import Monster
from Room import Inventory
from Player import Player
from Maze import Maze
import random
class Game:
    def __setup_rooms__(self):
        living_room = Room("Living room", None)
        graveyard = Room("Graveyard", Monster("Zombie",5,None,float('inf'),1 ))
        basement = Room("Basement", Monster("Ghost",10,"Fire",150,9))
        kitchen = Room("Kitchen", Monster("Witch",10,"Fire",75,3))
        tv_room = Room("Tv room", Monster("Ghostface",20,"Gun",100,5 ))
        resting_room = Room("Resting Room", Monster("Nosferatu",25, "Garlic", 200, 8))
        backyard = Room("Backyard", Monster("Werewolf",30,"Silver Sword", 100, 9))
        final_exit = Room("Exit", None)

        #living room exits
        living_room.add_exit("beloweast", graveyard)
        living_room.add_exit("belowwest", basement)
        living_room.add_exit("east", kitchen)
        living_room.add_exit("north", tv_room)
        living_room.add_exit("west", resting_room)
        living_room.add_exit("south", backyard)

        #graveyard
        graveyard.add_exit("east", basement)
        graveyard.add_exit("above", living_room)

        #basement
        basement.add_exit("west", graveyard)
        basement.add_exit("above", living_room)

        #Kitchen
        kitchen.add_exit("west", living_room)
        #if monsters == none
        kitchen.add_exit("northwest", tv_room)

        #Tv Room
        tv_room.add_exit("south", living_room)
        tv_room.add_exit("southeast", kitchen)
        tv_room.add_exit("northwest", resting_room)

        #Resting Room
        resting_room.add_exit("east",living_room)
        resting_room.add_exit("southeast", tv_room)
        resting_room.add_exit("northwest", backyard)

        #Backyard
        backyard.add_exit("north", living_room)
        backyard.add_exit("southeast", resting_room)
        backyard.add_exit("south", final_exit)

        #adding rooms
        self.rooms = {"Living Room" : living_room, "Graveyard" : graveyard, "Basement" : basement, "Kitchen" : kitchen, "Tv Room" :tv_room, "Resting room" : resting_room, "Backyard" : backyard,"Exit" : final_exit}

    def __generate_weapons__(self):
        valid_rooms = [room for room in self.rooms.values() if room.name != "Exit"] 
        """loops through each room short hand for 
            It's a shorthand for writing this longer version:
                valid_rooms = []
                for room in self.rooms.values():
                if room.name != "Exit":
                valid_rooms.append(room)"""
        weapons = ["Garlic","Gun","Silver Sword","Fire"]
        for weapon in weapons:
            room = random.choice(valid_rooms)
            room.inventory.add(weapon)
    

    def __create_player__(self):
        self.player = Player()
        self.player.__update_room__(self.rooms["Living Room"])
        self.player.inventory.add("Bat")
    
    def __move__(self, direction):
        if direction == "retreat":
            if not self.visited_rooms:
                print("Nowhere to retreat to")
                return
            self.current_room = self.visited_rooms[-1]
            self.visited_rooms.pop()
            return
        
        
        if direction in self.current_room.exits:
           
            next_room = self.current_room.exits[direction]
            if self.current_room.monster != None and self.current_room.monster.life_points > 0:
                return "Error can not move forward unless monster is defeated"

            if self.current_room.name == "Graveyard":
                grave = Maze()
                grave.play()
                self.visited_rooms.append(self.current_room)
                self.player.__update_room__(next_room)
                self.current_room = next_room
 
            else:
                self.visited_rooms.append(self.current_room)
                self.player.__update_room__(next_room)
                self.current_room = next_room  
                    


        else:
             print("Error")  

     

            
            
    def __end_condition__(self):
        if self.current_room == self.rooms["Exit"]:
             return "Game Over You Win!"
        elif self.player.health <= 0:
             return "Game Over You Lose"

        
    def __init__(self):
        self.rooms = {}
        self.__setup_rooms__()
        self.__generate_weapons__()
        
        self.current_room = self.rooms["Living Room"]
        self.visited_rooms = []
        self.__create_player__()
        self.end_condition = None
        
    def __main_func__ (self):
         print("Welcome to the manor")
         print("Your goal is to esacpe this haunted place before you become a part of it!\nYou will encounter all sorts of creatures that have roamed in humans' imagination for centuriues,\nso tread lightly...\nThis game is unlike other games where almost no direction will be given to players who dare try to \nesacpe!\nOnly with knowledge of the ghoul releam and instinct may you escape.\nGood Luck.")
        
         
         while(self.__end_condition__() is None):
            print("="*40)
            print("\n")
            forward = []
            retreat = []

            for direction, destination in self.current_room.exits.items():
                if destination in self.visited_rooms:
                    retreat.append(direction)
                else:
                    forward.append(direction)

            print("Current room: " + self.current_room.name , "Health:" + str(self.player.health),"\nNext rooms direction" + str(forward), "\nRetreatable rooms:" + str(retreat), "\nItems to pick up:" + str(self.current_room.inventory.items))
            if self.current_room.monster != None:
                

                print(str(self.current_room.monster.name)+" LP: " + str(self.current_room.monster.life_points))
                
                if(self.current_room.name == "Graveyard"):
                     print("YOU HAVE ENTERED THE GRAVEYARD NO WEAPON WILL SAVE YOU HERE ONLY LUCK FOR WHAT IS DEAD MAY NEVER DIE")
                else:
                    print(self.current_room.monster.name + " is appearing to block your path \n you can use your weapons to defeat them")
            print("="*40)
            print("Options \n 1. move \n 2. pick up weapon \n 3. use weapon \n 4. show inventory \n 5. stop the game")
            i = input("what would you like to do: ")
            
            if(i == "1" or i == "move"):
                direction = input("What direction: ")
                self.__move__(direction)
            elif(i=="2" or i == "pick up weapon"):
                 weapon = input("object: ")
                 self.player.__pick_up__(weapon)
            elif (i== "3" or i == "use weapon"):
                 weapon = input("object: ")
                 self.player.use_weapon(weapon, self.current_room.monster)
            elif (i== "4" or i == "show inventory"):
                 self.player.inventory.show()

            elif (i == "stop the game" or i == "5"):
                 return "GameOver"
        
         print(str(self.__end_condition__()))
