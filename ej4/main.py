#programa que permite registrar la información de los empleadosDe una compañía 
#y le permita calcular el valor a pagar por concepto de nomina a Cada empleado.
from tabulate import tabulate
import modules.corefiles as c
import modules.empleados as emp
if __name__ == '__main__':
    info = c.Verifydata('compañia.json')
    empleados,colillas = info.values()
    def MainMenu():
        def Excecute(func):
            func
            MainMenu()
        menu =[['1.', 'Registrar info de empleado'], ['2.', 'Calcular valor a pagar a empleado'], ['3.', 'Salir']]
        c.os.system('cls')
        print(tabulate(menu, tablefmt='grid'))
        op = input('\n)..'  )
        if (op == '1'):
            c.os.system('cls')
            Excecute(emp.AddEmpleado(empleados))
        elif (op == '2'):
            c.os.system('cls')
            Excecute(emp.RegSalario(empleados,colillas))
        elif (op == '3'):
            finalUpdate = {
                'empleados':empleados,
                'colillas':colillas
            }
            c.UpdateFile('compañia.json',finalUpdate)
            c.sys.exit('Hasta Pronto!')
        else:
            MainMenu()
    MainMenu()