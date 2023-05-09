from Player.Inventory import Inventory
from Items.Weapon import Weapon
from Items.Healpotion import HealthPotion


class Merchant:
    def __init__(self, clazz: str):
        self.inventory = Inventory()
        self.shopWeapon = None
        match clazz:
            case "knight":
                self.shopWeapon = Weapon("sword", 100)
            case "mage":
                self.shopWeapon = Weapon("staff", 100)
            case "archer":
                self.shopWeapon = Weapon("bow", 100)
        if self.shopWeapon != None:
            self.inventory.addItem("weapons", self.shopWeapon.showWeaponStats())
            for i in range(10):
                self.shopPotion = HealthPotion(2)
                self.inventory.addItem("potions", self.shopPotion.showPotion())

    def itemBought(self,key,id):
        self.boughtItem=self.inventory.showInventory(key,id)
        self.inventory.deleteItem(key,id)        
        return self.boughtItem
    

