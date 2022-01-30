from unicodedata import category
from container import Container

def create_box():
    box = []
    for i in range(16):
        box.append(Container(i+1))
    return box

def get_itemlocation(box,item):
    for i in range(16):
        if box[i].does_itemexist(item):
            return i+1

def get_categoryLocation(box,category):
    for i in range(16):
        if box[i].get_category() == category:
            return i+1

def does_itemexist(box,item):
    for i in box:
        if i.does_itemexist(item):
            return True
    return False
def does_categoryexist(box,category):
    for i in box:
        if i.does_categoryexist(category):
            return True
    return False
def add_item(box, item, category):
    if does_itemexist(box,item): #if there is already one of the item
        box[get_itemlocation(box,item)-1].add_item(item,category)
    elif does_categoryexist(box,category): #if there is already one of the category type
        box[get_categoryLocation(box,category)-1].add_item(item,category)
    elif Container.capacity == 0: #if there is not enough space to make another category just exit
        return
    else:
        for i in box: #create new container
            if i.get_status() == "empty":
                i.add_item(item,category)
                Container.capacity-=1
    return

def remove_item(box,item):
    if does_itemexist(box,item):
        box[get_itemlocation(box,item)-1].remove_item(box,item)
    return

