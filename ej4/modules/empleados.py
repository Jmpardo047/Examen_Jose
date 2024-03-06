import modules.corefiles as c
import json
def AddEmpleado(empleados:dict):
    print('---- AGREGAR INFORMMACIÓN DE EMPLEADO ----')
    print('Ingrese el id del empleado')
    id = str(c.ValidInt())
    print('Ingrese el nombre del empleado')
    name = c.Validstr()
    cargo = MenuCargos()
    print('Ingrese el sotck mínimo del producto')
    nwEmp = {
        'id': id,
        'nombre': name,
        'cargo': cargo,
        'salario':{}
    }
    empleados.update({id:nwEmp})

def MenuCargos():
    c.os.system('cls')
    print('Ingrese el cargo del empleado')
    print('1. Almacenista\n2. Jefe IT\n3. Administrador\n4. Mensajero\n5. Gerente')
    n = c.Validstr()
    if (n == '1'):
        rol = 'Almacenista'
        return rol
    elif (n == '2'):
        rol = 'Jefe IT'
        return rol
    elif (n == '3'):
        rol = 'Administrador'
        return rol
    elif (n == '4'):
        rol = 'Mensajero'
        return rol
    elif (n == '5'):
        rol = 'Gerente'
        return rol
    else:
        return MenuCargos()

def RegSalario(empleados:dict,colillas:dict):
    print('ingrese el id del empleado a quien se le calculará el salario')
    id = ValidEmp(empleados)
    if (bool(id) == True):
        route = empleados.get(id)
        print('Ingrese el valor por dia')
        valueDia = c.ValidFloat()
        print('Ingrese la cantidad de días trabajados')
        diasTotal = c.ValidInt()
        print('Ingrese la cantidad de horas extra trabajadas')
        horasExtra = c.ValidInt()
        print('Ingrese el descuento por cafetería')
        desCafe = c.ValidFloat()
        print('Ingrese la cuota de prestamo')
        prestamo = c.ValidFloat()
        print('Ingrese el mes en que se realizará el pago')
        mes = c.Validstr()
        print('Ingrese la fecha en que se realizará el pago')
        date = c.Validstr()
        totalExtra = horasExtra*5500
        sueldoBase = valueDia*diasTotal
        totalPagar = (((sueldoBase)+totalExtra)-(desCafe+prestamo))
        route['salario'] = totalPagar
        nwPago = {
            'mes':mes,
            'fecha':date,
            'sueldo base':sueldoBase,
            'pago horas extra': totalExtra,
            'cuota prestamo': prestamo,
            'descuento cafeteria': desCafe,
            'total': totalPagar
        }
        colillas.update({id:nwPago})
    else:
        pass

def ValidEmp(empleados:dict):
    id = str(c.ValidInt())
    if (id in empleados.keys()):
        return id
    else:
        print('El id de empleado ingresado no se encuentra registrado')
        c.os.system('pause')

def Consultar(empleados:dict,colillas:dict):
    c.os.system('cls')
    print('1.Consultar total pagado a un empleado\n2. Consultar colillas de pago')
    op = c.Validstr()
    if (op == '1'):
        print('ingrese el id del empleado al cual le quiere consultar el total pagado')
        id = ValidEmp(empleados)
        if (bool(id) == True):
            salario = colillas[id]['total']
            print(f'El total pagado a este empleado fue {salario}')
            c.os.system('pause')
        else:
            pass
    elif (op == '2'):
        print('ingrese el id del empleado al cual le quiere consultar su colilla de pago')
        id = ValidEmp(empleados)
        if (bool(id) == True):
            colilla = colillas.get(id)
            printer = json.dumps(colilla,indent=4)
            print(printer)
            c.os.system('pause')
        else:
            pass
    else:
        pass