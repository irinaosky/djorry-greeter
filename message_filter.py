def is_important(message):
    text = message.lower()

    if "важно" in text or "срочно" in text:
        return True
    else:
        return False
def get_category(message):
    text = message.lower()

    if "срочно" in text:
        return "Срочно"
    elif "важно" in text:
        return "Важное"
    elif "экскурсия" in text:
        return "Мероприятия"
    else:
        return "Обычное"
messages = [
    "СРОЧНО:Сегодня математика в 9:00",
    "ВАЖНО: завтра родительское собрание",
    "В пятницу состоится экскурсия в музей",
    "СРОЧНО: завтра экскурсия, подтвердить участие",
    "Всем хороших выходных!"
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
