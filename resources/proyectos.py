from models.assistant_app import AssistantAppModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sqlalchemy.orm import query
from models.user_app import UserAppModel
import requests

class ProyectosList(Resource):
    def get(self, rut):
        api_gestion = "http://3.139.99.125:8080/proyectos"
        req = requests.get(api_gestion)
        proyectos_alumno = list()
        for proyecto in req.json():
            if rut == proyecto[1]:
                proyectos_alumno.append(proyecto[2])
        user_app = UserAppModel.find_by_rut(rut)
        return {'user':user_app.json(),'proyectos': proyectos_alumno}