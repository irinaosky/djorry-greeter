def is_important(message):
    text = message.lower()

    if "важно" in text or "срочно" in text:
        return True
    else:
        return False
messages = [
    "Доброе утро!",
    "СРОЧНО:Сегодня математика",
    "ВАЖНО: завтра родительское собрание",
    "Спасибо всем!"
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

