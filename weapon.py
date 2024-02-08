class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = Weapon(
    name="Iron Sword",
    weapon_type="sharp",
    damage=10,
    value=10)
short_bow = Weapon(name="Short Bow", weapon_type="ranged", damage=8, value=8)
fists = Weapon(name="Fists", weapon_type="blunt", damage=2, value=0)
dagger = Weapon(name="Dagger", weapon_type="sharp", damage=6, value=5)
long_bow = Weapon(name="Long Bow", weapon_type="ranged", damage=12, value=15)
club = Weapon(name="Club", weapon_type="blunt", damage=5, value=3)
