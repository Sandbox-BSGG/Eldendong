from Player.Player import Player


class Mage(Player):

    def attack(self, type: str):
        match type:
            case "basic":
                damageDone = self.randInt(5, 15)
                newEnd = self.attributes["end"]-4
                if newEnd <= 0:
                    self.attributes.update({"end": 0})
                else:
                    self.attributes.update({"end": newEnd})
                return damageDone
            case "light":
                damageDone = self.randInt(1, 5)
                newEnd = self.attributes["end"]-2
                if newEnd <= 0:
                    self.attributes.update({"end": 0})
                else:
                    self.attributes.update({"end": newEnd})
                return damageDone
            case "heavy":
                damageDone = self.randInt(15, 30)
                newEnd = self.attributes["end"]-6
                if newEnd <= 0:
                    self.attributes.update({"end": 0})
                else:
                    self.attributes.update({"end": newEnd})
                return damageDone
