from flask import Flask
from flask_restplus import Api
from src.api.todo_resource import TodoResource, TodosResource
from src.api import app, api
from flask_injector import FlaskInjector
from injector import inject
from src.dependencies import configure

def create_app():
    api.init_app(app)
    api.add_resource(TodoResource)
    api.add_resource(TodosResource)
    FlaskInjector(app=app, modules=[configure])
    
    return app
