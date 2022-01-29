class Container:
    def __init__(self,category,num_items,item,location):
        self.container_location = location
        self.status = "empty"
        self.category = category
        self.num_items = num_items
        self.items = {
            "item_name" : item,
            "item_count": 0
        }

    def add_item(self, item):
        if item in self.items: #if the item exists, just increase the item_count value
            self.items[item] += 1
        else:
            self.items[item] = 1 #else we add it to the collection
        self.num_items+=1
        self.status = "used"
        return

    def remove_item(self,item): #removes item from container
        if(item in self.items):
            self.num_items-=1
            self.items.remove(item);
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

