#programa en Python que permita convertir pesos a dólares, pesos a euros, euros a pesos y pesos a yenes.
from tabulate import tabulate
import corefiles as c
import sys
if  __name__ == "__main__":
    op = [[1,'pesos a dólares'],[2,'pesos a euros'],[3,'pesos a euros'],[4,'pesos a yenes'],[5,'salir']]
    def MainMenu():
        print(tabulate(op,headers=['número','opción'],tablefmt='grid'))
        n = input(')..')
        if (n == '1'):
            c.PesosDolares()
            MainMenu()
        elif (n == '2'):
            c.PesosEuros()
            MainMenu()
        elif (n == '3'):
            c.EurosPesos()
            MainMenu()
        elif (n == '4'):
            c.PesosYenes()
            MainMenu()
        elif (n == '5'):
            print('hasta pronto!')
            sys.exit
        else:
            MainMenu()
    MainMenu()
    