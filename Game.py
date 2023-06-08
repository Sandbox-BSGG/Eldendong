import random
from Enemies.Enemy import Enemy
from Npcs.Merchant import Merchant
from Player.Player import Player
from Story.Dialog import Dialog
import time

dialog = Dialog()
dialog.intro()
gameLength = random.randint(20, 50)
classes = ["knight", "mage", "archer"]
enemyList = []
chooseClass = str(input("Choose your class: Knight, Mage, Archer:  ")).lower()

while chooseClass not in classes:
    print("Not a Class")
    chooseClass = input("Choose your class: Knight, Mage, Archer: ").lower()

player = Player(chooseClass)
merchant = Merchant(chooseClass)


def enemyGenerator():
    names = ["rat", "skeleton", "spider", "zombie"]
    for i in range(random.randint(0, 3)):
        enemyList.append(Enemy(names[random.randint(0, 3)]))


dialog.gameRule()
time.sleep(0)# Change to 2 later
print("Type help to see all your options as a Player")


while True:
    dialog.actions()
    action = str(input()).lower()

    if action == "help":
        dialog.help()

    elif action == "game rules":
        dialog.gameRule()

    elif action == "stats":
        print(player.showPlayerStats())

    elif action == "inv":
        print(player.inventory.showInventory())

    elif action == "w":
        print("You walked forward")
        enemyGenerator()
        for i in range(len(enemyList)):
            print(enemyList[i].showEnemy("name"))

    elif action == "a":
        print("You walked left")
        fe = True
    elif action == "s":
        print("You walked backwards")
    elif action == "d":
        print("You walked right")

    elif action == "stop":
        print("Thansk for playing and goodbye")
        break
    else:
        print("Wrong input")
        dialog.actions()
        action = str(input())
