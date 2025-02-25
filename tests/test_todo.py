import pytest
from src import todo
from src import todolist


@pytest.fixture
def todo_list():
    return TodoList()

def test_add_todo(todo_list):
    todo = todo_list.add_todo("Test task", "2025-03-01")
    assert todo.id == 1
    assert todo.description == "Test task"
    assert todo.due_date == "2025-03-01"
    assert len(todo_list.todos) == 1

def test_delete_todo(todo_list):
    todo = todo_list.add_todo("Test task")
    todo_list.delete_todo(todo.id)
    assert len(todo_list.todos) == 0

def test_edit_todo_description(todo_list):
    todo = todo_list.add_todo("Initial description")
    updated_todo = todo_list.edit_todo(todo.id, description="Updated description")
    assert updated_todo.description == "Updated description"

def test_edit_todo_due_date(todo_list):
    todo = todo_list.add_todo("Task without due date")
    updated_todo = todo_list.edit_todo(todo.id, due_date="2025-03-10")
    assert updated_todo.due_date == "2025-03-10"

def test_edit_nonexistent_todo(todo_list):
    with pytest.raises(ValueError):
        todo_list.edit_todo(999, description="Does not exist")
