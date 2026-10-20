from message_filter import is_important, get_category

with open("messages.txt", "a", encoding="utf-8"):
    pass

while True:
    print("\n🐶 Фильтр сообщений")
    print("1 - Добавить сообщение")
    print("2 - Показать важные сообщения")
    print("3 - Показать статистику")
    print("0 - Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "0":
        print("До свидания!")
        break
    elif choice == "1":
        message = input("Введите новое сообщение: ")

        if message.strip():
            with open("messages.txt", "a", encoding="utf-8") as file:
                file.write(message + "\n")

            print("Сообщение сохранено!")
        else:
            print("Ошибка! Пустое сообщение не сохраняется.")
    elif choice == "2":
        with open("messages.txt", "r", encoding="utf-8") as file:
            saved_messages = file.read().splitlines()
        
        print("Всего сохранённых сообщений:", len(saved_messages))
        for message in saved_messages:
            if is_important(message):
                print("!", message)
    elif choice == "3":
        counts = {
        "Срочно": 0,
        "Важное": 0,
        "Мероприятия": 0,
        "Обычное": 0,
        "Пустое": 0
    }
        with open ("messages.txt", "r", encoding="utf-8") as file:
            saved_messages = file.read().splitlines()

        for message in saved_messages:
            category = get_category(message)
            counts[category] += 1
        print("\n📊 Статистика сообщений:")

        for category, count in counts.items():
            print(f"{category}: {count}")
        print("Всего сообщений:", sum(counts.values()))

    else:
        print("Ошибка! Выберите 0, 1, 2 или 3.")