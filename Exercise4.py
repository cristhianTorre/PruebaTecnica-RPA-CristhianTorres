from sys import stdin
import sys

#Variables globales
dairy_products = []
dairy_stock = []

cleaning_products = []
cleaning_stock = []

grain_products = []
grain_stock = []

#Funcion con menu ajustado
def menu():
    print("Sistema de inventario. Ingrese una opcion:")
    print("------------------------------------------")
    print("1. Agregar producto")
    print("2. Ver reporte de inventario")
    print("3. Salir")
    option = input("Su opcion: ")
    if(option == "1"):
        addProduct()
    elif(option == "2"):
        viewInventory()
    elif(option == "3"):
        return 0
    else:
        print("Digite un comando valido")
        menu()

#Funcion para agregar producto con opciones disponibles
def addProduct():
    print("Grupos disponibles:")
    print("1. dairy")
    print("2. cleaning")
    print("3. grain")
    group = input("Digite el numero del grupo: ")
    if not (group == "1" or group == "2" or group == "3"):
        print("Opcion no valida, por favor revise las opciones disponibles")
        addProduct()
    name = input("Escriba el nombre del producto a registrar: ")
    stock = input("Cantidad del producto: ")
    if (verifyExist(name, group, stock)):
        print("¡Producto ya existente, existencias actualizadas!")
    else:
        print("¡Producto creado!")
    menu()

#Valida y agrega a las listas globales los valores deseados
def verifyExist(name, group, stock):
    global dairy_products
    global dairy_stock
    global cleaning_products
    global cleaning_stock
    global grain_products
    global grain_stock
    if(group == "1"):
        if(name in dairy_products):
            index = dairy_products.index(name)
            dairy_stock[index] += int(stock)
            return True
        else:
            dairy_products.append(name)
            dairy_stock.append(int(stock))
            return False
    elif(group == "2"):
        if(name in cleaning_products):
            index = cleaning_products.index(name)
            cleaning_stock[index] += int(stock)
            return True
        else:
            cleaning_products.append(name)
            cleaning_stock.append(int(stock))
            return False
    else:
        if(name in grain_products):
            index = grain_products.index(name)
            grain_stock[index] += int(stock)
            return True
        else:
            grain_products.append(name)
            grain_stock.append(int(stock))
            return False

#Crea una matriz con las variables globales y les da formato de tabla
def viewInventory():
    tabla = []
    """Valida si existen productos para agregarlos a la matriz"""
    if(len(dairy_products) != 0):
        for i in range(0, len(dairy_products)):
            tabla.append([dairy_products[i], "dairy", dairy_stock[i]])
    if(len(cleaning_products) != 0):
        for i in range(0, len(cleaning_products)):
            tabla.append([cleaning_products[i], "cleaning", cleaning_stock[i]])
    if(len(grain_products) != 0):
        for i in range(0, len(grain_products)):
            tabla.append([grain_products[i], "grain", grain_stock[i]])
    """Formato de tabla con encabezados"""
    print("{:<15} {:<15} {:<10}".format("Nombre", "Grupo", "Existencias"))
    print("------------------------------------------")
    for v in tabla:
        nombre, grupo, existencias = v
        print("{:<15} {:<15} {:<10}".format(nombre, grupo, existencias))
    print("------------------------------------------")
    menu()

menu()
