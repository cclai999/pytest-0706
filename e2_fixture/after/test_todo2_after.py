import pytest

from todo import Tasks


# noinspection DuplicatedCode
def test_initial_empty_todos():
    todos = Tasks()
    assert len(todos) == 0


def test_initial_filled_todos(todos):
    assert len(todos) == 2
    assert todos.get_task(1)['id'] == 1


def test_add_todo(todos):
    new_item = {
            'title': '買牛奶',
            'note': '2瓶'
        }
    new_id = todos.create_task(new_item)
    assert todos.get_task(new_id)['title'] == '買牛奶'
    assert todos.get_task(new_id)['note'] == '2瓶'
    assert todos.get_task(new_id)['done'] is False
