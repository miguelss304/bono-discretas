# Bono de Programacion — Matematicas Discretas I
Universidad Nacional de Colombia  
Estudiante: Miguel Angel Sanchez Sandoval
Docente: Jhoan Sebastian Tenjo Garcia

---

## Descripcion general

Este repositorio contiene la solucion a dos problemas de conteo combinatorio
como parte del bono de programacion del segundo corte de Matematicas Discretas I.
Cada problema incluye logica matematica documentada e interfaz grafica interactiva.

---

## Problemas resueltos

### Problema 1 — Permutaciones P(n, r)

Cuenta el numero de formas de **ordenar** r objetos distintos tomados
de un conjunto de n objetos distintos. El orden importa.

**Formula:**
```
P(n, r) = n! / (n - r)!
```

**Ejemplo:** P(10, 3) = 720 — hay 720 formas de ordenar 3 objetos de un conjunto de 10.

El programa calcula P(n, r), compara una implementacion iterativa y una recursiva
del factorial, y muestra casos de ejemplo predefinidos.

---

### Problema 2 — Combinaciones C(n, r)

Cuenta el numero de formas de **escoger** r objetos de un conjunto de n
objetos distintos sin importar el orden.

**Formula:**
```
C(n, r) = n! / (r! * (n - r)!)
```

**Ejemplo:** C(10, 3) = 120 — hay 120 formas de escoger 3 objetos de un conjunto de 10.

El programa calcula C(n, r), verifica la identidad simetrica C(n,r) = C(n,n-r),
genera el triangulo de Pascal hasta la fila n, y muestra casos de ejemplo.

---

## Requisitos

- Python 3.8 o superior
- Libreria `pyglet`

Instalar pyglet:
```
pip install pyglet
```

---

## Archivos del proyecto

```
bono-discretas/
├── interfaz1.py       <- Ejecutar este archivo
├── matematicas.py     <- Logica matematica documentada
├── pixelplay.ttf      <- Fuente personalizada
├── icon.ico           <- Icono de la ventana
└── README.md
```

---

## Instrucciones de ejecucion

1. Clona el repositorio o descarga los archivos
2. Instala pyglet si no lo tienes:
```
pip install pyglet
```
3. Asegurate de que todos los archivos esten en la misma carpeta
4. Ejecuta la interfaz:
```
python interfaz1.py
```

---

## Uso del programa

1. Selecciona la pestana **Permutaciones P(n,r)** o **Combinaciones C(n,r)**
2. Ingresa los valores de **n** y **r**
3. Presiona **Calcular** o la tecla **Enter**
4. El resultado aparece en el panel derecho con el procedimiento completo

El programa valida que:
- n y r sean enteros no negativos
- r no sea mayor que n

---

## Ejemplos de entrada y salida

### Permutaciones
| n  | r | P(n, r)    |
|----|---|------------|
| 4  | 2 | 12         |
| 5  | 3 | 60         |
| 10 | 3 | 720        |
| 20 | 5 | 1860480    |

### Combinaciones
| n  | r | C(n, r) |
|----|---|---------|
| 4  | 2 | 6       |
| 5  | 0 | 1       |
| 10 | 3 | 120     |
| 20 | 5 | 15504   |

---

## Eficiencia

Ambos algoritmos tienen complejidad **O(n)** en tiempo.  
El factorial iterativo usa **O(1)** en espacio.  
El factorial recursivo usa **O(n)** en espacio por la pila de llamadas.
