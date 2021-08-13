from db import db
from flask import Flask
from flask.json import jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user_app import Campus, CampusCareer, Career, UserApp, UserList
from resources.assistant_app import AssistantApp, AssistantsList, ManagerAssistant, ManagerRange, RangeAssistant
from resources.proyectos import ProyectosList
from resources.user import UserRegister


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Alexis'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth


# Rutas Estudiantes
api.add_resource(UserApp, '/student/<string:name>')
#api.add_resource(UserApp, '/student/<string:name>')
#api.add_resource(UserApp, '/student/rut/<int:rut>')
api.add_resource(ProyectosList, '/student/rut/<int:rut>/proyectos')
api.add_resource(Campus, '/student/campus/<string:campus>')
api.add_resource(Career, '/student/career/<int:career>')
api.add_resource(UserList, '/student/all')
api.add_resource(CampusCareer, '/student/campus/<string:campus>/career/<int:career>')



# Rutas Ayudantes
api.add_resource(AssistantApp, '/assistant/rut/<int:rut>')
api.add_resource(ManagerAssistant, '/assistant/manager/<int:manager>')
api.add_resource(RangeAssistant, '/assistant/range/<string:range>')
api.add_resource(ManagerRange, '/assistant/manager/<int:manager>/range/<string:range>')
api.add_resource(AssistantsList, '/assistant/all')
db.init_app(app)
if __name__ == '__main__':
    
    app.run(port=5000,debug=True)