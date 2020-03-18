from injector import singleton
from src.data.todo_adapter import  TodoAdapter
from src.core.service.todo_service import TodoService
from src.core.todo.todo_repository import TodoRepository


def configure(binder):
    binder.bind(TodoRepository, to=TodoAdapter, scope=singleton)
    binder.bind(TodoService, to=TodoService, scope=singleton)
