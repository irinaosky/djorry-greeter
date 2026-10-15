def get_clean_words(message):
    punctuation = ":!?.,;"

    for symbol in punctuation:
        message = message.replace(symbol, " ")

    words = message.lower().split()

    return words

def is_important(message):
    words = get_clean_words(message)

    if "важно" in words or "срочно" in words:
        return True
    else:
        return False

def get_category(message):
    words = get_clean_words(message)

    if "срочно" in words:
        return "Срочно"
    elif "важно" in words:
        return "Важное"
    elif "экскурсия" in words:
        return "Мероприятия"
    else:
        return "Обычное"

if __name__ == "__main__":

    messages = [
        "СРОЧНО:Сегодня математика в 9:00",
        "ВАЖНО: завтра родительское собрание",
        "В пятницу состоится экскурсия в музей",
        "СРОЧНО: завтра экскурсия, подтвердить участие",
        "Всем хороших выходных!",
        "Это НЕВАЖНОЕ сообщение"
    ]
    important_messages = []
    for message in messages:
        if is_important(message):
            important_messages.append(message)

    if len(important_messages) == 0:
        print("Сегодня важных сообщений нет")
    else:
        print("---ВАЖНЫЕ СООБЩЕНИЯ---")
        print(f"Найдено важных сообщений: {len(important_messages)}")

        for message in important_messages:
            print(message)

    print("=" *40)

    for message in messages:
        print(f"Сообщение: {message}")
        print(f"Категория: {get_category(message)}")
        print("---")

    category_counts = {
        "Срочно": 0,
        "Важное": 0,
        "Мероприятия": 0,
        "Обычное": 0
    }
    for message in messages:
        category = get_category(message)
        category_counts[category] = category_counts[category] + 1
    print("---СТАТИСТИКА СООБЩЕНИЙ---")
    for category in category_counts:
        print(f"{category}: {category_counts[category]}")

    total_counted = 0

    for category in category_counts:
        total_counted = total_counted + category_counts[category]

    print(f"Всего распределено сообщений: {total_counted}")

    if len(messages) == total_counted:
        print("Все сообщения обработаны")
    else:
        print("Ошибка: количество сообщений не совпадает")