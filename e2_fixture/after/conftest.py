import pytest
from todo import Tasks

@pytest.fixture
def todos():
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
    return todos
