import random
from hero import Hero, items


def make_choice(*args) -> int:
    print("Варианты действий:")
    for i, value in enumerate(args):
        print(i + 1, value)
    return int(input("Сделай свой выбор: "))


def is_true(chance: int) -> bool:
    if int(random.random() * 100) in range(0, chance):
        return True
    return False


def battle(chance: int, fail_damage: int, success_damage: int) -> None:
    if is_true(chance):
        enemy.get_attack(success_damage)
        ch = make_choice("Защищаться", "Атаковать")
        if ch == "1":
            hero.heal(enemy.damage)
        else:
            enemy.get_attack(hero.damage)
    else:
        hero.get_attack(fail_damage)


hero = Hero("Тыкающий Федя")
enemy = Hero("Георгий, типо-рисующая ленивая черепашка")

print("Привет, о славный username")
print(
    "Этот мир погряз в боли и отчаянии и только ты можешь с этим справиться!"
)
print("Готов ли ты дать им отпор?")
input()
ch = make_choice("Пошарить вокруг", "В поисках приключений")
if ch == 1:
    item = random.choice(items)
    if item == "монеток":
        hero.add_money(random.randint(1, 10))
    else:
        hero.add_equip(item)
    print("Мой инвентарь: " + hero.get_invent())
else:
    while enemy.hp > 0 and hero.hp > 0:
        ch = make_choice(
            "Подкрасться со спины", "Подготовить засаду", "Пойти напролом"
        )
        enemy.hp += 100
        if ch == 1:
            battle(65, fail_damage=20, success_damage=30)
        elif ch == 2:
            battle(30, fail_damage=35, success_damage=50)
        else:
            battle(100, fail_damage=15, success_damage=0)
    if hero.hp <= 0:
        print(f"{hero.name} проиграл(а).")
    else:
        print(f"{enemy.name} проиграл.")
