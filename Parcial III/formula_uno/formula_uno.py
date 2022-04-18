# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:21:05 2022
@author: Alejandro Bolívar

E S C E N A R I O
La Fórmula 1, conocida también como F1, es la competencia
internacional más popular de carros de carreras. Cada carrera se
denomina Gran Premio y la competición que las agrupa se denomina
Campeonato Mundial de Fórmula 1. Las carreras de Fórmula 1 se celebran
en circuitos urbanos o en circuitos especialmente construidos.
Con la finalidad de registrar posibles cambios en las estrategias de las
escuderías por cada corredor participante se le realiza el siguiente registro
en el archivo de nombre “C a r r e r a . T x t ” , Almacenándose la información 
correspondiente a la ultima carrera de Formula 1 que este disputó, de la 
siguiente manera: en la primera línea se almacena la información
del nombre del circuito, nombre del piloto y la hora de inicio de la carrera.
Adicionalmente, por cada vuelta realizada al circuito se toma: el tiempo de duración de la vuelta
(expresado minutos, segundos y centésimas de segundos), el tiempo de demora en el Pit
Stop expresado en segundos, así como la cantidad de llantas sustituidas.
Problema
Se requiere que diseñe una aplicación en VB2010 bajo consola, que procese la 
información del archivo antes mencionado que determine e imprima por pantalla:
• Cantidad de veces que entró al Pit Stop el piloto. (Tiempo en Pit Stop>0)
• Hora de culminación de la competencia por el piloto, expresada en hora y minuto.
• La mejor vuelta realizada por el piloto (el tiempo que duro su vuelta mas rápida).
CONSIDERACIONES
 La hora de inicio de la carrera se encuentra en formato de hora militar, horas y minutos.
 En el archivo sólo se registran las vueltas completas al circuito por un solo piloto.
 No necesariamente el vehículo culmina la carrera.
 Si no entra al Pit Stop en el archivo se coloca como tiempo de parada 0 seg. 
Por supuesto si no entra al Pit
Stop, no se le cambian llantas (Cero llantas).
 La conversión de tiempo son: 1 hora = 60 Min, 1Min = 60 Seg, 1Seg. = 1000 Cseg.
Requerimientos
 Un subprograma que dado los datos de un tiempo en minutos, segundos y centésimas de segundo lo
transforme en centésimas de Segundos totales.
 Un subprograma que dado dos datos tiempos expresados en minutos, segundos y centésimas de
segundo, devuelva el tiempo menor.
 Cualquier otro tipo de subprograma que crea necesario realizar para que el procedimiento Main sea
de forma los más modular posible.

Carrera.Txt
Turquia, José Corredor, 7, 10
1, 40, 112, 0, 0 
1, 25, 953, 0, 0  
1, 40, 855, 0, 0  
1, 35, 942, 0, 0  
1, 29, 672, 18, 4  
1, 36, 639, 0, 0  
1, 46, 539, 0, 0  
1, 43, 784, 0, 0

Cálculos a desarrollar (tiempo en centésimas de segundo de cada vuelta)
100112
85953
100855
95942
107672
96639
106539
103784
797496 <- Tiempo total Cseg

Duración de la Carrera: Min Seg Cseg
13 17 496
Hora de finalizacion
7 23
Tiempo más rápido
1 25 953
Entradas a pit Stop
1
"""

# subprograma que dado los datos de un tiempo en minutos, segundos y centésimas de segundo lo 
# transforme en centésimas de Segundos totales.
def transformar(minutos, seg, cseg):
    transformar = (minutos * 60000) + (seg * 1000) + cseg
    return transformar

# Subprograma que transforma centesimas de segundos totales a datos de  minutos, segundos y centésimas de segundo
def devolucion(cst):
    minutos = cst // 60000
    seg = (cst % 60000) // 1000
    cseg = cst % 1000
    return minutos, seg, cseg
    
# subprograma que dado dos datos tiempos expresados en minutos, segundos y centésimas de 
# segundo, devuelve el tiempo menor.
def menor(min1, seg1, cseg1, min2, seg2, cseg2):
    csa = transformar(min1, seg1, cseg1)
    csb = transformar(min2, seg2, cseg2)
    if csa < csb:
        csm = csa
    elif csa > csb:
        csm = csb
    minutos, seg, cseg = devolucion(csm)
    return  minutos, seg, cseg

# subprograma de lectura de los datos de una vuelta 
def leer(registro):
    linea = registro.split(',')
    minutos = int(linea[0])
    seg = int(linea[1])
    cseg = int(linea[2])
    segpit = int(linea[3])
    cauchos = int(linea[4])
    return minutos, seg, cseg, segpit, cauchos

# Subprograma que suma dos horas expresadas en hh:min
def sumahora(hi, mi, minutos):
    if minutos > 60:
        mf = mi + minutos % 60
        hf = hi + minutos // 60
    else:
        mf = mi + minutos
        hf = hi
    return  hf,  mf

def main():

    # apertura de archivo
    arch = open("carrera.txt", "r")

    # lectura de la primera línea del archivo
    registro = arch.readline()
    linea = registro.split(',')
    circuito = linea[0]
    nombre = linea[1]
    hi = int(linea[2])
    mi = int(linea[3])

    # inicialización de contadores y acumuladores
    contadorpit = 0
    duracion = 0
    band = 0

    # inicio de ciclo 
    for registro in arch:

        minutos, seg, cseg, segpit, cauchos = leer(registro)

        # determinar si entrá al pit
        if segpit > 0:
            contadorpit = contadorpit + 1

        # cálculo de la duracion de la carrera 
        duracion = duracion + transformar(minutos, seg, cseg) + (segpit * 1000)

        # cálculo de la vuelta mas rapida
        if band == 0:
            band = 1
            mr = minutos
            sr = seg + segpit
            csr = cseg
        else:
            mr, sr, csr = menor(mr, sr, csr, minutos, seg + segpit, cseg)
    
    print("Circuito: ", circuito)
    print("Piloto: ", nombre)
    # impresion de la duracion de la carrera 
    minc, segc, csegc = devolucion(duracion)
    print("Duracion de la carrera:%d min %d seg %d cseg " % (minc, segc, csegc))

    # impresion de la hora de finalizacion
    hf, mf = sumahora(hi, mi, minc)
    print("Hora de finalizacion de la carrera: %d : %d " % (hf, mf))

    # impresion del tiempo mas rápido 
    print("Tiempo mas rapido: %d min %d seg %d cseg " % (mr, sr, csr))

    # impresion del numero de paradas a pit stop
    print("Entradas a pit stop: ", contadorpit)

    arch.close()

if __name__ == "__main__":
    main()
