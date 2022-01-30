from motorcontrol import *
import time
class Container:
    capacity = 16
    def __init__(self,location):
        self.container_location = location
        self.status = "empty"
        self.category = "unused"
        self.num_items = 0
        self.items = { }

    def add_item(self, item, category):
        led_on(self.container_location)
        motor_control(self.container_location)
        if item in self.items: #if the item exists, just increase the item_count value
            self.items[item] += 1
        else:
            self.items[item] = 1 #else we add it to the collection
            self.category = category
        self.num_items+=1
        self.status = "used"
        time.sleep(5)
        led_off(self.container_location)
        return

    def remove_item(self,item): #removes item from container
        led_on(self.container_location)
        motor_control(self.container_location)
        if(item in self.items):
            self.num_items-=1
            del self.items[item]
            if self.num_items == 0:
                self.category = "unused"
                self.status = "empty"
                Container.capacity+=1
        #turn on led(self.container_location)
        time.sleep(5)
        led_off(self.container_location)
        return

    def get_category(self): #gets the category of the container
        return self.category

    def get_numitems(self): #get total number of items in container
        return self.num_items

    def get_numofsingleitem(self,item): #returns how many of that specific item are in the container
        return self.items[item]

    def does_itemexist(self,item): #checks to see if an item exists in this container
        if item in self.items:
            return True;
        else:
            return False;
    def get_status(self):
        return self.status


