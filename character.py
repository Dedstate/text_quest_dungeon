import random

class Hero:
    def __init__(self, name):
        self.hp = 100
        self.damage = 5
        self.brony = 20
        self.name = name
        self.money = 10
        self.invent = []

    def add_equip(self, new_equip):
        self.invent.append(new_equip)
        if new_equip == 'sword':
            self.damage += 15
        elif new_equip == 'shield':
            self.brony += 15
        else:
            self.brony += 5

    def info_equip(self):
        return ", ".join(self.invent)


items = ['Ржавый меч', 'монеток', 'обожженный щит', 'драная накидка']
