class Hero:
    def __init__(self, name: str):
        self.hp = 100
        self.damage = 15
        self.brony = 0
        self.name = name
        self.money = 10
        self.invent = []

    def add_equip(self, new_equip: str) -> None:
        self.invent.append(new_equip)
        if new_equip == "ржавый меч":
            self.damage += 15
        elif new_equip == "обожженный щит":
            self.brony += 15
        elif new_equip == "драная накидка":
            self.brony += 10

    def add_money(self, money: int) -> None:
        self.money += money

    def get_invent(self) -> str:
        if self.invent:
            return ", ".join(self.invent) + f", а также {self.money} монеток"
        return f"только {self.money} монеток"

    def get_attack(self, value: int) -> None:
        if self.brony >= value:
            self.brony -= value
        elif self.brony < value:
            self.hp -= value - self.brony
            self.brony = 0

    def heal(self, value: int) -> None:
        if value + self.hp > 100:
            self.brony += value - (100 - self.hp)
            self.hp = 100
        else:
            self.hp += value


items = ["ржавый меч", "монеток", "обожженный щит", "драная накидка"]
