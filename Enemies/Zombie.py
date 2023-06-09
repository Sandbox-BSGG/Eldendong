from Enemies.Enemy import Enemy


class Zombie(Enemy):

    def attack(self, type: str):
        match type:
            case "basic":
                damageDone = self.randInt(3, 10)
                newEnd = self.attributes["end"]-self.randInt(1, 5)
                self.attributes.update({"end": newEnd})
                return damageDone
            case "light":
                damageDone = self.randInt(3, 5)
                newEnd = self.attributes["end"]-self.randInt(1, 3)
                self.attributes.update({"end": newEnd})
                return damageDone
            case "heavy":
                damageDone = self.randInt(15, 30)
                newEnd = self.attributes["end"]-self.randInt(5, 10)
                self.attributes.update({"end": newEnd})
                return damageDone
