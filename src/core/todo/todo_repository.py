from src.core.todo.todo_model import TodoModel
from abc import ABC, abstractmethod
from typing import List

class TodoRepository(ABC):
    @abstractmethod
    def insert(self, title: str) -> TodoModel:
        pass

    @abstractmethod
    def update(self, id: str, title: str, active: bool) -> TodoModel:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass

    @abstractmethod
    def get(self, id: str) -> TodoModel:
        pass

    @abstractmethod
    def get_all(self) -> []:
        pass
