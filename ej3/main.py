# programa en Python que permita registrar los productos de una Tienda de viveres.
import corefiles as c
if  __name__ == "__main__":
    nwDc = {}
    productos = c.Verifydata('inventario.json',nwDc)
    rp = True
    while rp:
        c.os.system('cls')
        c.AddProduct(productos)
        rp = bool(input('desea agregar otro producto?, S(Si) o Enter(No)'))
    c.UpdateFile('inventario.json',productos)
    


