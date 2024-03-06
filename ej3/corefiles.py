import json
import os
import sys
BASE = 'data/'
def AddProduct(productos:dict):
    print('---- AGREGAR PRODUCTO A LA TIENDA ----')
    print('Ingrese el id del producto')
    id = ValidInt()
    print('Ingrese el nombre del producto')
    name = Validstr()
    print('Ingrese el valor unitario del prducto')
    valor = ValidFloat()
    print('Ingrese el sotck mínimo del producto')
    stockMin = ValidInt()
    print('Ingrese el stock máximo del producto')
    stockMax = ValidInt()
    nwProduct = {
        'id': id,
        'nombre': name,
        'valor unitario': valor,
        'stock minimo' : stockMin,
        'stock maximo': stockMax
    }
    productos.update({id:nwProduct})


def ValidInt():
    try:
        n = int(input(')..'))
    except ValueError:
        DelLine()
        return ValidInt()
    else:
        return n
    
def ValidFloat():
    try:
        n = float(input(')..'))
    except ValueError:
        DelLine()
        return ValidFloat()
    else:
        return n

def Validstr():
    n = input(')..')
    if(bool(n) == True):
        return n
    else:
        DelLine()
        return Validstr()

def DelLine():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

def Verifydata(archivo,data):
    if (CheckFile(archivo) == True):
        return ReadFile(archivo)
    else:
        UpdateFile(archivo,data)
        return ReadFile(archivo)    
    
def CheckFile(archivo):
    if ((os.path.isfile(BASE+archivo))):
        return True
    else:
        return False

def ReadFile(archivo):
    with open(BASE+archivo,'r') as rf:
        return json.load(rf)
    
def UpdateFile(archivo,data):
    with open(BASE+archivo,'w') as wf:
        json.dump(data,wf,indent=4)