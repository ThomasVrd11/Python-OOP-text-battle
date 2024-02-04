from character import Hero, Villain
from weapon import short_bow, iron_sword
import random

hero = Hero(name="Hero", hp=100)
hero.equip(iron_sword)
villain = Villain(name="Villain", hp=100, weapon=short_bow)

while hero.hp > 0 and villain.hp > 0:
    hero_action = input("What will the hero do? (attack, defend) ").strip().lower()
    villain_action =random.choice(["attack", "defend"])
    hero.is_defending = False
    villain.is_defending = False

    if hero_action == "attack":
        hero.attack(villain)
    elif hero_action == "defend":
        hero.defend()
    else:
        print("Invalid action. Try again.")
        continue

    if villain_action == "defend":
        villain.defend()
    elif hero.is_defending:
        print(f"{hero.name} successfully defended against {villain.name}'s attack!")
    else:
        villain.attack(hero)

    hero.health_bar.draw()
    villain.health_bar.draw()

    if hero.hp == 0:
        print("The Hero has been defeated!")
        break
    elif villain.hp == 0:
        print("The Villain has been defeated!")
        break

    input("Press Enter to continue to the next round...")