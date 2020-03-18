import uuid
from src.core.todo.todo_model import TodoModel
from src.core.todo.todo_repository import TodoRepository
from typing import List

todo_list = []

todo_list.append(
    TodoModel(title="Apple",
              active=True,
              id="c5740aea-7476-432b-8ffc-a1c2be23dc31").dict())
todo_list.append(
    TodoModel(title="Bananas",
              active=True,
              id="ebe85a19-4e65-4976-9e56-713e9219610a").dict())


class TodoAdapter(TodoRepository):
    def insert(self, title: str) -> TodoModel:
        id = str(uuid.uuid4())

        new_task = TodoModel(
            title=title,
            active=True,
            id=id
        )

        todo_list.append(new_task.dict())
        return new_task

    def update(self, id: str, title: str, active: bool) -> TodoModel:
        print("Task Id: {}".format(id))
        todo_task: TodoModel = self.get(id=id)
        print(todo_task)
        if todo_task is None:
            print("Todo task is not exist")
            
        todo_task["title"] = title
        todo_task["active"] = active

        return todo_task

    def delete(self, id: str) -> bool:
        todo_task: TodoModel = self.get(id=id)
        
        if todo_task is not None:
            todo_list.remove(todo_task)
        
        return todo_task not in todo_list 

    def get(self, id: str) -> TodoModel:
        return next(filter(lambda item: item['id'] == id, todo_list), None)

    def get_all(self) -> []:
        return todo_list
    
    
