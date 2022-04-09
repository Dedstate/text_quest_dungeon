class Hero:
    def __init__(self, name):
        self.hp = 100
        self.damage = 15
        self.brony = 0
        self.name = name
        self.money = 10
        self.invent = []

    def add_equip(self, new_equip):
        self.invent.append(new_equip)
        if new_equip == "ржавый меч":
            self.damage += 15
        elif new_equip == "обожженный щит":
            self.brony += 15
        elif new_equip == "драная накидка":
            self.brony += 10

    def info_equip(self):
        return ", ".join(self.invent)

    def get_attack(self, value):
        if self.brony >= value:
            self.brony -= value
        elif self.brony < value:
            self.hp -= value - self.brony
            self.brony = 0


items = ["ржавый меч", "монеток", "обожженный щит", "драная накидка"]
