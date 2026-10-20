import pytest

from message_filter import get_clean_words, is_important, get_category

def test_clean_words():
    assert get_clean_words("СРОЧНО:Завтра!") == ["срочно", "завтра"]


def test_urgent_message():
    assert is_important("СРОЧНО: завтра собрание") == True


def test_not_important():
    assert is_important("Это НЕВАЖНОЕ сообщение") == False

def test_important_extended():
    assert is_important("ВАЖНОЕ: завтра принести деньги") == True

@pytest.mark.parametrize("message, expected", [
    ("СРОЧНО: завтра собрание", "Срочно"),
    ("ВАЖНО: завтра собрание", "Важное"),
    ("ВАЖНОЕ: завтра принести деньги", "Важное"),
    ("Завтра экскурсия", "Мероприятия"),
    ("Всем хороших выходных!", "Обычное"),
], ids=["urgent", "important", "important_extended", "event", "normal"])

def test_categories(message, expected):
    assert get_category(message) == expected

@pytest.mark.parametrize("message, expected", [
    ("", []),
    (" ", []),
], ids=["empty", "space"])
def test_empty_message(message, expected):
    assert get_clean_words(message) == expected

@pytest.mark.parametrize("message", [
    "",
    " ",
    "   ",
])
def test_empty_category(message):
    assert get_category(message) == "Пустое"