import random

greetings = [
    "Привет,{name}! Джорри уже бежит к тебе!",
    "Ого, {name}! Джорри уже принёс тебе тапок в подарок!",
    "Джорри говорит: '{name}, ты пахнешь как лучший друг!'",
    "Внимание! Джорри объявляет {name} самым классным человеком дня!",
    "Гав! {name}, Джорри хочет обнять тебя всеми четырьмя лапами!",
]

name = input("Как тебя зовут?")

special_names = {
    "Irina": "Мама",
    "Sergey": "Папа",
    "Djorry": "Главный Босс"
}
name = special_names.get(name, name)

greeting = random.choice(greetings)

print(greeting.format(name=name))
