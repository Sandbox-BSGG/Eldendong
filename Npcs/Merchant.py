from Player.Inventory import Inventory
from Items.Weapon import Weapon
from Items.Healpotion import HealthPotion
import random


class Merchant:
    def __init__(self, clazz: str):
        self.inventory = Inventory()
        self.shopWeapon = None
        for i in range(10):
            match clazz:
                case "knight":
                    self.shopWeapon = Weapon("sword", self.numGenerator())
                case "mage":
                    self.shopWeapon = Weapon("staff", self.numGenerator())
                case "archer":
                    self.shopWeapon = Weapon("bow", self.numGenerator())
            if self.shopWeapon != None:
                self.inventory.addItem(
                    "weapons", self.shopWeapon.showWeaponStats())
        for i in range(10):
            self.shopPotion = HealthPotion(self.numGenerator(1, 3))
            self.inventory.addItem("potions", self.shopPotion.showPotion())

    def itemBought(self, key, id):
        self.boughtItem = self.inventory.showInventory(key, id)
        self.inventory.deleteItem(key, id)
        return self.boughtItem

    def numGenerator(self, start=30, end=200):
        return random.randint(start, end)
