class Inventory(Exception):
# From ChatGPT/ Exeption is used for Error handling
    inventory = {
        "gold": 0,
        "weapons": [],
        "potions": [],
    }

    def addItem(self, key, value):
        if key == "gold":
            setValue = self.inventory["gold"] + value
            self.inventory.update({key: setValue})
        else:
            self.inventory.setdefault(key, []).append(value)

    def deleteItem(self, key, index):
        if key!="gold":
            self.inventory[key].pop(index)
        else:
            raise Inventory("DEBUG: Invalid item! Try replacing with updateGold function")

    def updateGold(self, value):
        setValue = self.inventory["gold"] - value
        self.inventory.update({"gold":setValue})

    def showInventory(self):
        print(f"Gold: {self.inventory['gold']}\nWeapons: {self.inventory['weapons']}\nPotions: {self.inventory['potions']}\n")