#programa que permite registrar la información de los empleadosDe una compañía 
#y le permita calcular el valor a pagar por concepto de nomina a Cada empleado.
import os
import sys
from tabulate import tabulate
import modules.corefiles as c
if __name__ == '__main__':
    def MainMenu():
        def Excecute(func):
            os.system('cls')
            func
            MainMenu()
        info = c.Verifydata('compañia.json')
        empleados,colillas = info.values()
        menu =[['1.', 'Registrar info de empleado'], ['2.', 'Calcular valor a pagar a empleado'], ['3.', 'Salir']]
        print(tabulate(menu, tablefmt='grid'))
        op = input('\n)..'  )
        if (op == '1'):
            pass
        elif (op == '2'):
            pass
        elif (op == '3'):
            sys.exit('Hasta Pronto!')
        else:
            MainMenu()
    MainMenu()