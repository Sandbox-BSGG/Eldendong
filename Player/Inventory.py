import copy  # From ChatGPT/ used for copying object


class Inventory(Exception):
    # From ChatGPT/ Exeption is used for Error handling
    def __init__(self):
        self.inventory = {
            "gold": 0,
            "weapons": [],
            "potions": [],
        }

    def addItem(self, key, value):
        newVal = copy.deepcopy(value)
        if key == "gold":
            setValue = self.inventory["gold"] + value
            self.inventory.update({key: setValue})
        else:
            self.inventory.setdefault(key, []).append(newVal)

    def deleteItem(self, key, id):
        if key != "gold":
            for item in self.inventory[key]:
                if item["id"] == int(id):
                    self.inventory[key].remove(item)

        else:
            raise Inventory(
                "DEBUG: Invalid item! Try replacing with updateGold function")

    def addGold(self, value):
        setValue = self.inventory["gold"] + value
        self.inventory.update({"gold": setValue})

    def subtractGold(self, value):
        setValue = self.inventory["gold"] - value
        self.inventory.update({"gold": setValue})

    def showInventory(self, type=None, id=None):
        if type == "" or type == None:
            return (
                f"Gold: {self.inventory['gold']}\nWeapons: {self.inventory['weapons']}\nPotions: {self.inventory['potions']}\n")
        elif type != None and id != None:
            for element in self.inventory[type]:
                if id == element["id"]:
                    return element
        elif type != None:
            return self.inventory[type]
