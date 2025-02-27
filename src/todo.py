#src/todo.py

class Todo:
    def __init__(self, id, description, due_date=None):
        self.id = id
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return f"Todo(id={self.id}, description='{self.description}', due_date='{self.due_date}')"


