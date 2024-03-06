import os
def ValidateFloat(): #validar dato tipo flotante
    try:
        n = float(input(')..'))
    except ValueError:
        return ValidateFloat()
    else:
        return n
    
def PesosDolares(): #covertir pesos a dolares
    os.system('cls')
    print('Ingrese el valor de pesos que quiere convertir a dolares')
    x = ValidateFloat()
    cantidadConv = (x/3944)
    print(f'{x} pesos equivalen a {cantidadConv} dolares')
    os.system('pause')

def PesosEuros():   #covertir pesos a euros
    os.system('cls')
    print('Ingrese el valor de pesos que quiere convertir a euros')
    x = ValidateFloat()
    cantidadConv = (x/4279)
    print(f'{x} pesos equivalen a {cantidadConv} euros')
    os.system('pause')

def PesosYenes():   #covertir pesos a yenes
    os.system('cls')
    print('Ingrese el valor de pesos que quiere convertir a yenes')
    x = ValidateFloat()
    cantidadConv = (x/26.30)
    print(f'{x} pesos equivalen a {cantidadConv} yenes')
    os.system('pause')

def EurosPesos():   #covertir euros a pesos
    os.system('cls')
    print('Ingrese el valor de euros que quiere convertir a pesos')
    x = ValidateFloat()
    cantidadConv = (x*4279)
    print(f'{x} euros equivalen a {cantidadConv} pesos')
    os.system('pause')
