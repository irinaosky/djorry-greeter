import pytest

from message_filter import get_clean_words, is_important, get_category

def test_clean_words():
    assert get_clean_words("СРОЧНО:Завтра!") == ["срочно", "завтра"]


def test_urgent_message():
    assert is_important("СРОЧНО: завтра собрание") == True


def test_not_important():
    assert is_important("Это НЕВАЖНОЕ сообщение") == False

@pytest.mark.parametrize("message, expected", [
    ("СРОЧНО: завтра собрание", "Срочно"),
    ("ВАЖНО: завтра собрание", "Важное"),
    ("Завтра экскурсия", "Мероприятия"),
    ("Всем хороших выходных!", "Обычное"),
], ids=["urgent", "important", "event", "normal"])

def test_categories(message, expected):
    assert get_category(message) == expected