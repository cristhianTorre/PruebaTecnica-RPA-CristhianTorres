# Prueba técnica
Repositorio público con prueba técnica del ing. Cristhian Camilo Torres para Globaltek Development S.A
## Lenguaje de programación: Python
### Ejecución de los diferentes archivos:
`py Exercise1.py`
`py Exercise2.py`
`py Exercise3.py`
`py Exercise4.py`
### Ejercicio 1
Formato de entrada: numero espacio numero ejemplo; 6 5

Se multiplica el caracter requerido y se suma a una variable por cada vez que avanza el ciclo

    def sum_rec(numero, terminos):
    suma = 0
    """Suma de la serie X numero repetido hasta el n-esimo termino"""
    for i in range (1,int(terminos)+1):
        """(x + xx + xxx + ...)"""
        suma += int(numero*i)
    return suma

### Ejercicio 2
Formato de entrada: [numero, numero, numero]

Se hace las respectivas validaciones por cada numero que se encuentra en la lista y devuelve un nuevo arreglo con los valores encontrados. 

    def verifyList(lista):
    result = []
    """Recorre la lista y valida cada valor de acuerdo a las especificaciones dadas"""
    for i in range (0, len(lista)):
        """Retorna la lista si es mayor a 1000"""
        if (int(lista[i]) > 1000):
            return result
        """Verifica que sea menor o igual a 600 y divisible por 5 para agregarlo a la lista"""
        elif (int(lista[i]) <= 600 and int(lista[i]) % 5 == 0):
            result.append(int(lista[i]))
        """Debe omitir otros valores"""
        else:
            pass
    return result

### Ejercicio 3
Formato de entrada: [numero, numero, numero]

Se recorre la lista y se valida si cada numero esta en una nueva lista para ser agregado en forma de lista o ser agregado a la lista de lista ya existente

    def matrizRepetidos(lista):
    matriz = []
    for i in range(0, len(lista)):
        validacion = inMatriz(lista[i], i, lista)
        if(validacion == -1):
            matriz.append([int(lista[i])])
        else:
            matriz[validacion].append(int(lista[i]))
    return matriz

### Ejercicio 4
Formato de entrada: numero

Los diferentes menus reciben un unico parametro para opciones, cuando se solicitan nombres se pueden usar los diferentes caracteres

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
