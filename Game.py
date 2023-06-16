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
shopCategories = ["weapons", "potions"]
chooseClass = str(input("Choose your class: Knight, Mage, Archer:  ")).lower()
chooseTarget = True
itemsToSell = False
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
    xp = 0
    gold = 0
    for i in range(random.randint(1, 3)):
        randonName = names[random.randint(0, 3)]
        match randonName:
            case "rat":
                enemyList.append(Rat("rat"))
            case "skeleton":
                enemyList.append(Skeleton("skeleton"))
            case "spider":
                enemyList.append(Spider("spider"))
            case "zombie":
                enemyList.append(Zombie("zombie"))
        xp += 10
        gold += 20
    return xp, gold


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
                movementAction(attack)
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
            damageDone += player.showPlayerStats("dps")
            print(
                f"You have {player.showPlayerStats('end')} endurance remaining")
            for enemy in enemyList:
                if target == enemy.showEnemy("id"):
                    enemy.takeDamage(damageDone)
                    print(
                        f"""You dealt {damageDone} damage!
        {enemy.showEnemy("name")} has {enemy.showEnemy("hp")} HP left! 
                        """
                    )
                    if enemy.showEnemy("hp") == 0:
                        enemyList.remove(enemy)
            if len(enemyList) == 0:
                dialog.allDead()
                print(f"You received {xpAndGold[0]} XP")
                print(f"You received {xpAndGold[1]} Gold")
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
                    dialog.turnOver()
                    nextTurn = True

        elif inCombat == True:
            for enemy in enemyList:
                if player.showPlayerStats("hp") <= 0:
                    dialog.dead()
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
        dialog.merchantShop()
        time.sleep(0.3)
        weapons = merchant.inventory.showInventory("weapons")
        potions = merchant.inventory.showInventory("potions")
        for weapon in weapons:
            print(
                f"ID: {weapon['id']}  Name: {weapon['name']}  Gold value: {weapon['value']}  Damage: {weapon['dps']}"
            )
            time.sleep(0.1)
        print("\n")
        for potion in potions:
            print(
                f"ID: {potion['id']}  Name: {potion['name']}  Gold value: {potion['value']}  Damage: {potion['healing']}"
            )
            time.sleep(0.1)
        print("\n")
        dialog.merchantAction()
        buyOrSell = input("Shop action: ").lower()

        if buyOrSell == "buy":
            dialog.merchantBuy()
            category = input("Shop action: ").lower()
            while category not in shopCategories:
                dialog.merchantBuy()
                category = input("Shop action: ").lower()
            dialog.idToBuy()
            item = input("Shop action: ").lower()
            try:
                playerGold = player.inventory.showInventory("gold")
                newItem = merchant.itemBought(category, item, int(playerGold))
                if newItem == 0:
                    dialog.noGold()
                    time.sleep(0.4)
                else:
                    player.inventory.addItem(category, newItem)
                    player.inventory.subtractGold(newItem["value"])
                    if category == "weapons":
                        print(
                            f"You bought a {newItem['name']} with {newItem['dps']} DPS! "
                        )
                        dialog.weaponEqiupped()
                        player.updateDps(newItem["id"])
                    elif category == "potions":
                        print(
                            f"You bought a {newItem['name']} with {newItem['healing']} healing! "
                        )

            except:
                dialog.somethingWentWrong()

        elif buyOrSell == "sell":
            dialog.merchantSell()
            category = input("Shop action: ")
            forbiddenId = 0
            if category == "weapons":
                dialog.WeaponNotShownInShop()
                weaponIndex = 0
                for i in player.inventory.showInventory("weapons"):
                    weaponIndex += 1

                for weapon in player.inventory.showInventory("weapons"):

                    if weapon["dps"] == player.showPlayerStats("dps"):
                        forbiddenId = weapon["id"]

                    elif weapon["dps"] != player.showPlayerStats("dps"):
                        itemsToSell = True
                        print(weapon)

                if itemsToSell:
                    dialog.idToSell()
                    sellWeaponId = input("Shop action: ")
                    try:
                        if forbiddenId != sellWeaponId:
                            sellItem = player.inventory.showInventory(
                                "weapons", int(sellWeaponId))
                            player.inventory.addGold(sellItem["value"])
                            player.inventory.deleteItem(
                                "weapons", sellWeaponId)
                            print(
                                f"You now have {player.inventory.showInventory('gold')} Gold")
                    except:
                        dialog.somethingWentWrong()
                else:
                    dialog.nothingToSell()

            elif category == "potions":
                potionToSell = False
                potionIndex = 0
                for i in player.inventory.showInventory("potions"):
                    potionIndex += 1
                dialog.yourPotions()
                for potion in player.inventory.showInventory("potions"):
                    if potionIndex > 0:
                        print(potion)
                        potionToSell = True
                if potionToSell:
                    dialog.idToSell()
                    sellPotionId = input("Shop action: ")

                    try:
                        sellPotion = player.inventory.showInventory(
                            "potions", int(sellPotionId))
                        player.inventory.addGold(sellPotion["value"])
                        player.inventory.deleteItem("potions", sellPotionId)
                        print(
                            f"You now have {player.inventory.showInventory('gold')} Gold")

                    except:
                        dialog.somethingWentWrong()
                else:
                    dialog.nothingToSell()

            else:
                dialog.somethingWentWrong()

        elif buyOrSell == "help":
            dialog.help()
            time.sleep(1)

        elif buyOrSell == "leave":
            inShop = False


dialog.gameRule()
time.sleep(0)  # Change to 2 later
dialog.notifyHelp()


def switchWeapon():
    dialog.yourWeapons()
    for weapon in player.inventory.showInventory("weapons"):
        print(weapon)
    dialog.equipWeapon()
    equipWeapon = input("Action: ")
    try:
        player.updateDps(int(equipWeapon))
    except:
        dialog.somethingWentWrong()


def movementAction(action):
    if action == "help":
        dialog.help()

    elif action == "game rules":
        dialog.gameRule()

    elif action == "stats":
        print(player.showPlayerStats())

    elif action == "inv":
        print(player.inventory.showInventory())

    elif action == "help":
        dialog.help()

    elif action == "heal":
        healing()

    elif action == "switch":
        switchWeapon()

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
        exit()


while player.showPlayerStats("hp") > 0:
    dialog.actions()
    action = str(input("Player: ")).lower()
    movementAction(action)
