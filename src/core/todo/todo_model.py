import uuid
from pydantic import BaseModel

class TodoModel(BaseModel):
    id: str = None
    title: str = None
    active: bool = False

    def change_title(self, title: str):
        self.title = title

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

