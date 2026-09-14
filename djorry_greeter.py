import random
import datetime

current_time = datetime.datetime.now()
hour = current_time.hour


moods = [
    "счастливый", 
    "грустный", 
    "весёлый", 
    "сонный", 
    "игривый"
    ]

mood = random.choice(moods)

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
    "Djorry": "Главный Босс",
    "Victor": "Мой лучший друг"
}
name = special_names.get(name, name)

greeting = random.choice(greetings)

print(greeting.format(name=name))
print(f"Сегодня Djorry: {mood}!")

if hour == 7:
    print("Джорри, пора на утреннюю прогулку!")
elif hour == 14:
    print("Джорри, пора обедать!")
elif hour == 15:
    print("Джорри, получи вкусняшку!")
elif hour == 19:
    print("Джорри, пора на вечернюю прогулку!")
elif hour == 21:
    print("Джорри, пора ужинать!")
else:
    print("Сейчас у меня свободное время!")
