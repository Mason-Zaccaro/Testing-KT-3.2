def get_string_length(s: str) -> int:
    return len(s)

import pytest

@pytest.fixture
def empty_string():
    return ""

@pytest.fixture
def single_line_string():
    return "Hello, World!"

@pytest.fixture
def multi_line_string():
    return """
    Это
    многострочная
    строка.
    """

@pytest.fixture
def space_string():
    return "   "

# Тесты
def test_empty_string(empty_string):
    assert get_string_length(empty_string) == 0

def test_single_line_string(single_line_string):
    assert get_string_length(single_line_string) == 13

def test_multi_line_string(multi_line_string):
    assert get_string_length(multi_line_string) == 43

def test_space_string(space_string):
    assert get_string_length(space_string) == 3