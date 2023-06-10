import random
from Enemies.Rat import Rat
from Enemies.Skeleton import Skeleton
from Enemies.Spider import Spider
from Enemies.Zombie import Zombie
from Npcs.Merchant import Merchant
from Player.Archer import Archer
from Player.Knight import Knight
from Player.Mage import Mage
from Story.Dialog import Dialog
import time

dialog = Dialog()
dialog.intro()
gameLength = random.randint(20, 50)
classes = ["knight", "mage", "archer"]
attackList = ["basic", "light", "heavy"]
enemyList = []
chooseClass = str(input("Choose your class: Knight, Mage, Archer:  ")).lower()
chooseTarget = True

while chooseClass not in classes:
    print("Not a Class")
    chooseClass = input("Choose your class: Knight, Mage, Archer: ").lower()

merchant = Merchant(chooseClass)


def choosePlayer(chooseClass):
    match chooseClass:
        case "knight":
            return Knight("knight")
        case "mage":
            return Mage("mage")
        case "archer":
            return Archer("archer")


player = choosePlayer(chooseClass)


def enemyGenerator():
    names = ["rat", "skeleton", "spider", "zombie"]
    counter = 0
    gold = 0
    for i in range(random.randint(1, 3)):
        randonName = names[random.randint(0, 3)]
        match randonName:
            case"rat":
                enemyList.append(Rat("rat"))
            case"skeleton":
                enemyList.append(Skeleton("skeleton"))
            case"spider":
                enemyList.append(Spider("spider"))
            case"zombie":
                enemyList.append(Zombie("zombie"))
        counter += 10
        gold += 20
    return counter, gold


def healing():
    print(player.inventory.showInventory("potions"))
    while True:
        potion = input("Choose your potion: ").lower()
        try:
            int(potion)
            player.usePotion(potion)
            break

        except (ValueError, IndexError):
            continue


def combatEncounter():
    chooseTarget = True
    inCombat = True
    nextTurn = False
    notEnoughEnd = True

    xpAndGold = enemyGenerator()

    dialog.inCombat()
    time.sleep(0.3)
    while inCombat:
        if player.showPlayerStats("end") >= 1 and nextTurn == False:
            dialog.encounter()
            for i in range(len(enemyList)):
                print(enemyList[i].showEnemy("name"))
            dialog.chooseMob()

            while chooseTarget:
                target = input("Player Combat: ").lower()
                try:
                    target = int(target)
                    for enemy in enemyList:
                        if target == enemy.showEnemy("id"):
                            chooseTarget = False
                        else:
                            continue
                except (ValueError, IndexError):
                    dialog.Nan()

            chooseTarget = True
            time.sleep(0.3)
            dialog.chooseAttack()
            attack = input("Player: ").lower()

            while attack not in attackList:

                if attack == "help":
                    dialog.help()
                    attack = input("Player: ").lower()
                elif attack == "heal":
                    healing()
                else:
                    dialog.attackInvalid()
                attack = input("Player: ").lower()
            while notEnoughEnd:
                if attack not in attackList:
                    dialog.attackInvalid()
                    attack = input("Player: ").lower()

                elif attack == "light" and player.showPlayerStats("end") < 2:
                    dialog.noEnd()
                    attack = input("Player: ").lower()

                elif attack == "basic" and player.showPlayerStats("end") < 4:
                    dialog.noEnd()
                    attack = input("Player: ").lower()

                elif attack == "heavy" and player.showPlayerStats("end") < 8:
                    dialog.noEnd()
                    attack = input("Player: ").lower()

                else:
                    notEnoughEnd = False

            notEnoughEnd = True

            damageDone = player.attack(attack)
            damageDone+= player.showPlayerStats("dps")
            print(
                f"You have {player.showPlayerStats('end')} endurance remaining")
            for enemy in enemyList:
                if target == enemy.showEnemy("id"):
                    enemy.takeDamage(damageDone)
                    print(f"""You dealt {damageDone} damage!
        {enemy.showEnemy("name")} has {enemy.showEnemy("hp")} HP left! 
                        """)
                    if enemy.showEnemy("hp") == 0:
                        enemyList.remove(enemy)
            if len(enemyList) == 0:
                dialog.allDead()
                print(f"You recived {xpAndGold} XP")
                player.addStat("xp", xpAndGold[0])
                player.inventory.addGold(xpAndGold[1])
                print(player.lvlUp())
                xpAndGold = 0
                player.nextRound()
                player.addStat("hp", 200)
                nextTurn = True
                inCombat = False
            else:

                if player.showPlayerStats("end") >= 1:
                    turn = input("Do you want to end turn? Y/N: ").lower()
                    if turn == "y" or turn == "yes":
                        nextTurn = True
                else:
                    print("No Endurance turn ended")
                    nextTurn = True

        elif inCombat == True:
            for enemy in enemyList:
                if player.showPlayerStats("hp") <= 0:
                    print("YOU DIED")
                    inCombat = False
                    break
                enemyDamage = enemy.attack(attackList[random.randint(0, 2)])
                player.takeDamage(enemyDamage)
                print(f"{enemy.showEnemy('name')} dealt {enemyDamage} to you!")
                print(f"You have {player.showPlayerStats('hp')} HP remaining")
                time.sleep(1)
            nextTurn = False
            player.nextRound()


def merchantEncounter():
    inShop = True

    while inShop:
        print("You have encountered a Merchants shop!")
        print("IMPORTANT: This Merchant will disappear if you leave his shop")
        time.sleep(0.3)
        weapons = merchant.inventory.showInventory("weapons")
        potions = merchant.inventory.showInventory("potions")
        for weapon in weapons:
            print(
                f"ID: {weapon['id']}  Name: {weapon['name']}  Gold value: {weapon['value']}  Damage: {weapon['dps']}")
            time.sleep(0.1)
        print("\n")
        for potion in potions:
            print(
                f"ID: {potion['id']}  Name: {potion['name']}  Gold value: {potion['value']}  Damage: {potion['healing']}")
            time.sleep(0.1)
        print("\n")
        print("Do you want to buy or sell something? buy / sell / leave / help")
        buyOrSell = input().lower()


dialog.gameRule()
time.sleep(0)  # Change to 2 later
dialog.notifyHelp()


while player.showPlayerStats("hp") > 0:
    dialog.actions()
    action = str(input("Player: ")).lower()

    if action == "help":
        dialog.help()

    elif action == "game rules":
        dialog.gameRule()

    elif action == "stats":
        print(player.showPlayerStats())

    elif action == "inv":
        print(player.inventory.showInventory())

    elif action == "w":
        dialog.actionW()
        combatEncounter()

    elif action == "a":
        dialog.actionA()
        merchantEncounter()
    elif action == "s":
        dialog.actionS()
        combatEncounter()
    elif action == "d":
        dialog.actionD()
        combatEncounter()
    elif action == "stop":
        dialog.stop()
        break
