
class Inventory:
    def __init__(self):
        #self refers to the objects itself
        #init is a specialized function that runs automatically when you create a new inventory 
        #self is the name of the object
        self.items ={}
        #creates an empty dictionary( like an empty bag)
    def add(self, name, qty=1):
        #item is name of item you add
        #
        self.items[name] = self.items.get(name, 0) + qty
        #self.items.get(name, 0) looks up the item in the dictionary
            #if it exist, it returns the current quantity
            # if it doesn;t it returns 0
        # + qty: adds new quantity at the top
        #self.items[item] = save the results back into dictionary


    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def show(self):
        for item, qty in self.items.items():
            print(f"{item}: {qty}")
    
    
    
   
        
    
class Monster:
    def __init__(self, name, attack_power, weakness, life_points, speed):
        self.name = name
        self.attack_power = attack_power
        self.weakness = weakness
        self.life_points = life_points
        self.speed = speed
        



class Room:
    #attributes
    def __init__(self, name, monster):#constructor
        self.name = name
        self.inventory = Inventory() #composition
        self.monster = monster
        self. exits = {}
    
    def add_exit(self, direction, Room):
        self.exits[direction] = Room
    
    
        
    
    

 

    