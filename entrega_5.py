#                   Secuencia de prueba                        #
#                                                              #
#   Escoja la opción          |             1              |   #
#   Ingrese el nombre         |           Juan             |   #
#   Ingrese el permiso        |          creador           |   #
#                                                              #
#   Escoja la opción          |             2              |   #
#   Ingrese el nombre         |           Juan             |   #
#                                                              #
#   Escoja la opción          |             3              |   #
#   Ingrese el nombre         |           Juan             |   #
#   Ingrese el permiso nuevo  |        instructor          |   #
#                                                              # 
#   Escoja la opción          |             2              |   #
#   Ingrese el nombre         |           Juan             |   #
#                                                              #
#   Escoja la opción          |             5              |   #
#                                                              #
#   Escoja la opción          |             4              |   #
#   Ingrese el nombre         |           Juan             |   #
#                                                              #
#   Escoja la opción          |             5              |   #
#                                                              #

import requests

url = 'https://ing-rest-api-e-5.herokuapp.com'
permisos = ["creador", "instructor", "externo"]

while True:
    # Menú
    print("\nMenú")
    print("1.Obtener Proyectos de un estudiante ")
    print("2.Agregar una nueva persona y un proyecto")
    print("3.Comprobar si una persona está habilitada para reservar una máquina para su proyecto")
    print("5.Eliminar las reservas asociadas a una máquina cuando se elimina la máquina ")
    print("6.Obtener el tipo de máquina de una reserva")
    #
    option = int(input("\nElija una opción: "))
    #
    # rut en la base de datos: 193849581
    if (option == 1):
        rut = input("\nIngrese el rut: ")
        req = requests.get(url + '/student/rut/' + rut + '/proyectos')
        print(url + '/student/rut/' + rut + '/proyectos')
        user = req.json()['user']
        nombre = user['name']
        print(nombre)
        proyectos = req.json()['proyectos']
        
        print("El nombre es:", nombre)
        print("Los proyectos son:")
        for proyecto in proyectos:
            print(proyecto)
    elif (option == 2):
        pass
    elif (option == 3):
        pass
    elif (option == 4):
        pass
    elif (option == 5):
        pass
    elif (option == 6):
        break
    else:
        print("\nIngrese una opción válida")