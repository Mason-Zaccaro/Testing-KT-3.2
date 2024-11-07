def save_string_to_file(s: str, file_path: str) -> None:
    with open(file_path, 'w') as file:
        file.write(s)

import pytest
import os

@pytest.fixture
def temp_file(tmpdir):
    file_path = tmpdir.join("test_file.txt")
    return str(file_path)


@pytest.fixture
def sample_string():
    return "Hello, World!"

# Тесты
def test_save_string_to_file(temp_file, sample_string):
    save_string_to_file(sample_string, temp_file)

    assert os.path.exists(temp_file)

    with open(temp_file, 'r') as file:
        content = file.read()
        assert content == sample_string

def test_save_empty_string_to_file(temp_file):
    save_string_to_file("", temp_file)

    assert os.path.exists(temp_file)

    with open(temp_file, 'r') as file:
        content = file.read()
        assert content == ""

def test_save_multi_line_string_to_file(temp_file):
    multi_line_string = """
    This is a
    multi-line
    string.
    """

    save_string_to_file(multi_line_string, temp_file)

    assert os.path.exists(temp_file)

    with open(temp_file, 'r') as file:
        content = file.read()
        assert content == multi_line_string