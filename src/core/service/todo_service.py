from typing import List
from injector import inject
from src.core.todo.todo_model import TodoModel
from src.core.todo.todo_repository import TodoRepository

class TodoService:
    @inject
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def get_task(self, id: str):
        return self.todo_repository.get(id)

    def get_all_tasks(self) -> []:
        return self.todo_repository.get_all()

    def add_task(self, title: str) -> TodoModel:
        
        return self.todo_repository.insert(
            title=title
        )

    def update_task(self, todo_model: TodoModel):
        return self.todo_repository.update(
            id=todo_model.id,
            title=todo_model.title,
            active=todo_model.active)

    def delete_task(self, todo_model: TodoModel):

        return self.todo_repository.delete(id=todo_model["id"])
