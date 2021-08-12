from models.assistant_app import AssistantAppModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sqlalchemy.orm import query
from models.user_app import UserAppModel
class UserApp(Resource):
    parser = reqparse.RequestParser()
    ''''
    parser.add_argument('permission',
            type=str,
            required = True,
            help = " This field cannot be left blank "
        )'''
    #@jwt_required()
    def get(self, name):
        user_app = UserAppModel.find_by_name(name)
        if user_app:
            print (user_app.json())
            return user_app.json()
        return {'message':'User_app not found'},404
    def get(self, rut):
        user_app = UserAppModel.find_by_rut(rut) 
        if user_app:
            return user_app.json()
        return {'message':'User_app not found'},404

    def post(self, name):
        if UserAppModel.find_by_name(name):
            return {'message':"An user with name '{}' already exists.".format(name)},400
        request_data = UserApp.parser.parse_args() 
        user_app = UserAppModel(name,request_data['permission'])
        try:
            user_app.save_to_db()
        except:
            return {'message':'An error ocurred inserting the user'}, 500
        return user_app.json(),201 ###### I AM NOT SURE
    
    def delete(slef, name):
        user = UserAppModel.find_by_name(name)
        if user:
            user.delete_from_db()
        return {'message':'Item deleted'}
        
    def put(self,name):
        request_data = UserApp.parser.parse_args()

        user = UserAppModel.find_by_name(name)

        if user is None:
            user = UserAppModel(name, request_data['permission'])
        else:
            user.permission = request_data['permission']
        user.save_to_db()
        return user.json()
    

class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserAppModel.query.all()]} # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))} with lambda expressions
class Campus(Resource):
    def get(self, campus):
        return {'users': [user.json() for user in UserAppModel.find_by_campus(campus)]}
class Career(Resource):
    def get(self, career):
        return {'users': [user.json() for user in UserAppModel.find_by_career(career)]}
class CampusCareer(Resource):
    def get(self, campus, career):
        return {'users': [user.json() for user in UserAppModel.find_by_career_campus(career, campus)]}
class Assistant(Resource):
    def get(self, rut):
        assistant_app = AssistantAppModel.find_by_rut(rut) 
        if assistant_app:
            return assistant_app.json()
        return {'message':'User_app not found'},404
    






