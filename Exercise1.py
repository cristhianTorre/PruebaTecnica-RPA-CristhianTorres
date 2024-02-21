from sys import stdin
import sys

#Funcion principal
def main():
    entrada = sys.stdin.readline().split()
    print(sum_rec(entrada[0], entrada[1]))

#Funcion con la operacion numerica
def sum_rec(numero, terminos):
    suma = 0
    """Suma de la serie X numero repetido hasta el n-esimo termino"""
    for i in range (1,int(terminos)+1):
        """(x + xx + xxx + ...)"""
        suma += int(numero*i)
    return suma


main()
    
