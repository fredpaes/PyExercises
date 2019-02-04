# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio).
def maximum(number1:int, number2:int):
    '''if number1 > number2:
        print(number1)
    else:
        print(number2)'''
    rpta = number1 if number1 > number2 else number2
    print('El número mayor es', rpta)
# maximum(10, 84)

# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(n1:int, n2:int, n3:int):
    if n1 > n2 and n1 > n3:
        rpta = n1
    elif n2 > n3 and n2 > n3:
        rpta = n2
    else:
        rpta = n3
    print('El número mayor es', rpta)
# max_de_tres(4, 8, 6)

# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
def longitud(char):
    rpta = 0
    # print(type(char))
    # print(isinstance(char, str))
    if isinstance(char, list) or isinstance(char, str):
        for x in char:
            rpta += 1
        return rpta
    else:
        return rpta
# print(longitud(['hola', 5, True]))

# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def vocal(char:str):
    vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    value = False
    if char in vocales:
        value = True
    return value
# print(vocal('j'))

# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def ops(data:list):
    suma = 0
    multi = 1
    # if isinstance(data, list):
    for x in data:
        suma += x
        multi *= x
    # else:
    #     return 'No data permitida'
    return print('la suma es', suma, 'y la multiplicación es', multi)
# ops((5, 2, 4))

# Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(char:str):
    x = -1
    neo = ''
    while x >= -len(char):
        neo += char[x]
        x -= 1
    return neo
# print(inversa('estoy probando'))

# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def es_palindromo(char:str):
    palind = inversa(char)
    if char == palind:
        return True
    else:
        return False
# print(es_palindromo('reconocer'))

# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(l1: list, l2: list):
    valor = False
    for i in l1:
        if i in l2:
            valor = True
    return valor

print(superposicion([4, 2, 6], [1, 2]))

# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
def generar_n_caracteres(n:int, char:str):
    return char * n
# print(generar_n_caracteres(3, 'hola'))

# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
def procedimiento(data:list):
    char = '*'
    histograma = ''
    for x in data:
        histograma += char * x + '\n'
    return histograma
# print(procedimiento([4,9,7]))

# SOLUCIONES
# http://www.pythondiario.com/2013/05/ejercicios-resueltos-en-python-parte-1.html
# ENUNCIADOS
# http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html