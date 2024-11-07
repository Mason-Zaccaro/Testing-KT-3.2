import pytest
import sqlite3

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    conn.commit()

    yield conn, cursor

    cursor.execute('DELETE FROM test_table')
    conn.commit()

    conn.close()


def test_insert_and_retrieve_data(db_connection):
    conn, cursor = db_connection

    cursor.execute("INSERT INTO test_table (name) VALUES ('Гоша')")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Антон')")
    conn.commit()

    cursor.execute("SELECT name FROM test_table")
    names = cursor.fetchall()
    assert names == [('Гоша',), ('Антон',)]


def test_insert_and_retrieve_another_data(db_connection):
    conn, cursor = db_connection

    # Вставляем другие данные в таблицу
    cursor.execute("INSERT INTO test_table (name) VALUES ('Коля')")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Азиз')")
    conn.commit()

    cursor.execute("SELECT name FROM test_table")
    names = cursor.fetchall()
    assert names == [('Коля',), ('Азиз',)]