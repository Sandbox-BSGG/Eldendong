from Items.Healpotion import HealthPotion
from Inventory import Inventory
from Items.Weapon import Weapon
import random


class Player:

    def __init__(self, playerClass: str):
        self.attributes = {
            "hp": 50,
            "maxHp": 50,
            "end": 10,
            "dps": 0,
            "lvl": 1,
            "xp": 0,
            "maxEnd": 10}
        self.starterPotion = HealthPotion(1)
        match playerClass:
            case "knight":
                self.starterWeapon = Weapon("sword", self.randInt(5, 10))
            case "mage":
                self.starterWeapon = Weapon("staff", self.randInt(5, 10))
            case "archer":
                self.starterWeapon = Weapon("bow", self.randInt(5, 10))
        self.inventory = Inventory()
        self.inventory.addItem("weapons", self.starterWeapon.showWeaponStats())
        self.inventory.addItem("potions", self.starterPotion.showPotion())
        self.updateDps(1)

    def usePotion(self, id):
        getPotion = self.inventory.showInventory("potions", id)
        healing = getPotion["healing"] + self.attributes["hp"]
        if healing > self.attributes["maxHp"]:
            self.attributes.update({"hp": self.attributes["maxHp"]})
            self.inventory.deleteItem("potions", 0)
            return f"full heal"
        else:
            self.attributes.update({"hp": healing})
            self.inventory.deleteItem("potions", 0)
            return f"healing {getPotion['healing']}"

    def updateDps(self, id):
        getWeapon = self.inventory.showInventory("weapons", id)
        self.attributes.update({"dps": getWeapon})

    def showPlayerStats(self, type=None):
        if type == "" or type == None:
            return (
                f"HP: {self.attributes['hp']}\nEndurance: {self.attributes['end']}\nDPS: {self.attributes['dps']}\n"
            )
        else:
            return self.attributes[type]

    def takeDamage(self, damage: int):
        newHp = self.attributes["hp"] - damage
        self.attributes.update({"hp": newHp})

    def sellItem(self, key, id):
        sellItem = self.inventory.showInventory(key, id)
        self.inventory.addGold(sellItem["value"])
        self.inventory.deleteItem(key, id)

    def randInt(self, start=0, end=10):
        return random.randint(start, end)

    def nextRound(self):
        self.attributes.update({"end": self.attributes["maxEnd"]})

    def addStat(self, stat: str, value):  # mainly used for xp
        newStat = self.attributes[stat]+value
        return self.attributes.update({stat: newStat})

    def lvlUp(self):
        if self.attributes["xp"] == 100 or self.attributes["xp"] >= 100:
            self.attributes.update({"lvl": self.attributes["lvl"]+1})
            self.addStat("maxEnd", 5)
            self.addStat("maxHp", 10)
            return
        else:
            xpNeeded = 100-self.attributes["xp"]
            return f"You need {xpNeeded} XP for the next level"