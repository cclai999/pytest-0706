# noinspection DuplicatedCode
import pytest
from todo import Tasks


def test_initial_empty_todos():
    todos = Tasks()
    assert len(todos) == 0


def test_initial_todos():
    items = [
        {
            'id': 1,
            'title': '交電話費',
            'note': '500元',
            'done': False
        },
        {
            'id': 2,
            'title': '錄教學影片',
            'note': 'rest api for todo app',
            'done': False
        }
    ]
    todos = Tasks(items)
    assert len(todos) == 2
    assert todos.get_task(1)['id'] == 1
