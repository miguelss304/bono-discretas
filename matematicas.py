# ============================================================
# PROBLEMA 1: Calculadora general de permutaciones P(n, r)
# ============================================================
# Una permutacion P(n, r) cuenta el numero de formas de ordenar
# r objetos distintos tomados de un conjunto de n objetos distintos.
#
# En las permutaciones el orden SI importa:
# (A, B) y (B, A) representan arreglos diferentes.
#
# Formula:
#
#           P(n, r) = n! / (n-r)!
#
# Ejemplo:
#
# P(4, 2) = 4! / (4-2)!
#         = 24 / 2
#         = 12
#
# Es decir, existen 12 formas distintas de ordenar
# 2 objetos seleccionados de un conjunto de 4.
#
# El programa implementa herramientas relacionadas con
# el calculo de permutaciones:
#
# - Calculo iterativo del factorial
#
# - Calculo recursivo del factorial
#
# - Comparacion entre ambas implementaciones
#
# - Calculo general de P(n,r)
#
# - Casos de prueba predefinidos para validar resultados
#
# Observacion:
# Las permutaciones aparecen frecuentemente en problemas
# de ordenamientos, asignaciones, distribuciones y
# arreglos donde la posicion de los elementos afecta
# el resultado final.
# ============================================================


def factorial_iterativo(n):
    """
    Calcula n! de forma iterativa usando un ciclo for.
    Multiplica secuencialmente: 1 x 2 x 3 x ... x n

    Ventaja: eficiente en memoria, no apila llamadas.
    Complejidad: O(n) en tiempo, O(1) en espacio.

    Parametros:
        n (int): numero entero no negativo

    Retorna:
        int: el valor de n!
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """
    Calcula n! de forma recursiva: la funcion se llama a si misma
    reduciendo n en 1 cada vez hasta llegar al caso base.

    Definicion matematica:
        0! = 1            (caso base)
        n! = n x (n-1)!  (caso recursivo)

    Desventaja: para n muy grandes puede superar el limite de
    recursion de Python (por defecto ~1000 llamadas).
    Complejidad: O(n) en tiempo, O(n) en espacio (pila de llamadas).

    Parametros:
        n (int): numero entero no negativo

    Retorna:
        int: el valor de n!
    """
    if n == 0 or n == 1:   # Caso base: detiene la recursion
        return 1
    return n * factorial_recursivo(n - 1)  # Llamada recursiva


def calcular_permutacion(n, r):
    """
    Calcula P(n, r) = n! / (n - r)! usando factorial_iterativo.

    Parametros:
        n (int): total de objetos disponibles (n >= 0)
        r (int): objetos a ordenar (0 <= r <= n)

    Retorna:
        int: numero de permutaciones P(n, r)
    """
    return factorial_iterativo(n) // factorial_iterativo(n - r)


def comparar_factoriales(n):
    """
    Compara los resultados de ambas implementaciones del factorial
    para verificar que producen el mismo resultado.

    Parametros:
        n (int): numero a evaluar

    Retorna:
        dict con los resultados de ambas implementaciones y si coinciden
    """
    iter_result = factorial_iterativo(n)
    rec_result  = factorial_recursivo(n)
    return {
        "iterativo": iter_result,
        "recursivo": rec_result,
        "son_iguales": iter_result == rec_result
    }


def casos_de_ejemplo_1():
    """
    Retorna una lista de casos predefinidos para mostrar en la interfaz.
    Incluye los casos P(10,3) y P(20,5) solicitados por el enunciado,
    mas casos pequenos verificables manualmente.

    Retorna:
        lista de tuplas: [(n, r, P(n,r)), ...]
    """
    casos = [(4, 2), (5, 3), (6, 0), (10, 3), (20, 5)]
    return [(n, r, calcular_permutacion(n, r)) for n, r in casos]

# ============================================================
# PROBLEMA 2: Calculadora general de combinaciones C(n, r)
# ============================================================
# Una combinacion C(n, r) cuenta el numero de formas de escoger
# r objetos distintos tomados de un conjunto de n objetos distintos.
#
# A diferencia de las permutaciones, aqui el orden NO importa:
# (A, B) y (B, A) representan la misma seleccion.
#
# Formula:
#
#           C(n, r) = n! / (r!(n-r)!)
#
# Ejemplo:
#
# C(4, 2) = 4! / (2!(4-2)!)
#         = 24 / (2·2)
#         = 6
#
# Es decir, existen 6 formas distintas de escoger
# 2 objetos de un conjunto de 4 sin importar el orden.
#
# Ademas del calculo general de combinaciones, este problema
# implementa herramientas adicionales relacionadas con
# propiedades combinatorias:
#
# - Verificacion automatica de la identidad:
#
#       C(n,r) = C(n,n-r)
#
# - Generacion de filas del triangulo de Pascal
#
# - Casos de prueba predefinidos para validar resultados
#
# Observacion:
# Las combinaciones aparecen frecuentemente en problemas
# de seleccion, probabilidades, conteo y coeficientes
# binomiales.
# ============================================================

def calcular_combinacion(n, r):
    """
    Calcula C(n, r) = n! / r!(n - r)! usando factorial_iterativo.

    Parametros:
        n (int): total de objetos disponibles (n >= 0)
        r (int): objetos a ordenar (0 <= r <= n)

    Retorna:
        int: numero de combinaciones C(n, r)
    """
    return factorial_iterativo(n) // (factorial_iterativo(r) * factorial_iterativo(n - r))

def verificar_identidad(n, r):
    """
    Verifica que C(n, r) == C(n, n-r)
    """
    lado_izquierdo = calcular_combinacion(n, r)
    lado_derecho   = calcular_combinacion(n, n - r)
    return {
        "C(n,r)":   lado_izquierdo,
        "C(n,n-r)": lado_derecho,
        "son_iguales": lado_izquierdo == lado_derecho
    }
    
def generar_triangulo_pascal(n):
    """
    Genera el triangulo de Pascal hasta la fila n.

    Retorna:
        list of lists: cada sublista es una fila del triangulo
    """
    triangulo = []
    for i in range(n + 1):
        fila = [calcular_combinacion(i, r) for r in range(i + 1)]
        triangulo.append(fila)
    return triangulo

#matriz = generar_triangulo_pascal(3)

#for fila in matriz:
#    print(fila)
    
def casos_de_ejemplo_2():
    """
    Retorna una lista de ejemplos predefinidos de C(n, r)
    con casos pequenos verificables manualmente y casos medianos.
 
    Retorna:
        list of tuples: [(n, r, C(n,r)), ...]
    """
    casos = [(4, 2), (5, 0), (5, 5), (10, 3), (20, 5)]
    return [(n, r, calcular_combinacion(n, r)) for n, r in casos]