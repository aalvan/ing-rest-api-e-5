from flask_restful import Resource
import requests

api_gestion = "http://3.139.99.125:8080/proyectos"
req = requests.get(api_gestion)

for proyecto in req.json():
    print(proyecto[1])