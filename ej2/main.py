# programa en Python que permita leer la información de un usuario Y la almacene en un diccionario.
import json
import os
import corefiles as c
if  __name__ == "__main__":
    users = {}
    print('---- INGRESE INFO DEL NUEVO USUARIO ----\n')
    print('Ingrese el id del usuario')
    id = c.ValidInt()
    print('Ingrese el nombre del usuario')
    name = c.Validstr()
    print('Ingrese los apellidos del usuario')
    lastName = c.Validstr()
    print('Ingrese la ciudad donde vive el usuario')
    ciudad = c.Validstr()
    print('Ingrese la dirección donde reside el usuario')
    direccion = c.Validstr()
    print('Ingrese longitud de la ubicación del usuario')
    longitud = c.ValidFloat()
    print('Ingrese altitud de la ubicación del usuario')
    latitud = c.ValidFloat()
    print('Ingrese el email del usuario')
    email = c.Validstr()
    print('Ingrese la edad del usuario')
    edad = c.ValidInt()
    print('Ingrese la ocupación del usuario')
    ocupacion = c.Validstr()
    nwDict = {
        'id': id,
        'nombre': name,
        'apellidos': lastName,
        'ubicacion':{
            'direccion': direccion,
            'ciudad': ciudad,
            'longitud': longitud,
            'latitud': latitud
        },
        'email': email,
        'edad': edad,
        'ocupacion': ocupacion
    }
    users.update({id:nwDict})
    printer = json.dumps(users[id],indent=4,)
    os.system('cls')
    print(printer)
    os.system('pause')