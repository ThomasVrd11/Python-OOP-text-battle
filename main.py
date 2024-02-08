from character import Hero, Villain
from weapon import short_bow, iron_sword, long_bow
import random

hero = Hero(name="Hero", hp=100)
hero.equip(long_bow)
villain = Villain(name="Villain", hp=100, weapon=short_bow)

while hero.hp > 0 and villain.hp > 0:
    hero.is_defending = False
    villain.is_defending = False

# --------------Hero's Turn----------------
    hero_action = input(
        "Choose an action for the Hero (attack/defend): ").strip().lower()
    villain_action = random.choice(['attack', 'defend'])

    if hero_action == "attack":
        hero.attack(villain)
    elif hero_action == "defend":
        hero.defend()

# --------------Villain's Turn----------------
    if villain_action == "defend":
        villain.defend()
    elif villain_action == "attack":
        villain.attack(hero)

# --------------End of Round----------------
    hero.is_defending = False
    villain.is_defending = False

    hero.health_bar.draw()
    villain.health_bar.draw()


# --------------Check for Winner----------------
    if hero.hp == 0:
        print("The Hero has been defeated!")
        break
    elif villain.hp == 0:
        print("The Villain has been defeated!")
        break
# ---------------Next Round----------------
    input("Press Enter to continue to the next round...")
