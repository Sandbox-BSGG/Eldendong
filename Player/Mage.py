from Player.Player import Player


class Mage(Player):

    def attack(self, type: str):
        match type:
            case "basic":
                damageDone = self.randInt(3, 10)
                newEnd = self.attributes["end"]-2
                self.attributes.update({"end": newEnd})
                return damageDone
            case "light":
                damageDone = self.randInt(3, 5)
                newEnd = self.attributes["end"]-4
                self.attributes.update({"end": newEnd})
                return damageDone
            case "heavy":
                damageDone = self.randInt(15, 30)
                newEnd = self.attributes["end"]-8
                self.attributes.update({"end": newEnd})
                return damageDone
            
m=Mage("mage")
m.showPlayerStats("end")
m.attack("basic")
m.showPlayerStats("end")
