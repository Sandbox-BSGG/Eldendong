from Player.Inventory import Inventory
from Items.Weapon import Weapon
from Items.Healpotion import HealthPotion
import random


class Merchant:
    def __init__(self, clazz: str):
        self.inventory = Inventory()
        self.shopWeapon = None
        self.weaponTypes=["sword","staff","bow"]
        self.godWeaponType=None
        for i in range(10):
            match clazz:
                case "knight":
                    self.shopWeapon = Weapon(self.weaponTypes[0], self.numGenerator())
                    self.godWeaponType=0
                case "mage":
                    self.shopWeapon = Weapon(self.weaponTypes[1], self.numGenerator())
                    self.godWeaponType=1
                case "archer":
                    self.shopWeapon = Weapon(self.weaponTypes[2], self.numGenerator())
                    self.godWeaponType=1

            if self.shopWeapon != None:
                self.inventory.addItem(
                    "weapons", self.shopWeapon.showWeaponStats())
        for i in range(10):
            self.shopPotion = HealthPotion(self.numGenerator(1, 3))
            self.inventory.addItem("potions", self.shopPotion.showPotion())
        self.godWeapon=Weapon(self.weaponTypes[self.godWeaponType],600,"God killing weapon")
        self.inventory.addItem("weapons",self.godWeapon.showWeaponStats())


    def itemBought(self, key, id, gold):
        self.boughtItem = self.inventory.showInventory(key, int(id))
        if gold<self.boughtItem["value"]:
            return 0
        else:
            self.inventory.deleteItem(key, id)
            return self.boughtItem

    def numGenerator(self, start=30, end=200):
        return random.randint(start, end)
