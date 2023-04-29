import copy  # From ChatGPT/ used for copying object


class Inventory(Exception):
    # From ChatGPT/ Exeption is used for Error handling
    inventory = {
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
                if item["id"] == id:
                    self.inventory[key].remove(item)

        else:
            raise Inventory(
                "DEBUG: Invalid item! Try replacing with updateGold function")

    def updateGold(self, value):
        setValue = self.inventory["gold"] - value
        self.inventory.update({"gold": setValue})

    def showInventory(self,type=None):
        if type == "" or type == None:
            return(
                f"Gold: {self.inventory['gold']}\nWeapons: {self.inventory['weapons']}\nPotions: {self.inventory['potions']}\n")
        else:
            return self.inventory[type]
