import json
import os
import sys
BASE = 'data/'
baseDict = {
    'Empleados': {},
    'colillas de pago': {}
}
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

def Verifydata(archivo):
    if (CheckFile(archivo) == True):
        return ReadFile(archivo)
    else:
        UpdateFile(archivo,baseDict)
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