from character import Hero, Villain
from weapon import short_bow, iron_sword

hero = Hero(name="Hero", hp=100)
hero.equip(iron_sword)
villain = Villain(name="Villain", hp=100, weapon=short_bow)

while True:
    hero.attack(villain)
    villain.attack(hero)

    hero.health_bar.draw()
    villain.health_bar.draw()

    input()
