
import json
from src.api import api
from injector import inject
from collections import OrderedDict
from flask import Flask, request, jsonify
from flask_restplus import Resource, fields
from src.data.todo_adapter import TodoAdapter
from src.core.todo.todo_model import TodoModel
from src.core.service.todo_service import TodoService


@inject
@api.route('/todo/<string:id>', endpoint='todo-resource')
class TodoResource(Resource):

    def __init__(self, service: TodoService, api=None, *args, **kwargs, ):
        self.service = service
        super().__init__(api=api, *args, **kwargs)

    def get(self, id):
        return self.service.get_task(id), 200

    def put(self, id):
        title = request.form['title']
        active = request.form['active']

        updated_task = self.service.update_task(
            todo_model=TodoModel(id=id, title=title, active=active))

        return updated_task, 200

    def delete(self, id):
        todo_task = self.service.get_task(id)

        if todo_task is None:
            return {"result": False, "message": "The is not exist"}

        return {"result": self.service.delete_task(todo_task)}, 200


@inject
@api.route('/todos', endpoint='todos-resource')
class TodosResource(Resource):

    def __init__(self, service: TodoService, api=None, *args, **kwargs, ):
        self.service = service
        super().__init__(api=api, *args, **kwargs)

    def get(self):
        all_items = self.service.get_all_tasks()
        print(all_items)
        return list(all_items), 200

    def post(self):
        title = request.form['title']
        new_task = self.service.add_task(title=title)
        return new_task.dict(), 201
