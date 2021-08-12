from models.assistant_app import AssistantAppModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sqlalchemy.orm import query
from models.assistant_app import AssistantAppModel

class AssistantApp(Resource):
    def get(self, rut):
        assistant_app = AssistantAppModel.find_by_rut(rut) 
        if assistant_app:
            print(assistant_app.json())
            return assistant_app.json()
        return {'message':'User_app not found'},404
class ManagerAssistant(Resource):
    def get(self, manager):
        return {'users': [user.json() for user in AssistantAppModel.find_by_manager(manager)]}
class RangeAssistant(Resource):
    def get(self, range):
        return {'users': [user.json() for user in AssistantAppModel.find_by_range(range)]}
class ManagerRange(Resource):
    def get(self, manager, range):
        return {'users': [user.json() for user in AssistantAppModel.find_by_manager_range(manager, range)]}
class AssistantsList(Resource):
    def get(self):
        return {'users': [user.json() for user in AssistantAppModel.query.all()]}