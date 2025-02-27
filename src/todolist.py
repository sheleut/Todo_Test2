#src/todolist.py

class TodoList:
    def __init__(self):
        self.todos = []
        self.counter = 0

    def add_todo(self, description, due_date=None):
        self.counter += 1
        todo = Todo(self.counter, description, due_date)
        self.todos.append(todo)
        return todo

    def delete_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo.id != todo_id]

    def edit_todo(self, todo_id, description=None, due_date=None):
        for todo in self.todos:
            if todo.id == todo_id:
                if description is not None:
                    todo.description = description
                if due_date is not None:
                    todo.due_date = due_date
                return todo
        raise ValueError("Todo not found")

    def get_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
