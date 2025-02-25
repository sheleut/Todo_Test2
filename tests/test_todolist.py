# test_todolist.py

def test_add_todo(todo_list):
    todo = todo_list.add_todo("Testaufgabe", "2025-03-01")
    assert todo.id == 1
    assert todo.description == "Testaufgabe"
    assert todo.due_date == "2025-03-01"
    assert len(todo_list.todos) == 1

def test_delete_todo(todo_list):
    todo = todo_list.add_todo("Testaufgabe")
    todo_list.delete_todo(todo.id)
    assert len(todo_list.todos) == 0

def test_edit_todo_description(todo_list):
    todo = todo_list.add_todo("Initiale Beschreibung")
    updated_todo = todo_list.edit_todo(todo.id, description="Aktualisierte Beschreibung")
    assert updated_todo.description == "Aktualisierte Beschreibung"

def test_edit_todo_due_date(todo_list):
    todo = todo_list.add_todo("Aufgabe ohne Fälligkeitsdatum")
    updated_todo = todo_list.edit_todo(todo.id, due_date="2025-03-10")
    assert updated_todo.due_date == "2025-03-10"

def test_edit_nonexistent_todo(todo_list):
    with pytest.raises(ValueError):
        todo_list.edit_todo(999, description="Existiert nicht")
