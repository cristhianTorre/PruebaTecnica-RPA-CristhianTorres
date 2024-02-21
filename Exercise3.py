from sys import stdin
import sys

#Funcion principal
def main():
    """Recibe la entrada en forma de lista"""
    lista = sys.stdin.readline().strip().replace('[', '').replace(']', '').replace(',', '').split()
    print(matrizRepetidos(lista))

#Funcion para agregar los numeros repetidos
def matrizRepetidos(lista):
    matriz = []
    for i in range(0, len(lista)):
        validacion = inMatriz(lista[i], i, lista)
        if(validacion == -1):
            matriz.append([int(lista[i])])
        else:
            matriz[validacion].append(int(lista[i]))
    return matriz

#Funcion para validar si ya se encuentra el valor en la matriz y retorna el indice donde se encontro
def inMatriz(valor, indice, lista):
    for i in range(0, indice):
        if(i == indice):
            return -1
        elif(valor == lista[i]):
            return i
        else:
            pass
    return -1

main()
