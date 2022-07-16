# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:48:03 2022

@author: bolivar
"""
'''
'Declaracion de variables
'variables de entrada
nombre
genero
hora
velocidad

'Variables de salida
multa
porcentaje
contp1
nombre3m
multa3m
promedio

'Variables de proceso
cont2ni, cont2
band, band1f
band3m, cont1f, cont3m
acums
'''

# Declaracion de constantes
limite1 = 49.69
limite2 = 37.26

# inicializacion de variables
cont1f = 0
cont2 = 0
cont2ni = 0
cont3m = 0
contp1 = 0
band = 0
band3m = 0
acums = 0
band1f = 0

# Manejo de archivos
arch1 = open("datostransito.txt", 'r')
arch2 = open("resultados.txt", 'w')

# Proceso
for registro in arch1:
    # lectura de datos
    contenido = registro.split(',')

    nombre = contenido[0]
    genero = int(contenido[1])
    hora = int(contenido[2])
    velocidad = float(contenido[3])

    # Proceso

    if 0<= hora <=12:
        if velocidad > limite1 :
            multa = (velocidad - limite1) * 2.5
            arch2.write( nombre + " Es infractor y debe cancelar una multa de %.2f " % multa + " $" + '\n')
            if genero == 1 and band1f == 0 :
                cont1f += 1
                acums += multa
            elif genero == 2 and band3m == 0 :
                cont3m += 1
                if cont3m == 3 :
                    nombre3m = nombre
                    multa3m = multa
                    band3m = 1
        else:
            arch2.write(nombre + " No es un infractor" + '\n')

    if 13 <= hora <= 24:
        cont2 += 1
        if velocidad > limite2 :
            multa = (velocidad - limite2) * 2.5
            arch2.write( nombre + " Es infractor y debe cancelar una multa de  %.2f " % multa + " $" + '\n')
            if band == 0 :
                band = 1
            elif genero == 2 and band3m == 0 :
                cont3m += 1
                if cont3m == 3 :
                    nombre3m = nombre
                    multa3m = multa
                    band3m = 1
        else:
            arch2.write(nombre + " No es un infractor" + '\n')
            cont2ni += 1

    if band == 1 :
        contp1 += 1

if cont2 > 0 :
    porcentaje = (cont2ni * 100) / cont2
    arch2.write("El porcentaje es %.2f" % porcentaje + '\n')
else:
    arch2.write("No hubo conductores del turno 2" + '\n')

if band == 1 :
    arch2.write("Despues de encontrar al primer infractor fueron procesados %d" % contp1 + " vehiculos" + '\n')

if band3m == 1 :
    arch2.write("El tercer infractor masculino fue " + nombre3m + " y debe cancelar una multa de %.2f " % multa3m + " $" + '\n')

if cont1f > 0 :
    promedio = acums / cont1f
    arch2.write("El promedio es %.2f " % promedio + '\n')

arch1.close()
arch2.close()