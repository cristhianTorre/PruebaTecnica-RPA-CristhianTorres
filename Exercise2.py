from sys import stdin
import sys

#Funcion principal
def main():
    """Entrada de datos en forma de lista"""
    lista = sys.stdin.readline().strip().replace('[', '').replace(']', '').replace(',', '').split()
    print(verifyList(lista))

#Funcion con las validaciones correspondientes
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

main()
