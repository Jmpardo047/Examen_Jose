def AddProduct(productos):
    print('---- AGREGAR PRODUCTO A LA TIENDA ----')
    print('Ingrese el id del producto')
    id = ValidInt()
    print('Ingrese el nombre del producto')
    name = Validstr()
    print('Ingrese los apellidos del usuario')
    lastName = Validstr()
    print('Ingrese la ciudad donde vive el usuario')
    ciudad = Validstr()
    print('Ingrese la dirección donde reside el usuario')
    direccion = Validstr()
    print('Ingrese longitud de la ubicación del usuario')
    longitud = ValidFloat()

def ValidInt():
    try:
        n = int(input(')..'))
    except ValueError:
        return ValidInt()
    else:
        return n
    
def ValidFloat():
    try:
        n = float(input(')..'))
    except ValueError:
        return ValidFloat()
    else:
        return n

def Validstr():
    n = input(')..')
    if(bool(n) == True):
        return n
    else:
        return Validstr()