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

