# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:20:22 2022

@author: bolivar

 Respuesta al ejercicio de Preparaduria
 Escenario: Circunferencias Tangentes
 Elaborado por: Prof. Alejandro Bolívar
 Fecha: 19-04-2022
 
P R O B L E M A
Elabore un programa que dado el archivo de datos de nombre “Circunferencias.txt”, 
el cual posee en cada línea, las coordenadas (x, y) del centro y la longitud del 
radio de un par de circunferencias, determine e imprima en el archivo ”Resultados.txt”:
1- Para cada par de circunferencias, las coordenadas (x, y) del centro y la 
longitud del radio de ambas circunferencias y la relación tangencial que existe 
entre las mismas (1: externa, 2: interna, 3: No tangencial y 4: Son iguales) y
2- Para todas las circunferencias, Coordenadas (x, y) y longitud del radio de la
circunferencia con el mayor radio.

Tangente Extena
Dc1c2 = r1 + r2
Tangente Interna
Dc1c2 = r1 − r2
No Tangentes
Dc1c2 != r1-r2
Dc1c2 != r1+r2

NOTA: la circunferencia C1 , será aquella que posee el mayor radio entre las 
dos circunferencias, Además debe ser diferente a la circunferencia C2.

Recuerde: que la distancia entre dos puntos se determina como: 
    dist = ((x2-x1)**2+(y2-y1)**2)**0.5
    
Ejemplo del archivo de datos: “Circunferencias.txt
0.00, 0.00, 4.00, 0.00, 2.00, 2.00
0.00, 0.00, 2.00, 7.00, 0.00, 5.00
1.00, 2.00, 6.00, 7.00, 2.00 ,4.50
1.00, 1.00, 2.00, 1.00, 1.00, 2.00

Archivo de salida: “Resultados.txt”
[(0.00, 0.00), 4.00] [(0.00, 2.00), 2.00] 2
[(7.00, 0.00), 5.00] [(0.00, 0.00), 2.00] 1
[(1.00, 2.00), 6.00] [(7.00, 2.00), 4.50] 3
[(1.00, 1.00), 2.00] [(1.00, 1.00), 2.00] 4
Circunferencia con mayor radio: [(1.00, 2.00), 6.00]

Elabore e implemente los siguientes subprogramas
a) Un procedimiento que lea de un archivo de datos la información de una 
    Circunferencia, radio y coordenadas del centro
b) Un procedimiento que intercambie los datos de dos circunferencias.
c) Una función que dada la información de las coordenadas de dos puntos 
    determine la distancia entre ellos.
d) Una función que dada la información de dos circunferencia retorne el 
    tipo de forma tangencial que estas forman (1:externa, 2: interna, 
    3: No tangencial y 4: Son iguales)
e) Un procedimiento que imprima hacia un archivo sin salto de línea, 
    el contenido de una variable tipo Circunferencia, con el mismo formato 
    mostrado en el ejemplo, [(X , Y), R]

"""

# Subprograma que lee la informacion de una circunferencia
def leercircunferencias(registro):
    linea = registro.split(',')
    xc1 = float(linea[0])
    yc1 = float(linea[1])
    r1 = float(linea[2])
    xc2 = float(linea[3])
    yc2 = float(linea[4])
    r2 = float(linea[5])

    return xc1, yc1, r1, xc2, yc2, r2

# Subprograma que determina la distancia entre dos puntos
def distancia(x1, y1, x2, y2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
    return distancia

# Subprograma que Determina el tipo de circunferencia tangencial formas dos circunferencia
def tipocircunferencia(xc1, yc1, r1, xc2, yc2, r2):
    dist = distancia(xc1, yc1, xc2, yc2)
    if dist == r1 + r2:
        tipocircunferencia = 1
    elif dist == r1 - r2:
        if (xc1 == xc2) and (yc1 == yc2):
            tipocircunferencia = 4
        else:
            tipocircunferencia = 2
    else:
        tipocircunferencia = 3
    return tipocircunferencia

# Subprograma que ordena las circunferencias por radio
def ordenar(xc1, yc1, r1, xc2, yc2, r2):
    if r2 > r1:
        aux = xc1
        xc1 = xc2
        xc2 = aux
        
        aux = yc1
        yc1 = yc2
        yc2 = aux
        
        aux = r1
        r1 = r2
        r2 = aux
    return xc1, yc1, r1, xc2, yc2, r2

# Subprograma que imprime la informacion de una cirucnferencia
def imprimircircunferencia(arch, xc, yc, r):
    arch.write("[(%.2f ,%.2f), %.2f] " % (xc, yc, r))

def main():
    # Variables auxiliares
    primero = True
    
    # Manejo de archivo de datos
    arch1 = open("circunferencias.txt", "r")
    arch2 = open("clasificacion.txt", "w")

    # Ciclo de lectura
    for registro in arch1:
        xc1, yc1, r1, xc2, yc2, r2 = leercircunferencias(registro)

        # Determinacion del tipo de circunferencia
        xc1, yc1, r1, xc2, yc2, r2 = ordenar(xc1, yc1, r1, xc2, yc2, r2)
        tc = tipocircunferencia(xc1, yc1, r1, xc2, yc2, r2)

        # Impresion de las circunferencias
        imprimircircunferencia(arch2, xc1, yc1, r1)
        imprimircircunferencia(arch2, xc2, yc2, r2)
        arch2.write("%d \n" % tc)

        # Determiancion del mayor
        if primero:
            primero = False
            xcmax = xc1
            ycmax = yc1
            rmax = r1
        elif r1 > rmax:
            xcmax = xc1
            ycmax = yc1
            rmax = r1

    # impresion del mayor
    arch2.write("Circunferencia con mayor radio: ")
    imprimircircunferencia(arch2, xcmax, ycmax, rmax)

    # Cierre de archivos
    arch1.close()
    arch2.close()

    # Mensaje al usuario
    print("La ejecucion ha finalizado con exito")

if __name__ == "__main__":
    main()