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
