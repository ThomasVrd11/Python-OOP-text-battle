from weapon import fists
from health_bar import HealthBar


class Character:
    race = "Human"

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.hp_max = hp

        self.weapon = fists

    def attack(self, target) -> None:
        target.hp -= self.weapon.damage
        target.hp = max(target.hp, 0)
        target.health_bar.update()
        print(f"{self.name} attacked {target.name} for {self.weapon.damage} damage with {self.weapon.name}")


class Hero(Character):
    def __init__(self, name, hp) -> None:
        super().__init__(name=name, hp=hp)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon}!")
        self.weapon = self.default_weapon

    def defend(self):
        print(f"{self.name} is defending and will take less damage this turn.")
        self.is_defending = True

class Villain(Character):
    def __init__(self, name, hp, weapon) -> None:
        super().__init__(name=name, hp=hp)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")

    def defend(self):
        print(f"{self.name} is defending and will take less damage this turn.")
        self.is_defending = True
