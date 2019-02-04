# La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
def max_in_list(l1: list):
    # return max(l1)
    if len(l1) > 0:
        num = l1[0]
        for x in l1:
            if x > num:
                num = x
        print('El número mayor es:', num)
    else:
        print('No hay número que comparar')
# max_in_list([3, 5, 0, -1, 8, -10])

# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
def funcion_mas_larga(l1: list):
    if len(l1) > 0:
        word = l1[0]
        num = len(l1[0])
        for x in l1:
            if len(x) > num:
                word = x
                num = len(x)
        print('Most large word is:', word)
    else:
        print('No hay palabras que comparar')
# funcion_mas_larga(['el', 'enano', 'del', 'lago'])

# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
def filtrar_palabras(n: int, l1: list):
    palabras = []
    for x in l1:
        if len(x) > n:
            palabras.append(x)
    return palabras
# print(filtrar_palabras(4, ['los', 'dragones', 'marinos', 'de', 'Wano']))

# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
def mayus_cant():
    texto = input('Ingrese un texto: ')

# Construir un pequeño programa que convierta números binarios en enteros.

# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

# Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a. También se puede hacer elegir al usuario la letra a buscar.(Un poco mas emocionante)

# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales. Se puede hacer que el usuario sea quien elija la palabra.

# Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
